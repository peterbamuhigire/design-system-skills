# Reference: OKLCH Ramp Construction (operationalized)

How to actually build a tonal ramp in OKLCH instead of lightening toward white in HSL. OKLCH
(`oklch(L C H)`) is a perceptually-uniform space: equal moves in **L** look like equal moves in
lightness to the eye, which HSL does not give you. CSS Color 4 ships `oklch()` natively in all
evergreen browsers — author tokens directly in it.

## The three channels

- **L — lightness, `0`–`1` (or `0%`–`100%`).** This is the channel you step the ramp on. `1` is
  reference white, `0` is black. Body surfaces live high (~0.97), body text lives low (~0.25).
- **C — chroma, `0`–~`0.37`.** Saturation/colourfulness. Unbounded in theory; real sRGB-displayable
  chroma is small and **depends on L and H** — a hue can hold more chroma at mid L than near the
  ends. Pushing C past the sRGB gamut silently clips; keep an eye on it (see gamut note).
- **H — hue angle, `0`–`360`.** Same convention as a hue wheel (~`30`≈orange, ~`145`≈green,
  ~`260`≈blue). Hold it roughly constant down the ramp; rotate it **deliberately** (see below).

## The construction recipe (the 50→900 ramp)

1. **Fix the anchor.** Convert your real-anchor hex to OKLCH; read off its `H` and its `L`/`C`.
   The anchor usually lands as the ramp's **500** step (the accent).
2. **Choose the L stops, evenly in L — not evenly in hex.** A 10-step ramp on roughly:

   | Step | 50 | 100 | 200 | 300 | 400 | 500 | 600 | 700 | 800 | 900 |
   |---|---|---|---|---|---|---|---|---|---|---|
   | **L** | 0.97 | 0.93 | 0.86 | 0.78 | 0.70 | 0.62 | 0.53 | 0.44 | 0.34 | 0.24 |

   The spacing is intentionally *not* perfectly linear — perceptual ramps compress slightly at the
   dark end so 800→900 still reads as a distinct step. Tune the exact L values per anchor.
3. **Shape chroma as an arc, not a constant.** Chroma should **peak in the mid-tones** (≈300–600)
   and **fall off at both ends**: the lightest tints (50/100) carry very low C so they don't go
   chalky/neon, and the darkest shades (800/900) carry reduced C so they don't go muddy/black-mush.
   A typical arc: `0.02, 0.04, 0.08, 0.12, 0.15, 0.16, 0.15, 0.12, 0.09, 0.06`. The peak C is
   gamut-limited — clamp it to what sRGB can show at that L/H.
4. **Rotate hue only with intent.** Holding H constant is the safe default. Small, deliberate
   rotations buy realism: warm the light tints a few degrees and cool the dark shades a few degrees
   (or vice-versa) to mimic how real pigments and light behave. Keep total rotation small (≤ ~15°)
   or the ramp stops reading as one colour.
5. **Re-check every step in-gamut.** If a step needs more chroma than sRGB can render at that L/H,
   the browser gamut-maps it (often desaturating) — so cap C deliberately rather than letting it
   clip. Use `@supports (color: oklch(0 0 0))` only if you must ship an sRGB-hex fallback.

## Neutrals are a ramp too

Build greys as a **low-chroma ramp on the anchor hue** (C ≈ `0.005`–`0.02`), never pure
`oklch(L 0 0)`. A trace of the brand hue in every neutral is what makes the system feel authored
rather than defaulted — and it satisfies the doctrine rule against `#000`/`#fff` (a near-black is
`oklch(0.20 0.02 H)`, a near-white surface is `oklch(0.98 0.01 H)`).

## Why this over HSL

HSL's `lightness` is not perceptual: `hsl(60 100% 50%)` (yellow) and `hsl(240 100% 50%)` (blue)
are both "50% light" yet the yellow is blindingly brighter. A ramp stepped on HSL lightness
therefore has uneven perceived jumps and muddy mid-tones. OKLCH fixes this by construction, which
is why the SKILL's step 3 mandates a perceptually-uniform space.

## Cross-refs
- `references/semantic-color-roles.md` — mapping these ramp positions to roles.
- `examples/oklch-palette-worked.md` — a full applied ramp, light + dark, with contrast checks.
- `doctrine/references/wcag-2.2-criteria.md` — design with APCA, certify with the WCAG ratios.
