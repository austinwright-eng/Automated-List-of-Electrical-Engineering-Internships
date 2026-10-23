"""Public ATS indexes and employer-provided JobPosting structured data.

Only links on the configured board's host are followed. Missing or broken
pages produce incomplete snapshots rather than evidence that jobs closed.
"""

from __future__ import annotations

import asyncio
import json
import re
from datetime import UTC, datetime
from html.parser import HTMLParser
from urllib.parse import urljoin, urlsplit

from ..models import INCOMPLETE_CAPPED, INCOMPLETE_MALFORMED, Fetch, Job, source_board_key

MAX_PAGES = 30
MAX_JOBS = 300


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.postings = []
        self._anchor = None
        self._script = None
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a":
            self._anchor = (
                None if "invisible" in attrs.get("class", "").split()
                else [attrs.get("href", ""), ""]
            )
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self._script = ""

    def handle_data(self, text):
        if self._anchor is not None:
            self._anchor[1] += text
        if self._script is not None:
            self._script += text

    def handle_endtag(self, tag):
        if tag == "a" and self._anchor is not None:
            self.links.append(tuple(self._anchor))
            self._anchor = None
        if tag == "script" and self._script is not None:
            try:
                self._walk(json.loads(self._script))
            except (ValueError, TypeError):
                pass
            self._script = None

    def _walk(self, value):
        if isinstance(value, list):
            for item in value:
                self._walk(item)
        elif isinstance(value, dict):
            kind = value.get("@type")
            if kind == "JobPosting" or isinstance(kind, list) and "JobPosting" in kind:
                self.postings.append(value)
            self._walk(value.get("@graph"))


def _location(value):
    places = value if isinstance(value, list) else [value]
    locations = []
    for place in places:
        address = place.get("address") if isinstance(place, dict) else None
        if not isinstance(address, dict):
            continue
        country = address.get("addressCountry")
        if isinstance(country, dict):
            country = country.get("name")
        parts = [address.get("addressLocality"), address.get("addressRegion"), country]
        locations.append(", ".join(p.strip() for p in parts if isinstance(p, str) and p.strip()))
    return "; ".join(dict.fromkeys(filter(None, locations))) or "—"


def _posting(company, url, identity, data):
    title, description = data.get("title"), data.get("description")
    if (not isinstance(title, str) or not title.strip()
            or not isinstance(description, str) or not description.strip()):
        raise ValueError("missing JobPosting title or description")
    expires = data.get("validThrough")
    if isinstance(expires, str):
        try:
            until = datetime.fromisoformat(expires.replace("Z", "+00:00"))
            if until.replace(tzinfo=until.tzinfo or UTC) < datetime.now(UTC):
                return None
        except ValueError:
            pass
    posted = data.get("datePosted")
    if not isinstance(posted, str) or not re.match(r"^\d{4}-\d{2}-\d{2}(?:$|T)", posted):
        posted = None
    return Job(
        id=f"{company['ats']}:{company['slug']}:{identity}",
        source=company["ats"], company=company["name"], company_slug=company["slug"],
        title=title.strip(), location=_location(data.get("jobLocation")), url=url,
        posted_at=posted, description=description,
        board_key=source_board_key(company, company["ats"], company["slug"]),
    )


async def fetch_board(company, net, base, path_pattern, *, paginated=False):
    host = urlsplit(base).netloc
    url = base
    visited = set()
    links = {}
    reason = None
    while url:
        if url in visited or len(visited) >= MAX_PAGES:
            reason = INCOMPLETE_CAPPED
            break
        visited.add(url)
        text = await net.get_text(url)
        page = Page(text)
        recognized = "iCIMS_JobsTable" in text if paginated else "jobs-list" in text
        if not recognized:
            reason = INCOMPLETE_MALFORMED
            break
        before = len(links)
        next_url = None
        for href, label in page.links:
            target = urljoin(url, href)
            parsed = urlsplit(target)
            if parsed.netloc != host or parsed.scheme != "https":
                continue
            match = re.fullmatch(path_pattern, parsed.path)
            if match:
                identity = match.group(1)
                canonical = target.split("?")[0]
                links.setdefault(identity, canonical + "?in_iframe=1" if paginated else canonical)
            if paginated and "Next page of results" in label:
                if parsed.path == "/jobs/search":
                    next_url = target
        if len(links) > MAX_JOBS:
            links = dict(list(links.items())[:MAX_JOBS])
            reason = INCOMPLETE_CAPPED
            break
        if next_url and len(links) == before:
            reason = INCOMPLETE_MALFORMED
            break
        url = next_url
    # An unrecognized empty page is never proof of a successful empty board.
    if not links:
        return Fetch([], complete=False, incomplete_reason=reason or INCOMPLETE_MALFORMED)
    sem = asyncio.Semaphore(6)

    async def detail(identity, target):
        async with sem:
            try:
                page = Page(await net.get_text(target))
                if len(page.postings) != 1:
                    raise ValueError("expected one JobPosting")
                return _posting(company, target, identity, page.postings[0]), None
            except Exception:  # one broken detail must not close unseen jobs
                return None, INCOMPLETE_MALFORMED

    details = await asyncio.gather(*(detail(i, u) for i, u in links.items()))
    reason = reason or next((error for _, error in details if error), None)
    return Fetch([job for job, _ in details if job], complete=reason is None,
                 incomplete_reason=reason)
