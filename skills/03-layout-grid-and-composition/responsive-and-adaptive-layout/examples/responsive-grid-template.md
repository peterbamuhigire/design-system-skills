# Worked example: A real responsive card grid (intrinsic + container queries + clamp)

A complete, copy-real responsive section for a product/feature listing. It demonstrates the three
core moves of `responsive-and-adaptive-layout` together: **intrinsic reflow** (no media query),
**container queries** (the card adapts to its own placement), and **fluid type/space via `clamp()`**.
It carries the authored composition — a named focal point and intentional asymmetry — into the
*smallest* size, not just desktop. Built on
`03-layout-grid-and-composition/layout-grid-and-spacing` and within the budgets of
`doctrine/references/web-performance-budgets-2026.md`.

---

## Stated decision (declared BEFORE markup, per the skill's Outputs)

- **Surfaces:** ~320px phone → ultrawide; measure capped so text never stretches past ~66ch.
- **Breakpoints:** essentially none at page level — the grid reflows intrinsically. One container
  query on the *card* (the only portable component, reused in a hero and in the grid). The content
  breaks (card text too cramped) at ~28rem and ~44rem of **card** width — so those are the card's
  breakpoints, regardless of viewport.
- **Focal point:** the first card is **featured** — it spans two columns and uses the wide internal
  layout, so the eye has a clear entry on every screen, including the phone (where it leads the stack).
- **Asymmetry:** the featured card's 2-col span + the offset of the section heading from the grid
  edge create deliberate tension — not a flat, even N-up field.
- **Fluid type/space:** `clamp()` floors/ceilings taken from `type-scale-and-spacing.md`; `rem`
  floor **and** ceiling so zoom works.

---

## HTML

```html
<section class="features">
  <header class="features__intro">
    <p class="eyebrow">Platform</p>
    <h2>Everything your team ships, in one adaptive surface</h2>
  </header>

  <ul class="features__grid" role="list">
    <!-- Featured = the focal point: spans 2 cols, gets the wide card layout -->
    <li class="card-wrap card-wrap--featured">
      <article class="card">
        <div class="card__media"><img src="a.avif" width="800" height="600"
             sizes="(min-width:64em) 33vw, 100vw"
             srcset="a-400.avif 400w, a-800.avif 800w" loading="lazy" decoding="async" alt=""></div>
        <div class="card__body">
          <h3>Real-time collaboration</h3>
          <p>Edit together with no merge conflicts and presence built in.</p>
          <a class="card__cta" href="#">Explore</a>
        </div>
      </article>
    </li>

    <li class="card-wrap"><article class="card"> … </article></li>
    <li class="card-wrap"><article class="card"> … </article></li>
    <li class="card-wrap"><article class="card"> … </article></li>
    <li class="card-wrap"><article class="card"> … </article></li>
  </ul>
</section>
```

The featured card and the grid cards share **identical** `.card` markup. The only difference is the
wrapper's width — and the card adapts to that via a **container query**, so it is correct in both
places with no special-case CSS.

---

## CSS

