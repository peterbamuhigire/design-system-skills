"""Constraint-checked design-system assembly and portable output formats."""

from __future__ import annotations

import json
from typing import Any

from .catalog import Catalog, STACKS


class DecisionError(ValueError):
    """Raised when a design brief is incomplete, contradictory, or unsafe."""


ALLOWED_BRIEF_KEYS = {
    "name",
    "audience",
    "job",
    "outcome",
    "mode",
    "stack",
    "brand",
    "must_have",
    "must_not",
    "density",
    "motion",
    "variance",
}


def _require_text(brief: dict[str, Any], key: str) -> str:
    value = brief.get(key)
    if not isinstance(value, str) or not value.strip():
        raise DecisionError(f"brief field is required: {key}")
    return value.strip()


def _dial(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 10:
        raise DecisionError(f"{name} must be an integer from 1 to 10")
    return value


def _terms(values: Any, key: str) -> list[str]:
    if values is None:
        return []
    if not isinstance(values, list) or not all(isinstance(item, str) and item.strip() for item in values):
        raise DecisionError(f"{key} must be a list of non-empty strings")
    return [item.strip() for item in values]


def _best(catalog: Catalog, query: str, domain: str, stack: str | None) -> dict[str, Any]:
    result = catalog.search(query, domain=domain, stack=stack, strict=True, limit=3)
    return result["results"][0]


def build_design_system(brief: dict[str, Any], catalog: Catalog) -> dict[str, Any]:
    if not isinstance(brief, dict):
        raise DecisionError("brief must be an object")
    unknown = set(brief).difference(ALLOWED_BRIEF_KEYS)
    if unknown:
        raise DecisionError(f"unknown brief keys: {sorted(unknown)}")
    name = _require_text(brief, "name")
    audience = _require_text(brief, "audience")
    job = _require_text(brief, "job")
    outcome = _require_text(brief, "outcome")
    mode = brief.get("mode", "app")
    if mode not in {"app", "marketing"}:
        raise DecisionError("mode must be app or marketing")
    stack = brief.get("stack")
    if stack is not None and stack not in STACKS:
        raise DecisionError(f"unsupported stack: {stack}")
    if stack is not None:
        catalog.search("component", stack=stack, limit=1)
    must_have = _terms(brief.get("must_have"), "must_have")
    must_not = _terms(brief.get("must_not"), "must_not")
    if set(item.casefold() for item in must_have).intersection(item.casefold() for item in must_not):
        raise DecisionError("brief contains contradictory must_have and must_not constraints")
    dials = {
        "density": _dial(brief.get("density", 5), "density"),
        "motion": _dial(brief.get("motion", 4), "motion"),
        "variance": _dial(brief.get("variance", 4), "variance"),
    }
    style = _best(catalog, f"{job} {outcome} {mode}", "style", stack)
    typography = _best(catalog, f"{audience} readability localization", "typography", stack)
    color = _best(catalog, f"{job} state contrast theme", "color", stack)
    ux = _best(catalog, f"{job} error recovery focus", "ux", stack)
    chart = _best(catalog, f"{job} capacity comparison decision", "chart", stack)
    product = _best(catalog, f"{job} {outcome}", "product", stack)
    decisions = {
        "product": product,
        "style": style,
        "typography": typography,
        "color": color,
        "ux": ux,
        "chart": chart,
    }
    for item in must_not:
        if any(item.casefold() in json.dumps(value, ensure_ascii=False).casefold() for value in decisions.values()):
            raise DecisionError(f"catalog decision conflicts with must_not constraint: {item}")
    return {
        "schema_version": "1.0",
        "catalog_revision": catalog.revision,
        "decision_id": f"{name.casefold().replace(' ', '-')}-design-system",
        "brief": {
            "name": name,
            "audience": audience,
            "job": job,
            "outcome": outcome,
            "mode": mode,
            "stack": stack,
            "brand": brief.get("brand"),
            "must_have": must_have,
            "must_not": must_not,
        },
        "dials": dials,
        "decisions": decisions,
        "alternatives": {
            "style": [style["record_id"]],
            "interaction": [ux["record_id"]],
        },
        "evidence_contract": {
            "required": [
                "state-and-content-matrix",
                "token-to-render-trace",
                "responsive-and-keyboard-check",
                "independent-review",
            ],
            "status": "NOT_ASSESSED",
        },
        "provenance": {
            "catalog_source": str(catalog.source) if catalog.source else "in-memory",
            "catalog_revision": catalog.revision,
            "method": "deterministic lexical retrieval plus typed constraint checks",
        },
    }


def format_decision(decision: dict[str, Any], output: str = "json") -> str:
    if output == "json":
        return json.dumps(decision, ensure_ascii=False, indent=2, sort_keys=True)
    if output not in {"markdown", "text"}:
        raise DecisionError("output must be json, markdown, or text")
    brief = decision["brief"]
    lines = [
        f"Design system: {brief['name']}",
        f"Mode: {brief['mode']} | Stack: {brief.get('stack') or 'unspecified'}",
        f"Audience: {brief['audience']}",
        f"Job: {brief['job']}",
        f"Outcome: {brief['outcome']}",
        "",
        "Dials:",
        *(f"- {key}: {value}/10" for key, value in decision["dials"].items()),
        "",
        "Decisions:",
    ]
    for key, value in decision["decisions"].items():
        lines.append(f"- {key}: {value['title']} [{value['record_id']}]")
    lines.extend(
        [
            "",
            "Evidence status: NOT_ASSESSED until the required render, interaction, review, and trace records exist.",
        ]
    )
    return "\n".join(lines)
