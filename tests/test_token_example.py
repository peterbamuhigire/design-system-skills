import json
from pathlib import Path

from scripts.validate_token_example import validate


ROOT = Path(__file__).resolve().parents[1]
TOKEN_SOURCE = ROOT / "skills/09-design-systems-tokens-and-theming/design-tokens-and-naming/examples/tokens.json"


def test_canonical_token_example_passes():
    assert validate(TOKEN_SOURCE) == []


def test_component_primitive_bypass_fails(tmp_path):
    data = json.loads(TOKEN_SOURCE.read_text(encoding="utf-8"))
    data["button"]["primary"]["radius"]["$value"] = "{radius.200}"
    path = tmp_path / "tokens.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    findings = validate(path)
    assert any("component token must reference the semantic tier" in item for item in findings)


def test_alias_cycle_fails(tmp_path):
    data = json.loads(TOKEN_SOURCE.read_text(encoding="utf-8"))
    data["semantic"]["radius"]["control"]["sm"]["$value"] = "{semantic.radius.control.md}"
    data["semantic"]["radius"]["control"]["md"] = {"$value": "{semantic.radius.control.sm}", "$type": "dimension"}
    path = tmp_path / "tokens.json"
    path.write_text(json.dumps(data), encoding="utf-8")
    findings = validate(path)
    assert any("alias cycle" in item for item in findings)
