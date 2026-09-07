import json
import copy
import pytest
import subprocess
import sys
from pathlib import Path

from scripts.validate_design_delivery_evidence import validate_manifest


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize('field', ['surfaces', 'path'])
@pytest.mark.parametrize('value', [None, {}, [], True, '', ' '])
def test_surface_and_render_types_name_their_findings(tmp_path, field, value):
    original = ROOT / 'tests/fixtures/design-delivery/manifest.json'
    data = json.loads(original.read_text(encoding='utf-8'))
    if field == 'surfaces':
        data['surfaces'] = [value]
    else:
        data['renders'][0]['path'] = value
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(data), encoding='utf-8')
    expected = 'surfaces must' if field == 'surfaces' else 'render 0 must provide a path'
    assert any(expected in finding for finding in validate_manifest(path))


def test_nul_render_path_fails_function_and_cli(tmp_path):
    original = ROOT / 'tests/fixtures/design-delivery/manifest.json'
    data = json.loads(original.read_text(encoding='utf-8'))
    data['renders'][0]['path'] = 'bad\x00.svg'
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(data), encoding='utf-8')
    assert any('render 0 invalid or inaccessible path' in e for e in validate_manifest(path))
    result = subprocess.run([sys.executable, str(ROOT / 'scripts/validate_design_delivery_evidence.py'), str(path)],
                            capture_output=True, text=True)
    assert result.returncode == 1
    assert 'invalid or inaccessible path' in result.stdout
    assert 'Traceback' not in result.stderr


@pytest.mark.parametrize('value', [None, [], {}, True, '', ' '])
@pytest.mark.parametrize('field', ['owner', 'artifact_id', 'artifact_type', 'verdict', 'stage_result', 'check_result', 'check_id', 'evidence_type', 'verification'])
def test_malformed_nested_fields_fail_without_crash(tmp_path, field, value):
    original = ROOT / 'tests/fixtures/design-delivery/manifest.json'
    data = copy.deepcopy(json.loads(original.read_text(encoding='utf-8')))
    for render in data['renders']:
        render['path'] = str((original.parent / render['path']).resolve())
    if field == 'stage_result':
        data['stages']['generation']['result'] = value
    elif field in ('check_result', 'check_id'):
        data['checks'][0][field.removeprefix('check_')] = value
    elif field in ('evidence_type', 'verification'):
        record = {'type': 'command-log', 'reference': 'retained-log.txt', 'verification': 'AUTOMATED'}
        record['type' if field == 'evidence_type' else 'verification'] = value
        data['stages']['generation'] = {'result': 'PASS', 'evidence': [record]}
    else:
        data[field] = value
    path = tmp_path / 'manifest.json'
    path.write_text(json.dumps(data), encoding='utf-8')
    assert validate_manifest(path)


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
