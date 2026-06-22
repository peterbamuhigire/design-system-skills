---
name: fluid-responsive-typography
description: Use when type must scale smoothly across screen sizes without breakpoint-snapping — a website, landing page, web/app UI, dashboard, email, or any browser-rendered artifact that runs from a budget phone (~320–360px) to ultrawide. Builds modular fluid type scales with `clamp()` (deriving the min/preferred/max and the vw coefficient from the math, not guessing), controls line-length/measure across breakpoints, sets fluid line-height, scales type to its CONTAINER with container-query units, and keeps it all from breaking browser zoom/reflow (WCAG 1.4.4 / 1.4.10). This is the fluid-sizing entry skill for typography; pairs with font-selection-and-pairing (pick the faces and scale there) and responsive-and-adaptive-layout (make the whole grid respond there).
status: active
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
    - claude-code
    - codex
---

# Fluid Responsive Typography
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- A type scale must interpolate smoothly between a floor and a ceiling across widths — phone to
  ultrawide — instead of jumping at hand-tuned breakpoints.
- You are writing the `clamp()` for headings/display and need the *derivation* (min, preferred
  with its `vw` coefficient, max) rather than copy-pasted magic numbers.
- Line length (measure) drifts too long on wide screens or too cramped on phones and must be
  capped/controlled across breakpoints.
- A type block lives in a resizable component (card, sidebar, modal) and should size to its
  **container**, not the viewport — container-query type.
- An existing page uses `font-size: 5vw` (or similar) and breaks browser zoom / 200% reflow.

## Do Not Use When

- The typeface itself is not yet chosen, or you need the underlying modular scale steps — set
  those first in `01-typography-and-fonts/font-selection-and-pairing` (this skill interpolates
  *between* its steps; it does not invent sizes).
- The whole page grid/columns/breakpoint strategy is the question, not just type sizing — use
  `03-layout-grid-and-composition/responsive-and-adaptive-layout` (its sibling pair); set the
  responsive grid there, size the type here.
- The artifact is a fixed-canvas document or slide (DOCX/PPTX/PDF) with no fluid viewport — fluid
  `clamp()`/`vw` has nothing to interpolate against; use a fixed scale.
- The task is purely choosing weights/pairings or running a slop audit — those are other
  `01-typography-and-fonts` skills.

## Required Inputs

- The **realistic width range** the type must survive — the smallest target width and the largest
  (e.g. 320 or 360px → 1440px), not an assumed default. The `clamp()` floor/ceiling anchor here.
- The **modular scale steps** (px + rem) to make fluid, from
  `font-selection-and-pairing/references/type-scale-recipes.md` and
  `doctrine/references/type-scale-and-spacing.md` (ratio ≥1.25, real jumps, inverse line-height).
- Which blocks are **container-portable** (rendered at more than one container width) — these get
  container-query type, not viewport `vw`.
- The reading context for **measure**: long-form body wants ~60–75ch; UI labels are short.

## Workflow

1. **Anchor the range, then derive — never guess the `vw`.** Pick the floor width (smallest
   realistic viewport) and ceiling width (largest the design must survive). For each step that
   should be fluid, set MIN = its size at the floor width and MAX = its size at the ceiling width
   (both in `rem`, so zoom works). Then compute the preferred line so it hits MIN at the floor and
   MAX at the ceiling. With widths in `rem` (`px/16`):

   ```
   slope (vw coeff) = (MAX − MIN) / (ceilingRem − floorRem) × 100
   intercept (rem)  = MIN − slope/100 × floorRem
   PREFERRED        = {intercept}rem + {slope}vw
   font-size        = clamp(MIN, {intercept}rem + {slope}vw, MAX)
   ```

   Full derivation, a sign-of-intercept check, and a generated scale in
   `references/fluid-scale-math.md`. Generators (utopia.fyi) emit this; you still verify the px
   endpoints by hand.

2. **Always set a `rem` floor AND a `rem` ceiling — never a bare `vw`.** A pure-`vw` size (or a
   `clamp()` with a `vw` bound) defeats browser zoom and 200% reflow — a **WCAG 1.4.4 / 1.4.10**
   failure (`doctrine/references/wcag-2.2-criteria.md`). The floor keeps phones legible; the
   ceiling stops ultrawide ballooning. Test by reading at *both* extremes plus 200% zoom.

3. **Do not fluid-scale body copy.** Keep `--fs-body` a fixed `rem` (typically 1rem/16px). Fluid
   body text changes the line length as the window moves and harms reading rhythm; let the
   *measure* (step 4) adapt instead. Make display/h1/h2/h3 fluid; leave body and captions fixed.

4. **Control measure (line length) across breakpoints, independently of font size.** Cap the text
   column so a line never runs past comfortable reading regardless of viewport. Use
   `width: min(100% - 2rem, 66ch)` (or `inline-size`) with `margin-inline: auto`: ~60–66ch for
   long-form body, up to ~75ch max, narrower for large display. `ch` is font-relative, so the cap
   tracks the chosen face. This is the breakpoint-independent half of "responsive type" that pure
   `clamp()` sizing forgets — see `doctrine/references/type-scale-and-spacing.md`.

5. **Set fluid (size-inverse) line-height.** Leading must tighten as type grows: small text
   ≈ ×1.6, large text ×1.3 down to ×1.05 (`type-scale-and-spacing.md`). Because the size is now
   fluid, prefer a **unitless** `line-height` (it tracks the computed size automatically), or for a
   block whose size sweeps a wide range, interpolate leading too with `clamp()` so the hero never
   keeps body leading. Unitless is the default; clamp the leading only when one element spans a big
   size range.

