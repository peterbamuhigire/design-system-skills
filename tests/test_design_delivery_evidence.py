import json
from pathlib import Path

from scripts.validate_design_delivery_evidence import validate_manifest


ROOT = Path(__file__).resolve().parents[1]


def test_design_delivery_fixture_is_conditionally_valid():
    path = ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    assert validate_manifest(path) == []
    assert data["verdict"] == "CONDITIONAL"
    assert set(data["stages"]) == {"generation", "reopen", "render", "visual_qa", "accessibility"}
    assert all(stage["result"] == "NOT ASSESSED" for stage in data["stages"].values())


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


def test_pass_manifest_cannot_hide_unassessed_stage():
    path = ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["verdict"] = "PASS"
    temp = ROOT / "tests" / "fixtures" / "design-delivery" / "pass-with-unassessed-stage.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        assert any("required delivery stage" in item for item in validate_manifest(temp))
    finally:
        temp.unlink()


def test_malformed_manifest_reports_a_finding_instead_of_crashing():
    temp = ROOT / "tests" / "fixtures" / "design-delivery" / "malformed-manifest.json"
    temp.write_text(json.dumps(["not", "an", "object"]), encoding="utf-8")
    try:
        assert validate_manifest(temp) == ["manifest root must be an object"]
    finally:
        temp.unlink()


def test_pass_manifest_rejects_self_asserted_stage_evidence():
    path = ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["verdict"] = "PASS"
    for stage in data["stages"].values():
        stage["result"] = "PASS"
        stage["evidence"] = "owner says this stage passed"
    for check in data["checks"]:
        check["result"] = "PASS"
    temp = ROOT / "tests" / "fixtures" / "design-delivery" / "self-asserted-pass.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        findings = validate_manifest(temp)
        assert any("self-assertion is not evidence" in item for item in findings)
    finally:
        temp.unlink()


def test_pass_manifest_rejects_unassessed_required_check():
    path = ROOT / "tests" / "fixtures" / "design-delivery" / "manifest.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["verdict"] = "PASS"
    for stage in data["stages"].values():
        stage["result"] = "PASS"
        stage["evidence"] = [
            {
                "type": "retained-artifact",
                "reference": "evidence/stage-record.md",
                "verification": "INDEPENDENT",
            }
        ]
    data["checks"][0]["result"] = "NOT ASSESSED"
    for check in data["checks"][1:]:
        check["result"] = "PASS"
    temp = ROOT / "tests" / "fixtures" / "design-delivery" / "pass-with-unassessed-check.json"
    temp.write_text(json.dumps(data), encoding="utf-8")
    try:
        findings = validate_manifest(temp)
        assert any("required checks are not PASS" in item for item in findings)
    finally:
        temp.unlink()


def test_retained_adversarial_fixtures_are_rejected():
    malformed = ROOT / "tests" / "fixtures" / "design-delivery" / "adversarial" / "malformed-root.json"
    self_asserted = ROOT / "tests" / "fixtures" / "design-delivery" / "adversarial" / "self-asserted-pass.json"
    assert validate_manifest(malformed) == ["manifest root must be an object"]
    assert any("self-assertion is not evidence" in item for item in validate_manifest(self_asserted))
