# Phase 1 — P0 Skill Specs

Each spec is a build-ready brief. Format = `_TEMPLATE/SKILL.md`. Every skill: trigger-rich
`description`, the dual-compat sections, cites doctrine + the named 2026-standards ref, ships ≥1
`examples/*`. Paths are under `skills/<group>/<skill>/`.

---
## Cluster A — Documents & Presentations (group 13)

### `docx-report-and-document-formatting`  *(the missing core doc skill — fixes the 30/100)*
- **Does:** premium DOCX — style hierarchy, TOC, headers/footers, letterhead, tables, captions, page numbering, embed+subset fonts, accessible tags.
- **Workflow:** pick group-1 editorial type → set a real style set (H1–H4, body, caption with px/pt) → grid/margins → tables → embed+subset → accessibility tags → export check.
- **references/:** `docx-style-system.md` (named styles + sizes), `tables-and-figures.md`, `accessible-docx-tags.md`.
- **examples/:** `report-style-table.md` (a full applied style spec), `before-after-default-vs-designed.md`.
- **Standards:** font embedding/subsetting (doctrine), WCAG doc tags (`wcag-2.2-criteria.md`).

### `pdf-proposal-and-bankable-document-design`
- **Does:** designed PDF proposals/reports — cover system, section dividers, exhibit pages, print-ready embedding.
- **references/:** `proposal-section-architecture.md`, `cover-and-divider-systems.md`, `print-ready-pdf-checklist.md`.
- **examples/:** `proposal-cover-spec.md`, `exhibit-page-layout.md`.

### `pitch-deck-narrative-and-craft`  *(= the `deck-system` canonical from Phase 0.4)*
- **Does:** deck story arc, slide economy, builds, presenter craft; the 8 old decks become its `examples/variant-*`.
- **references/:** `deck-narrative-and-structure.md`, `presenter-and-delivery.md`.

---
## Cluster B — Design Systems, Tokens & Handoff (group 09) — fixes the 34/100

### `design-tokens-and-naming`
- **Does:** token architecture primitive→semantic→component; naming; multi-brand; export (CSS vars, JSON, Style Dictionary).
- **references/:** `token-tiers-and-naming.md`, `token-export-formats.md`.
- **examples/:** `tokens.json` worked set + `semantic-mapping.md`.
- **Standards:** OKLCH colour tokens; dark-mode semantic roles.

### `component-library-architecture`
- **Does:** atomic design, variants, composition, state coverage, documentation.
- **references/:** `atomic-structure.md`, `component-doc-template.md`.
- **examples/:** `button-component-spec.md` (full variant + state matrix).

### `design-handoff-and-dev-spec`
- **Does:** Figma-to-dev handoff, redlines, specs, acceptance for design-to-code fidelity.
- **references/:** `handoff-checklist.md`, `redline-and-spec-format.md`.
- **examples/:** `component-handoff-sheet.md`.

---
## Cluster C — Accessibility & Ops (group 00, cross-cutting) — P0 disqualifiers

### `accessibility-wcag-2-2-compliance`
- **Does:** operationalize `wcag-2.2-criteria.md` into a build+audit workflow — focus, ARIA, keyboard, target size 24px, screen-reader.
- **references/:** cites `doctrine/references/wcag-2.2-criteria.md`; `aria-patterns.md`, `keyboard-and-focus.md`.
- **examples/:** `wcag-2.2-audit-sheet.md` (a filled audit).

### `internationalization-and-rtl-design`
- **Does:** locale layout, RTL mirroring, translation-expansion tolerance, locale number/date/currency formatting.
- **references/:** `rtl-mirroring-rules.md`, `string-expansion-budgets.md`.
- **examples/:** `rtl-before-after.md`.

### `performance-as-ux-and-core-web-vitals`
- **Does:** treat LCP/INP/CLS budgets as design constraints; perceived-performance patterns.
- **references/:** cites `doctrine/references/web-performance-budgets-2026.md`; `perceived-performance-patterns.md`.
- **examples/:** `performance-budget-sheet.md`.

### `design-qa-and-pre-launch-review`
- **Does:** pre-ship QA — spec/pixel parity, cross-device/browser, the anti-slop + a11y + perf gates as one checklist.
- **references/:** `pre-launch-qa-checklist.md` (composes the slop, a11y, perf gates).
- **examples/:** `qa-review-filled.md`.

---
## Cluster D — Colour (group 02)

