# Reference: Spacing Rhythm — the 8pt scale and how to spend space

One spacing unit, expressed as multiples everywhere, is what separates a *designed* layout from an
*assembled* one. Mixing 13px here and 19px there is a slop tell; a coherent scale is invisible and
that is the point. This file is the concrete spacing system the `layout-grid-and-spacing` skill
draws on. Standards basis: the 8pt grid (Material Design metrics; Apple HIG point system), the Chwezi
anti-slop rhythm rule, and `doctrine/references/type-scale-and-spacing.md` § Spacing rhythm — this
file is the operational expansion of that one line.

---

## 1. Pick the base unit (4pt or 8pt)

- **8pt base** — the default for screens. Every gap, pad, and margin is a multiple of 8. Pairs cleanly
  with most type scales and divides evenly on @1x/@2x/@3x raster.
- **4pt base** — use when dense UI (data tables, toolbars, compact forms) needs finer control. Treat
  **4pt as the *half-step*** of an 8pt system, not a free-for-all — 4 is allowed, 6 is not.
- **Commit to ONE base per artifact** and record it. The base is a stated decision, like the typeface.

---

## 2. The scale (8pt)

```
4 · 8 · 16 · 24 · 32 · 40 · 48 · 64 · 80 · 96 · 128
```

Token-friendly naming (use these names in code/design tokens, never raw magic numbers):

| Token | px (8pt) | Typical use |
|---|---|---|
| `space-3xs` | 4 | Icon-to-label, hairline insets (4pt half-step). |
| `space-2xs` | 8 | Tight grouping inside a component. |
| `space-xs` | 16 | Default gap between related items; base body line gap. |
| `space-sm` | 24 | Card padding; gutter between columns. |
| `space-md` | 32 | Gap between sub-sections within a block. |
| `space-lg` | 48 | Block-to-block separation. |
| `space-xl` | 64 | Major section breaks. |
| `space-2xl` | 96 | Hero / page-region separation. |
| `space-3xl` | 128 | Full-bleed section rhythm on large viewports. |

A value outside this set (e.g. 13, 19, 30) is a defect — round to the nearest token.

---

## 3. The proximity law — *uneven* space carries meaning

Whitespace is active material, not leftover (Lupton). Equal padding everywhere destroys grouping.

> **Space between unrelated things must be larger than space within a group.**

| Relationship | Spend | Example |
|---|---|---|
| Within a tight group (label + value) | `space-2xs`–`space-xs` (8–16) | A stat and its caption. |
| Between related items in a section | `space-sm` (24) | Cards in one cluster. |
| Between sub-sections | `space-md`–`space-lg` (32–48) | Intro block → feature block. |
| Between page-level sections | `space-xl`–`space-2xl` (64–96) | Hero → body → footer. |

If the gap inside a group equals the gap between groups, the grouping is invisible — the
"identical-gutters-everywhere" slop tell. Make the jump obvious (≥1.5× from one tier to the next).

---

## 4. Gutter vs. section spacing (do not conflate)

- **Gutter** — the *horizontal* gap between grid columns (`space-sm`, 24px is a common web default).
  It is constant across the grid by design.
- **Section spacing** — the *vertical* rhythm between stacked blocks. It **varies** by relationship
  (the proximity law). A single value used for both is the flat-page tell.

---

## 5. Baseline rhythm (long-form text & documents)

Where reading is dominant (essays, reports, multi-column prose), snap **leading to the spacing grid**
so lines across columns share a baseline. With an 8pt base and 16px body at 1.5 line-height, the line
box is 24px — a clean multiple, so paragraphs land on the grid. Choose body size + line-height so the
line box is a multiple of the base (16/24, 18/24-or-30 round, 20/32). This is what makes a two-column
document read as typeset rather than pasted.

- Small text (<32pt): line-height ≈ 1.5–1.6× (see type-scale-and-spacing.md).
- Large text (32pt+): tighter, 1.1–1.3× — but still round the resulting line box toward the grid.

---

## 6. Fluid spacing (2026)

For section rhythm that scales with the viewport without a stack of breakpoints, use `clamp()` keyed
to the scale's endpoints rather than a fixed value:

```css
:root { --section-gap: clamp(2rem, 6vw, 6rem); } /* 32px → 96px, fluid */
```

Keep the clamp's min and max **on the token scale** (32 and 96 above) so the system stays coherent at
both ends. Container-driven spacing (a component spacing itself to its container, not the viewport) is
owned by the sibling `responsive-and-adaptive-layout`.

---

## 7. Anti-patterns this reference exists to prevent

- **Arbitrary one-off values** (13, 19, 30px) — not on the scale, so the rhythm reads as accidental.
- **Uniform padding everywhere** — equal space within and between groups; grouping carries no meaning.
- **Gutter = section spacing** — one global gap conflating horizontal and vertical rhythm.
- **Filling empty space to "balance"** — whitespace is placed to signal importance, not mopped up.
- **Leading off the grid** in multi-column prose — baselines drift, text reads as pasted.
