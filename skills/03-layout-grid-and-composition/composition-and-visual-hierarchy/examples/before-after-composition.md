# Worked Example: Composing one real screen — before / after

One real screen — the **hero of a SaaS pricing page** (Maduuka-class product) — composed twice. The
**before** is the convergent AI mean: flat, centred, three equal cards, pure-`#000`-on-`#FFF`. The
**after** names a focal point, drives hierarchy from extremes, sets a Z eye-path, adds asymmetric
tension, fixes figure-ground, and softens the halation edge. This walks the `SKILL.md` workflow,
states the composition decision *before* the CSS, then runs the Authored-Composition Checklist.

Standards basis: `references/hierarchy-techniques.md`, `references/composition-and-flow.md`,
`doctrine/references/type-scale-and-spacing.md`, `doctrine/references/ai-slop-taxonomy.md`, and the
Mission (`doctrine/design-doctrine.md` §0). The grid + spacing unit comes from the sibling
`layout-grid-and-spacing` — this example composes hierarchy *on* that grid.

The content inventory (ranked): (1) the value-proposition headline, (2) the "Start free" primary
action, (3) one supporting subhead, (4) three plan summaries, (5) a "no card required" reassurance
line.

---

## BEFORE — the slop composition (what to reject)

```css
/* Everything centred, everything equal — the zero-decision default */
.hero { text-align: center; max-width: 720px; margin: 0 auto; padding: 64px 0; }

.hero__headline { font-size: 32px; font-weight: 600; color: #000; }   /* timid */
.hero__subhead  { font-size: 20px; font-weight: 400; color: #000; }   /* near-equal step */
.hero__cta      { font-size: 16px; font-weight: 600; }                /* lost below the fold of attention */

/* Three identical cards in an even grid — auto-arrangement, nothing leads */
.plans { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; }
.plan  { padding: 24px; border: 1px solid #000; background: #fff; text-align: center; }
```

Why it fails (mapped to the anti-patterns in `SKILL.md`):

- **Everything equal, nothing leads** — 32 vs 20px is a *timid* step (no 3× jump); 600 vs 400 is a
  *timid* weight gap. No element wins the first fixation. No named focal point.
- **Dead-centre symmetry as the only structure** — every block on one centred axis; no tension.
- **The uniform card grid** — three identical plan cards, one global gutter; the signature of
  auto-arrangement (`ai-slop-taxonomy.md`).
- **Whitespace as filler** — even 64px padding and one 24px gap everywhere; space confers no rank.
- **Pure-`#000`-on-`#FFF`** — the headline edge shimmers (halation); fatiguing where the eye dwells.
- **No eye-path** — centred symmetry gives the eye nowhere deliberate to enter or exit.

---

## AFTER — the stated composition decision (declared BEFORE the CSS)

- **Focal point (named):** the **value-prop headline** wins — *largest* (a real 3×-class jump over
  body) **and** *most isolated* (a 96px clear field below it). Source of dominance: scale + isolation.
- **Three levels (extremes):**
  - Primary — headline: `~4rem`, weight `800`.
  - Secondary — subhead + primary CTA: `1.25rem` / a high-contrast filled button.
  - Tertiary — the three plan summaries and the reassurance line: `0.95rem`, light weight.
- **Eye-path:** **Z-pattern** — brand/eyebrow top-left → headline (entry, upper band) → product
  visual top-right → diagonal down to the **"Start free" CTA at the bottom-left→right exit**.
- **Asymmetry + tension:** the hero copy is pinned **left (7 cols)** with the product visual **right
  (5 cols)** — a `7+5` split, never `6+6`. The large headline on the left pulls against the smaller
  visual across open space: that pull is the tension.
- **Figure-ground:** headline is near-black ink isolated in open space (value + isolation contrast);
  the *one* promoted plan ("Pro") becomes the figure among the three via scale + a tinted plate, so
  the plan row is **not** a flat identical-card field.
