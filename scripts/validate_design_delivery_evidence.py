#!/usr/bin/env python3
"""Validate a machine-readable design delivery evidence manifest."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_VERDICTS = {"PASS", "CONDITIONAL", "BLOCKED"}
REQUIRED_CHECKS = {"design-doctrine", "typography", "accessibility", "render-parity"}


def validate_manifest(manifest_path: Path) -> list[str]:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"]
    findings: list[str] = []
    for key in ("artifact_id", "surfaces", "renders", "checks", "verdict", "owner"):
        if key not in data:
            findings.append(f"missing required field: {key}")
    surfaces = data.get("surfaces")
    if not isinstance(surfaces, list) or not surfaces or any(not str(x).strip() for x in surfaces):
        findings.append("surfaces must be a non-empty list")
    renders = data.get("renders")
    if not isinstance(renders, list) or not renders:
        findings.append("renders must be a non-empty list")
    else:
        for index, render in enumerate(renders):
            if not isinstance(render, dict) or not str(render.get("path", "")).strip():
                findings.append(f"render {index} must provide a path")
                continue
            path = (manifest_path.parent / str(render["path"])).resolve()
            if not path.is_file():
                findings.append(f"render {index} not found: {render['path']}")
    checks = data.get("checks")
    if not isinstance(checks, list):
        findings.append("checks must be a list")
    else:
        check_ids = {str(c.get("id")) for c in checks if isinstance(c, dict)}
        missing = sorted(REQUIRED_CHECKS - check_ids)
        findings.extend(f"missing required check: {item}" for item in missing)
        for index, check in enumerate(checks):
            if not isinstance(check, dict) or check.get("result") not in {"PASS", "CONDITIONAL", "FAIL", "NOT ASSESSED"}:
                findings.append(f"check {index} must have a valid result")
    verdict = data.get("verdict")
    if verdict not in ALLOWED_VERDICTS:
        findings.append(f"verdict must be one of {sorted(ALLOWED_VERDICTS)}")
    if verdict == "PASS" and findings:
        findings.append("PASS is forbidden while findings exist")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    findings = validate_manifest(args.manifest.resolve())
    print("design-delivery-evidence-validator:")
    print(f"- manifest: {args.manifest}")
    print(f"- findings: {len(findings)}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: design delivery evidence is complete")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
