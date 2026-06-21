# Reference: Container Queries & Intrinsic Layout — real CSS patterns

Most "responsiveness" should require **no breakpoint at all**: CSS Grid and Flexbox can respond to
content and available space on their own, and components can adapt to *their container* rather than
the global viewport. This file is the pattern library the `responsive-and-adaptive-layout` skill
draws on. Standards basis: CSS Grid, CSS Containment / Container Queries, CSS `min()`/`max()`/`clamp()`,
logical properties. Cite alongside `doctrine/references/web-performance-budgets-2026.md` (CLS) and
`03-layout-grid-and-composition/layout-grid-and-spacing` (the grid these patterns make responsive).

---

## 1. Intrinsic reflow with zero media queries

The single most useful responsive pattern. A card field that flows from 1 → N columns by available
space, never producing a column too narrow to read:

```css
.grid {
  display: grid;
  /* min(100%, 16rem) stops a single card overflowing on very small screens;
     auto-fit + 1fr lets columns grow to fill the row. No media query needed. */
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 16rem), 1fr));
  gap: clamp(1rem, 2vw, 2rem);
}
```

- `auto-fit` collapses empty tracks so remaining items stretch to fill (use `auto-fill` instead to
  preserve empty tracks — e.g. when you want items to keep a fixed max width and not stretch).
- The `min(100%, 16rem)` floor is what prevents the classic overflow bug where `minmax(16rem, 1fr)`
  blows out a 320px viewport.

**The "RAM" idiom** (Repeat, Auto-fit/fill, Minmax) is the intrinsic default — reach for an explicit
breakpoint only when the *design itself* must change, not merely because the screen got wider.

### Sidebar that collapses by content, not by breakpoint

```css
.with-sidebar {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}
.with-sidebar > .sidebar {
  flex-basis: 16rem;
  flex-grow: 1;             /* takes its basis, grows to share leftover */
}
.with-sidebar > .main {
  flex-basis: 0;
  flex-grow: 999;           /* greedily takes the rest until it can't, then wraps */
  min-inline-size: 60%;     /* below this the sidebar drops underneath — no media query */
}
```

This is the *Every Layout* "Sidebar": the wrap happens because the main column hits its
`min-inline-size`, i.e. driven by content width, not a guessed device pixel.

---

## 2. Container queries — components adapt to their CONTAINER

A viewport media query cannot answer "how wide is the box *this component* is sitting in." The same
card is wide in a hero and narrow in a 4-up grid at the **same** viewport width. Container queries
fix this: the component defines the width at which *it* re-lays-out, independent of page context.

### Step 1 — establish a containment context on the wrapper

```css
.card-wrap {
  container-type: inline-size;   /* query this element's inline (width) size */
  container-name: card;          /* optional name; lets you target a specific ancestor */
}
```

`container-type: inline-size` means descendants can query the wrapper's width. (Use `size` only when
you also query height and can guarantee the box has an intrinsic block size — it requires both-axis
containment and can collapse height, so `inline-size` is the safe default.)

### Step 2 — switch the component's internal layout by container width

```css
.card {
  display: grid;
  gap: 1rem;
  grid-template-columns: 1fr;     /* stacked: media over text (narrow container) */
}

@container card (min-width: 28rem) {
  .card {
    grid-template-columns: 12rem 1fr;   /* wide container → media beside text */
    align-items: center;
  }
}

@container card (min-width: 44rem) {
  .card {
    grid-template-columns: 16rem 1fr;   /* even wider → larger media, roomier text */
  }
}
```

Drop the **same** `.card` markup into a 1-up hero, a 2-up split, or a 4-up grid: each instance reads
*its own* container and chooses the right internal layout. One component, correct everywhere — no
per-placement overrides, no viewport guessing.

### Container query units

Inside a container context you can size against the container itself: `cqi` (1% of container inline
size), `cqb` (block), `cqmin`/`cqmax`. Useful for padding/type that should track the component's own
width rather than the viewport:

```css
.card h3 { font-size: clamp(1.125rem, 4cqi, 1.5rem); }  /* scales to the card, not the window */
```

### When to use which

