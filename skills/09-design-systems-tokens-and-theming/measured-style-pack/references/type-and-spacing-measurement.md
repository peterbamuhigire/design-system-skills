# Reference: Type Scale and Spacing Measurement Method

Applies to `measured-style-pack` Workflow steps 5-6.

## Type scale

### Extract raw sizes

Prefer computed `font-size` values read from a live/inspectable reference (devtools, or a
programmatic DOM walk) over pixel measurement from a static image — it removes DPI and rendering
noise entirely. When only a static image/deck export is available, measure cap-height or x-height
in pixels at a known export DPI and convert to a comparable size unit; record the DPI used so the
measurement is reproducible.

### Compute pairwise ratios, not a single guess

1. Collect every **distinct** rendered size (de-duplicate; a heading used at 3 places is one data
   point for scale purposes, not three).
2. Sort ascending.
3. Compute the ratio of each adjacent pair: `size[i+1] / size[i]`.
4. Report the **median** of those pairwise ratios as "the scale ratio," and print the full list —
   a real reference is rarely a perfectly even geometric progression; the full list shows exactly
   where it deviates (e.g. a compressed step between body and small-caption sizes, a wide jump to
   a hero size).

### Cross-check against the doctrine floor

`doctrine/references/type-scale-and-spacing.md` sets a **≥1.25** ratio floor. A measured median
ratio below that floor is a genuine finding about the reference — report it as such (the reference
system may itself be under the floor, which is useful information for whoever approved it) rather
than silently rounding the pack up to 1.25. Rounding up stops the pack being a measurement of the
reference and turns it into a guess dressed as one.

## Spacing

### Extract raw values

Same preference order as type: computed `margin`/`padding`/`gap` values from an inspectable
reference beat pixel measurement from an image.

### Score base-unit candidates, don't assume 8px

For each common candidate base unit (typically 4px and 8px, occasionally 5px or 10px for some
systems):

- Compute the share of all measured gap values that are an exact (or near-exact, ±1px tolerance
  for image-derived measurements) multiple of that candidate.
- The winning base unit is the one **maximising that share**, not the smallest common factor of
  the raw numbers (a smallest-common-factor approach is fooled by a handful of odd one-off values
  and reports a unit far finer than the system actually uses).

### Report the modal value and the full histogram

The single most frequently recurring gap value (the mode) is what an eye actually perceives as
"the" spacing rhythm — report it explicitly, alongside median/MAD for context, and print the full
histogram of measured values grouped into base-unit multiples. A mean spacing value is close to
meaningless here: it is rarely a value that appears anywhere in the actual layout.

### Off-grid share as its own statistic

Report the share of measured gaps that do **not** land on any multiple of the winning base unit
within tolerance. A high off-grid share is a genuine finding — either the reference itself is
inconsistent (useful to flag before treating it as authoritative) or the capture/masking step let
through some noise that needs re-checking.