- **Halation-safe:** ink pulled to off-black `#16181d`; large hero surface to off-white `#fafafa`.
  The highest-contrast edge is softened on purpose (contrast still well within WCAG).

---

## AFTER — the CSS (concrete, copy-ready)

```css
:root {
  --ink: #16181d;          /* off-black — halation-safe, not #000 */
  --surface: #fafafa;      /* off-white — halation-safe, not #fff */
  --accent: #1f5f4f;       /* figure plate for the promoted plan */
  /* 8pt spacing scale (from layout-grid-and-spacing) */
  --space-sm: 24px; --space-md: 32px; --space-2xl: 96px; --space-3xl: 128px;
}

.hero {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-sm);
  background: var(--surface);
  color: var(--ink);
  align-items: center;
}

/* Asymmetry + tension: 7+5, copy left, visual right — never centred 6+6 */
.hero__copy   { grid-column: 1 / span 7; }
.hero__visual { grid-column: 8 / span 5; }   /* the smaller weight it pulls against */

/* PRIMARY — the focal point: scale extreme + isolation extreme */
.hero__headline {
  font-size: clamp(2.5rem, 6vw, 4rem);   /* real 3x-class jump over body */
  font-weight: 800;                       /* weight extreme, not 600 */
  line-height: 1.1;                        /* tight leading for large type */
  letter-spacing: -0.01em;                 /* confident heading tracking */
  margin-block-end: var(--space-2xl);      /* 96px of air = isolation = rank */
}

/* SECONDARY — clearly below the primary, clearly above tertiary */
.hero__subhead { font-size: 1.25rem; font-weight: 400; max-width: 42ch;
                 margin-block-end: var(--space-md); }
.hero__cta {                                  /* the Z-path exit */
  font-size: 1rem; font-weight: 700;
  background: var(--ink); color: var(--surface);
  padding: 16px 32px;                         /* 2x side padding for optical balance */
  border-radius: 10px;
}
.hero__reassure { font-size: 0.9rem; font-weight: 300; opacity: 0.7;
                  margin-block-start: var(--space-sm); }   /* tertiary */

/* PLAN ROW — NOT a uniform card grid: one plan is promoted to the figure */
.plans { grid-column: 1 / -1; display: grid; grid-template-columns: repeat(3, 1fr);
         gap: var(--space-sm); margin-block-start: var(--space-3xl); align-items: end; }
.plan  { padding: var(--space-md); border: 1px solid #e6e6e3; border-radius: 12px; }
.plan--pro {                                  /* the figure among the ground */
  background: var(--accent); color: var(--surface);
  transform: scale(1.06);                     /* scale contrast lifts it forward */
  padding-block: var(--space-2xl);            /* more air = more rank */
}
```

---

## AFTER — Authored-Composition Checklist (run against THIS composition)

1. **One named focal point** — the headline (largest + isolated by 96px). Yes.
2. **Hierarchy from extremes** — 3×-class scale jump, weight `800` vs `300`, 96px isolation vs 24px
   gaps. No timid steps. Yes.
3. **A deliberate eye-path** — Z: eyebrow top-left → headline → visual top-right → CTA exit. Yes.
4. **Intentional asymmetry + tension** — `7+5`, copy left pulling against the visual right. Yes.
5. **Clear figure-ground** — near-black headline isolated in open space; the "Pro" plan promoted to
   figure by scale + tinted plate. Yes.
6. **Whitespace confers rank** — headline gets the most air; spacing is uneven (96/128 vs 24). Yes.
7. **Halation controlled** — ink `#16181d` on `#fafafa`, not `#000` on `#fff`, at the focal edge. Yes.
8. **Not a flat field** — three plans, but "Pro" is promoted; not an even identical-card grid. Yes.

**Result:** a hero that reads as **authored** — one element leads, the eye has a clear entry and
exit, the composition holds asymmetric tension, the figure sits cleanly in front, and the
highest-contrast edge is softened on purpose. A templating tool would have shipped the *before*;
this is the moat (`doctrine/design-doctrine.md` §0).
