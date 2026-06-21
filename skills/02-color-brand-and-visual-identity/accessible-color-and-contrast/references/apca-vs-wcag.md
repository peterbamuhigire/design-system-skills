# Reference: APCA vs WCAG — design with one, certify with the other

This is the rule that keeps the colour group honest about contrast. The two methods are **not
competitors and not interchangeable** — they have opposite jobs.

| | **WCAG 2.x contrast ratio** | **APCA (Accessible Perceptual Contrast Algorithm)** |
|---|---|---|
| Role | **Conformance / certification** | **Design / judgement** |
| Status | Normative (WCAG 2.0/2.1/2.2 Recommendation) | **Draft** — the method in the WCAG 3.0 working draft; **not yet normative** |
| Output | A ratio, `1:1`–`21:1` | An `Lc` value, roughly `0`–`±108` |
| Model | Relative luminance (a simple `(L1+0.05)/(L2+0.05)`) | Perceptual: accounts for text size, weight, and polarity (dark-on-light vs light-on-dark) |
| Known weakness | Over-passes light-on-dark; can *fail* genuinely readable pairs; treats all text size/weight the same beyond one threshold | Not yet legally citable; thresholds still moving between drafts |

## The rule (from `doctrine/references/wcag-2.2-criteria.md` §Contrast method note)

> **Design with APCA, certify with WCAG.** Use APCA while choosing colours to judge *real*
> legibility; then verify against the 4.5:1 / 3:1 ratios for compliance.

- **APCA is the tool**, because it models how the eye actually reads — it knows that thin light
  text on black needs more separation than the same text dark-on-white, which the WCAG ratio is
  blind to. Use it to *make* the colour and stroke decisions.
- **WCAG 2.2 is the gate**, because it is the standard you certify, contract, and litigate
  against today. A pair that an APCA-tuned design produces must still be run through the WCAG
  ratio and pass the relevant floor. Until WCAG 3.0 is a Recommendation, the WCAG 2.x ratio is
  what "accessible" legally means.

**Never reverse them.** Certifying against APCA gives you no defensible conformance claim.
*Designing* against the bare WCAG ratio gives you pairs that test green but read badly (especially
in dark mode) and pairs you wrongly reject.

## The WCAG 2.2 floors you certify against (SC 1.4.3 / 1.4.11)

| Content | AA floor | AAA |
|---|---|---|
| Body / small text (< 24px, or < 18.66px bold) | **4.5:1** | 7:1 |
| Large text (≥ 24px, or ≥ 18.66px / 14pt bold) | **3:1** | 4.5:1 |
| UI components, meaningful icons, state-bearing borders, **focus rings** (1.4.11) | **3:1** | — |
| Disabled controls, pure decoration | exempt | — |

AA is the Chwezi floor for all work; reach AAA where feasible. Aim *past* the floor so a later
tint tweak doesn't drop you under it.

## How to compute the WCAG ratio (so the matrix is reproducible)

For each sRGB channel `c` in {R,G,B} as a `0–1` value:

```
cl = (c <= 0.03928) ? c/12.92 : ((c + 0.055)/1.055) ^ 2.4
L  = 0.2126*Rl + 0.7152*Gl + 0.0722*Bl     # relative luminance
ratio = (Llighter + 0.05) / (Ldarker + 0.05)
```

Round the ratio to one decimal *toward the failing side* (don't round 4.48 up to 4.5). Use a
checker (WebAIM Contrast Checker, the APCA `apca-w3` tool, or any conformant library) and record
the source.

## Rough APCA `Lc` guidance (design-time only — do not certify with these)

- `Lc 75+` — body text comfortably readable
- `Lc 60` — minimum for larger / heavier body
- `Lc 45` — large headings, ~24px+
- `Lc 30` — minimum for non-text / UI element boundaries
- `Lc 15` — invisibility floor; below this is effectively decorative

Use these to *choose*; then convert the decision to a WCAG ratio for the record.

## Don't over-contrast

A higher ratio is not automatically better. `#000` on `#fff` (≈ 21:1) vibrates and haloes —
APCA flags this (very high `Lc` with thin strokes reads as harsh) where the WCAG ratio cannot.
Use a near-black with a trace of brand hue on a slightly off-white surface; confirm it still
clears 4.5:1. **Legibility is the goal; the ratio is only the gate.**

## Provenance

- WCAG 2.2 SC 1.4.3, 1.4.11 — W3C Recommendation (w3.org/TR/WCAG22/).
- APCA — Andrew Somers / Myndex; the contrast method in the WCAG 3.0 working draft (draft, not
  normative). `git.apcacontrast.com`.
- Method note and AA-floor rule: `doctrine/references/wcag-2.2-criteria.md`.
