# Reference: Breakpoint Strategy — choose by content, keep few, prefer none

Breakpoints are a *last resort*, not the starting point. The first move is always intrinsic layout
(`container-queries-and-intrinsic.md`); a breakpoint is justified only where the **design must
change**, not merely where the screen got wider. This file is the decision guide the
`responsive-and-adaptive-layout` skill uses. Pairs with
`03-layout-grid-and-composition/layout-grid-and-spacing` (the composition each breakpoint re-states)
and `doctrine/references/type-scale-and-spacing.md` (the steps fluid `clamp()` interpolates).

---

## 1. The decision order (do these in sequence)

1. **Can it be intrinsic?** Try `auto-fit`/`minmax`, flex-wrap with `min-inline-size`, `clamp()`,
   and `min()`-capped measure first. Most layouts need **zero** media queries. If intrinsic reflow
   handles it, stop — you have no breakpoint to add.
2. **Is it a portable component?** If a single component must look right in several container widths,
   it gets a **container query**, not a viewport breakpoint (see the companion reference).
3. **Does the whole template re-arrange?** Only a page-global structural change — a sidebar appears,
   a hamburger becomes a horizontal bar, a 1-column reading view gains a margin column — earns a
   **viewport media query**.

If you reach step 3, continue below.

---

## 2. Choose the breakpoint where the CONTENT breaks

Do **not** target device names or fashionable pixel widths. Method:

1. Open the layout at the **smallest** realistic width and slowly widen it.
2. Watch for the point where it *breaks*: a line exceeds ~70–75ch and gets hard to read; a column
   becomes too narrow to hold its content; whitespace turns into an awkward gap; the focal point is
   lost or the hierarchy flattens.
3. Put the breakpoint **there** — at the content's natural failure point, which is design-specific
   and rarely lands on 768 or 1024.
4. Re-compose at that width (focal point, asymmetry, what leads) per `layout-grid-and-spacing` §8.

This yields breakpoints that belong to *your* content, and it is why a fixed device list is a slop
tell — it optimises for last year's hardware instead of this design.

---

## 3. Keep the set small — and in `em`/`rem`

- **Two to four** breakpoints is typical for a whole page. More than that usually means the base
  layout isn't intrinsic enough — fix the base, delete the breakpoints.
- Express widths in `em` (or `rem`) so they scale with the user's font size. A user who zooms text
  to 150% effectively shifts the breakpoints — the layout reorganises *for them*, which a `px`
  breakpoint cannot do.

```css
/* Mobile-first: base styles are the smallest layout; min-width queries ADD structure. */

/* ~40em ≈ 640px at default 16px root */
@media (min-width: 40em) {
  /* design change: e.g. intro gains a 2-col split, nav links show inline */
}

/* ~64em ≈ 1024px */
@media (min-width: 64em) {
  /* design change: e.g. a margin/aside column appears; hero pins left with air right */
}

/* optional cap for ultrawide: stop the measure growing, add gutters — not more columns of text */
@media (min-width: 100em) {
  .page { max-inline-size: 90rem; margin-inline: auto; }
}
```

A pragmatic *starting* scale (then move each one to where YOUR content actually breaks):

| Token | `em` | ≈ px | Typical design change |
|---|---|---|---|
| `sm` | 30em | 480 | large phone → small tablet; 1 → 2 cols for some fields |
| `md` | 48em | 768 | tablet; nav inline; intro splits |
| `lg` | 64em | 1024 | desktop; sidebar/aside appears |
| `xl` | 80em | 1280 | wide desktop; richer asymmetry, larger hero |

These are *defaults to override*, never targets to copy.

---

## 4. Mobile-first, `min-width`, progressive enhancement

- Author the **smallest** layout as the base; use `min-width` queries to *add* as space appears.
  This forces the scarcest-space decision (what is the focal point on a phone?) up front, where it
  is honest — instead of designing at 1440 and subtracting.
- This is progressive enhancement (Keith, *Resilient Web Design*): a robust core that works
  everywhere, enriched where the viewport allows — not graceful degradation of a desktop comp.
- **The mobile view still needs a focal point and at least one intentional asymmetry** (per
  `layout-grid-and-spacing`). A flat single-column stack of identical cards is the failure this
  whole skill exists to prevent.

`max-width` (desktop-first) queries are admissible only for a deliberate *ceiling* (e.g. capping an
ultrawide measure) — not as the primary cascade.

---

## 5. Fluid type & space across the breakpoints

Between breakpoints, size should **bend, not snap**. Use `clamp()` so type and spacing interpolate
smoothly; the floor and ceiling must be **real steps from
`doctrine/references/type-scale-and-spacing.md`** — `clamp()` interpolates between the scale, it does
not invent sizes.

```css
h1 { font-size: clamp(2rem, 1.2rem + 4vw, 3.5rem); }   /* floor 2rem, ceiling 3.5rem = scale steps */
```

Always a `rem` floor **and** ceiling, never pure `vw` (illegible small, huge wide, and it breaks
browser zoom — a WCAG 1.4.4 failure; see `doctrine/references/wcag-2.2-criteria.md`). With fluid
type doing the interpolation, you often need *fewer* breakpoints — the page already adapts smoothly.

---

## 6. Test surfaces

Verify at: a small phone (~320–360px), a large phone, a tablet portrait, a laptop, a wide desktop,
and an **ultrawide** (≥1920px — confirm the measure is capped, not endlessly stretched). Also test
at **200% browser zoom** (WCAG 1.4.4 reflow): content must remain usable with no horizontal scroll
at 320px-equivalent — the proof that `em` breakpoints and `clamp()` floors were done right.

---

## Provenance

Marcotte (*Responsive Web Design* — media queries as one adaptive layout, not per-device comps),
Keith (*Resilient Web Design* — progressive enhancement, mobile-first), Bell & Pickering (*Every
Layout* — prefer intrinsic to breakpoints), grounded in the CSS specs. Per
`doctrine/design-doctrine.md` §2, AI-tool breakpoint lists are evidence of the convergent mean to
*avoid*, not authority for what to choose.
