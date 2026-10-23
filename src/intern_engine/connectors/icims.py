"""iCIMS public internship search, including every advertised next page."""

from ..models import Fetch
from ._public_html import fetch_board


async def fetch(company, net):
    results = []
    for keyword in ("intern", "co-op"):
        results.append(await fetch_board(
            company, net,
            f"https://{company['slug']}.icims.com/jobs/search?ss=1"
            f"&searchKeyword={keyword}&in_iframe=1",
            r"/jobs/(\d+)/[^/]+/job/?", paginated=True,
        ))
    jobs = {job.id: job for result in results for job in result.jobs}
    reason = next((r.incomplete_reason for r in results if not r.complete), None)
    return Fetch(list(jobs.values()), complete=all(r.complete for r in results),
                 incomplete_reason=reason)
