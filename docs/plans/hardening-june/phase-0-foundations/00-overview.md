# Phase 0 — Foundations

**Goal:** restructure and instrument the engine so all later infill is clean. **Score: 51 → ~62.**
No new craft skills yet — this phase fixes the *cabinet*, not the *contents*.

## Objectives
1. Migrate the 37 existing skills into the **13-group + 1 cross-cutting** taxonomy (`01-taxonomy-migration.md`).
2. Add two engine-wide **2026-standards** references and cite them (`02-cross-cutting-standards-refs.md`).
3. Enforce the **`examples/` convention** (`03-examples-convention.md`).
4. **De-dupe** the 8 decks and the colour/brand overlap (`04-dedup-decks-and-color.md`).

## Definition of Done
- [ ] All 37 skills live under the new group folders; every `metadata.category` updated; README router + CLAUDE/AGENTS reflect the 14 groups; no skill deleted; no dangling internal links.
- [ ] `doctrine/references/wcag-2.2-criteria.md` and `web-performance-budgets-2026.md` exist and are cited by the relevant skills.
- [ ] `CONTRIBUTING.md` + `_TEMPLATE` mandate ≥1 worked example; the convention is documented and checkable.
- [ ] Decks consolidated to `_deck-system/` (or 1 skill + variants); colour/brand overlap resolved.
- [ ] Re-audit checkpoint: run `skill-engine-audit`; taxonomy dimension should move from 48 → ~70, overall to ~62.

## Sequencing
1 (taxonomy) → 4 (de-dupe, depends on new groups) → 2 (refs) and 3 (convention) can run anytime.
Do the taxonomy migration as ONE reviewed commit per source-group to keep diffs legible.

## Effort
Taxonomy migration **L**, refs **M**, convention **S**, de-dupe **M**. ~1–2 focused sessions.
