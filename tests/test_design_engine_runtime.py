from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.design_engine.catalog import Catalog, CatalogError, NoResultsError, default_catalog_path
from engine.design_engine.decisions import DecisionError, build_design_system, format_decision
from engine.design_engine.persistence import PersistenceError, resolve_project, save_page_override, save_project


@pytest.fixture()
def catalog() -> Catalog:
    return Catalog.from_file(default_catalog_path())


def test_catalog_has_all_domains_and_stacks(catalog: Catalog) -> None:
    assert len(catalog.records) == 13
    assert len(catalog.stack_guidance) == 22


def test_search_is_deterministic_and_explains_match(catalog: Catalog) -> None:
    first = catalog.search("usability research retest", domain="ux", stack="react")
    second = catalog.search("usability research retest", domain="ux", stack="react")
    assert first == second
    assert first["results"][0]["record_id"] == "ux-observe-fix-retest"
    assert first["results"][0]["explanation"]


def test_synonyms_and_explicit_domain_work(catalog: Catalog) -> None:
    result = catalog.search("colour contrast danger", domain="color")
    assert result["route"]["reason"] == "explicit domain"
    assert result["results"][0]["record_id"] == "color-semantic-state"


def test_invalid_domain_and_stack_are_typed_errors(catalog: Catalog) -> None:
    with pytest.raises(CatalogError):
        catalog.search("button", domain="not-a-domain")
    with pytest.raises(CatalogError):
        catalog.search("button", stack="not-a-stack")
    assert catalog.search("component state", domain="react", stack="vue")["abstained"] is True


def test_status_filter_keeps_deprecated_guidance_out_of_current_results(catalog: Catalog) -> None:
    assert catalog.search("legacy flat", domain="style")["abstained"] is True
    legacy = catalog.search("legacy flat", domain="style", status="legacy")
    assert legacy["results"][0]["record_id"] == "style-legacy-flat"


def test_strict_search_abstains_instead_of_fabricating(catalog: Catalog) -> None:
    with pytest.raises(NoResultsError):
        catalog.search("quantum telescope", domain="chart", strict=True)


def test_decision_builder_rejects_unknown_and_contradictory_constraints(catalog: Catalog) -> None:
    brief = {
        "name": "Workshop booking",
        "audience": "community coordinator",
        "job": "reserve a room",
        "outcome": "submit a valid booking",
        "must_have": ["keyboard"],
        "must_not": ["keyboard"],
    }
    with pytest.raises(DecisionError):
        build_design_system(brief, catalog)
    with pytest.raises(DecisionError):
        build_design_system({**brief, "must_not": [], "unknown": "nope"}, catalog)


def test_decision_builder_returns_shared_structured_and_markdown_views(catalog: Catalog) -> None:
    decision = build_design_system(
        {
            "name": "Workshop booking",
            "audience": "community coordinator",
            "job": "reserve a room and review capacity",
            "outcome": "submit a valid booking",
            "mode": "app",
            "stack": "react",
            "density": 4,
            "motion": 2,
            "variance": 5,
        },
        catalog,
    )
    assert decision["evidence_contract"]["status"] == "NOT_ASSESSED"
    markdown = format_decision(decision, "markdown")
    assert "Workshop booking" in markdown
    assert "NOT_ASSESSED" in markdown
    assert json.loads(format_decision(decision, "json")) == decision


def test_persistence_is_atomic_non_destructive_and_page_overrides_merge(tmp_path: Path, catalog: Catalog) -> None:
    decision = build_design_system(
        {
            "name": "Workshop booking",
            "audience": "coordinator",
            "job": "book a room",
            "outcome": "confirm a reservation",
        },
        catalog,
    )
    saved = save_project(tmp_path, "community-workshops", decision)
    assert saved.is_file()
    with pytest.raises(PersistenceError):
        save_project(tmp_path, "community-workshops", decision)
    save_page_override(tmp_path, "community-workshops", "calendar", {"dials": {"density": 7}})
    resolved = resolve_project(tmp_path, "community-workshops", "calendar")
    assert resolved["dials"]["density"] == 7
    with pytest.raises(PersistenceError):
        save_project(tmp_path, "../escape", decision)
