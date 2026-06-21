# Reference: Hierarchy Techniques

The operational levers that turn an arrangement of equal blocks into an order the eye reads. This
reference is the "what wins, and by how much" companion to `composition-and-flow.md` (which owns
the *path* the eye travels). Numbers trace to `doctrine/references/type-scale-and-spacing.md`;
the anti-slop framing traces to `doctrine/references/ai-slop-taxonomy.md` and the Mission in
`doctrine/design-doctrine.md` §0.

---

## Focal point — exactly one

A composition needs **one** element that wins the first fixation. Pick its source of dominance:

| Source of dominance | How it wins | Use when |
|---|---|---|
| **Scale** | Far larger than everything else | A hero headline, a key number, a primary visual |
| **Isolation** | Far more whitespace around it | A single CTA, a verdict line, a price |
| **Contrast** | Highest value/colour/weight jump on the page | A status, a brand mark, a call to action |
| **Position** | Most off-centre / at the eye-path entry | A pinned-left hero, a corner anchor |

Rules:

- **One, not three.** Two or more elements competing for first fixation cancel to zero hierarchy —
  the page reads flat. This is the *competing focal points* slop tell.
- **Name it before composing.** If you cannot write "X wins," there is no focal point — the
  defining AI-slop composition failure (`ai-slop-taxonomy.md`: everything equal, nothing leads).
- The focal point usually combines two sources (e.g. *largest* **and** *most isolated*). One strong
  combined contrast beats five timid ones (Vignelli).

---

## The three-level rule

Resolve the content inventory into **three** ranks and no more in any one view:

1. **Primary** — the focal point. One element.
2. **Secondary** — supports the primary (subhead, supporting visual, secondary action).
3. **Tertiary** — everything else (metadata, footnotes, fine print).

Three levels keep a view coherent (`type-scale-and-spacing.md`: at most ~3 font sizes per
section). Four or more competing levels read as noise. Each level must be **unmistakably** distinct
from the next — see extremes below.

---

## Build the levels from extremes, not middle steps

The difference between "designed" and "assembled" is the *size of the gap* between levels. Use
extremes on all three axes:

### Scale extremes
- **Real jumps, not timid ones.** Hero-to-body can be **3× or more** (`type-scale-and-spacing.md`).
  Sizes that sit almost the same (18 vs 20) are a slop signal.
- Build off a real ratio — Golden (1.618) for editorial confidence, 1.25 (major third) as the safe
  minimum. Example 1.25 scale off 16px: 12 · 16 · 20 · 25 · 31 · 39 · 49 · 61.

### Weight extremes
- Contrast **100/200 against 800/900**, not 400 against 600 (`type-scale-and-spacing.md`).
- Combine weight **with** size, never weight alone — a heavy small label still loses to a light
  large headline.

### Space extremes (whitespace as rank — see below)
- The most important element gets the **most air**. Isolation is a dominance source in its own
  right; a small element with a large clear field around it can out-rank a bigger crowded one.

> The test: squint until detail blurs. If the three levels still separate by sheer blob size and
> darkness, the extremes are doing their job. If they merge into one grey field, the hierarchy is
> timid — widen the gaps.

---

## Whitespace as rank

Negative space is structure, not leftover. It does four jobs:

1. **Confers rank** — the element with the most air around it reads as most important. Space *is*
   hierarchy.
2. **Groups** — elements close together are read as belonging together (proximity).
3. **Separates** — a wide gap says "different thing"; a tight gap says "same thing."
4. **Sets pace** — generous space slows the eye and signals importance; tight space speeds it.

Confident whitespace is **uneven**: tight where things relate, wide where they don't. Uniform
padding around everything is the *whitespace-as-filler* slop tell — it carries no meaning, so
nothing is grouped and nothing leads. Do not fill empty space to "balance" a page; earn it by using
it to rank and group. (Lupton, *Thinking with Type*.)

---

## The halation rule

**Never compose a focal point on a pure `#000` against pure `#FFF` edge.**

*Halation* is an optical effect: at a maximum-contrast boundary the two values appear to vibrate or
bleed into each other, producing an edge-shimmer that fatigues the eye. It is a property of human
vision, not a style preference (Paduraru, *Fundamentals of Creating a Great UI/UX*; logged in
`docs/book-study/01-ui-ux-craft.md` as the physical *reason* behind the engine's long-standing
"avoid pure black/white" rule in `type-scale-and-spacing.md`).

The fix — soften the highest-contrast boundary deliberately:

- Pull body/heading ink to a **near-black** instead of `#000` (e.g. an off-black around `#16181d`
  / a very dark neutral).
- Pull the background off pure white to a faint **off-white** (e.g. `#fafafa`–`#f5f5f4`) where the
  surface is large.
- Keep the *contrast ratio* well within WCAG (this softening is cosmetic optics, not a contrast
  reduction below the floor — verify against `doctrine/references/wcag-2.2-criteria.md`).

This applies most at the **focal point**, where the eye dwells longest. A halation-safe focal edge
is one of the quiet tells that a human composed the screen.

---

## What this prevents (the anti-patterns this reference exists to kill)

- **Everything equal, nothing leads** — no named focal point; levels separated by timid steps.
- **Competing focal points** — three winners, therefore none.
- **Whitespace as filler** — uniform padding that confers no rank.
- **Pure-#000-on-#FFF focal edges** — ignored halation, a shimmering, fatiguing boundary.

If any appears, fix it before shipping — see the Authored-Composition Checklist in `SKILL.md`.
