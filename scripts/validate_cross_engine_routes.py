"""Validate declared cross-engine handoffs against a sibling-engine workspace."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def validate_cross_engine_routes(root: Path, workspace_root: Path) -> list[str]:
    findings: list[str] = []
    fixture_path = root / "tests" / "cross-engine-route-fixtures.yml"
    try:
        fixtures = yaml.safe_load(fixture_path.read_text(encoding="utf-8")) or []
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot read cross-engine route fixtures: {exc}"]
    if not isinstance(fixtures, list):
        return ["cross-engine route fixtures must be a list"]

    for index, fixture in enumerate(fixtures):
        if not isinstance(fixture, dict):
            findings.append(f"cross-engine route fixture {index} must be an object")
            continue
        label = str(fixture.get("id", index))
        source_value = str(fixture.get("source", ""))
        reference = str(fixture.get("reference", ""))
        repository = str(fixture.get("target_repository", ""))
        target_value = str(fixture.get("target", ""))
        source = root / source_value
        if not source.is_file():
            findings.append(f"cross-engine route {label} source not found: {source_value}")
        elif reference not in source.read_text(encoding="utf-8"):
            findings.append(f"cross-engine route {label} reference absent from source: {reference}")

        target_repository = workspace_root / repository
        if not target_repository.is_dir():
            findings.append(
                f"cross-engine route {label} NOT ASSESSED: target repository not found: {repository}"
            )
            continue
        target = target_repository / target_value
        if not target.is_file():
            findings.append(f"cross-engine route {label} target not found: {repository}/{target_value}")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument(
        "--workspace-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="directory containing the named sibling repositories",
    )
    args = parser.parse_args()
    findings = validate_cross_engine_routes(args.root.resolve(), args.workspace_root.resolve())
    print("cross-engine-route-validator:")
    print(f"- workspace: {args.workspace_root.resolve()}")
    print(f"- findings: {len(findings)}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: all declared cross-engine handoffs resolve in the inspected workspace")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
