# 03 - Existing Groups Re-Audit

**Date:** 2026-06-22
**Scope:** 82 active `SKILL.md` files across groups 00-14, plus their `examples/` and `references/`
subtrees.
**Score:** **74 / 100** (prior post-v2 skill-depth score: 64)

## Method

This audit rechecked the current filesystem after the boilerplate-head rewrite and group-04 split.
Machine checks found:

- 82 active skills.
- 0 active skills missing examples.
- Average active `SKILL.md` length: about 144 lines.
- Average references per skill: about 2.8.
- 0 active skills still containing `## Evidence Produced`.
- 0 active skills still containing stale pre-taxonomy sibling paths.

## Verdict

Skill depth improved materially. The old full generated entrypoint phrase is gone from active
`SKILL.md` files, and many legacy heads now describe real routing, required inputs, and boundaries.
That alone removes the prior audit's largest skill-depth cap.

The engine is now a **74-tier skill engine**: solid, applied, example-backed, and internally
coherent enough to trust for routing. It is not yet a 75+ skill-depth engine because thin
single-reference skills, adapter skills, and the render/mobile implementation boundary still show
through.

## Group scores

| Group | Score | Prior v2 | Current assessment |
|---|---:|---:|---|
| 00 cross-cutting ops / QA / a11y | 73 | 64 | Strong audit/remediation spine; migration-table residue removed; living slop-doctrine refresh added. |
| 01 typography and fonts | 64 | 63 | Stable; variable/fluid type are strong, but three plumbing skills have zero own refs. |
| 02 color, brand, visual identity | 69 | 66 | Logo and OKLCH spine are strong; active color-path links are current. |
| 03 layout, grid, composition | 67 | 66 | Coherent and authored; still not deep on print/production. |
| 04 web and UI design | 72 | 65 | Big lift from reauthored heads, the group split, and removal of migration tables. |
| 05 UX process, research, psychology | 65 | 63 | Demo-driven and remediation are strong; psychology remains more legacy/reference-heavy. |
| 06 sector and domain UX | 63 | 61 | Ecommerce/fintech strong; sector-strategies and legal still feel adapter-like. |
| 07 mobile iOS/Android/cross-platform | 70 | 66 | Current platform presentation guidance is good; RN/Expo handoff is stronger, while full implementation remains external. |
| 08 motion and interaction | 66 | 64 | Useful and cleanly routed, but still thin. |
| 09 design systems, tokens, theming | 67 | 66 | Clean token/handoff group; governance and CI publishing remain future work. |
| 10 content design and UX writing | 67 | 66 | Voice/tone gives the group a real upstream system. |
| 11 imagery, illustration, art direction | 66 | 65 | AI-image provenance and illustration style close the old 2026 gap. |
| 12 data-viz and dashboards | 66 | 64 | Chart-selection split is useful; data-visualization migration residue is removed. |
| 13 presentations and documents | 67 | 64 | Email relocation and XLSX owner lift readiness; render execution remains external. |
| 14 conversion and web page patterns | 72 | n/a | New group is coherent: landing, nav/IA, onboarding, trust, states. Active links now point to group 14. |

**Aggregate:** group means now land around the high-60s, but the engine-level score is set to
**74** because the two structural hygiene penalties from the prior audit are now closed and the
slop/RN gaps have targeted additions. The active
skill heads and routes pass the threshold for solid professional use.

## Strongest current skills

- `distinctive-by-design` - still the engine's flagship "show, do not tell" example.
- `color-system-and-palette` - the most complete color-system skill.
- `logo-and-wordmark-design` - one of the strongest authored craft skills.
- `demo-driven-design-process` - operationalizes the creative-selection doctrine.
- `product-design-audit` and `ux-remediation-and-redesign` - create a working audit-to-fix loop.
- `slop-doctrine-refresh-and-research-loop` - keeps the anti-slop doctrine research-backed as
  definitions change.
- `ecommerce-and-checkout-ux` and `trust-credibility-and-social-proof` - strong ethical conversion craft.
- `xlsx-and-financial-model-presentation` - strongest example of a non-web output type gaining a real owner.

## Remaining skill-depth defects

### 1. Some skills are adapters, not deep craft owners

`premium-font-scan`, `font-embedding-and-licensing`, `sector-strategies`, and `color-selection` are
useful, but they do not carry the same authored craft depth as the top skills. That is acceptable if
treated as plumbing/adapters; it is a score drag if counted as equivalent craft.

### 2. Newer P1 skills are often single-reference

The examples are real, but many new skills have only one own reference file. They are operational,
not yet richly sourced.

### 3. The execution boundary still caps several skills

Document, deck, spreadsheet, email, and mobile skills often stop at design specification or handoff.
That is appropriate for a design engine, but it keeps skill depth below the excellent-pro tier when
judged against end-to-end artifact production.

## What changed from the prior audit

| Prior finding | Current result |
|---|---|
| Full boilerplate shells capped skill depth at 64. | Mostly resolved in active skill heads. |
| `distinctive-by-design` gap was embarrassing. | Resolved; the worked before/after remains strong. |
| Examples drought was closed. | Still closed: 82 / 82 active skills have examples. |
| Group 04 was overloaded. | Resolved structurally; conversion/page patterns now live in group 14. |
| Dangling P1 references existed. | Resolved as missing skills and as active stale path strings. |

## Bottom line

This is now a genuinely useful, example-backed, high-coverage design skill engine. The next quality
lift is not another broad wave of skills; it is targeted depth and execution:

1. Add second references to thin P1 skills where they are meant to be enduring craft owners.
2. Decide whether render implementation belongs here or in a companion engine.
3. Add Flutter/full-app implementation depth if cross-platform mobile should move past low-70s.
