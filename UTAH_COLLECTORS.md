# Public-board collectors for the Utah expansion

This change adds JazzHR and iCIMS collectors and registers:

- Space Dynamics Laboratory: `jazzhr:spacedynamicslaboratory`, verified at its
  [public board](https://spacedynamicslaboratory.applytojob.com/apply/).
- General Dynamics Mission Systems: `icims:careers-gdms`, verified at its
  [public board](https://careers-gdms.icims.com/jobs/search?ss=1&searchKeyword=intern&in_iframe=1).

The EE overlay remains separate from the upstream employer registry. These
employer boards include locations outside Utah; the existing US, EE, internship,
and season filters apply. No filter is widened by this change.

## Collection behavior

JazzHR lists public posting links in one index. iCIMS searches both `intern` and
`co-op` and follows the advertised next-page links. IDs use the board tenant
and posting ID, rather than a title slug that can change. Each detail page must
contain exactly one employer-provided JobPosting JSON-LD record with a title
and description. Locations, publication dates and descriptions come from that
record. Existing enrichment extracts explicit seasons from inline descriptions.

Requests use the existing shared retry, timeout and host-limiting transport.
Only HTTPS links on the configured board host are followed. Detail requests
are bounded to six concurrent requests. Index traversal is limited to 30 pages
and 300 unique postings per query; reaching a bound marks the result incomplete.
Missing or broken detail pages preserve valid results but mark the snapshot
incomplete, protecting unseen stored jobs from being closed. Expired postings
with an explicit `validThrough` are omitted. Unrecognized or empty index pages
are conservatively incomplete; support for a specific empty-board message can
be added once a real response is verified.

iCIMS detail URLs retain `in_iframe=1`, which exposes the actual structured
posting rather than the surrounding careers-site shell. Duplicate IDs from
the two keyword queries are merged.

## Verification

Live verification on October 23, 2026 UTC returned complete snapshots from both
boards. SDL returned 34 records and GDMS returned 85 records in the initial
successful check. These are whole-source records, not qualifying internship
counts. A second pass applied production scope filtering, deduplication and
enrichment, retaining 22 US matches including these five with Utah locations:

| Employer | Opening | Season evidence |
| --- | --- | --- |
| SDL | [CVS: Electrical Engineer Intern](https://spacedynamicslaboratory.applytojob.com/apply/PkQiCbVHQR/CVS-Electrical-Engineer-Intern), North Logan | Summer 2027 in description |
| SDL | [CVS: FPGA Electrical Engineer Intern](https://spacedynamicslaboratory.applytojob.com/apply/SznZA6uzbW/CVS-FPGA-Electrical-Engineer-Intern), North Logan | Summer 2027 in description |
| GDMS | [Electrical Engineering Intern](https://careers-gdms.icims.com/jobs/75138/electrical-engineering-intern-%28summer-2027%29/job?in_iframe=1), West Valley City | Summer 2027 in title |
| GDMS | [Embedded Software Engineer – Intern](https://careers-gdms.icims.com/jobs/75013/embedded-software-engineer-%e2%80%93-intern/job?in_iframe=1), Salt Lake City / Boise | Not stated; recent posting, no term inferred |
| GDMS | [Electrical Engineer – Intern](https://careers-gdms.icims.com/jobs/75019/electrical-engineer-%e2%80%93-intern/job?in_iframe=1), Salt Lake City / Boise | Not stated; recent posting, no term inferred |

Results and counts can change as employers edit their boards. The nine new
automated tests passed with all existing tests (649 total), as did lint,
workflow validation and the committed-artifact accuracy gate.

Tests cover stable identity, duplicate links, location parsing, inline season
extraction, pagination including disabled next links, expired postings, off-host
links, missing/malformed/failed details, partial snapshots, collection limits,
tenant validation, and compatibility with the existing JSON HTTP transport.

The published dashboard, stored jobs and global collection timestamp are not
regenerated in this code PR. A full collection after merge is needed to publish
the new results without misrepresenting a two-board check as a registry-wide run.

## Remaining work

L3Harris's SuccessFactors site exposes a public RSS feed, but this batch does
not register it: feed completeness and reliable closure behavior still need
verification. Juniper Systems' embedded Paycor board also remains a candidate.
No LinkedIn, Indeed, or Handshake website scraper is added.

SDL's internship descriptions exclude current Utah State University students
from its national internship program and direct them to student employment;
qualification requirements should be checked on each employer posting.
