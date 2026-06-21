---
name: composition-and-visual-hierarchy
description: Use when arranging the ELEMENTS within a layout so the eye reads them in an authored order — a hero, a landing page, a dashboard, a deck slide, a DOCX/PDF report cover, or any screen that must say "someone composed this on purpose." Establishes a single focal point, drives hierarchy with scale + weight + space extremes, sets a deliberate eye-path (Z / F / diagonal), uses intentional asymmetry and tension, controls figure-ground separation, treats whitespace as structure, and applies the halation rule (no pure #000/#FFF edges). Strips the everything-equal, uniform-card-grid, dead-centre AI-slop composition tells. Pairs with layout-grid-and-spacing (that skill sets the grid; this skill decides what wins on it).
status: active
metadata:
  portable: true
  category: 03-layout-grid-and-composition
  compatible_with:
    - claude-code
    - codex
---

# Composition And Visual Hierarchy
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- You have a grid and spacing decided and must now decide **what the eye sees first, second,
  third** — the order of reading, not the column structure.
- Composing a hero, landing section, dashboard, deck slide, report cover, or any screen that must
  read as **deliberately authored** rather than a neutral arrangement of equal blocks.
- A composition has gone flat: every element is roughly the same size and weight, nothing leads,
  the eye has no entry point and no path — the single most common slop failure.
- Reviewing a layout that "has all the right parts" but feels lifeless, and you need to inject a
  focal point, scale/weight extremes, tension, and figure-ground separation.
- You need to justify *why* this composition reads as crafted — to a client, a critique, or a
  design-QA gate.

## Do Not Use When

- The decision is the **grid, columns, gutters, margins, or spacing unit** — use the sibling
  `03-layout-grid-and-composition/layout-grid-and-spacing` first. That skill builds the scaffold;
  this skill composes *on* it. (They are a pair — set the grid there, decide the hierarchy here.)
- The decision is **which typeface** — use `01-typography-and-fonts/font-selection-and-pairing`.
- The decision is **which colours** — use `02-color-brand-and-visual-identity`. (You will *use*
  colour here for figure-ground and weight, but the palette itself is decided there.)
- The work is **responsive breakpoint behaviour** — use
  `03-layout-grid-and-composition/responsive-and-adaptive-layout`. Compose the focal point and
  eye-path here, then have that skill re-establish them at each width.
- The internal design of a **chart or table** (encodings, data-ink) — use the data-visualisation
  skill. This skill governs how the chart sits in the composition, not its own marks.

## Required Inputs

- The content inventory **ranked by importance** — you cannot build a hierarchy without knowing
  which single element must dominate, which support it, and which are tertiary.
- The grid + spacing decision from `layout-grid-and-spacing` (the scaffold this composition lives
  on).
- The type scale and weight range from `doctrine/references/type-scale-and-spacing.md` (the size
  and weight extremes hierarchy is built from).
- The artifact's reading context: is it scanned fast (landing/deck) or read deeply (report/long
  form)? This sets whether you compose for a glance or a sustained path.

## Workflow

1. **Name the one focal point — before composing anything.** Every composition needs exactly one
   element that wins the first fixation: the largest, the most isolated, the highest-contrast, or
   the most off-centre. Write it down ("the hero headline wins"). If you cannot name it, the
   composition has none — which is the defining AI-slop failure (`ai-slop-taxonomy.md`: everything
   equal, nothing leads). One focal point, not three; competing focal points cancel to zero. See
   `references/hierarchy-techniques.md` §Focal point.

