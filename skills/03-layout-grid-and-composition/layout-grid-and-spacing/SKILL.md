---
name: layout-grid-and-spacing
description: Use when composing or restyling the LAYOUT of any artifact — a website or landing page, an app/web UI screen, a dashboard, a DOCX/PPTX/PDF report or proposal, or a pitch deck — and you must decide column structure, spacing, alignment, and where the eye lands. Establishes a grid and a single spacing unit, builds hierarchy through scale + space + alignment, introduces intentional asymmetry and a focal point, and strips out the uniform-card / everything-centred / identical-gutter AI-slop layout tells. This is the default entry skill for layout and spacing in the design engine.
status: active
metadata:
  portable: true
  category: 03-layout-grid-and-composition
  compatible_with:
    - claude-code
    - codex
---

# Layout, Grid And Spacing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- About to compose or recompose the layout of any artifact: a web page/landing page, an app or
  web UI screen, a dashboard, a DOCX/PPTX/PDF report or proposal, or a pitch-deck slide.
- Deciding column structure, gutters, margins, section spacing, and where the reader's eye should
  land first.
- A layout risks defaulting to the AI mean: an even grid of identical cards, everything centred,
  the same gap everywhere, and no focal point.
- Reviewing an existing layout that feels "assembled" rather than designed and you need to give
  it deliberate structure and tension.

## Do Not Use When

- The decision is purely *which typeface* — use
  `01-typography-and-fonts/font-selection-and-pairing`. (Set type, then lay it out here.)
- The decision is purely *which colours* — use `02-color-brand-and-visual-identity`.
- The work is a chart or table's internal design (axes, encodings, data-ink) — use the
  data-visualisation skill in this same category. This skill governs the *page-level grid the
  chart sits in*, not the chart's own marks.
- A binding client/brand grid or template already mandates the structure — follow it and record
  it, but still apply the optical-alignment and focal-point hygiene below.

## Required Inputs

- Artifact type and output format (web / UI / DOCX / PPTX / PDF / slide).
- The content inventory: what blocks exist, and their relative *importance* (you cannot build
  hierarchy without knowing what should dominate).
- The viewport/page range the layout must survive (breakpoints for web/UI; page or slide
  dimensions for documents).
- The chosen type scale and spacing unit, if already set, from
  `doctrine/references/type-scale-and-spacing.md`.

## Workflow

1. **Pick ONE spacing unit and commit to it.** Use a **4pt or 8pt** base and express every gap,
   pad, and margin as a multiple of it (8 · 16 · 24 · 32 · 48 · 64 …). This is the same rhythm
   rule as `doctrine/references/type-scale-and-spacing.md` §Spacing rhythm — consistent multiples
   are what separate "designed" from "assembled." Mixing 13px here and 19px there is a slop tell.

2. **Lay a grid, then design *against* it.** Choose a column count appropriate to the medium
   (12 columns is a flexible web default; documents often read best on a strict **2–3 column**
   or a single wide measure). The grid is scaffolding, in the Müller-Brockmann sense — it exists
   so you can place elements with intent and, deliberately, *break* it for emphasis. A grid you
   never depart from produces the dead, even page; a grid you ignore produces chaos. Hold both.

3. **Decide the focal point before placing anything.** Every composition needs one element that
   wins — the largest, the most isolated, or the most off-centre. Name it. If everything is the
   same size and evenly spaced, there is no focal point and the eye has nowhere to enter: that is
   the single most common AI-slop layout failure.

4. **Build hierarchy from three levers, not one.** Combine **scale** (size jumps, per the type
   scale's ≥1.25 ratio and real 3×-class hero jumps), **space** (more whitespace *around* a thing
   reads as more important than the thing itself), and **alignment** (a shared edge groups
   elements; a broken edge separates them). Vignelli's discipline: a few strong relationships,
   ruthlessly repeated — not many timid ones.

5. **Introduce intentional asymmetry and tension.** Centre-everything is the safe, lifeless
   default. Following the Swiss/International Typographic tradition (Müller-Brockmann, Tschichold's
   asymmetric typography), shift weight off the centre line: a wide content column beside a narrow
   margin column, a hero pinned left with air to its right, an image bleeding off one edge.
   Asymmetry is what makes a layout look *authored* — a choice a templating tool would not make.