6. **Scale container-portable type to its CONTAINER, not the viewport.** A heading inside a card
   that appears both full-width and in a 4-up grid must size to where it is *placed*. Set
   `container-type: inline-size` on the wrapper and size the type in **`cqi`** (1cqi = 1% of the
   container inline-size) inside a `clamp()`: `font-size: clamp(1.25rem, 0.9rem + 3cqi, 2rem)`.
   Now the same component is large in a hero and modest in a sidebar at the *same* viewport width —
   the viewport-`vw` version cannot do this. Pairs with
   `03-layout-grid-and-composition/responsive-and-adaptive-layout` (container queries).

7. **Keep the modular relationship intact.** Fluid steps still derive from the chosen ratio
   (≥1.25) with real jumps and weight extremes — `clamp()` interpolates the *journey* of each step
   between its floor and ceiling; it does not flatten the scale. Verify hero÷body is still a real
   multiple (≈3–6×) at the ceiling.

8. **Run the fluid-type anti-slop / a11y checklist** (below). If any item fails, fix before
   shipping. Hand the chosen faces' loading/subsetting to `font-embedding-and-licensing`.

## The Fluid-Type Checklist (run every time)

1. Every fluid step has a **`rem` floor AND a `rem` ceiling** — no bare `vw`/`cqi` bound anywhere.
2. The preferred line's `vw`/`cqi` coefficient is **derived** (min/max at named widths), not guessed.
3. **Body and captions stay fixed `rem`** — only display/headings are fluid.
4. **200% zoom and 320px reflow both pass** — text scales and nothing is clipped (WCAG 1.4.4/1.4.10).
5. **Measure is capped** (`min(…, ~66ch)` + `margin-inline: auto`) independently of font size.
6. **Line-height is size-inverse** (unitless default; clamp leading only for wide-range elements).
7. Container-portable type uses **`cqi` + `container-type`**, not viewport `vw`.
8. The **modular ratio and weight extremes survive** at both extremes — hero÷body still a real jump.
9. The browser **root font-size is never overridden** (that breaks user zoom and rem math).

If the checklist cannot be satisfied, say so and ask — never ship a `vw`-only size that breaks zoom.

## Anti-Patterns (the fluid-type slop / a11y tells)

- **Pure-`vw` sizing:** `font-size: 5vw` (or a `clamp()` with a `vw` bound) — illegible on phones,
  gigantic on ultrawide, and it **breaks browser zoom** (WCAG 1.4.4 failure).
- **Guessed coefficients:** a `clamp()` with a `vw` number picked by eye instead of derived, so the
  type misses its intended endpoints.
- **Fluid body text:** scaling paragraph copy with the viewport — the line length wanders and
  reading rhythm dies. Body is fixed; the *measure* adapts.
- **No measure cap:** full-width body that runs 120ch on a wide monitor — unreadable, and a clear
  "unconsidered" tell.
- **Frozen leading:** keeping ×1.6 body line-height on a 64px hero so the hero looks airy and loose.
- **Viewport units for component type:** `vw` on a card heading that should respond to its container.
- **Overriding `html { font-size }` in px:** kills the user's zoom preference and the rem chain.

## Sourcing authority (the asymmetry rule)

Grounds **only** in human design and web-standards authority — never an AI tool's sizing
suggestions, per `doctrine/design-doctrine.md` §2. Canonical sources:

- **The CSS specifications** — `clamp()`/`min()`/`max()` math functions, container query units
  (`cqi`), and viewport/`ch` units — admissible as *standards*, not AI endorsement.
- **WCAG 2.2 (W3C)** — 1.4.4 Resize Text and 1.4.10 Reflow as the hard floor for any `vw`/fluid size.
- The Chwezi type-scale doctrine (Gingerich; Paduraru) for ratio, inverse line-height, and measure.

When an AI tool offers `font-size: 6vw` with no floor/ceiling, treat it as the convergent mistake to
*avoid* — not as a pattern to adopt.

## Outputs

- A stated fluid-type decision **before** any CSS: the floor/ceiling widths, which steps are fluid
  (and which stay fixed), the derived `clamp()` for each, the measure cap, and the line-height plan.
- The fluid CSS itself — `clamp()` scale, capped measure, size-inverse leading, and `cqi`
  container-query type where needed — see `examples/fluid-type-scale.md`.
- A completed fluid-type checklist, within the budgets of
  `doctrine/references/web-performance-budgets-2026.md` and the Mission of
  `doctrine/design-doctrine.md` §0.

## Examples

- `examples/fluid-type-scale.md` — a real fluid type scale for a 320→1440px range: the stated
  floor/ceiling, the `clamp()` derivation shown step by step for each heading (with the `vw`
  coefficient computed), a verified px-endpoint table, the capped measure, size-inverse fluid
  line-height, and a container-query (`cqi`) heading variant — run against the checklist.

## References

- `references/fluid-scale-math.md` — the `clamp()` derivation (min/preferred/max + the `vw`
  coefficient), the intercept-sign sanity check, container-query (`cqi`) units, and a generated scale.
- `doctrine/references/type-scale-and-spacing.md` — the modular ratio, inverse line-height, and
  measure rules the fluid scale interpolates between (clamp does not invent sizes).
- `doctrine/references/wcag-2.2-criteria.md` — 1.4.4 resize-text / 1.4.10 reflow: the zoom floor any
  fluid/`vw` size must not break.
- `01-typography-and-fonts/font-selection-and-pairing` — pick the faces and the modular scale first;
  see its `references/type-scale-recipes.md` for the base px/rem steps.
- `03-layout-grid-and-composition/responsive-and-adaptive-layout` — the sibling pair: make the whole
  grid respond there; size the type fluidly here.
- `doctrine/references/web-performance-budgets-2026.md` — `font-display`/preload and CLS constraints
  fluid type must respect.
<!-- dual-compat-end -->
