"""Validate repaired local route references and every routing-fixture target."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def active_skills(root: Path) -> dict[str, Path]:
    return {
        path.parent.name: path
        for path in root.glob("skills/**/SKILL.md")
        if "_TEMPLATE" not in path.parts
    }


def validate_routes(root: Path) -> list[str]:
    findings: list[str] = []
    skills = active_skills(root)

    routing_path = root / "tests" / "routing-fixtures.yml"
    routing = yaml.safe_load(routing_path.read_text(encoding="utf-8")) or []
    for index, fixture in enumerate(routing):
        expected = str(fixture.get("expected", ""))
        if expected not in skills:
            findings.append(f"routing fixture {index} targets missing skill: {expected}")

    fixture_path = root / "tests" / "route-existence-fixtures.yml"
    fixtures = yaml.safe_load(fixture_path.read_text(encoding="utf-8")) or []
    for index, fixture in enumerate(fixtures):
        source_value = str(fixture.get("source", ""))
        reference = str(fixture.get("reference", ""))
        target_value = str(fixture.get("target", ""))
        source = root / source_value
        target = root / target_value
        label = str(fixture.get("id", index))
        if not source.is_file():
            findings.append(f"route fixture {label} source not found: {source_value}")
        elif reference not in source.read_text(encoding="utf-8"):
            findings.append(f"route fixture {label} reference absent from source: {reference}")
        if not target.is_file():
            findings.append(f"route fixture {label} target not found: {target_value}")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    findings = validate_routes(args.root.resolve())
    print("route-existence-validator:")
    print(f"- checked routing fixtures and repaired-route fixtures")
    print(f"- findings: {len(findings)}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: route targets exist and repaired references are present")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