6. **Treat whitespace as active material, not leftover.** Negative space is a design element you
   place on purpose — to isolate the focal point, to group and separate, to set pace. Generous,
   *uneven* whitespace (tight where things relate, wide where they don't) signals confidence;
   uniform padding around everything signals a default. Do not "fill" empty space; earn it.

7. **Align optically, not just mathematically.** Numerically-equal coordinates often *look* wrong:
   a circle or triangle beside a square must overshoot the box to appear aligned; punctuation,
   bullets, and icons hang fractionally outside the text edge to look flush; large type needs
   negative side-bearing trims to sit on a margin. Trust the eye over the measurement (Lupton,
   *Thinking with Type*). Where baseline rhythm applies (long-form text/documents), snap leading
   to the spacing grid so lines across columns share a baseline.

8. **Make the breakpoints deliberate — but prefer letting the grid adapt itself.** For web/UI, the
   layout must be *redesigned* at each breakpoint, not merely reflowed: a 3-column desktop grid that
   collapses to a single stacked column of identical cards on mobile re-creates the slop pattern.
   Decide what the focal point and the asymmetry become at each width. Two 2026 tools reduce how many
   breakpoints you need: **container queries** (`container-type: inline-size` + `@container` — a
   component adapts to *its container*, not the viewport, so one block lays out correctly in a wide
   column and a narrow rail) and **intrinsic layout** (e.g. `repeat(auto-fit, minmax(min(100%, 16rem),
   1fr))` reflows 1→N columns with *no* media query). Name them here; the sibling
   `03-layout-grid-and-composition/responsive-and-adaptive-layout` owns the depth (breakpoint
   strategy, fluid `clamp()`, the full intrinsic pattern library). For documents, decide how the grid
   behaves across page breaks and on the slide master.

9. **Run the anti-slop layout checklist** (below). If any item fails, fix before shipping.

## The Anti-Slop Layout Checklist (run every time)

1. One spacing unit (4pt/8pt), every gap a multiple of it — no arbitrary one-off values.
2. A named focal point — one element deliberately wins; the eye has a clear entry.
3. Hierarchy built from scale **and** space **and** alignment together, not size alone.
4. At least one intentional asymmetry / off-centre tension — not everything centred.
5. Whitespace placed *unevenly* and on purpose, not uniform padding everywhere.
6. Optical alignment applied where maths and the eye disagree (overshoot, hanging punctuation).
7. Each breakpoint/page state re-composed, not collapsed into a uniform card stack.

If the content genuinely *is* a uniform set (e.g. a true catalogue grid), say so and still break
the monotony with a featured/hero item, a varied span, or asymmetric framing — never ship a flat,
evenly-spaced card field as the whole composition.

## Anti-Patterns (the AI-slop layout tells)

- **The uniform card grid:** N identical cards in an even N-column grid with one global gutter —
  the signature of auto-arrangement. No item leads, nothing is grouped.
- **Everything centred:** every block centre-aligned down a single axis, because centring is the
  zero-decision default. Reads as a placeholder, not a composition.
- **Identical gutters everywhere:** the same gap between unrelated and related elements alike, so
  grouping carries no meaning.
- **No focal point:** uniform sizes and spacing, so the eye has nowhere to enter and no path to
  follow.
- **Dead-centre symmetry as the only structure:** never departing from the grid; mistaking
  evenness for order.
- **Whitespace as filler:** padding everything equally to "balance" rather than using space to
  signal importance and grouping.
- **Pixel-true but optically wrong:** trusting equal coordinates over the eye on shapes,
  punctuation, and large type.

## Sourcing authority (the asymmetry rule)

Grounds **only** in human design authority — never in an AI tool's layout suggestions, per
`doctrine/design-doctrine.md` §2. Canonical sources for this skill:

- **Josef Müller-Brockmann — *Grid Systems in Graphic Design*** — the grid as a discipline of
  intent; columns, fields, margins, and rhythm.
- **Jan Tschichold** — asymmetric typography and the authored, off-centre composition.
- **Massimo Vignelli** — a few strong, ruthlessly repeated relationships; the grid as a tool of
  clarity, not decoration.
- **Ellen Lupton — *Thinking with Type*** — optical alignment, hierarchy, and whitespace as
  active material.

When an AI tool happens to recommend a "12-col grid with even gutters and centred cards," treat
that as evidence of the convergent mean to *avoid*, not as endorsement.

## Outputs

- A stated layout decision: the spacing unit, the grid (columns/margins), the named focal point,
  the chosen asymmetry, and how each breakpoint/page state re-composes — declared **before** any
  markup, CSS, or document layout is produced.
- A completed anti-slop layout checklist.
- A layout that reads as deliberately authored, consistent with the Mission in
  `doctrine/design-doctrine.md` §0.

## Examples

- `examples/grid-template-worked.md` — a real **12-column + 8pt** landing-page grid applied
  end-to-end: the stated decision (7+5 hero, 8+4 features, named focal point), copy-ready CSS Grid +
  spacing tokens, a container-query variant, re-composition at each breakpoint, and the anti-slop
  checklist run against it. Read this to see the workflow above turned into shippable layout.

## References

- `references/grid-systems-catalog.md` (the named grid structures — manuscript, column, modular,
  12/16-col, asymmetric, compound — with column/gutter/margin guidance, uneven-split ratios, and the
  CSS Grid mapping; also flags container queries / intrinsic layout and defers their depth).
- `references/spacing-rhythm.md` (the operational **8pt scale**: tokens, the proximity law for
  *uneven* spacing, gutter vs. section spacing, baseline rhythm, and fluid `clamp()` spacing).
- `doctrine/design-doctrine.md` (§0 Mission — "the moat is looking human-made"; §2 sourcing-
  authority asymmetry rule).
- `doctrine/references/type-scale-and-spacing.md` (spacing-unit rhythm, type-scale ratios and
  real jumps, line-height, weight extremes — the numbers this layout's hierarchy is built on).
- `03-layout-grid-and-composition/responsive-and-adaptive-layout` (sibling — owns the *depth* of
  container queries, intrinsic layout, breakpoint strategy, and fluid responsiveness; this skill
  owns the grid + spacing decision the responsive layer adapts).
<!-- dual-compat-end -->
