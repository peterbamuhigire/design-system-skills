# Reference: Colour-blind-safe palettes & the non-colour-cue rule

Colour-vision deficiency (CVD) affects ~**8% of men** and ~**0.5% of women** of Northern-European
descent — for a 1,000-visitor page, that's dozens of people who cannot reliably tell your red
status from your green one. This reference makes any *meaning-carrying* colour survive them.

## The three CVD types you must design for

| Type | What's affected | Confuses | Prevalence |
|---|---|---|---|
| **Deuteranopia / deuteranomaly** | Green cone (most common) | red ↔ green, green ↔ brown | ~6% of men |
| **Protanopia / protanomaly** | Red cone; reds also look darker | red ↔ green, red ↔ black | ~2% of men |
| **Tritanopia / tritanomaly** | Blue cone (rare) | blue ↔ green, yellow ↔ pink, teal ↔ grey | ~0.01% |

Total colour-blindness (monochromacy) is very rare but is the reason the **non-colour-cue rule**
below is absolute, not a nicety.

## Rule 1 — Never encode meaning by hue alone (WCAG 1.4.1 Use of Colour)

> Colour is never the *only* visual means of conveying information, indicating an action,
> prompting a response, or distinguishing an element.

Every meaning-carrying colour gets a **redundant non-colour cue**:

| Where colour is doing the work | Add this second cue |
|---|---|
| Status (success/warning/error/info) | An **icon** (✓ ⚠ ✕ ℹ) **and/or a text label** |
| Required form field | The word "(required)" or a `*` **with** a text legend — never the colour alone |
| Link inside body text | **Underline** (don't remove it), or weight + an indicator |
| Validation (valid/invalid) | Icon + message text, not just a green/red border |
| Line / bar / pie series | **Direct labels**, plus **dash style / marker shape / pattern** |
| "You are here" / active nav | Weight, an underline/marker, or position — not colour only |

Colour is the *accelerator* (fast for the 92% who see it), never the *sole carrier*.

## Rule 2 — Separate colours by more than hue

Two colours that differ only in hue can collapse to the same grey under CVD. Always also separate
by **lightness** and **chroma**. A quick test: convert the set to greyscale — if two swatches look
the same, they will confuse a colour-blind user even though they pass contrast.

**Avoid the classic traps:** pure red ↔ green (deutan/protan); red ↔ black (protan); teal ↔ grey,
blue ↔ purple, yellow ↔ pink (tritan).

## Rule 3 — Use a vetted safe set; simulate before shipping

### Okabe–Ito (8-colour categorical, the reference safe set)
Designed to be unambiguous for all common CVD types.

| Name | Hex |
|---|---|
| Black | `#000000` |
| Orange | `#E69F00` |
| Sky blue | `#56B4E9` |
| Bluish green | `#009E73` |
| Yellow | `#F0E442` |
| Blue | `#0072B2` |
| Vermillion | `#D55E00` |
| Reddish purple | `#CC79A7` |

### IBM Design colour-blind-safe (5-colour categorical)
`#648FFF` `#785EF0` `#DC267F` `#FE6100` `#FFB000` — high lightness spread; good on light or dark.

### Sequential / continuous data
Use **Viridis** (`#440154 → #31688E → #35B779 → #FDE725`) or **Cividis** (tuned specifically for
CVD). Both are perceptually uniform and monotonic in lightness, so they survive greyscale and all
CVD types. Avoid red→green diverging scales; if you need diverging, use blue↔orange or
blue↔brown and anchor with a neutral midpoint.

## A CVD-safe status set (status by lightness + icon, not just hue)

| Role | Light-mode hex | On surface `#FBFBFB` | Non-colour cue | Note |
|---|---|---|---|---|
| Success | `#0F7D3D` (deep green) | 4.9:1 ✓ | ✓ icon + "Success" | deeper than mid-green so protanopes see weight |
| Warning | `#9A6700` (amber-brown text) | 4.6:1 ✓ | ⚠ icon + "Warning" | dark amber, not yellow (yellow fails contrast on white) |
| Error | `#C0341D` (vermillion-red) | 5.1:1 ✓ | ✕ icon + "Error" | leans vermillion (Okabe–Ito) so it parts from green by lightness too |
| Info | `#1257A8` (blue) | 6.0:1 ✓ | ℹ icon + "Info" | distinct from success by hue *and* lightness |

Success vs Error here differ in **lightness and hue**, so they stay distinct in greyscale — the
icon is the guarantee, the colour is the accelerator.

## The simulation step (do this before shipping)

Run the candidate set through a CVD simulator for **all three** types — deutan, protan, tritan —
not just one. Tools: Coblis (color-blindness.com), Sim Daltonism (macOS), Chrome DevTools
Rendering → "Emulate vision deficiencies", or a `feColorMatrix` simulation. If any two
meaning-bearing colours converge, separate them further by lightness or rely harder on the
non-colour cue.

## Provenance

- WCAG 2.2 SC 1.4.1 *Use of Colour* (A) — W3C Recommendation; see
  `doctrine/references/wcag-2.2-criteria.md`.
- Okabe & Ito, "Color Universal Design" (2008).
- IBM Design Language — colour-blind-safe palette.
- Viridis / Cividis — Stéfan van der Walt & Nathaniel Smith (matplotlib); Cividis: Nuñez,
  Anderton & Renslow (2018), tuned for CVD.
- Anti-slop / authority basis: `doctrine/design-doctrine.md` §2.
