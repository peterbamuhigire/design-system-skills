import json
from pathlib import Path

from scripts.validate_design_delivery_evidence import validate_manifest


ROOT = Path(__file__).resolve().parents[1]


def test_design_delivery_fixture_passes():
    assert validate_manifest(ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json") == []


def test_pass_manifest_cannot_hide_missing_render():
    path = ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["renders"][0]["path"] = "missing.svg"
    temp = ROOT / "tests" / "fixtures" / "design-delivery" / "missing-render-manifest.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        assert any("not found" in item for item in validate_manifest(temp))
    finally:
        temp.unlink()
