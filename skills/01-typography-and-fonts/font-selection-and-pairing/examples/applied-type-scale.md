# Worked example: A real type scale for a named brief

A complete, copy-real application of `font-selection-and-pairing` end to end: a stated pairing
with a reason, a concrete px/rem type scale, the fluid `clamp()` version, variable-font axis
settings, and the anti-slop checklist run. Built on
`references/pairing-catalog.md` (S1) and `references/type-scale-recipes.md` (Recipe B + fluid).

---

## The brief

> **Maduuka — SaaS landing page.** Maduuka is a retail point-of-sale product for East-African
> small merchants. The marketing site must read as a confident, contemporary product — *not* a
> templated startup page — and survive from a 360px budget phone to a 1240px+ desktop. Output:
> web (HTML/CSS). Audience: startup/product. No client brand guideline mandates fonts.

Classify → **03 Modern Product / Grotesque** (`font-groups-and-usage.md`).

---

## Stated decision (declared BEFORE any markup, per the skill's step 4)

- **Display / headings: Bricolage Grotesque (800).** A distinctive, slightly contrasty grotesque
  that a templating tool would never reach for — it gives Maduuka an authored, branded headline
  voice. OFL, so fully embeddable. (Deliberately **not** Space Grotesk, the named AI convergence
  trap, nor Poppins/Montserrat.)
- **Body: Hanken Grotesk (400).** A calm, legible geometric grotesque that recedes under the
  display face and holds long marketing copy. OFL.
- **Reason (one line):** *"An expressive OFL grotesque headline (Bricolage 800) over a quiet
  geometric body (Hanken 400) gives Maduuka a confident, non-slop product voice with real weight
  contrast — and both faces ship without a licence problem."*

This is pairing **S1** from `references/pairing-catalog.md`: cross-mood-matched grotesques, weight
extremes 800/400, both OFL.

---

## The type scale — Recipe B (Perfect Fourth, 1.333, base 16px)

A SaaS landing wants a dramatic hero, so the Perfect Fourth's ~5.6× hero-to-body jump is correct.

| Token | Role | px | rem | line-height | weight | face |
|---|---|---|---|---|---|---|
| `--fs-caption` | eyebrow / fine print | 12 | 0.750 | 1.5 | 500 | Hanken |
| `--fs-body`    | paragraph copy | 16 | 1.000 | 1.6 (≈26px) | 400 | Hanken |
| `--fs-h5`      | small labels | 21 | 1.333 | 1.4 | 600 | Hanken |
| `--fs-h4`      | sub-section | 28 | 1.777 | 1.3 | 700 | Bricolage |
| `--fs-h3`      | feature title | 38 | 2.369 | 1.2 | 800 | Bricolage |
| `--fs-h2`      | section head | 50 | 3.157 | 1.1 | 800 | Bricolage |
| `--fs-h1`      | page head | 67 | 4.209 | 1.05 | 800 | Bricolage |
| `--fs-display` | hero headline | 89 | 5.610 | 1.0 | 800 | Bricolage |

- **Real jump:** hero 89px ÷ body 16px ≈ **5.6×** — obvious hierarchy, no timid near-equal steps.
- **Weight extremes:** Bricolage **800** display vs Hanken **400** body — contrast carried by weight
  + size together, per `type-scale-and-spacing.md`.
- **≤3 sizes per section:** the hero uses display + body + one caption; feature cards use h3 + body.
- **Tracking:** −0.01em on `--fs-h1`/`--fs-display`; 0 on body; +0.08em uppercase on `--fs-caption`.

---

## Fluid `clamp()` version (ship this — no breakpoints)

Floors = the size at 360px (22.5rem); ceilings = the px above (77.5rem). Body stays fixed.

```css
:root {
  --fs-caption: 0.75rem;                                    /* fixed 12px */
  --fs-body:    1rem;                                       /* fixed 16px — never fluid body */
  --fs-h3:      clamp(1.75rem, 1.477rem + 1.21vw, 2.369rem);/* 28 → 38px */
  --fs-h2:      clamp(2rem,    1.341rem + 2.93vw, 3.157rem);/* 32 → 50px */
  --fs-h1:      clamp(2.5rem,  1.466rem + 4.6vw,  4.209rem);/* 40 → 67px */
  --fs-display: clamp(3rem,    1.6rem  + 6.2vw,  5.61rem);  /* 48 → 89px */
}
```

At 360px the hero is 48px (fits the budget phone); at 1240px+ it reaches the full 89px. Both bounds
are `rem`, so 200% zoom reflows cleanly (WCAG 1.4.4 holds).

---

## Variable-font axes (one file each, the whole weight range)

Both faces are variable — register the range once, drive contrast from CSS instead of shipping five
static weights.

```css
@font-face {
  font-family: "Bricolage Grotesque";
  src: url("/fonts/bricolage.woff2") format("woff2-variations");
  font-weight: 200 800; font-display: swap;
}
@font-face {
  font-family: "Hanken Grotesk";
  src: url("/fonts/hanken.woff2") format("woff2-variations");
  font-weight: 300 900; font-display: swap;
}
:root { font-optical-sizing: auto; }

.hero h1 { font-family:"Bricolage Grotesque"; font-size:var(--fs-display);
           font-variation-settings:"wght" 800; line-height:1.0; letter-spacing:-0.01em; }
body     { font-family:"Hanken Grotesk"; font-size:var(--fs-body);
           font-variation-settings:"wght" 400; line-height:1.6; }
.section-head { font-family:"Bricolage Grotesque"; font-size:var(--fs-h2);
                font-variation-settings:"wght" 800; line-height:1.1; }
.eyebrow { font-size:var(--fs-caption); text-transform:uppercase;
           letter-spacing:0.08em; font-variation-settings:"wght" 500; }
```

The 800-vs-400 weight contrast — the doctrine's "weight extremes" rule — comes from **two files**,
not ten, because the faces are variable.

---

## Fallback set (after the chosen face, never instead)

```css
--font-display: "Bricolage Grotesque", "Hanken Grotesk", Georgia, serif;
--font-body:    "Hanken Grotesk", system-ui, sans-serif;
```

The fallback follows the chosen face; we did **not** silently default to a bare system stack.
Handoff to `font-embedding-and-licensing` for subsetting + correct web-font load.

---

## The Anti-Slop Checklist (run, per the skill)

1. ✅ Faces named with a one-line contextual reason, stated **before** output.
2. ✅ Neither face banned — Bricolage Grotesque + Hanken Grotesk (checked vs `ai-slop-banned-fonts.md`,
   including the "escape" list; we deliberately avoided Space Grotesk/Poppins/Montserrat).
3. ✅ A real display+body **pairing** (Bricolage display / Hanken body), not one font for everything.
4. ✅ Both OFL — licence permits use **and** embedding.
5. → Loading/subsetting handed to `font-embedding-and-licensing` (woff2-variations, `font-display:swap`).
6. ✅ Sensible fallback set placed **after** the chosen faces.

Scale hygiene also passes: ratio 1.333 (≥1.25), 5.6× hero jump, weight extremes 800/400,
inverse line-height (1.6 body → 1.0 hero), ≤3 sizes per section.

---

## References

- `skills/01-typography-and-fonts/font-selection-and-pairing/SKILL.md` (the workflow this applies).
- `references/pairing-catalog.md` (pairing S1 used here).
- `references/type-scale-recipes.md` (Recipe B + the fluid `clamp()` and variable-axis method).
- `doctrine/references/type-scale-and-spacing.md` · `pairing-principles.md` · `ai-slop-banned-fonts.md`
  · `font-groups-and-usage.md`.