2. **Build hierarchy from extremes, never from middle steps.** Separate the levels with **scale
   extremes** (a real 3×-class jump from hero to body, per `type-scale-and-spacing.md` "real jumps,
   not timid ones"), **weight extremes** (100/200 against 800/900, not 400 against 600 — same ref),
   and **space extremes** (isolate the focal point with far more air than anything else gets).
   Three levels, each unmistakably distinct. Timid, near-equal steps are the slop tell — they read
   as "assembled," because a templating tool spaces everything evenly.
   See `references/hierarchy-techniques.md`.

3. **Choose a deliberate eye-path and place elements along it.** Decide the route the eye takes:
   **Z-pattern** for sparse, visual, scan-fast layouts (centred hero, top-bar nav); **F-pattern**
   for text-dense pages where readers scan left edges; a **diagonal or radial path** when one image
   or number anchors the field. Place the focal point at the path's *entry*, the primary action at
   its *exit*. Treat F/Z as eye-tracking *heuristics under* this skill's focal-point rule, never as
   laws (sourcing-authority caveat). See `references/composition-and-flow.md` §Eye-path.

4. **Compose with intentional asymmetry and tension.** Dead-centre symmetry is the zero-decision
   default; it reads as a placeholder. Following the Swiss/asymmetric tradition (Tschichold,
   Müller-Brockmann), pull the focal point off the centre line and let a large element pull against
   a smaller one across open space — that *pull* is tension, and tension is what makes a composition
   look authored. A composition with no tension is inert. See `references/composition-and-flow.md`
   §Asymmetry and tension.

5. **Control figure-ground — make the focal point sit clearly in front.** The eye must instantly
   separate the subject (figure) from its background (ground). Establish it with contrast in
   value, scale, or focus: a dark subject on a light field, a sharp element over a blurred one, a
   large mark in open space. Ambiguous figure-ground (everything the same value and weight on a
   busy field) is fatiguing and reads as machine-flat. Never place type on a busy field unaided —
   use a contrast overlay (`type-scale-and-spacing.md`). See `references/composition-and-flow.md`
   §Figure-ground.

6. **Treat whitespace as structure, not leftover.** Negative space is a compositional element you
   place on purpose: it isolates the focal point, groups what belongs together, separates what does
   not, and sets the reading pace. The most important element is the one with the *most air around
   it* — space confers rank. Uneven, confident whitespace (tight where things relate, wide where
   they don't) signals authorship; uniform padding everywhere signals a default. Do not "fill"
   space; earn it. See `references/hierarchy-techniques.md` §Whitespace as rank.

7. **Apply the halation rule at every high-contrast edge.** Pure `#000` against pure `#FFF`
   produces *halation* — an optical edge-shimmer where the values vibrate and fatigue the eye
   (Paduraru, *Fundamentals*; corroborated in `docs/book-study/01-ui-ux-craft.md`). Never compose a
   focal point on a pure-black-on-pure-white edge. Pull the dark to a near-black (e.g. an off-black
   ink) and/or the light to an off-white, so the highest-contrast boundary in your composition is
   *deliberately* softened. This is a physical optics reason, not a style preference. See
   `references/hierarchy-techniques.md` §The halation rule.

8. **Read the composition back as a stranger would.** Squint at it (blur the detail) and check:
   does one thing still dominate? Is there a single obvious entry and a path out? Is there
   asymmetric tension, or did it settle to centre? Then run the checklist below.

## The Authored-Composition Checklist (run every time)

1. **One named focal point** — exactly one element wins the first fixation; you can say which.
2. **Hierarchy from extremes** — scale, weight, and space each separate the levels unmistakably;
   no timid near-equal steps.
3. **A deliberate eye-path** — Z / F / diagonal chosen on purpose; focal point at entry, primary
   action at exit.
4. **Intentional asymmetry + tension** — the focal point is off-centre and pulls against the rest;
   not dead-centre symmetry as the only structure.
5. **Clear figure-ground** — the subject separates instantly from the ground by value/scale/focus;
   no type on a busy field unaided.
6. **Whitespace confers rank** — the most important element has the most air; space is uneven and
   placed, not uniform filler.
7. **Halation controlled** — no pure `#000`-on-`#FFF` high-contrast edge at the focal point;
   softened to off-black / off-white on purpose.
8. **Not a flat field** — if the content is genuinely a uniform set, one item is still promoted
   (a featured/hero) so it does not ship as an even, identical-card grid.

## Anti-Patterns (the AI-slop composition tells)

- **Everything equal, nothing leads** — uniform sizes, weights, and spacing, so the eye has no
  entry and no path. The defining composition slop (`ai-slop-taxonomy.md`).
- **The uniform card grid** — N identical cards in an even grid: auto-arrangement with no focal
  point and no flow. Never ship a flat, evenly-spaced card field as the whole composition.
- **Dead-centre symmetry as the only structure** — centring everything because it is the
  zero-decision default; mistaking evenness for order, producing an inert, tensionless page.
- **Competing focal points** — three things all shouting; with no single winner the hierarchy
  collapses to flat.
- **Timid hierarchy** — levels separated by near-equal steps (18px vs 20px, 400 vs 600) so nothing
  reads as clearly dominant.
- **Whitespace as filler** — padding everything equally to "balance," instead of using space to
  confer rank and grouping.
- **Ambiguous figure-ground** — subject and background at the same value/weight on a busy field;
  fatiguing and machine-flat.
- **Pure-black-on-pure-white focal edges** — ignoring halation; the highest-contrast boundary
  shimmers and tires the eye.
- **Glassmorphism / frosted-blur as a decorative focal surface** — taught by primers
  (*Fundamentals of Creating a Great UI/UX*) but a convergent slop tell and usually a contrast
  failure (`ai-slop-taxonomy.md` §Counter-doctrinal). Use a deliberate, legible surface instead.

## Sourcing authority (the asymmetry rule)

Grounds **only** in human design authority — never in an AI tool's composition suggestions, per
`doctrine/design-doctrine.md` §2. Canonical sources for this skill:

- **Jan Tschichold** — asymmetric typography and the authored, off-centre composition.
- **Josef Müller-Brockmann — *Grid Systems in Graphic Design*** — placing elements with intent on
  (and deliberately against) the grid.
- **Massimo Vignelli** — a few strong, ruthlessly repeated relationships; one decisive contrast
  over many timid ones.
- **Ellen Lupton — *Thinking with Type*** — hierarchy, figure-ground, and whitespace as active
  material.
- **Rudolf Arnheim — *Art and Visual Perception*** — figure-ground, visual weight, balance, and
  tension as perceptual forces.
- The **halation** optical rule and the F/Z scanning heuristics are taken from
  `docs/book-study/01-ui-ux-craft.md` as *heuristics under* the doctrine, not as taste authority.

When an AI tool happens to recommend "a centred hero with three equal cards below," treat that as
evidence of the convergent mean to **avoid**, not as endorsement.

## Outputs

- A stated composition decision, declared **before** any markup or layout: the named focal point,
  the three hierarchy levels and the scale/weight/space extremes separating them, the chosen
  eye-path, the asymmetry/tension, the figure-ground treatment, and the halation-safe values.
- A completed Authored-Composition Checklist.
- A composition that reads as deliberately authored, consistent with the Mission in
  `doctrine/design-doctrine.md` §0 — "the moat is looking human-made."

## Examples

- `examples/before-after-composition.md` — one real screen (a pricing-page hero) composed twice:
  a **before** that fails as flat, centred, three-equal-cards, pure-#000-on-#FFF slop, and an
  **after** that names a focal point, drives hierarchy from extremes, sets a Z eye-path, adds
  asymmetric tension, fixes figure-ground, and softens the halation edge — with copy-ready CSS and
  the checklist run against it. Read this to see the workflow turned into shippable composition.

## References

- `references/hierarchy-techniques.md` — the operational levers: focal point, the three-level rule,
  scale/weight/space extremes, whitespace-as-rank, and the halation rule (with values).
- `references/composition-and-flow.md` — eye-path (Z / F / diagonal / radial), intentional
  asymmetry and tension, figure-ground separation, and how flow re-reads at each viewport.
- `doctrine/design-doctrine.md` (§0 Mission — "the moat is looking human-made"; §2
  sourcing-authority asymmetry rule).
- `doctrine/references/ai-slop-taxonomy.md` (the "everything equal / uniform card grid / no focal
  point" composition slop and the glassmorphism inoculation this skill refuses).
- `doctrine/references/type-scale-and-spacing.md` (the scale ratios, real jumps, weight extremes,
  line-height, and the not-pure-black rule this hierarchy is built from).
- `03-layout-grid-and-composition/layout-grid-and-spacing` (the **pair** — sets the grid + spacing
  unit + focal-point placement this skill composes hierarchy on top of).
<!-- dual-compat-end -->
