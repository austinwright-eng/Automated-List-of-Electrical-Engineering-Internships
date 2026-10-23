import asyncio
import json

import httpx

from intern_engine import enrich, filters, registry
from intern_engine.connectors import _public_html, jazzhr
from intern_engine.connectors._public_html import Page, fetch_board
from intern_engine.models import INCOMPLETE_MALFORMED
from intern_engine.net import HostLimiter
from intern_engine.net import Net as HttpNet

COMPANY = {"name": "Lab", "ats": "jazzhr", "slug": "lab"}
BASE = "https://lab.applytojob.com/apply/"
DETAIL = BASE + "ABC123/Electrical-Intern"


def posting(**changes):
    data = {
        "@type": "JobPosting", "title": "Electrical Engineer Intern",
        "datePosted": "2026-10-19", "description": "This internship is for summer 2027.",
        "jobLocation": {"address": {"addressLocality": "Logan", "addressRegion": "UT"}},
    }
    data.update(changes)
    return '<script type="application/ld+json">' + json.dumps(data) + '</script>'


class Net:
    def __init__(self, pages):
        self.pages = pages
        self.urls = []

    async def get_text(self, url):
        self.urls.append(url)
        result = self.pages[url]
        if isinstance(result, Exception):
            raise result
        return result


def index(extra=""):
    return '<div class="jobs-list"><a href="' + DETAIL + '">Intern</a></div>' + extra


def test_jazzhr_identity_location_inline_season_and_duplicates():
    net = Net({BASE: index(index()), DETAIL: posting()})
    result = asyncio.run(jazzhr.fetch(COMPANY, net))
    assert result.complete and len(result.jobs) == 1
    job = result.jobs[0]
    assert job.id == "jazzhr:lab:ABC123"
    assert job.location == "Logan, UT"
    assert filters.is_united_states(job.location)
    assert filters.seasons_from_text(job.description) == ["Summer 2027"]
    assert net.urls.count(DETAIL) == 1


def test_unknown_page_and_missing_detail_are_incomplete():
    for pages in [{BASE: "captcha"}, {BASE: index(), DETAIL: "Posting unavailable"},
                  {BASE: index(), DETAIL: RuntimeError("timeout")}]:
        result = asyncio.run(jazzhr.fetch(COMPANY, Net(pages)))
        assert not result.complete
        assert result.incomplete_reason == INCOMPLETE_MALFORMED


def test_partial_detail_failure_retains_successful_jobs():
    other = BASE + "OTHER/Other-Intern"
    net = Net({BASE: index('<a href="' + other + '">Other</a>'),
               DETAIL: posting(), other: "invalid"})
    result = asyncio.run(jazzhr.fetch(COMPANY, net))
    assert not result.complete and len(result.jobs) == 1


def test_expired_posting_omitted_and_off_host_links_not_followed():
    net = Net({BASE: index('<a href="https://evil.example/apply/EVIL/Intern">Intern</a>'),
               DETAIL: posting(validThrough="2000-01-01")})
    result = asyncio.run(jazzhr.fetch(COMPANY, net))
    assert result.complete and not result.jobs
    assert len(net.urls) == 2


def test_icims_pagination_and_disabled_next():
    base = "https://careers-lab.icims.com/jobs/search"
    detail1 = "https://careers-lab.icims.com/jobs/123/ee/job"
    detail2 = "https://careers-lab.icims.com/jobs/456/ee/job"
    next_url = base + "?pr=1&in_iframe=1"
    net = Net({
        base: '<div class="iCIMS_JobsTable"><a href="' + detail1 + '">EE</a>'
              '<a href="?pr=1&amp;in_iframe=1"><span>Next page of results</span></a>',
        next_url: '<div class="iCIMS_JobsTable"><a href="' + detail2 + '">EE</a>'
                  '<a class="glyph invisible" href="?pr=0">Next page of results</a>',
        detail1 + "?in_iframe=1": posting(), detail2 + "?in_iframe=1": posting(),
    })
    company = dict(COMPANY, ats="icims", slug="careers-lab")
    result = asyncio.run(fetch_board(company, net, base, r"/jobs/(\d+)/[^/]+/job", paginated=True))
    assert result.complete and len(result.jobs) == 2


def test_graph_posting_and_tenant_validation():
    data = {"@graph": [{"@type": "Organization"}, {"@type": ["JobPosting"]}]}
    page = Page('<script type="application/ld+json">' + json.dumps(data) + '</script>')
    assert len(page.postings) == 1
    import pytest
    with pytest.raises(registry.RegistryCorrupt):
        registry.validate_company(dict(COMPANY, slug="bad/path"))


def test_html_transport_preserves_json_transport():
    async def run():
        def respond(request):
            if request.url.path == "/html":
                return httpx.Response(200, text="<h1>Electrical Intern</h1>")
            return httpx.Response(200, json={"jobs": []})
        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as client:
            net = HttpNet(client, HostLimiter())
            assert await net.get_text("https://lab.test/html") == "<h1>Electrical Intern</h1>"
            assert await net.get_json("https://lab.test/json") == {"jobs": []}
    asyncio.run(run())


def test_inline_description_promotes_unstated_season_without_network():
    async def run():
        result = await jazzhr.fetch(COMPANY, Net({BASE: index(), DETAIL: posting()}))
        job = result.jobs[0]
        job.season = filters.NOT_STATED
        job.season_inferred = True
        done, requests = await enrich.enrich_jobs([job], {}, Net({}))
        assert done == {job.id} and requests == 0
        assert job.season == "Summer 2027" and not job.season_inferred
    asyncio.run(run())


def test_job_limit_marks_partial_snapshot_and_retains_valid_jobs(monkeypatch):
    monkeypatch.setattr(_public_html, "MAX_JOBS", 1)
    other = BASE + "DEF456/Other-Intern"
    net = Net({BASE: index('<a href="' + other + '">Other</a>'), DETAIL: posting()})
    result = asyncio.run(jazzhr.fetch(COMPANY, net))
    assert not result.complete and result.incomplete_reason == "result-cap"
    assert len(result.jobs) == 1
