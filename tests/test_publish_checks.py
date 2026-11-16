import json
from datetime import UTC, datetime, timedelta

import pytest

from intern_engine import config, mailer, paths, registry
from tools import verify_accuracy


@pytest.fixture
def registry_files(tmp_path, monkeypatch):
    base = [{"name": "Base", "ats": "ashby", "slug": "base"}]
    overlay = [{"name": "Extra", "ats": "jazzhr", "slug": "extra"}]
    (tmp_path / "companies.json").write_text(json.dumps(base), encoding="utf-8")
    (tmp_path / "companies.ee.json").write_text(json.dumps(overlay), encoding="utf-8")
    monkeypatch.setattr(paths, "DATA_DIR", str(tmp_path))
    monkeypatch.setattr(paths, "COMPANIES_PATH", str(tmp_path / "companies.json"))
    monkeypatch.setattr(config, "load_config", lambda: {"role_scope": "ee"})
    monkeypatch.delenv("ALLOW_REGISTRY_DRIFT", raising=False)
    return tmp_path


def test_publish_gate_counts_ee_overlay_and_still_detects_drift(registry_files):
    assert verify_accuracy.registry_drift(2) is None
    assert "registry has 2" in verify_accuracy.registry_drift(1)


def test_tech_scope_counts_only_base(registry_files, monkeypatch):
    monkeypatch.setattr(config, "load_config", lambda: {"role_scope": "tech"})
    assert verify_accuracy.registry_drift(1) is None
    assert verify_accuracy.registry_drift(2)


def test_ci_allows_historical_count_but_still_rejects_corrupt_registry(
        registry_files, monkeypatch):
    monkeypatch.setenv("ALLOW_REGISTRY_DRIFT", "1")
    assert verify_accuracy.registry_drift(1) is None
    (registry_files / "companies.ee.json").write_text("broken", encoding="utf-8")
    with pytest.raises(registry.RegistryCorrupt):
        verify_accuracy.registry_drift(1)


@pytest.mark.parametrize(
    ("fetched", "workday_errors", "workday_quarantined", "allowed"),
    [
        (2999, 1709, 100, True),   # outside Workday: 2938 / 3238
        (2500, 1709, 100, False),  # other providers also degraded
        (2999, 50, 100, False),    # few Workday errors
        (2999, 180, 1600, False),  # Workday was mostly quarantined
        (2999, 1709, None, False), # old snapshot lacks outage evidence
    ],
)
def test_registry_coverage_during_workday_outage(
    fetched, workday_errors, workday_quarantined, allowed,
):
    stats = {
        "companies_total": 5108,
        "companies_by_source": {"workday": 1870, "other": 3238},
        "fetched_ok": fetched,
        "quarantined": max(371, workday_quarantined or 0),
        "errors_by_source": {"workday": workday_errors},
        "workday_quarantined": workday_quarantined,
        "fetch_success_rate_registry": fetched / 5108,
    }
    gates, warnings = [], []
    verify_accuracy.check_registry_coverage(stats, gates, warnings)
    if allowed:
        assert not gates and "[workday-outage]" in warnings[0]
    else:
        assert not warnings and "[registry-decay]" in gates[0]


@pytest.fixture
def no_email(monkeypatch):
    for name in ("BREVO_API_KEY", "SUPABASE_URL", "SUPABASE_SERVICE_KEY", "MAIL_FROM"):
        monkeypatch.delenv(name, raising=False)


def test_unused_email_ignores_inherited_digest_history(no_email):
    old = (datetime.now(UTC) - timedelta(days=10)).isoformat()
    assert mailer.delivery_health({"last_digest_at": old}, 333) == (
        True, "email service is not configured")


def test_partial_email_configuration_still_fails(no_email, monkeypatch):
    monkeypatch.setenv("BREVO_API_KEY", "test-key")
    ok, reason = mailer.delivery_health({}, 333)
    assert not ok and "SUPABASE_URL" in reason and "MAIL_FROM" in reason


def test_configured_email_still_detects_stalled_delivery(no_email, monkeypatch):
    for name, value in {"BREVO_API_KEY": "test-key", "SUPABASE_URL": "https://db.test",
                        "SUPABASE_SERVICE_KEY": "test-key", "MAIL_FROM": "test@example.com"}.items():
        monkeypatch.setenv(name, value)
    old = (datetime.now(UTC) - timedelta(days=10)).isoformat()
    ok, reason = mailer.delivery_health({"last_digest_at": old}, 333)
    assert not ok and "333 roles waiting" in reason
    monkeypatch.setenv("MAIL_FROM", "invalid")
    assert not mailer.delivery_health({}, 0)[0]
