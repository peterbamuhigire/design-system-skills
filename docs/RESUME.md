# RESUME / Status - where to pick up (updated 2026-07-13)

Single source of truth for "what's done / what's next" on design-system-skills.
(Supersedes `RESUME-2026-06-21.md`, which is historical.)

## Current state

- **82 active skills across 15 groups, 100% example-complete and 100% contract-compliant.**
- The zero-debt conformance baseline is enforced in CI. Local and canonical validation pass for
  all 82 active skills; 46 routing fixtures achieve 100% precision at the top-three threshold.
- The earlier overall design-readiness audit score remains **81/100** (progression: 51 -> about
  67 -> about 73 -> 80 -> 81). That score measures broader output capability, not skill-contract
  conformance.
- Latest re-audit: `docs/audits/post-v2-plan/`:
  - taxonomy and structure: **86**
  - output-readiness: **78**
  - skill-depth: **74**
- The fresh audit replaced the old post-v2 analysis rather than adding another audit folder.

## Done

- Phase 0: taxonomy, standards refs, examples convention, deck/brand de-dup.
- Phase 1: 23 P0 skills plus P0-ten hardening.
- Examples backfill: all active skills ship a worked example.
- `product-design-audit` skill: audits a real product across web, SaaS, iOS/Mac/iPad/iPhone,
  Android, and desktop; routes findings to the skill that fixes each issue.
- 8-category intent-based font taxonomy reconciled: folders, manifests, and doctrine.
- Critical study of 20 UI/UX books: `docs/book-study/`, synthesis `00-synthesis.md`.
- v2 plan executed: Track A doctrine refs and inoculation notes; Track B new skills; Track C
  changes; Track D full P1 wave.
- The two cheapest post-v2 fixes landed:
  - reauthored the old boilerplate `SKILL.md` heads;
  - split overloaded group 04 into focused group 04 plus new
    `14-conversion-and-web-page-patterns`; moved email to group 13.
- Fresh current re-audit completed and replaced `docs/audits/post-v2-plan/`.
- Final cleanup pass closed the two measured hygiene blockers: 0 active `Evidence Produced`
  sections and 0 active stale sibling-path references.
- Added `slop-doctrine-refresh-and-research-loop`, a living AI-slop self-review skill wired to
  the digital-research engine's source-evaluation discipline.
- Added RN/Expo implementation-readiness gates to `cross-platform-design-parity`, using the local
  React Native book as historical pattern input and current RN/Expo docs as the version-sensitive
  source of truth.
- Normalised all 82 active skills to the July 2026 portable contract: neighbour-aware triggers,
  input/output contracts, decision rules, capability boundaries, degraded mode, stop/recovery
  behaviour, evidence, acceptance conditions, and five concrete anti-patterns.
- Added `governance/skill-authoring-standard.md`, a rebuilt `_TEMPLATE`, local validation and
  routing scripts, 46 routing fixtures, a zero-debt baseline, and GitHub Actions enforcement.
- Reduced `data-visualization/SKILL.md` below the 500-line limit through a linked reference while
  retaining routing, workflow, decisions, and safety in the entrypoint.

## Next

Skill-contract repair is complete. Remaining work is capability expansion:

1. **Build P2 differentiators only where they improve output readiness:**
   3D/WebGL, scroll/page transitions, print/production layout, multi-brand theming/governance,
   public-sector/education UX, sustainability, advanced analytical exhibits.
2. **Resolve the two structural ceilings:**
   - **Specs-not-render wall:** the engine specifies artifacts but does not execute a render
     pipeline for DOCX/PDF/PPTX/XLSX/email/front-end output.
   - **Cross-platform mobile floor:** React Native/Expo handoff is stronger now, but Flutter
     implementation depth and full app-build ownership remain outside the design engine.

## Working method that worked

Parallel specialist passes, strict top-0.1% rubric, no banned fonts, real worked examples, no lorem,
and orchestrator-owned shared-file edits. Watch for shared-file write races when using parallel
agents.

For catalogue maintenance, run:

```powershell
python -X utf8 scripts/validate_engine.py --baseline tests/quality-baseline.json
python -X utf8 scripts/routing_smoke_test.py
```
