---
name: accessible-color-and-contrast
description: Use when colour must stay legible and inclusive — verifying or fixing text/UI contrast, building a colour-blind-safe palette or status set, choosing focus-ring and border colours, or auditing an existing palette before launch. Designs with APCA for real legibility, certifies against WCAG 2.2 (4.5:1 body / 3:1 large-and-UI) as the hard gate, never encodes meaning by hue alone, and makes every status/data colour distinguishable to deuteranopia, protanopia, and tritanopia. The contrast-and-accessibility authority for the colour group.
status: active
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Accessible Color And Contrast
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- A palette, theme, or token set is being finalised and every foreground/background pair must be
  proven to clear WCAG 2.2 contrast before it ships (text, icons, borders, focus rings, charts).
- You are choosing or fixing status colours (success / warning / error / info), data-series
  colours, links, or any colour that *carries meaning* — and it must survive colour-blindness.
- Auditing or refreshing an existing artifact's colours for accessibility, or resolving a
  Lighthouse / axe contrast failure, or a "users can't tell the red from the green" report.
- Picking a focus indicator, disabled-state, or placeholder colour where "looks faint" is not
  enough — it must measure ≥ 3:1 against its surround.

## Do Not Use When

- You are choosing the base palette / brand hue / tonal ramp from scratch — start at
  `02-color-brand-and-visual-identity/color-system-and-palette` (it already runs the contrast
  gate); come *here* to harden, certify, and colour-blind-proof what it produced.
- The accessibility issue is keyboard, ARIA, target size, or screen-reader — that is
  `00-cross-cutting-ops-qa-a11y/accessibility-wcag-2-2-compliance`. (Contrast lives here; the
  rest of WCAG lives there. They co-activate.)
- The work is categorical/sequential **chart encoding strategy** — bring the colour-blind-safe
  ramps from here, then hand the encoding to the data-viz group.

## Required Inputs

- The candidate colours as measurable values (hex, or OKLCH/sRGB) — not names. "Brand blue" is
  not checkable; `#2563EB` is.
- For every colour: the exact background(s) it sits on, the text size and weight (so you apply
  the right threshold), and whether the colour *encodes meaning* (status, data series, link).
- The target conformance level (AA is the Chwezi floor; AAA where feasible —
  `doctrine/references/wcag-2.2-criteria.md`) and whether dark mode must also be certified.

## Workflow

1. **Design with APCA, certify with WCAG — keep the two jobs separate.** Use APCA (the
   perceptual algorithm in the WCAG 3.0 *draft*) while tuning, because it tracks real legibility
   across light *and* dark far better than the 2.x ratio, which over-passes light-on-dark and
   can fail perfectly readable pairs. Then run the WCAG 2.2 ratio as the **conformance gate** —
   it is what you legally and contractually certify against
   (`doctrine/references/wcag-2.2-criteria.md` §Contrast method note). See `references/apca-vs-wcag.md`.

2. **Apply the right threshold to each pair — these are floors, not targets.** Body / small text
   **≥ 4.5:1**; large text (≥ 24px, or ≥ 18.66px / 14pt bold) **≥ 3:1**; meaningful UI components,
   icons, borders that convey state, and focus rings **≥ 3:1** (WCAG 2.2 SC 1.4.3 and 1.4.11,
   per `doctrine/references/wcag-2.2-criteria.md`). Aim past the floor (AAA is 7:1 / 4.5:1) so a
   later tint tweak doesn't drop you below. Disabled controls are exempt from 1.4.3 — but exempt
   is not invisible; keep them perceivable.

3. **Measure every pair and record it — no eyeballing.** Build the foreground×background matrix,
   compute the ratio for each, mark PASS/FAIL against the threshold from step 2, and *keep the
   table* as the contrast evidence (it ships with the palette). Any FAIL is rejected: retune the
   ramp step (darken text, deepen the surface, raise chroma on the accent) and re-measure until
   it passes. "It looks fine" is not a measurement. See `examples/contrast-checked-palette.md`.

4. **Never encode meaning by hue alone — pair colour with a second cue.** ~8% of men (and ~0.5%
   of women) have a colour-vision deficiency, so red-vs-green status, "the blue line vs the green
   line," or a red asterisk as the *only* signal fails them (WCAG 1.4.1 Use of Colour). Always
   add a redundant non-colour cue: an icon (✓ ⚠ ✕ ℹ), a text label, a shape, a pattern/dash style,
   or position. Colour becomes the *accelerator*, never the sole carrier. See
   `references/colorblind-safe-palettes.md`.

