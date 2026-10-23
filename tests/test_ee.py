"""EE inclusion boundaries and integration with upstream lifecycle rules."""

import json

import pytest

from intern_engine import (
    config,
    dashboard,
    ee,
    filters,
    models,
    paths,
    pipeline,
    publish,
    radar,
    registry,
)


@pytest.mark.parametrize("title", [
    "Electrical Engineering Intern", "Electronics Co-op", "FPGA Design Intern",
    "ASIC Verification Intern", "RTL Intern", "Analog IC Design Intern",
    "Mixed-Signal Intern", "PCB Layout Intern", "Power Electronics Intern",
    "Power Systems Engineering Intern", "RF Engineering Intern",
    "Antenna Design Intern", "Signal Processing Intern", "Firmware Intern",
    "Embedded Software / Hardware Intern", "Controls Engineering Co-op",
    "Instrumentation Intern", "Avionics Intern", "Hardware Validation Intern",
    "Digital Design Verification Intern", "Wireless Engineering Intern",
])
def test_ee_titles(title):
    assert filters.is_internship(title)
    assert filters.role_matches(title, "ee")
    assert filters.role_category(title, "ee") != "Other"


@pytest.mark.parametrize("title", [
    "Software Engineering Intern", "Data Science Intern", "Systems Intern",
    "Test Engineering Intern", "Validation Intern", "Mechanical Engineer Intern",
    "Civil Engineering Intern", "Power BI Analyst Intern", "PowerPoint Intern",
    "Hardware Sales Intern", "Electrical Product Management Intern",
    "Corporate Communications Intern", "Firmware Recruiting Intern",
    "FPGA PhD Intern", "Marketing Intern - Electronics",
    "Hardware Sourcing Intern", "Electrical Procurement Intern",
    "Electrical Engineer I (For 2026 Interns Only)",
])
def test_ambiguous_and_unrelated_titles_are_rejected(title):
    assert not ee.is_ee(title)


def test_upstream_scopes_and_defaults_are_preserved():
    assert config.validate_config({})["role_scope"] == "tech"
    assert config.validate_config({"role_scope": "ee"})["role_scope"] == "ee"
    assert filters.role_matches("Software Intern", "tech")
    assert not filters.role_matches("Electrical Intern", "tech")
    assert filters.role_matches("Marketing Intern", "all")
    with pytest.raises(ValueError):
        filters.role_matches("Intern", "typo")


def test_scope_switch_closes_software_even_without_a_new_fetch():
    records = {
        "swe": {"title": "Software Intern", "is_open": True},
        "ee": {"title": "Electrical Intern", "is_open": True},
    }
    pipeline._close_out_of_scope(records, config.validate_config({"role_scope": "ee"}))
    assert not records["swe"]["is_open"]
    assert records["swe"]["closed_reason"] == "out-of-scope"
    assert records["ee"]["is_open"]


@pytest.mark.parametrize("title", [
    "2027 Electrical Engineer Intern", "Electrical Co-op (June - Dec 2027)",
])
def test_cleanup_agrees_with_ingestion_year_and_month_fallbacks(title):
    cfg = config.validate_config({"role_scope": "ee"})
    record = {"title": title, "is_open": True, "season": "Summer 2027"}
    assert filters.detect_season(title, config.cycles(cfg)) == "Summer 2027"
    assert pipeline._close_out_of_scope({"a": record}, cfg) == 0
    assert record["is_open"]


def test_ingestion_uses_same_scope_and_ee_category():
    company = {"name": "Acme", "slug": "acme", "ats": "greenhouse"}
    jobs = [models.Job(
        id=f"greenhouse:acme:{i}", source="greenhouse", company="Acme",
        company_slug="acme", title=title, location="Austin, TX",
        url=f"https://example.com/{i}", posted_at="2026-10-01T00:00:00Z",
    ) for i, title in enumerate([
        "Electrical Intern - Summer 2027", "Software Intern - Summer 2027",
    ])]
    cfg = config.validate_config({"role_scope": "ee"})
    kept, *_ = pipeline._keep_matching([(company, models.Fetch(jobs), None)], cfg, {})
    assert len(kept) == 1
    assert kept[0].category == "Electrical & Hardware"


def test_ee_dashboard_has_no_inherited_signup():
    dashboard.generate({}, {"generated_at": "2026-10-23T00:00:00Z"})
    html = open(paths.DASHBOARD_PATH, encoding="utf-8").read()
    assert "Electrical Engineering internships" in html
    assert "kvgkvgduomwuszbrygam" not in html
    assert "request_email_subscription" not in html
    for name in ("confirm.html", "unsubscribe.html"):
        text = open(f"{paths.DOCS_DIR}/{name}", encoding="utf-8").read()
        assert "supabase" not in text
        assert "not configured" in text


def test_ee_feed_does_not_announce_inherited_software_closures():
    records = {
        "ee": {"id": "ee", "company": "EE Co", "title": "Electrical Intern",
               "is_open": True, "url": "https://example.com/ee"},
        "swe": {"id": "swe", "company": "Software Co", "title": "Software Intern",
                "is_open": False, "first_seen_at": "2026-10-22T00:00:00Z"},
    }
    assert publish.write_feed(records, data_as_of="2026-10-23T00:00:00Z") == 1
    text = open(paths.FEED_PATH, encoding="utf-8").read()
    assert "Electrical Intern" in text
    assert "Software Co" not in text


def test_ee_radar_does_not_reuse_software_history(monkeypatch):
    monkeypatch.setattr(radar, "_known_cache", {
        "software-co": {"name": "Software Co", "precision": "rolling"},
    })
    monkeypatch.setattr(radar, "_observed_cache", {"companies": {}})
    assert radar.scoped_rows({}, "Summer 2027") == []


def test_dashboard_history_does_not_mix_scope_counts():
    with open(paths.HISTORY_PATH, "w", encoding="utf-8") as f:
        f.write(json.dumps({"open": 1200}) + "\n")
        f.write(json.dumps({"open": 80, "role_scope": "ee"}) + "\n")
    assert dashboard._history_points() == [{"open": 80, "role_scope": "ee"}]


def test_ee_analytics_exclude_inherited_software_cohorts():
    records = {
        "ee": {"title": "Firmware Intern"},
        "swe": {"title": "Software Intern"},
    }
    assert pipeline._analytics_records(records) == {"ee": records["ee"]}


def test_overlay_is_additive_and_discovery_registry_stays_separate(tmp_path, monkeypatch):
    base = {"name": "Base", "slug": "base", "ats": "lever"}
    extra = {"name": "EE", "slug": "ee", "ats": "lever"}
    main = tmp_path / "companies.json"
    main.write_text(json.dumps([base]))
    overlay = tmp_path / "companies.ee.json"
    overlay.write_text(json.dumps([extra]))
    monkeypatch.setattr(paths, "COMPANIES_PATH", str(main))
    monkeypatch.setattr(paths, "DATA_DIR", str(tmp_path))
    assert registry.load() == [base]
    assert registry.load_for_collection() == [base, extra]
    assert json.loads(main.read_text()) == [base]
    overlay.write_text(json.dumps([{**base, "name": "Conflict"}]))
    with pytest.raises(registry.RegistryCorrupt, match="conflicts"):
        registry.load_for_collection()
