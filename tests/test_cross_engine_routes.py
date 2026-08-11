import tempfile
from pathlib import Path

import yaml

from scripts.validate_cross_engine_routes import validate_cross_engine_routes


ROOT = Path(__file__).resolve().parents[1]


def test_cross_engine_route_manifest_checks_source_and_target_shape():
    fixture_path = ROOT / "tests" / "cross-engine-route-fixtures.yml"
    fixtures = yaml.safe_load(fixture_path.read_text(encoding="utf-8"))
    with tempfile.TemporaryDirectory() as workspace:
        workspace_root = Path(workspace)
        for fixture in fixtures:
            target = workspace_root / fixture["target_repository"] / fixture["target"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("fixture target\n", encoding="utf-8")
        assert validate_cross_engine_routes(ROOT, workspace_root) == []


def test_missing_cross_engine_repository_is_not_a_pass():
    with tempfile.TemporaryDirectory() as workspace:
        findings = validate_cross_engine_routes(ROOT, Path(workspace))
    assert len(findings) == 4
    assert all("NOT ASSESSED" in finding for finding in findings)
