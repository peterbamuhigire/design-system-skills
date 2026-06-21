# Reference: Grid Systems Catalogue

The named grid structures a layout decision can draw on, with the column count, gutter, and margin
each is suited to. A grid is *scaffolding you place elements against and deliberately break* — pick
the structure from the medium and the content, never reflexively reach for "12 columns, even
gutters, centred cards" (that convergent default is the slop tell, not the answer). Standards basis:
Müller-Brockmann (*Grid Systems in Graphic Design*), Vignelli (*The Vignelli Canon*), the CSS Grid
specification, and the Swiss / International Typographic tradition. Cite alongside
`doctrine/references/type-scale-and-spacing.md` (the spacing unit every gutter/margin is a multiple
of) and the sibling `responsive-and-adaptive-layout` (which owns how these grids *respond* — see
§ Container queries & intrinsic layout below).

---

## 1. Grid anatomy (the vocabulary to state)

| Term | What it is | Decision it drives |
|---|---|---|
| **Columns** | The vertical tracks content snaps to. | Density and flexibility. |
| **Gutter** | The gap *between* columns. | Grouping rhythm; must be a spacing-unit multiple. |
| **Margin** | The outer space between content and the page/viewport edge. | Breathing room; asymmetric margins authorise composition. |
| **Field / module** | A column × row cell; the unit a modular grid is built from. | Editorial / dashboard layouts that align both axes. |
| **Baseline grid** | Horizontal rhythm lines leading snaps to. | Long-form text and multi-column alignment. |

State all five before any markup. "12-col, 24px gutter, 64px margin, 8px baseline" is a decision; an
unnamed grid is a default waiting to happen.

---

## 2. The grid types and when each fits

| Grid | Columns | Best for | Notes |
|---|---|---|---|
| **Manuscript / single-measure** | 1 wide column | Long-form reading, essays, document body, hero statements. | Set the measure to **45–75 characters** per line; wider tires the eye. The margin *is* the design. |
| **Column grid** | 2–6 | Documents, reports, editorial pages, brochures. | 2–3 columns read best in DOCX/PDF/print. Vary span — a heading bridging two columns breaks monotony. |
| **Modular grid** | columns × rows | Dashboards, catalogues, magazine spreads, KPI exhibits. | Both axes align. Use a **featured module** (2×2 inside a field of 1×1) to install a focal point. |
| **12-column** | 12 | Web/UI default; divisible by 2,3,4,6. | Flexible *because* you span it unevenly (e.g. 8+4, 7+5), **not** because you fill it with 12 even cards. |
| **16-column** | 16 | Dense desktop apps, data-heavy tools. | Finer placement control; collapse aggressively on small viewports. |
| **Asymmetric / off-axis** | irregular | Authored marketing pages, art-directed editorial. | A wide content column + a narrow rail (e.g. 9+3) is the workhorse of "this looks designed." |
| **Compound / broken** | nested | Layouts mixing reading and scanning zones. | A column grid for prose overlaid with a modular grid for cards — switch grids per zone, state both. |

---

## 3. Ratios and the off-centre rule

- **Even splits (6+6, 4+4+4) read as safe and lifeless.** Prefer an *intentional* uneven split:
  **8+4** (2:1), **7+5**, **9+3** (3:1). The uneven ratio is what a templating tool would not choose.
- **Rule of thirds / golden section** for focal placement: pin the hero to a third-line or the
  ~0.618 mark, not dead centre.
- **One asymmetry per composition is enough** (Vignelli: a few strong relationships, ruthlessly
  repeated). Two competing off-axis moves cancel out.

---

## 4. CSS Grid mapping (how the named grid becomes code)

| Concept | CSS Grid mechanism |
|---|---|
| 12 columns | `grid-template-columns: repeat(12, 1fr);` |
| Gutter | `gap: <spacing-unit multiple>;` (e.g. `gap: 24px;`) |
| Margin / max content width | wrap in a container with `max-width` + `margin-inline: auto` (or `padding-inline`). |
| Uneven span | `grid-column: span 8;` beside `grid-column: span 4;` |
| Named regions | `grid-template-areas: "hero hero rail";` — readable, self-documenting placement. |
| Bleed off one edge | place an item with `grid-column: 1 / -1` or negative margins past the container. |

Worked end-to-end CSS lives in `examples/grid-template-worked.md`.

---

## 5. Container queries & intrinsic layout (2026 — note, then defer)

Two modern shifts change *what the grid responds to*. This skill names them; the sibling
`responsive-and-adaptive-layout` owns the depth (`references/container-queries-and-intrinsic.md`).

- **Container queries** — a component sizes itself to **its container**, not the global viewport.
  Set `container-type: inline-size` on the parent and size children with `@container (min-width: …)`.
  This means the *same grid* can lay out differently in a wide main column vs. a narrow sidebar
  without a single media query — pick this when a component is reused across slots.
- **Intrinsic layout** — let the grid respond to content and available space with **no breakpoint**:
  `grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr))` reflows 1→N columns by
  itself. Use it for genuine card fields — but still break the monotony with a featured span, never
  ship the flat even field (see SKILL.md checklist item 7).

When you need real breakpoint strategy, fluid clamps, or the full intrinsic pattern library, go to
`responsive-and-adaptive-layout`. This skill's job is the *grid and spacing decision*; that skill's
job is *how it adapts*.

---

## 6. Anti-patterns this catalogue exists to prevent

- Reaching for **12 even columns + uniform gutter + centred cards** because it is the default, not
  because the content is a true 12-up field.
- An **unnamed grid** — gutters and margins chosen ad hoc per element, so nothing aligns to a system.
- **Symmetric splits only** (6+6 forever) — no off-axis tension, reads as a placeholder.
- **One global gap** used between both related and unrelated elements, so grouping carries no meaning
  (gutter ≠ section spacing — see `spacing-rhythm.md`).
