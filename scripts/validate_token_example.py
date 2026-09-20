#!/usr/bin/env python3
"""Fail-closed checks for the canonical three-tier token example.

This is a structural guard, not a contrast calculator or a claim of full DTCG
conformance. It checks the house invariant that components resolve through the
semantic layer and that all aliases resolve without cycles or type mismatches.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

REFERENCE = re.compile(r"^\{([^{}]+)\}$")
PRIMITIVE_ROOTS = {"color", "space", "font", "radius", "elevation", "duration", "easing"}
RESERVED_ROOTS = {"$description", "_themes", "semantic"} | PRIMITIVE_ROOTS


def _walk(node: object, path: tuple[str, ...] = ()) -> dict[str, dict]:
    found: dict[str, dict] = {}
    if not isinstance(node, dict):
        return found
    if "$value" in node:
        found[".".join(path)] = node
    for key, value in node.items():
        if not key.startswith("$") and key != "$value":
            found.update(_walk(value, path + (key,)))
    return found


def validate(path: Path) -> list[str]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        return [f"cannot read token source: {exc}"]
    if not isinstance(data, dict):
        return ["token source must be an object"]

    tokens = _walk(data)
    findings: list[str] = []
    for token_path, record in tokens.items():
        value = record.get("$value")
        if not isinstance(value, str):
            continue
        match = REFERENCE.fullmatch(value)
        if not match:
            continue
        target = match.group(1)
        if target not in tokens:
            findings.append(f"{token_path}: unresolved reference {target}")
        elif record.get("$type") and tokens[target].get("$type") and record["$type"] != tokens[target]["$type"]:
            findings.append(f"{token_path}: type {record['$type']} differs from {target} type {tokens[target]['$type']}")

    graph: dict[str, str] = {}
    for token_path, record in tokens.items():
        value = record.get("$value")
        if isinstance(value, str):
            match = REFERENCE.fullmatch(value)
            if match and match.group(1) in tokens:
                graph[token_path] = match.group(1)

    def visit(node: str, trail: list[str]) -> None:
        if node in trail:
            findings.append("alias cycle: " + " -> ".join(trail[trail.index(node):] + [node]))
            return
        target = graph.get(node)
        if target:
            visit(target, trail + [node])

    for token_path in graph:
        visit(token_path, [])

    component_tokens = {
        token_path: record
        for token_path, record in tokens.items()
        if token_path.split(".", 1)[0] not in RESERVED_ROOTS
    }
    for token_path, record in component_tokens.items():
        value = record.get("$value")
        if not isinstance(value, str):
            findings.append(f"{token_path}: component token must reference semantic token")
            continue
        match = REFERENCE.fullmatch(value)
        if not match or not match.group(1).startswith("semantic."):
            findings.append(f"{token_path}: component token must reference the semantic tier")

    if "button.primary.radius" in tokens:
        value = tokens["button.primary.radius"].get("$value")
        if value != "{semantic.radius.control.sm}":
            findings.append("button.primary.radius: expected semantic radius alias")
    required = {
        "semantic.color.action.danger.bg",
        "semantic.color.action.danger.fg",
        "semantic.radius.control.sm",
    }
    for token_path in sorted(required - tokens.keys()):
        findings.append(f"missing required semantic token: {token_path}")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("token_source", type=Path)
    args = parser.parse_args()
    findings = validate(args.token_source.resolve())
    print("token-example-validator:")
    print(f"- source: {args.token_source}")
    print(f"- findings: {len(findings)}")
    for finding in findings:
        print(f"[FAIL] {finding}")
    if not findings:
        print("PASS: aliases, tiers, required roles and cycle checks passed")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