### `dark-mode-and-theming`
- **Does:** dual-mode semantic palettes, elevation in dark, contrast parity, not-just-invert.
- **references/:** `dark-mode-semantic-roles.md`. **examples/:** `light-dark-token-pair.md` (OKLCH).

### `accessible-color-and-contrast`
- **Does:** WCAG 2.2 contrast + APCA design tool, non-colour cues, colour-blind-safe ramps.
- **references/:** cites `wcag-2.2-criteria.md`; `apca-vs-wcag.md`, `colorblind-safe-palettes.md`.
- **examples/:** `contrast-checked-palette.md`.

---
## Cluster E — Layout & Web/UI (groups 03, 04)

### `responsive-and-adaptive-layout`  *(group 03)*
- **Does:** breakpoint strategy, **container queries**, fluid/intrinsic layout, mobile-first, fluid type (clamp).
- **references/:** `container-queries-and-intrinsic.md`, `breakpoint-strategy.md`. **examples/:** `responsive-grid-template.md`.

### `navigation-and-information-architecture`  *(group 04)*
- **Does:** IA, menu systems, wayfinding, search, breadcrumb/hierarchy.
- **references/:** `ia-patterns.md`, `nav-pattern-catalog.md`. **examples/:** `sitemap-and-nav-spec.md`.

### `landing-page-and-conversion-design`  *(group 04)*
- **Does:** hero, value prop, social proof, CTA hierarchy, conversion-credibility (anti-dark-pattern).
- **references/:** `landing-anatomy.md`, `conversion-credibility.md`. **examples/:** `landing-wireframe-spec.md`.

### `empty-error-and-loading-states`  *(group 04)*
- **Does:** empty/zero, error, skeleton/loading, success as first-class design; pairs with content `error-empty-and-system-messaging`.
- **references/:** `state-matrix.md`. **examples/:** `states-for-a-table-component.md`.

---
## Cluster F — UX Process (group 05)

### `ux-research-and-usability-testing`
- **Does:** interviews, surveys, usability tests, synthesis, research-to-decision.
- **references/:** `research-method-selector.md`, `usability-test-protocol.md`. **examples/:** `research-plan-and-synthesis.md`.

### `wireframing-and-prototyping`
- **Does:** lo-fi→hi-fi fidelity ladder, clickable prototypes, when each fidelity is right.
- **references/:** `fidelity-ladder.md`. **examples/:** `wireflow-example.md`.

---
## Cluster G — Mobile (group 07) — fixes the 22/100

### `cross-platform-design-parity`
- **Does:** one design → idiomatic iOS + Android; when to unify vs diverge; RN/Flutter mapping.
- **references/:** `ios-vs-android-idioms.md`, `rn-flutter-mapping.md`. **examples/:** `parity-spec-one-screen.md`.
- **Standards:** HIG (Liquid Glass) + Material 3 Expressive deltas.

---
## Cluster H — Content (group 10)

### `ux-writing-and-microcopy`
- **Does:** buttons, labels, tooltips, confirmations; clarity-first interface copy; voice tie-in.
- **references/:** `microcopy-patterns.md`, `button-and-cta-copy.md`. **examples/:** `before-after-microcopy.md`.

### `error-empty-and-system-messaging`
- **Does:** helpful error/empty/system copy; pairs with `empty-error-and-loading-states`.
- **references/:** `error-message-formula.md`. **examples/:** `error-copy-library.md`.

---
## Cluster I — Imagery (group 11)

### `photography-art-direction`  *(highest "human-made" lever per the doctrine)*
- **Does:** photo style, treatment, cropping, sourcing; anti-stock-photo; AI-image direction handoff.
- **references/:** `photo-treatment-system.md`, `anti-stock-direction.md`. **examples/:** `art-direction-board.md`.

### `iconography-system-design`
- **Does:** custom icon set, grid, stroke, metaphor consistency, optical balance.
- **references/:** `icon-grid-and-stroke.md`. **examples/:** `icon-set-spec.md`.

---
## Cluster J — Data Viz (group 12)

### `dashboard-and-data-product-design`
- **Does:** KPI hierarchy, dashboard layout, drill-down, real-time data UX; pairs with `data-visualization`.
- **references/:** `kpi-hierarchy.md`, `dashboard-layout-patterns.md`. **examples/:** `dashboard-spec.md`.

---
**Every spec's acceptance:** SKILL.md in `_TEMPLATE` format, correct group/category, cites doctrine
+ the named standards ref, ships the listed `references/*` and ≥1 `examples/*`, names no banned font.
