# Reference: Fluid-Scale Math (`clamp()` derivation + a generated scale)

How to turn a modular type step into a fluid `clamp()` whose `vw` coefficient is **derived**, not
guessed — so the type hits exactly its intended size at the smallest and largest widths and bends
linearly between. Builds on `doctrine/references/type-scale-and-spacing.md` (the modular ratio and
inverse line-height the fluid step interpolates between — `clamp()` does not invent sizes). Cited by
the skill's step 1.

All `rem` assume the browser root of **16px** (`1rem = 16px`). **Never override `html { font-size }`
in px** — it breaks user zoom and the whole rem chain.

---

## 1. The shape of a fluid step

A fluid font-size is:

```css
font-size: clamp(MIN, PREFERRED, MAX);
```

- **MIN** — the size at the *smallest* target width (a `rem`, so zoom works).
- **MAX** — the size at the *largest* target width (a `rem`).
- **PREFERRED** — a linear `rem + vw` line that equals MIN at the floor width and MAX at the
  ceiling width. `clamp()` then holds MIN below the floor and MAX above the ceiling.

The whole game is computing **PREFERRED** correctly. A `clamp()` whose middle term is eyeballed is
the slop tell this file exists to kill.

---

## 2. The derivation (the only formula you need)

Let the floor viewport width be `floorRem = floorPx / 16` and the ceiling `ceilingRem = ceilingPx / 16`.
For a step with `MIN` and `MAX` (in rem):

```
slope (vw coefficient) = (MAX − MIN) / (ceilingRem − floorRem) × 100
intercept (rem)        = MIN − (slope / 100) × floorRem
PREFERRED              = {intercept}rem + {slope}vw
font-size              = clamp({MIN}rem, {intercept}rem + {slope}vw, {MAX}rem)
```

**Why ×100 on the slope:** `1vw = 1%` of the viewport width, i.e. `viewportPx/100`. Dividing the rem
rise by the rem run gives change-per-rem-of-viewport; ×100 converts that to change-per-`vw`.

**Why the intercept:** the line is `size = intercept + slope/100 × viewportRem`. Solving it to pass
through `(floorRem, MIN)` gives `intercept = MIN − slope/100 × floorRem`.

---

## 3. Sanity checks (do these every time)

1. **Endpoint check — the real test.** Plug both widths back in. At width `W` px,
   `vw_in_rem = slope/100 × (W/16)`, and `size = intercept + vw_in_rem`. It must equal MIN at the
   floor and MAX at the ceiling (±0.01rem rounding). If not, the slope or intercept is wrong.
2. **Intercept-sign check.** For type that *grows* with width (the normal case) the intercept is
   usually **positive** and smaller than MIN. A large **negative** intercept means the floor width is
   very small relative to the rise — legal, but re-check you didn't swap MIN/MAX.
3. **Floor < ceiling, MIN < MAX.** If MIN ≥ MAX the step shouldn't be fluid at all.
4. **`rem` on BOTH bounds.** A bare `vw`/`cqi` bound (`clamp(MIN, …, 6vw)`) defeats 200% zoom and
   reflow — **WCAG 1.4.4 / 1.4.10** failure (`doctrine/references/wcag-2.2-criteria.md`).

---

## 4. Worked single step (h1, 40 → 67px, 320 → 1440px)

```
floorRem   = 320 / 16  = 20      ceilingRem = 1440 / 16 = 90
MIN        = 40 / 16   = 2.5rem  MAX        = 67 / 16   ≈ 4.1875rem
slope      = (4.1875 − 2.5) / (90 − 20) × 100 = 1.6875 / 70 × 100 ≈ 2.411vw
intercept  = 2.5 − (2.411 / 100) × 20         = 2.5 − 0.482          ≈ 2.018rem
→ font-size: clamp(2.5rem, 2.018rem + 2.411vw, 4.1875rem);
```

Endpoint check: at 320px → 2.018 + 0.02411×20 = 2.018 + 0.482 = **2.5rem (40px)** ✓.
At 1440px → 2.018 + 0.02411×90 = 2.018 + 2.170 = **4.188rem (67px)** ✓.

---