| Use a **container query** when… | Use a **viewport (media) query** when… |
|---|---|
| The component appears in more than one column width | The decision is page-global (nav bar ↔ drawer) |
| You're building a reusable/library component | The whole template re-arranges (sidebar appears) |
| The same element must look right in hero *and* grid | You're responding to the device/window itself |

---

## 3. Fluid sizing with `clamp()`, `min()`, `max()`

`clamp(MIN, PREFERRED, MAX)` returns PREFERRED, bounded by MIN and MAX. The PREFERRED term mixes a
relative unit (so it scales) with the floor/ceiling holding it readable.

```css
:root {
  /* Fluid space tokens — bend between sizes instead of stepping at breakpoints */
  --space-s: clamp(0.75rem, 0.5rem + 1vw, 1.25rem);
  --space-m: clamp(1rem,   0.6rem + 2vw, 2rem);
  --space-l: clamp(2rem,   1rem  + 4vw, 4rem);
}
.section { padding-block: var(--space-l); }
.stack > * + * { margin-block-start: var(--space-m); }
```

Fluid type — floor and ceiling are **real steps from `type-scale-and-spacing.md`**; `clamp()` only
interpolates *between* the scale, it does not invent new sizes:

```css
h1 { font-size: clamp(2rem, 1.2rem + 4vw, 3.5rem); line-height: 1.1; }
h2 { font-size: clamp(1.5rem, 1.1rem + 2vw, 2.25rem); }
p  { font-size: clamp(1rem, 0.95rem + 0.3vw, 1.125rem); }
```

Rules:
- **Always set a `rem` floor AND ceiling.** A pure-`vw` size (`font-size: 5vw`) is illegible on
  phones, huge on ultrawide, and **breaks browser zoom** — a WCAG 1.4.4 reflow/zoom failure. The
  `rem` terms keep zoom working.
- Keep the slope gentle; a steep `vw` coefficient makes text lurch as the window resizes.

---

## 4. Constrain measure & use logical properties

Cap line length and centre content with no media query, authored in logical (writing-mode-safe)
properties so it survives RTL and vertical modes (pairs with `internationalization-and-rtl-design`):

```css
.prose {
  inline-size: min(100% - 2rem, 66ch);  /* never wider than ~66ch, gutter on small screens */
  margin-inline: auto;                  /* centre the measure */
}
.box { padding-inline: var(--space-m); padding-block: var(--space-l); }
```

Prefer `inline-size`/`block-size`, `margin-inline`/`margin-block`, `inset-inline`, `border-inline`
over physical `width`/`left`/`right` throughout.

---

## 5. Preventing layout shift on fluid media (CLS ≤ 0.1)

Per `doctrine/references/web-performance-budgets-2026.md`, reserve the box before the asset loads:

```css
img, video { max-inline-size: 100%; height: auto; }   /* fluid but not overflowing */
.media { aspect-ratio: 16 / 9; }                       /* reserves height → no jump */
```

```html
<img src="hero.avif" width="1600" height="900"        <!-- intrinsic ratio reserves space -->
     sizes="(min-width: 60rem) 50vw, 100vw"
     srcset="hero-800.avif 800w, hero-1600.avif 1600w"
     loading="lazy" decoding="async" alt="…">
```

Serve AVIF → WebP → fallback; lazy-load below the fold; never resize an on-screen block in a way
that reflows content already painted.

---

## 6. Honour the person and the device

Adaptivity is about context, not only pixel width:

```css
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
@media (prefers-color-scheme: dark)     { :root { color-scheme: dark; } }
@media (pointer: coarse) {                       /* touch → larger hit targets */
  .btn { min-block-size: 44px; min-inline-size: 44px; }  /* ≥24px is the WCAG 2.5.8 floor; aim ≥44 */
}
```

See `doctrine/references/wcag-2.2-criteria.md` for the 2.5.8 target-size rule and 1.4.4 zoom rule.

---

## Provenance

Patterns follow Marcotte (*Responsive Web Design*), Keith (*Resilient Web Design* / progressive
enhancement), and Bell & Pickering (*Every Layout*, intrinsic algorithmic layouts), grounded in the
CSS specifications. Per `doctrine/design-doctrine.md` §2, AI-tool recommendations are not authority
here; the specs and the named design literature are.
