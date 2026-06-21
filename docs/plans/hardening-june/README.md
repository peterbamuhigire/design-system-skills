# Hardening Plan — June 2026

Concrete execution plan to take design-system-skills from **51/100 → 90+** against the top-0.1%
bar. Derived from `docs/initial-analysis/` (the strict audit). Each phase is a subfolder with
detailed task breakdowns, specs, and acceptance criteria.

## Why
The audit (`docs/initial-analysis/00-executive-summary.md`) found a world-class **doctrine** on a
merely competent **skill layer**, with real gaps: no document skill, no accessibility/tokens,
**zero worked examples** across 37 skills, and stale 2026 standards. This plan fixes that in
sequence, score-visible at each step.

## Phases & targets

| Phase | Folder | Focus | Score target |
|---|---|---|---|
| **0** | `phase-0-foundations/` | Restructure taxonomy (13 groups), 2 cross-cutting 2026-standards refs, enforce `examples/` convention, de-dupe decks & colour/brand | 51 → **~62** |
| **1** | `phase-1-p0-skills/` | The ~24 P0 must-have skills (document render, tokens+handoff, accessibility, motion, RN/Flutter, responsive, UX-writing, mobile hardening) + harden the P0-ten | ~62 → **~70**, then **~85** as they harden |
| **2** | `phase-2-p1-wave/` | P1 wave: iconography, art-direction, prototyping, research, dashboards, editorial, i18n/RTL, dark-mode, email, trust/conversion, design-QA, real proposal/doc craft | → **~85** |
| **3** | `phase-3-ceiling/` | P2 + ongoing: 3D/WebGL, conversational/voice, ethics, green UX; Tier-1 reading-list extraction; standards upkeep | → **90+** |

## Source inputs (read before executing any phase)
- `docs/initial-analysis/02-coverage-and-taxonomy.md` — the 13-group structure.
- `docs/initial-analysis/04-gap-analysis-new-skills.md` — the 68 new skills, P0/P1/P2.
- `docs/initial-analysis/07-hardening-existing-skills.md` — per-skill `references/*`+`examples/*`.
- `docs/initial-analysis/06-2026-standards-benchmark.md` — the cited standards to encode.
- `docs/initial-analysis/08-reading-list.md` — books to buy & extract.

## Execution rules
- One phase at a time; each phase has a Definition of Done and a re-audit checkpoint (run the
  `skill-engine-audit` skill to confirm the score moved).
- Never delete a skill in restructuring — migrate it (git mv) and update routing.
- Every new/hardened craft skill ships ≥1 worked example (the `examples/` convention).
- Pull each repo before touching it; commit per logical unit.

## Status
Plan authored 2026-06-21. Execution not yet started — awaiting go.
