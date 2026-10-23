"""JazzHR public applytojob.com index and JobPosting detail pages."""

from ._public_html import fetch_board


async def fetch(company, net):
    return await fetch_board(
        company, net, f"https://{company['slug']}.applytojob.com/apply/",
        r"/apply/([A-Za-z0-9]+)/[^/]+/?",
    )
