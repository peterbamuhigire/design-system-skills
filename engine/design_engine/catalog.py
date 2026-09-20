"""Deterministic offline catalog search with typed routing and abstention."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from difflib import get_close_matches
import json
import re
import unicodedata
from pathlib import Path
from typing import Any


DOMAINS = (
    "product",
    "style",
    "typography",
    "color",
    "landing",
    "chart",
    "ux",
    "icons",
    "react",
    "web",
    "google-fonts",
    "gsap",
)

STACKS = (
    "html-tailwind",
    "react",
    "nextjs",
    "astro",
    "vue",
    "nuxtjs",
    "nuxt-ui",
    "svelte",
    "swiftui",
    "react-native",
    "flutter",
    "shadcn",
    "jetpack-compose",
    "threejs",
    "angular",
    "laravel",
    "javafx",
    "wpf",
    "winui",
    "avalonia",
    "uno",
    "uwp",
)

SYNONYMS = {
    "admin": "backoffice",
    "administrator": "backoffice",
    "analytics": "dashboard",
    "commerce": "ecommerce",
    "colour": "color",
    "font": "typography",
    "fonts": "typography",
    "login": "authentication",
    "signin": "authentication",
    "signup": "onboarding",
    "visualisation": "visualization",
    "visualise": "visualization",
}

TOKEN_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)?")


class CatalogError(ValueError):
    """Base error for invalid catalog requests or records."""


class NoResultsError(CatalogError):
    """Raised only when callers request strict search results."""


@dataclass(frozen=True)
class RouteDecision:
    domain: str
    confidence: float
    alternatives: tuple[tuple[str, float], ...]
    reason: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class SearchResult:
    record_id: str
    domain: str
    title: str
    score: float
    status: str
    stack: str | None
    explanation: tuple[str, ...]
    content: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["explanation"] = list(self.explanation)
        return payload


def _tokens(value: str) -> list[str]:
    normal = unicodedata.normalize("NFKC", value).casefold()
    words = TOKEN_RE.findall(normal.replace("_", "-"))
    expanded: list[str] = []
    for word in words:
        expanded.append(SYNONYMS.get(word, word))
    return expanded


class Catalog:
    """Load and search an independently authored, versioned JSON catalog."""

    def __init__(self, payload: dict[str, Any], source: Path | None = None):
        self.source = source
        self.payload = payload
        self.revision = str(payload.get("catalog_revision", "unversioned"))
        self.records = tuple(payload.get("records", ()))
        self.stack_guidance = tuple(payload.get("stack_guidance", ()))
        self._validate()

    @classmethod
    def from_file(cls, path: str | Path) -> "Catalog":
        source = Path(path).resolve()
        try:
            payload = json.loads(source.read_text(encoding="utf-8"))
        except FileNotFoundError as exc:
            raise CatalogError(f"catalog not found: {source}") from exc
        except json.JSONDecodeError as exc:
            raise CatalogError(f"catalog is not valid JSON: {source}") from exc
        if not isinstance(payload, dict):
            raise CatalogError("catalog root must be an object")
        return cls(payload, source)

    def _validate(self) -> None:
        if self.payload.get("schema_version") != "1.0":
            raise CatalogError("unsupported catalog schema_version")
        if not self.revision:
            raise CatalogError("catalog_revision is required")
        ids: set[str] = set()
        for record in self.records:
            required = {"id", "domain", "title", "tags", "status", "content", "evidence"}
            missing = required.difference(record)
            if missing:
                raise CatalogError(f"record missing fields: {sorted(missing)}")
            record_id = str(record["id"])
            if record_id in ids:
                raise CatalogError(f"duplicate record id: {record_id}")
            ids.add(record_id)
            if record["domain"] not in DOMAINS:
                raise CatalogError(f"unknown domain: {record['domain']}")
            if record["status"] not in {"active", "supplemental", "deprecated"}:
                raise CatalogError(f"invalid status for {record_id}")
            if not isinstance(record["tags"], list) or not record["tags"]:
                raise CatalogError(f"record tags must be non-empty: {record_id}")
            evidence = record["evidence"]
            if not isinstance(evidence, dict) or not evidence.get("source_type") or not evidence.get("reviewed"):
                raise CatalogError(f"record evidence is incomplete: {record_id}")
        seen_stacks: set[str] = set()
        for guidance in self.stack_guidance:
            stack = guidance.get("stack")
            if stack not in STACKS:
                raise CatalogError(f"unknown stack: {stack}")
            if stack in seen_stacks:
                raise CatalogError(f"duplicate stack guidance: {stack}")
            seen_stacks.add(stack)
            if not guidance.get("guidance") or not guidance.get("supported_versions"):
                raise CatalogError(f"incomplete stack guidance: {stack}")
        missing_domains = set(DOMAINS).difference(record["domain"] for record in self.records)
        if missing_domains:
            raise CatalogError(f"catalog has no records for domains: {sorted(missing_domains)}")
        missing_stacks = set(STACKS).difference(seen_stacks)
        if missing_stacks:
            raise CatalogError(f"catalog has no guidance for stacks: {sorted(missing_stacks)}")

    def route(self, query: str, domain: str | None = None) -> RouteDecision:
        query_tokens = set(_tokens(query))
        if not query_tokens:
            raise CatalogError("query must contain searchable text")
        if domain is not None and domain not in DOMAINS and domain != "all":
            raise CatalogError(f"invalid domain: {domain}")
        scores: list[tuple[str, float]] = []
        for candidate in DOMAINS:
            corpus = " ".join(
                " ".join(map(str, record["tags"])) + " " + str(record["title"])
                for record in self.records
                if record["domain"] == candidate
            )
            overlap = len(query_tokens.intersection(_tokens(corpus)))
            scores.append((candidate, float(overlap)))
        ranked = sorted(scores, key=lambda item: (-item[1], item[0]))
        if domain and domain != "all":
            return RouteDecision(domain, 1.0, tuple(ranked[:3]), "explicit domain")
        top_score = ranked[0][1]
        second_score = ranked[1][1]
        if top_score <= 0:
            return RouteDecision("style", 0.0, tuple(ranked[:3]), "no domain evidence; conservative style fallback")
        confidence = min(1.0, top_score / max(1.0, top_score + second_score))
        return RouteDecision(ranked[0][0], round(confidence, 3), tuple(ranked[1:3]), "lexical domain evidence")

    def search(
        self,
        query: str,
        *,
        domain: str | None = None,
        stack: str | None = None,
        status: str = "current",
        limit: int = 8,
        strict: bool = False,
    ) -> dict[str, Any]:
        if not isinstance(limit, int) or limit < 1 or limit > 50:
            raise CatalogError("limit must be an integer between 1 and 50")
        if stack is not None and stack not in STACKS:
            raise CatalogError(f"invalid stack: {stack}")
        if status not in {"current", "all", "legacy"}:
            raise CatalogError("status must be current, all, or legacy")
        route = self.route(query, domain)
        query_tokens = set(_tokens(query))
        candidates: list[SearchResult] = []
        for record in self.records:
            if route.domain != "all" and record["domain"] != route.domain:
                continue
            declared_stacks = set(record.get("stacks", []))
            if record.get("stack"):
                declared_stacks.add(record["stack"])
            if stack and declared_stacks and stack not in declared_stacks:
                continue
            if status == "current" and record["status"] == "deprecated":
                continue
            if status == "legacy" and record["status"] != "deprecated":
                continue
            corpus_tokens = set(_tokens(" ".join(map(str, record["tags"])))) | set(_tokens(str(record["title"])))
            content_tokens = set(_tokens(json.dumps(record["content"], ensure_ascii=False)))
            overlap = len(query_tokens.intersection(corpus_tokens))
            content_overlap = len(query_tokens.intersection(content_tokens))
            score = overlap * 4 + content_overlap
            explanation: list[str] = []
            if overlap:
                explanation.append(f"{overlap} query term(s) match title or tags")
            if content_overlap:
                explanation.append(f"{content_overlap} query term(s) match actionable content")
            if stack and (record.get("stack") == stack or stack in record.get("stacks", [])):
                score += 3
                explanation.append(f"stack match: {stack}")
            elif stack and record.get("stack") is not None:
                score -= 1
            if score > 0 and record["status"] == "active":
                score += 0.25
            if score <= 0:
                continue
            candidates.append(
                SearchResult(
                    record_id=record["id"],
                    domain=record["domain"],
                    title=record["title"],
                    score=round(score, 3),
                    status=record["status"],
                    stack=record.get("stack"),
                    explanation=tuple(explanation),
                    content=record["content"],
                )
            )
        results = sorted(candidates, key=lambda item: (-item.score, item.record_id))[:limit]
        if strict and not results:
            raise NoResultsError("no records satisfied the query and filters")
        return {
            "schema_version": "1.0",
            "catalog_revision": self.revision,
            "query": query,
            "route": route.to_dict(),
            "filters": {"domain": domain, "stack": stack, "status": status},
            "results": [item.to_dict() for item in results],
            "abstained": not bool(results),
        }


def default_catalog_path() -> Path:
    return Path(__file__).resolve().parents[2] / "data" / "design-catalog.json"
