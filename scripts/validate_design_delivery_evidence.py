#!/usr/bin/env python3
"""Validate a machine-readable design delivery evidence manifest."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_VERDICTS = {"PASS", "CONDITIONAL", "BLOCKED"}
ALLOWED_RESULTS = {"PASS", "CONDITIONAL", "FAIL", "NOT ASSESSED"}
REQUIRED_CHECKS = {"design-doctrine", "typography", "accessibility", "render-parity"}
REQUIRED_STAGES = {"generation", "reopen", "render", "visual_qa", "accessibility"}
ALLOWED_EVIDENCE_TYPES = {"command-log", "retained-artifact", "independent-review"}
ALLOWED_VERIFICATIONS = {"AUTOMATED", "INDEPENDENT"}


def _validate_stage_evidence(stage: str, value: dict, result: str, findings: list[str]) -> None:
    evidence = value.get("evidence")
    if result == "PASS":
        if not isinstance(evidence, list) or not evidence:
            findings.append(
                f"stage {stage} PASS requires retained evidence records; a self-assertion is not evidence"
            )
            return
        for index, record in enumerate(evidence):
            if not isinstance(record, dict):
                findings.append(f"stage {stage} evidence {index} must be an object")
                continue
            if record.get("type") not in ALLOWED_EVIDENCE_TYPES:
                findings.append(f"stage {stage} evidence {index} must have a retained evidence type")
            if not isinstance(record.get("reference"), str) or not record["reference"].strip():
                findings.append(f"stage {stage} evidence {index} must provide a reference")
            if record.get("verification") not in ALLOWED_VERIFICATIONS:
                findings.append(
                    f"stage {stage} evidence {index} must state AUTOMATED or INDEPENDENT verification"
                )
        return
    if not isinstance(evidence, str) or not evidence.strip():
        findings.append(f"stage {stage} must state evidence or why it is unavailable")


def validate_manifest(manifest_path: Path) -> list[str]:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"cannot read manifest: {exc}"]
    if not isinstance(data, dict):
        return ["manifest root must be an object"]
    findings: list[str] = []
    for key in ("artifact_id", "artifact_type", "surfaces", "renders", "stages", "checks", "verdict", "owner"):
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
    stages = data.get("stages")
    stage_results: dict[str, str] = {}
    if not isinstance(stages, dict):
        findings.append("stages must be an object")
    else:
        missing_stages = sorted(REQUIRED_STAGES - set(stages))
        findings.extend(f"missing required stage: {item}" for item in missing_stages)
        for stage in sorted(REQUIRED_STAGES):
            value = stages.get(stage)
            if not isinstance(value, dict):
                findings.append(f"stage {stage} must be an object")
                continue
            result = value.get("result")
            stage_results[stage] = str(result)
            if result not in ALLOWED_RESULTS:
                findings.append(f"stage {stage} must have a valid result")
            else:
                _validate_stage_evidence(stage, value, result, findings)

    checks = data.get("checks")
    check_results: dict[str, str] = {}
    if not isinstance(checks, list):
        findings.append("checks must be a list")
    else:
        check_ids = [str(c.get("id")) for c in checks if isinstance(c, dict)]
        duplicates = sorted({item for item in check_ids if check_ids.count(item) > 1})
        findings.extend(f"duplicate check id: {item}" for item in duplicates)
        missing = sorted(REQUIRED_CHECKS - set(check_ids))
        findings.extend(f"missing required check: {item}" for item in missing)
        for index, check in enumerate(checks):
            if not isinstance(check, dict) or check.get("result") not in ALLOWED_RESULTS:
                findings.append(f"check {index} must have a valid result")
                continue
            check_results[str(check["id"])] = str(check["result"])
    verdict = data.get("verdict")
    if verdict not in ALLOWED_VERDICTS:
        findings.append(f"verdict must be one of {sorted(ALLOWED_VERDICTS)}")
    if verdict == "PASS":
        incomplete_stages = sorted(
            stage for stage in REQUIRED_STAGES if stage_results.get(stage) != "PASS"
        )
        if incomplete_stages:
            findings.append(
                "PASS is forbidden while required delivery stages are not PASS: "
                + ", ".join(incomplete_stages)
            )
        incomplete_checks = sorted(
            check for check in REQUIRED_CHECKS if check_results.get(check) != "PASS"
        )
        if incomplete_checks:
            findings.append(
                "PASS is forbidden while required checks are not PASS: "
                + ", ".join(incomplete_checks)
            )
    if verdict == "PASS" and findings:
        findings.append("PASS is forbidden while findings exist")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    manifest_path = args.manifest.resolve()
    findings = validate_manifest(manifest_path)
    try:
        manifest_data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        manifest_data = {}
    if not isinstance(manifest_data, dict):
        manifest_data = {}
    print("design-delivery-evidence-validator:")
    print(f"- manifest: {args.manifest}")
    print(f"- findings: {len(findings)}")
    print(f"- delivery verdict: {manifest_data.get('verdict', 'UNKNOWN')}")
    stages = manifest_data.get("stages")
    if isinstance(stages, dict):
        stage_summary = ", ".join(
            f"{name}={value.get('result', 'UNKNOWN')}"
            for name, value in sorted(stages.items())
            if isinstance(value, dict)
        )
        print(f"- stages: {stage_summary}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: manifest structure is valid; delivery verdict is reported above")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
