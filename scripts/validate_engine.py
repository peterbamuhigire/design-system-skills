"""Validate design-system-skills structure and prevent quality regression."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

import yaml


ALLOWED_FRONTMATTER = {"name", "description", "license", "allowed-tools", "metadata"}
REQUIRED_HEADINGS = {
    "use when",
    "do not use when",
    "workflow",
    "outputs",
    "anti-patterns",
    "examples",
    "references",
}
PORTABLE_HEADINGS = {"capability contract", "degraded mode", "decision rules"}
ENCODING_NOISE = ("\ufffd", "â€”", "â€“", "â€™", "Ã—", "Â§")
FONT_CATEGORIES = (
    "01-formal-institutional",
    "02-editorial-literary",
    "03-modern-product-grotesque",
    "04-technical-data-code",
    "05-friendly-humanist",
    "06-expressive-display-artistic",
    "07-script-cursive-handwritten",
    "08-body-ui-workhorses",
)


def frontmatter(text: str) -> tuple[dict, str | None]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        return {}, "missing or unclosed frontmatter"
    try:
        data = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError as exc:
        return {}, f"invalid YAML: {exc.__class__.__name__}"
    return data if isinstance(data, dict) else {}, None


def is_empty_section(text: str, heading: str) -> bool:
    pattern = rf"(?ims)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text)
    if not match:
        return True
    body = re.sub(r"<!--.*?-->", "", match.group(1), flags=re.S).strip()
    return not body


def section_body(text: str, heading_pattern: str) -> str:
    pattern = rf"(?ims)^##\s+(?:{heading_pattern})\s*$\n(.*?)(?=^##\s+|\Z)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else ""


def scan(root: Path) -> dict:
    skill_files = [p for p in root.glob("skills/**/SKILL.md") if "_TEMPLATE" not in p.parts]
    findings: list[dict] = []
    names: list[str] = []

    for path in sorted(skill_files):
        text = path.read_text(encoding="utf-8")
        data, yaml_error = frontmatter(text)
        failed: list[str] = []
        if yaml_error:
            failed.append("frontmatter_yaml")
        name = data.get("name")
        description = data.get("description")
        metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
        if name:
            names.append(str(name))
        if name != path.parent.name:
            failed.append("identity")
        if set(data) - ALLOWED_FRONTMATTER:
            failed.append("frontmatter_keys")
        if not isinstance(description, str) or not description.startswith("Use when") or len(description) > 350:
            failed.append("trigger")
        if metadata.get("portable") is not True or not {"claude-code", "codex"}.issubset(
            set(metadata.get("compatible_with", []))
        ):
            failed.append("portable_metadata")

        headings = {h.strip().lower() for h in re.findall(r"^##\s+(.+?)\s*$", text, re.M)}
        if not REQUIRED_HEADINGS.issubset(headings):
            failed.append("required_sections")
        if not PORTABLE_HEADINGS.issubset(headings):
            failed.append("portable_contracts")
        if not ({"required inputs", "inputs"} & headings):
            failed.append("input_contract")
        input_body = section_body(text, r"Required Inputs|Inputs")
        output_body = section_body(text, "Outputs")
        decision_body = section_body(text, r"Decision Rules")
        anti_body = section_body(text, r"Anti-Patterns(?:\s*\([^\n]+\))?")
        if "|" not in input_body and not re.match(r"(?i)^None\b", input_body.strip()):
            failed.append("input_contract")
        if "|" not in output_body:
            failed.append("output_contract")
        if "|" not in decision_body or not re.search(r"fail|wrong|risk|consequence", decision_body, re.I):
            failed.append("decision_contract")
        anti_count = len(re.findall(r"(?m)^\s*[-*]\s+", anti_body))
        if anti_count < 5:
            failed.append("anti_pattern_depth")
        if not re.search(r"\b(stop|block|refuse|no-ship)\b", text, re.I):
            failed.append("stop_condition")
        if not re.search(r"\b(recover|recovery|fallback|degraded|conditional|unverified)\b", text, re.I):
            failed.append("recovery_condition")
        for heading in ("Workflow", "Outputs", "Anti-Patterns", "Examples", "References"):
            if is_empty_section(text, heading):
                failed.append("empty_contract_section")
                break
        if len(text.splitlines()) > 500:
            failed.append("line_limit")
        if any(marker in text for marker in ENCODING_NOISE):
            failed.append("encoding_noise")
        if not (path.parent / "examples").is_dir():
            failed.append("worked_example")
        findings.append({"path": path.relative_to(root).as_posix(), "failed": sorted(set(failed))})

    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    missing_fonts = [name for name in FONT_CATEGORIES if not (root / "fonts" / name).is_dir()]
    counts = Counter(code for item in findings for code in item["failed"])
    return {
        "skills": len(skill_files),
        "fully_compliant": sum(not item["failed"] for item in findings),
        "failure_counts": dict(sorted(counts.items())),
        "duplicate_names": duplicates,
        "missing_font_categories": missing_fonts,
        "findings": [item for item in findings if item["failed"]],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--baseline", type=Path)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = scan(args.root.resolve())
    regressions: dict[str, tuple[int, int]] = {}
    if args.baseline:
        baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        current = result["failure_counts"]
        for key in set(current) | set(baseline.get("failure_counts", {})):
            before = int(baseline.get("failure_counts", {}).get(key, 0))
            after = int(current.get(key, 0))
            if after > before:
                regressions[key] = (before, after)
        if result["skills"] < int(baseline.get("skills", 0)):
            regressions["skill_count_drop"] = (int(baseline["skills"]), result["skills"])
    result["regressions"] = regressions
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"skills={result['skills']} fully_compliant={result['fully_compliant']}")
        for key, count in result["failure_counts"].items():
            print(f"{key}={count}")
        for key, values in regressions.items():
            print(f"REGRESSION {key}: {values[0]} -> {values[1]}")
    return 1 if regressions or result["duplicate_names"] or result["missing_font_categories"] else 0


if __name__ == "__main__":
    sys.exit(main())
