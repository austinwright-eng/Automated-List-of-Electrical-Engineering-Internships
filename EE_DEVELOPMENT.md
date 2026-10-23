# Electrical Engineering fork

This fork adds an opt-in `role_scope: "ee"` to the upstream
[Internship Engine](https://github.com/zshah101/Automated-List-Of-Summer-2027-and-Fall-2026-Tech-Internships).
The original `tech` and `all` scopes remain available, and missing configuration
still defaults to upstream's tech scope. This deployment selects EE explicitly.

## Scope

EE matches title evidence for electrical/electronics, circuits/PCB/analog,
ASIC/FPGA/RTL/semiconductors, RF and signal processing, power, embedded/firmware,
and controls/instrumentation/avionics. Generic software, data science,
mechanical/civil, and ambiguous systems/test/validation titles do not qualify.
Non-engineering intent such as sales and marketing is excluded. Internship,
seniority, US location, cycle evidence, freshness, blocklist, and lifecycle
checks still apply. Description-only EE-degree requirements are not enough.

New jobs, stored-job cleanup, and the publication verifier share the same scope
predicate. `python run.py render` also closes out-of-scope inherited records
before rebuilding outputs. Storage keeps historical records; EE outputs exclude
unrelated software closures and posting-volume history.

The dashboard reuses existing search, category filters, saves, and CSV export.
The inherited email signup endpoint is removed; confirmation and unsubscribe
pages explain that email is unavailable. RSS works without notification secrets.
No notification service is needed for the initial dashboard.

Software opening windows are not EE forecasts. The EE dashboard and README hide
the inherited radar; its API includes only live EE signals, and its calendar has
no inherited forecasts. Independent EE history can be added in a later PR.

## Employer additions

`data/companies.json` remains the upstream/discovery registry.
`data/companies.ee.json` is an additive EE overlay, currently empty because this
first change reuses existing board coverage rather than inventing employer URLs.
Only collection reads the overlay; discovery and harvesting keep their existing
registry writes. Conflicting board identities fail rather than silently replacing
an existing board. Validate each new employer's public board before adding it.

Collection is not exhaustive: capped boards may omit older roles; some ATS searches
only request `intern` and may miss co-ops. A board in the registry does not imply
an active EE opening. Filter precision should be improved through real title
fixtures before widening ambiguous terms.

## Validation and launch

Install `requirements-dev.txt`, then run:

```sh
ruff check src tests tools run.py
actionlint
python -m pytest -q
python run.py update
MIN_OPEN_ROLES=70 MAX_STATS_AGE_HOURS=2 python tools/verify_accuracy.py
```

The update command writes local artifacts and queues alerts; it does not send
them. Do not run `notify` for development. The inherited update and audit
workflows deliberately target and write main, even on manual dispatch; do not
use them as feature-branch previews. CI on the PR is read-only.

Review filter examples and collection results in the PR before merging. After
merge approval, enable Actions and configure Pages for `main` / `docs`. The
repository homepage should then use the fork's Pages URL. Keep email and external
mirrors unconfigured until they have their own infrastructure. Existing 70/60
role floors and fetch-health checks remain publication gates.

## Upstream synchronization

1. Keep an `upstream` remote pointing to the original repository.
2. Bring upstream changes into a dedicated sync branch and open a PR into this
   fork; never overwrite main directly or force-reset it to upstream.
3. Preserve this deployment's EE config, `ee.py`, additive overlay, and scope
   integration. Review connector and schema changes normally.
4. Regenerate job data and all published artifacts with EE config after resolving
   source changes. Generated data conflicts should be resolved by regeneration,
   not by choosing an entire side of the source merge.
5. Run the full suite and publication checks. Review results before merging.

EE rules live separately from upstream's software regular expressions. The
shared ATS connectors, discovery machinery, deduplication, enrichment, and
partial-snapshot closure protections remain unchanged.