```css
:root {
  /* Fluid space + type tokens — floors/ceilings are real steps from type-scale-and-spacing.md */
  --space-s:  clamp(0.75rem, 0.5rem + 1vw, 1.25rem);
  --space-m:  clamp(1rem,   0.6rem + 2vw, 2rem);
  --space-l:  clamp(2.5rem, 1.5rem + 4vw, 5rem);
  --step-h2:  clamp(1.75rem, 1.2rem + 2.5vw, 2.75rem);
  --step-h3:  clamp(1.125rem, 1rem + 0.6vw, 1.375rem);
  --measure:  66ch;
}

.features {
  padding-block: var(--space-l);
  padding-inline: var(--space-m);
  max-inline-size: 90rem;        /* ultrawide cap: stop stretching, don't add text columns */
  margin-inline: auto;
}

/* Asymmetry: heading offset from the grid's left edge, not centred over it */
.features__intro {
  inline-size: min(100%, 40ch);
  margin-block-end: var(--space-l);
  margin-inline-start: 0;        /* deliberately flush-left, creating tension vs the grid */
}
.features__intro h2 { font-size: var(--step-h2); line-height: 1.1; }
.eyebrow { text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.8125rem; }

/* (1) INTRINSIC REFLOW — 1 → N columns, zero media queries, never a too-narrow column */
.features__grid {
  list-style: none;
  margin: 0;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr));
  gap: var(--space-m);
  align-items: start;
}

/* Focal point: featured spans 2 tracks when ≥2 tracks exist; harmless at 1-up (it just fills the row) */
.card-wrap--featured { grid-column: span 2; }

/* (2) CONTAINER QUERY — each card adapts to ITS OWN width, in hero OR grid */
.card-wrap { container-type: inline-size; container-name: card; }

.card {
  display: grid;
  gap: var(--space-s);
  grid-template-columns: 1fr;          /* narrow container: media stacked over text */
  background: Canvas;
  border: 1px solid color-mix(in oklch, CanvasText 12%, transparent);
  border-radius: 0.75rem;
  overflow: clip;
}
.card__media { aspect-ratio: 4 / 3; }  /* reserve space → CLS ≤ 0.1 */
.card__media img { inline-size: 100%; block-size: 100%; object-fit: cover; }
.card__body { padding: var(--space-m); }
.card__body h3 { font-size: var(--step-h3); line-height: 1.15; }
.card__body p  { max-inline-size: var(--measure); }

/* card content gets cramped past ~28rem of CARD width → side-by-side */
@container card (min-width: 28rem) {
  .card { grid-template-columns: 14rem 1fr; align-items: center; }
  .card__media { aspect-ratio: 1 / 1; }
}
/* the featured card sits in a wide track → larger media, roomier text */
@container card (min-width: 44rem) {
  .card { grid-template-columns: 20rem 1fr; }
  .card__body h3 { font-size: clamp(1.375rem, 4cqi, 1.75rem); }  /* type tracks the CARD, not viewport */
}

/* (3) Honour the person/device */
@media (prefers-reduced-motion: reduce) { .card { transition: none; } }
@media (pointer: coarse) { .card__cta { min-block-size: 44px; display: inline-flex; align-items: center; } }
```

---

## What each screen actually does

- **~320–600px (1 column):** the featured card leads the stack and, because its wrapper is now wide
  (full viewport), its **container query** fires at 28rem → it shows media-beside-text while the
  others below it stay stacked. The phone keeps a clear **focal point** — not a flat identical stack.
- **~600–1000px (2–3 columns, intrinsic):** `auto-fit` adds columns as space allows; the featured
  card spans two of them. Its wrapper crosses 44rem only when the track is wide → it adopts the
  largest internal layout. No media query was written for any of this.
- **Ultrawide:** `max-inline-size: 90rem` caps the section so the measure never stretches past
  comfortable reading; the grid gains columns, the text columns do not get wider.
- **200% zoom:** because type uses `clamp()` with `rem` floors and the breakpoints are container/`em`
  based, content reflows cleanly with no horizontal scroll — WCAG 1.4.4 holds.

---

## Checked against the Responsive Anti-Slop Checklist

1. ✅ Mobile-first; smallest size **re-composed** with a leading featured card, not a uniform stack.
2. ✅ Reflow is intrinsic (`auto-fit`/`minmax`/`clamp`); zero page-level media queries for the grid.
3. ✅ The portable `.card` uses **container queries**, adapting to placement (hero vs grid), not viewport.
4. ✅ The only breakpoints are content-driven (card text cramped at 28rem/44rem of *card* width).
5. ✅ Fluid type via `clamp()` with `rem` floor **and** ceiling; zoom works (no pure-`vw`).
6. ✅ `aspect-ratio` + intrinsic `width`/`height` on media reserve space → CLS ≤ 0.1.
7. ✅ Logical properties throughout (`inline-size`, `margin-inline`, `padding-block`); measure capped ~66ch.
8. ✅ A named focal point (featured card) and intentional asymmetry (offset heading + 2-col span)
   survive at the **smallest** size.
9. ✅ `prefers-reduced-motion` and coarse-pointer target size honoured.

---

## References

- `03-layout-grid-and-composition/responsive-and-adaptive-layout/SKILL.md` (the workflow this applies).
- `references/container-queries-and-intrinsic.md`, `references/breakpoint-strategy.md`.
- `doctrine/references/type-scale-and-spacing.md` (the steps the `clamp()` floors/ceilings come from).
- `doctrine/references/web-performance-budgets-2026.md` (CLS ≤ 0.1, responsive image budgets).
- `doctrine/references/wcag-2.2-criteria.md` (1.4.4 zoom/reflow; 2.5.8 target size).
- `03-layout-grid-and-composition/layout-grid-and-spacing` (focal point + asymmetry carried here).
