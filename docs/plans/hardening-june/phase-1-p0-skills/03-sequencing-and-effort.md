# Phase 1 — Sequencing & Effort

## Build order (value-first, dependency-aware)

**Wave 1 — the three worst output types (do first):**
1. `docx-report-and-document-formatting` + `pdf-proposal-and-bankable-document-design` (fixes Docs 30) — **M, M**
2. `design-tokens-and-naming` → `design-handoff-and-dev-spec` → `component-library-architecture` (fixes tokens/handoff 34; tokens first, others depend on it) — **M, M, M**
3. `cross-platform-design-parity` + harden `ios-ui-ux-design` & `android-ui-ux-design` (fixes mobile 22) — **M, L, L**

**Wave 2 — cross-cutting disqualifiers (unblock everything else):**
4. `accessibility-wcag-2-2-compliance`, `accessible-color-and-contrast` (depend on Phase 0 `wcag-2.2-criteria.md`) — **M, S**
5. `performance-as-ux-and-core-web-vitals` (depends on `web-performance-budgets-2026.md`) — **S**
6. `internationalization-and-rtl-design`, `design-qa-and-pre-launch-review` — **M, M**

**Wave 3 — core craft infill:**
7. `responsive-and-adaptive-layout`, `dark-mode-and-theming` — **M, M**
8. `navigation-and-information-architecture`, `landing-page-and-conversion-design`, `empty-error-and-loading-states` — **M, M, S**
9. `ux-writing-and-microcopy`, `error-empty-and-system-messaging` (pair with states) — **S, S**
10. `wireframing-and-prototyping`, `ux-research-and-usability-testing` — **M, M**
11. `photography-art-direction`, `iconography-system-design` — **M, M**
12. `dashboard-and-data-product-design` (harden alongside `data-visualization`) — **M**

**Wave 4 — finish the P0-ten hardening** (the remaining ones not done in Waves 1–3):
`color-system-and-palette`, `font-selection-and-pairing`, `layout-grid-and-spacing`,
`design-audit`, `visual-product-slop-audit`, `brand-visual-identity`, `motion-design`. — **L total**

## Parallelization
- Independent skills can be authored by parallel agents (one skill per agent), each briefed with
  its spec from `01-skill-specs.md` + the `_TEMPLATE`. **Caveat:** tokens → handoff/components and
  states → messaging have ordering deps; don't parallelize those pairs across the dependency.
- Run a `skill-engine-audit` re-check after Wave 2 and after Wave 4.

## Effort summary
24 new (mostly M, a few S/L) + 10 hardenings (L in aggregate). Estimate **3–5 focused sessions**
or ~2 with heavy parallel-agent authoring. Commit per skill or per wave.

## Definition of Done (Phase 1)
Engine ~61 skills; the three worst output types ≥ 65; every new skill + the P0-ten ship a worked
example; overall audit ~70 (creation) trending ~85 (hardened).
