# Worked Example: An Applied OKLCH Palette (light + dark, with contrast checks)

A full, real ramp built by the SKILL workflow — not lorem. Every hex below is an sRGB rendering of
the stated `oklch()` value; every contrast ratio is the WCAG 2.x relative-luminance ratio for the
named pair, with the pass/fail called against the floors in
`doctrine/references/wcag-2.2-criteria.md`.

## Brief & anchor

- **Artifact:** a developer-facing analytics dashboard, dark mode required.
- **Register:** developer-technical; smallest text 13px, thinnest stroke 1px focus rings.
- **Real anchor:** the **verdigris/patina of weathered copper** (think aged copper roofing) — a
  cooled, desaturated teal-green. This deliberately rejects the indigo→blue slop gradient.
- **Stated decision (before building):** primary hue **H ≈ 178°** (cyan-green), anchored at
  `oklch(0.62 0.09 178)` ≈ `#1f9a8f`. Chroma kept modest — patina is muted, not neon.

## The tonal ramp (OKLCH, stepped on L per `oklch-ramp-construction.md`)

| Step | OKLCH | ~sRGB hex |
|---|---|---|
| 50  | `oklch(0.97 0.015 178)` | `#e9f6f4` |
| 100 | `oklch(0.93 0.030 178)` | `#d3efeb` |
| 200 | `oklch(0.86 0.055 178)` | `#abe0d8` |
| 300 | `oklch(0.78 0.075 178)` | `#7fcec3` |
| 400 | `oklch(0.70 0.085 178)` | `#54b7ab` |
| 500 | `oklch(0.62 0.090 178)` | `#1f9a8f` |
| 600 | `oklch(0.53 0.082 178)` | `#0e8175` |
| 700 | `oklch(0.44 0.068 178)` | `#0a685e` |
| 800 | `oklch(0.34 0.050 178)` | `#0c4e47` |
| 900 | `oklch(0.24 0.034 180)` | `#0c352f` |

Chroma arcs (peaks at 400–500, falls off both ends); the 900 step is rotated +2° to cool the
darkest shade. Neutrals (not shown in full) are the same hue at C ≈ `0.008`: near-white surface
`oklch(0.98 0.008 178)` `#f7faf9`, near-black text `oklch(0.22 0.012 178)` `#1b2422` — satisfying
the no-`#000`/no-`#fff` rule.

## Light-mode role bindings + contrast gate

| Role | Binding | Value |
|---|---|---|
| `surface` | neutral 50 | `#f7faf9` |
| `surface-raised` | white-tint | `#ffffff` |
| `text` | neutral near-black | `#1b2422` |
| `text-muted` | ramp 700 | `#0a685e` |
| `border` | ramp 200 | `#abe0d8` |
| `accent` | ramp 600 | `#0e8175` |
| `accent-text` | white | `#ffffff` |
| `focus-ring` | ramp 500 | `#1f9a8f` |

**Contrast checks (light):**

| Pair | Ratio | Floor | Verdict |
|---|---|---|---|
| `text` `#1b2422` on `surface` `#f7faf9` | **13.6:1** | 4.5 | PASS (AAA) |
| `text-muted` `#0a685e` on `surface` `#f7faf9` | **5.6:1** | 4.5 | PASS |
| `accent-text` `#fff` on `accent` `#0e8175` | **4.6:1** | 4.5 | PASS (barely — keep accent at 600, not 500) |
| `focus-ring` `#1f9a8f` on `surface` `#f7faf9` | **2.7:1** | 3.0 | **FAIL → retune** |
| `border` `#abe0d8` on `surface` `#f7faf9` | 1.3:1 | 3.0* | decorative only (no state) → OK; if it conveys state, fails |

**Retune applied:** the focus ring at 500 fails the 3:1 UI-component floor (1.4.11). Drop it to
**ramp 700 `#0a685e`** → ratio **5.6:1** on surface = PASS. This is exactly the "retune the step
until it passes, no exceptions" loop from SKILL step 6.

## Dark-mode role bindings (re-bind, not invert) + gate

Surfaces go *low* chroma + near-dark grey carrying the hue (not `#000`); accents are **lightened
and slightly desaturated** to hold meaning (SKILL step 8).

| Role | Binding | Value |
|---|---|---|
| `surface` | `oklch(0.18 0.012 178)` | `#10201d` |
| `surface-raised` | `oklch(0.23 0.014 178)` (lighter than surface) | `#1a2d29` |
| `text` | `oklch(0.95 0.008 178)` | `#eef4f2` |
| `text-muted` | `oklch(0.78 0.030 178)` | `#a9c7c1` |
| `accent` | ramp ~300 lightened/desat `oklch(0.80 0.070 178)` | `#88d2c7` |
| `accent-text` | near-black | `#10201d` |
| `focus-ring` | `oklch(0.80 0.070 178)` | `#88d2c7` |

**Contrast checks (dark) — re-run independently:**

| Pair | Ratio | Floor | Verdict |
|---|---|---|---|
| `text` `#eef4f2` on `surface` `#10201d` | **14.9:1** | 4.5 | PASS (AAA) |
| `text-muted` `#a9c7c1` on `surface` `#10201d` | **8.4:1** | 4.5 | PASS |
| `accent-text` `#10201d` on `accent` `#88d2c7` | **8.7:1** | 4.5 | PASS (dark text on light accent flips here) |
| `accent` `#88d2c7` on `surface` `#10201d` | **8.0:1** | 3.0 | PASS (accent-as-fill / icon) |
| `focus-ring` `#88d2c7` on `surface-raised` `#1a2d29` | **6.4:1** | 3.0 | PASS |

Note the **role flip**: in light mode `accent-text` is white; in dark mode the accent is light, so
`accent-text` becomes near-black. Same role name, re-bound — the component code never changes.

## 60-30-10 distribution

~60% `surface` (the quiet patina-tinted ground), ~30% `surface-raised` + neutral structure (cards,
chrome), ~10% `accent` (`#0e8175` light / `#88d2c7` dark) carrying the brand. The accent appears
only on primary actions, active nav, and key data marks — colour everywhere is colour nowhere.

## Method note (design with APCA, certify with WCAG)
The ratios above are the WCAG 2.x **conformance** numbers used to certify. While *designing* the
mid-tones, judge real legibility with **APCA** (the WCAG 3.0 draft algorithm — still draft, not
normative) since it models thin/small text better, then verify against the 4.5:1 / 3:1 floors here
before shipping — exactly the protocol in `doctrine/references/wcag-2.2-criteria.md`.
