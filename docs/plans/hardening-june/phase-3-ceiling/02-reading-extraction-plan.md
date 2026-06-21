# Phase 3 — Reading-List Extraction Plan

Turn the bought books (`docs/initial-analysis/08-reading-list.md`) into canonical depth inside the
deepest skills. Extract Tier-1 first (highest leverage), then Tier-2/3 as headroom allows. Each
extraction lands as a `references/*.md` (the distilled principles, attributed) and ideally a
`examples/*` (an applied artifact). Honours the doctrine's sourcing-authority asymmetry — these are
*human* design authority.

## Tier-1 extraction map (do these first)

| Book | → Skill(s) | Extract into |
|---|---|---|
| **Bringhurst — The Elements of Typographic Style** | `font-selection-and-pairing`, `variable-fonts-and-opentype-features`, `fluid-responsive-typography` | scale ratios, measure/leading, pairing, OpenType → `references/bringhurst-principles.md` + `examples/applied-type-scale.md` |
| **Müller-Brockmann — Grid Systems** | `layout-grid-and-spacing`, `composition-and-visual-hierarchy` | grid construction, modular systems → `references/grid-systems-catalog.md` + `examples/grid-template-worked.md` |
| **Lupton — Thinking with Type** | `font-selection-and-pairing`, `ux-writing-and-microcopy`, `editorial-and-long-form-layout` | type anatomy, text setting → `references/text-setting.md` |
| **Albers — Interaction of Color** | `color-system-and-palette`, `accessible-color-and-contrast` | colour relativity, contrast → `references/color-interaction.md` + `examples/oklch-palette-worked.md` |
| **Tufte — The Visual Display of Quantitative Information** | `data-visualization`, `chart-selection-and-encoding`, `analytical-report-and-exhibit-design` | data-ink, integrity, small multiples → `references/tufte-principles.md` + `examples/chart-worked-examples.md` |
| **Norman — The Design of Everyday Things** | `ux-psychology`, `heuristic-evaluation-and-design-critique` | affordances, signifiers, mapping → `references/norman-principles.md` |
| **Wathan & Schoger — Refactoring UI** | `practical-ui-design`, `composition-and-visual-hierarchy`, `color-system-and-palette` | practical spacing/hierarchy/colour tactics → `references/refactoring-ui-tactics.md` + worked example |
| **Kholmatova — Design Systems** | `design-tokens-and-naming`, `component-library-architecture`, `design-system-governance-and-versioning` | pattern libraries, system models → `references/design-systems-models.md` |

## Tier-2/3 (as headroom allows)
Map per `08-reading-list.md` (e.g. Spiekermann → type rhythm; Reynolds *Presentation Zen* →
`pitch-deck-narrative-and-craft`; editorial-design bible → `editorial-and-whitepaper-design`;
Hoffmann/colour, motion, and accessibility titles → their groups). Keep the same pattern: distilled
`references/*` + an applied `examples/*`, attributed to the source.

## Order
Extract into the **most-used, highest-scoring-leverage** skills first (typography, colour, layout,
data-viz, design-systems) — these compound across every output type. One book per session is a
sustainable cadence.

## Acceptance
Each Tier-1 book has produced at least one `references/*` (attributed) in its mapped skill, and the
mapped skill has a worked example demonstrating the extracted principle.
