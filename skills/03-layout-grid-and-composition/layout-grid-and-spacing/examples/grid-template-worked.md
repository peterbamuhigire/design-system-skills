# Worked Example: A 12-column + 8pt grid, applied end-to-end

A concrete, shippable layout decision and its CSS — not prose *about* grids. The brief: a SaaS
product landing page (Maduuka-class) that must read as **authored**, not assembled. This walks the
SKILL.md workflow, states the decision *before* the markup, then gives real CSS, then runs the
anti-slop checklist against it.

Standards basis: CSS Grid, the 8pt scale (`references/spacing-rhythm.md`), the 12-column structure
(`references/grid-systems-catalog.md`), `doctrine/references/type-scale-and-spacing.md`, and the
doctrine Mission (`doctrine/design-doctrine.md` §0 — "looks human-made").

---

## 1. The stated decision (declared BEFORE any markup)

- **Artifact / format:** responsive web landing page.
- **Spacing unit:** **8pt base**. Tokens from `spacing-rhythm.md` (`--space-*`).
- **Grid:** **12 columns**, gutter `24px` (`space-sm`), outer margin via a `1200px` max-width
  container centred with fluid side padding.
- **Focal point:** the **hero headline + primary CTA**, pinned to the **left 7 columns** with air to
  its right — the largest type on the page and the only block that breaks the 12-col into an uneven
  **7+5** split. *This is the named element that wins.*
- **Asymmetry:** the hero is **7+5**, not 6+6 — content left, product shot right, off the centre line.
  The feature row below uses an intentional **8+4** (lead feature + supporting rail), not three even
  cards.
- **Whitespace:** uneven — `space-2xl` (96) between page sections, `space-sm` (24) within the feature
  cluster. Hero gets a `space-3xl` (128) bottom margin to isolate it.
- **Breakpoints (re-composed, not collapsed):**
  - ≥1024px — full 12-col, hero 7+5, features 8+4.
  - 640–1023px — hero stacks (headline over image), features become an intrinsic 2-up.
  - <640px — single column, but the lead feature keeps a colour/scale emphasis so the field is **not**
    a flat identical-card stack (checklist item 7).

---

## 2. The CSS (concrete, copy-ready)

```css
:root {
  /* 8pt spacing scale — every gap is a token, no magic numbers */
  --space-2xs: 8px;
  --space-xs: 16px;
  --space-sm: 24px;   /* the gutter */
  --space-md: 32px;
  --space-lg: 48px;
  --space-xl: 64px;
  --space-2xl: 96px;
  --space-3xl: 128px;

  --gutter: var(--space-sm);
  --max-content: 1200px;
}

/* Centred container with fluid side margin (the outer grid margin) */
.container {
  max-width: var(--max-content);
  margin-inline: auto;
  padding-inline: clamp(var(--space-sm), 5vw, var(--space-2xl));
}

/* The 12-column grid */
.grid-12 {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--gutter);
}

/* HERO — 7+5 uneven split = the deliberate asymmetry + focal point */
.hero {
  align-items: center;
  margin-block-end: var(--space-3xl); /* 128px — isolates the focal point */
}
.hero__copy  { grid-column: 1 / span 7; }   /* the winner: largest type lives here */
.hero__visual { grid-column: 8 / span 5; }   /* product shot, pushed right */

.hero__headline {
  /* real 3×-class jump over body; fluid so it survives every width */
  font-size: clamp(2.5rem, 6vw, 4.5rem);
  line-height: 1.1;            /* tight leading for large type */
  letter-spacing: -0.01em;     /* confident heading tracking */
  margin-block-end: var(--space-md);
}

/* SECTION rhythm — uneven, on the scale */
.section { margin-block: var(--space-2xl); } /* 96px between page sections */

/* FEATURES — 8+4, NOT three even cards */
.features { gap: var(--gutter); }
.features__lead    { grid-column: span 8; }  /* lead feature dominates */
.features__support { grid-column: span 4; }  /* supporting rail */
.features__support > * + * { margin-block-start: var(--space-sm); } /* 24px within group */

/* ---- Re-composition at each breakpoint (redesigned, not reflowed) ---- */

/* Tablet: hero stacks, features become a 2-up that still keeps a lead emphasis */
@media (max-width: 1023px) {
  .hero__copy, .hero__visual { grid-column: 1 / -1; }
  .features__lead    { grid-column: span 12; }
  .features__support { grid-column: span 6; }   /* 2-up rail */
}

/* Mobile: single column — lead feature keeps scale emphasis so it is NOT a flat card field */
@media (max-width: 639px) {
  .grid-12 { grid-template-columns: 1fr; }
  .features__lead    { grid-column: 1 / -1; }
  .features__support { grid-column: 1 / -1; }
  .features__lead { padding: var(--space-lg); border-radius: 12px; } /* the one that leads */
}
```

---

## 3. Container-query variant (2026 — when a block is reused across slots)

If the feature card is dropped into both a wide main column *and* a narrow sidebar, query the
**container**, not the viewport, so the same component lays out correctly in either slot:

```css
.feature-slot { container-type: inline-size; }

.feature-card { display: grid; gap: var(--space-xs); }          /* stacked by default */
@container (min-width: 28rem) {
  .feature-card { grid-template-columns: 5rem 1fr; align-items: center; } /* icon beside text */
}
```

> Depth on container queries, intrinsic `auto-fit` reflow, fluid clamps, and full breakpoint strategy
> lives in the sibling `responsive-and-adaptive-layout`. This example shows the *grid + spacing
> decision*; that skill owns *how it adapts*.

---

## 4. Anti-slop layout checklist — run against THIS layout

1. **One spacing unit (8pt), every gap a multiple** — ✅ all gaps are `--space-*` tokens; no magic numbers.
2. **A named focal point** — ✅ hero copy in cols 1–7, largest type, isolated by 128px.
3. **Hierarchy from scale + space + alignment** — ✅ 3×-class headline (scale), 128px isolation (space), 7-col shared edge (alignment).
4. **At least one intentional asymmetry** — ✅ hero 7+5 and features 8+4, never 6+6 / three-even.
5. **Whitespace placed unevenly, on purpose** — ✅ 96px between sections vs. 24px within the feature group.
6. **Optical alignment where maths and eye disagree** — ✅ headline gets `-0.01em` negative tracking to sit flush on the column edge.
7. **Each breakpoint re-composed, not collapsed** — ✅ mobile keeps a scale/padding emphasis on the lead feature; no flat identical-card stack.

**Result:** a layout that reads as authored — an uneven, intentional grid a templating tool would not
produce — consistent with the doctrine Mission.