5. **Choose colour-blind-safe colours for anything that carries meaning.** Status sets and data
   series must stay distinguishable under deuteranopia, protanopia, and tritanopia. Separate hues
   by *more than hue* — also by lightness and chroma — and avoid the classic traps: pure
   red↔green, and teal↔grey / blue↔purple for tritanopes. Prefer a vetted safe ramp (Okabe–Ito,
   IBM, Viridis for sequential) and simulate before shipping. `references/colorblind-safe-palettes.md`
   gives ready ramps and the simulation step.

6. **Treat dark mode as a second certification, not a freebie.** Passing in light mode does not
   imply passing in dark. Re-run APCA design + the WCAG gate (steps 1–3) on the dark roles
   independently; accents usually need lightening and slight desaturation to hold 3:1 / 4.5:1 on
   a near-dark surface. (Full dark-mode remapping lives in
   `02-color-brand-and-visual-identity/dark-mode-and-theming`; the contrast proof lives here.)

7. **Don't over-contrast either.** `#000` on `#fff` (≈ 21:1) vibrates and haloes — high ratio is
   not the goal, *legibility* is. APCA flags this where the WCAG ratio cannot. Use a near-black
   carrying a trace of brand hue on a slightly off-white surface; verify it still clears 4.5:1.

8. **State the result and hand off.** Output the certified pairs (with ratios), the non-colour
   cue paired to each meaningful colour, the colour-blind-safe status/series set, and the
   light + dark verdicts. Note the conformance level reached (AA / AAA per pair).

## Anti-Patterns

- Certifying against APCA, or *designing* against the bare WCAG ratio — the two tools have
  opposite jobs (design vs certify). Reversing them ships pairs that test green but read badly,
  or rejects pairs that are genuinely fine (`references/apca-vs-wcag.md`).
- Red/green (or any hue-only) status, links distinguished from body by colour alone, required
  fields marked only by a red asterisk — anything where removing colour removes the meaning.
- Eyeballing contrast, or treating 4.5:1 as a number to *barely* clear rather than a floor to
  clear comfortably. Shipping a palette with no recorded contrast table.
- `#000` on `#fff`, or chasing the highest possible ratio as if more is always better.
- Assuming dark mode inherits light-mode passes; using full-chroma accents on near-black.
- Justifying a status palette because "a generator suggested it" — accessibility traces to the
  perceptual evidence and the WCAG/APCA methods, not to a tool's default
  (`doctrine/design-doctrine.md` §2, the sourcing-authority asymmetry rule).

## Outputs

- A foreground×background **contrast matrix** with measured ratios and PASS/FAIL per WCAG 2.2
  threshold, for light and (where required) dark.
- A colour-blind-safe status/series set, each meaningful colour paired with a stated non-colour
  cue, plus the simulation note (deutan/protan/tritan).
- The conformance verdict (AA floor met; AAA where reached) and any retunes made to get there.

## Examples

- `examples/contrast-checked-palette.md` — a real, named palette with the full pair-by-pair
  contrast matrix (every foreground/background ratio + PASS/FAIL), the colour-blind-safe status
  set with its non-colour cues, and the dark-mode re-certification. A worked artifact, not lorem.

## References

- `doctrine/references/wcag-2.2-criteria.md` — the contrast floors (1.4.3 / 1.4.11), the
  "design with APCA, certify with WCAG" method note, and the AA-is-the-floor rule.
- `doctrine/design-doctrine.md` — Mission §0 (authored, defensible choices over convergent
  defaults) and Anti-Slop Charter §2 (the sourcing-authority asymmetry rule: methods and
  perceptual evidence are authority; a tool's default is not).
- `references/apca-vs-wcag.md` — when to use each, why, and the certification boundary.
- `references/colorblind-safe-palettes.md` — vetted safe ramps, the three CVD types, and the
  non-colour-cue rule (WCAG 1.4.1 Use of Colour).
- Human authority (named for provenance, not citable in-repo): Okabe & Ito colour-blind-safe
  palette; IBM Design colour-blind-safe set; Viridis (Smith & van der Walt) for sequential data;
  WCAG 2.2 SC 1.4.1 / 1.4.3 / 1.4.11; APCA (Somers, in the WCAG 3.0 draft).
<!-- dual-compat-end -->