## 5. Generated scale — Perfect Fourth (1.333), base 16px, 320 → 1440px

Body and captions stay **fixed** (fluid body harms reading rhythm). Display/h1/h2/h3 are fluid.
Derivation per §2; every row endpoint-checked per §3.

| Token | px floor → ceiling | MIN (rem) | MAX (rem) | slope (vw) | intercept (rem) |
|---|---|---|---|---|---|
| `--fs-display` | 48 → 89 | 3.0    | 5.5625 | 3.661 | 2.268 |
| `--fs-h1`      | 40 → 67 | 2.5    | 4.1875 | 2.411 | 2.018 |
| `--fs-h2`      | 32 → 50 | 2.0    | 3.125  | 1.607 | 1.679 |
| `--fs-h3`      | 28 → 38 | 1.75   | 2.375  | 0.893 | 1.571 |

```css
:root {
  /* fixed — never fluid */
  --fs-caption: 0.75rem;                                       /* 12px */
  --fs-body:    1rem;                                          /* 16px */
  /* fluid — derived, both bounds rem */
  --fs-h3:      clamp(1.75rem,   1.571rem + 0.893vw, 2.375rem);  /* 28 → 38px */
  --fs-h2:      clamp(2rem,      1.679rem + 1.607vw, 3.125rem);  /* 32 → 50px */
  --fs-h1:      clamp(2.5rem,    2.018rem + 2.411vw, 4.1875rem); /* 40 → 67px */
  --fs-display: clamp(3rem,      2.268rem + 3.661vw, 5.5625rem); /* 48 → 89px */
}
```

Hero ÷ body at the ceiling: 89 ÷ 16 ≈ **5.6×** — the modular jump survives fluid sizing (§7 of the
skill). Generators (utopia.fyi) emit identical math; still verify the px endpoints by hand.

---

## 6. Fluid line-height (size-inverse)

Leading tightens as type grows (`type-scale-and-spacing.md`: small ≈ ×1.6, large ×1.3 → ×1.05).
Two valid approaches:

- **Unitless (default).** A unitless `line-height` multiplies the *computed* size, so it tracks the
  fluid font-size automatically: `body { line-height: 1.6 } .hero h1 { line-height: 1.05 }`.
- **Clamped leading (wide-range elements only).** When one element sweeps a large size range, clamp
  the leading in `rem` so the ratio itself shifts: `line-height: clamp(2.6rem, …, 4rem)`. Reserve
  this for the hero/display; unitless covers everything else.

Never carry ×1.6 body leading onto a 64px hero — that loose, airy hero is a slop tell.

---

## 7. Container-query units (`cqi`) — size to the container, not the viewport

For type inside a **portable** component (a card heading shown both full-width and 4-up), swap `vw`
for **`cqi`** (1cqi = 1% of the nearest query container's inline-size). Same `clamp()` math, but the
percentage tracks the *container* width:

```css
.card { container-type: inline-size; }          /* the wrapper becomes the query container */
.card h3 {
  font-size: clamp(1.25rem, 0.95rem + 3cqi, 2rem);
  line-height: 1.2;
}
```

Now the heading is large when the card is wide (hero) and modest when narrow (sidebar) **at the same
viewport width** — which `vw` cannot do. Derive the `cqi` coefficient the same way as `vw`, but using
the container's min/max inline-size as the floor/ceiling instead of the viewport. Pairs with
`03-layout-grid-and-composition/responsive-and-adaptive-layout` (container queries).

The §3 rule still holds: keep a `rem` floor and ceiling — a bare `cqi` bound breaks zoom just as `vw`
does.

---

## References

- `doctrine/references/type-scale-and-spacing.md` — the ratio, inverse line-height, and measure these
  fluid steps interpolate between.
- `doctrine/references/wcag-2.2-criteria.md` — 1.4.4 resize-text / 1.4.10 reflow (the rem-bound rule).
- `skills/01-typography-and-fonts/font-selection-and-pairing/references/type-scale-recipes.md` — the
  base px/rem modular scales (Recipes A/B/C) these fluid steps are built from.
- `skills/01-typography-and-fonts/fluid-responsive-typography/examples/fluid-type-scale.md`.
