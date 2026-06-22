# Phase 3 — Ongoing Program (stay at 90+)

A world-class engine decays without upkeep (standards move, fonts become slop, skills drift). This
is the maintenance loop.

## 1. Standards upkeep cadence
- **Quarterly:** refresh `doctrine/references/wcag-2.2-criteria.md`,
  `web-performance-budgets-2026.md`, and the mobile platform refs (HIG / Material) — re-verify the
  numbers against primary sources (W3C, web.dev, Apple, Google) under the digital-research engine's
  no-hallucination rule. Bump any changed threshold and note it in the doctrine changelog.
- **On platform release** (WWDC, Google I/O, new WCAG draft): targeted update to the affected
  skills + refs.
- **Banned-font watch:** review `ai-slop-banned-fonts.md` for newly-converged AI defaults (Geist
  was added 2026-06-21; the next "Inter" will appear) — AI-vendor sources are ban-evidence only.

- **AI-slop doctrine watch:** run `slop-doctrine-refresh-and-research-loop` with the
  digital-research engine when visual/product/textual slop definitions shift. Update the taxonomy
  only with evidence grade, scope, design consequence, and date checked.

## 2. Re-audit cadence
- Run the **`skill-engine-audit`** skill (in skills-web-dev) after every phase and then
  **quarterly**. Compare the master scorecard to the prior run; any dimension that slipped below 75
  becomes the next sprint's backlog.
- Keep the rubric fixed so scores are comparable over time.

## 3. Examples & freshness hygiene
- Enforce the `examples/` convention on every new skill (CI-style check: a craft skill without
  `examples/` is incomplete).
- Periodically refresh worked examples so they reflect current best practice, not 2026-frozen craft.

## 4. Contribution loop
- New skills follow `CONTRIBUTING.md` + `_TEMPLATE`; placed via `02-coverage-and-taxonomy.md`'s
  group structure; cite doctrine + the standards refs.
- When a group exceeds ~9 skills, split it (the taxonomy was sized for ~6–8 per group).

## 5. Success metric
The engine holds **90+** on the `skill-engine-audit` scorecard with **no dimension below 75**, and
every output type (web, web-app, iOS, Android, cross-platform, documents, presentations, brand,
data products, handoff) scores **≥ 80**. That is the definition of "rivals the world's top studios"
for this engine.
