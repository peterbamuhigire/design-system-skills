# Reference: Colour Measurement Method

Applies to `measured-style-pack` Workflow step 4. Adapted from ECC's `taste-distillation`
colour-grade measurement, retargeted from video frames to static UI/brand references
(screenshots, deck exports, live computed styles).

## Convert to OKLCH first

Sample colour in OKLCH (`oklch(L C H)`), matching the primitive-token convention in
`design-tokens-and-naming` step 4: lightness is perceptual, so distance between samples is
meaningful, and a chroma/hue drift is separable from a pure lightness difference. Keep the
original hex/sRGB alongside for legacy fallback, but do all statistics in OKLCH.

## Bucket by lightness band, not globally

A single global mean colour is close to useless: a brand's identity usually lives in one or two
lightness bands (e.g. a saturated accent that only appears in midtones, everything else
near-neutral). Use fixed bands so packs are comparable across references:

```
bands (L*, 0-100 scale): [0-15] shadow, [15-35] low-mid, [35-55] mid, [55-75] high-mid, [75-100] highlight
```

For each band, collect every sampled pixel/swatch whose lightness falls in it.

## Median + MAD per band, not mean + std

Chroma samples from a real reference are typically right-skewed (a handful of highly saturated
accent pixels among a much larger neutral majority). A mean-based statistic overweights those
outliers and produces a pack that reads far more saturated than the reference actually looks.
Report, per band:

- **median chroma**, **MAD (median absolute deviation) of chroma**
- **median hue** (circular median if the band spans a hue discontinuity), spread
- **sample count** in the band (so a thin band — e.g. only 12 shadow samples — is flagged as
  low-confidence rather than presented with the same weight as a 4,000-sample midtone band)

## Report the whole curve

Print every band's statistics, not just the darkest and lightest. Calling a reference "uniform" or
"neutral" from only its endpoints is a pure reporting artefact — the real signature is very
commonly in the midtones.

## Background/ink share as a first-class statistic

Record the share of sampled pixels below a near-black lightness threshold (e.g. L\*10) and,
separately, the share above a near-white threshold. Neither is visible from median/MAD alone: a
sample can have a plausible median lightness and low spread while its shadow region has been
lifted (too little true dark) or crushed (too much). This is the design-token equivalent of ECC's
"background share" statistic that caught a video grade with a technically good MAE but visibly
wrong blacks.

## Mask the furniture before sampling

Exclude, by crop or explicit region mask, before any statistic is computed:

- Browser chrome, OS window decoration, cursor, scrollbars
- Ad units, cookie/consent banners
- Lorem Ipsum / placeholder content blocks
- Any UI chrome not part of the reference's own design (a third-party embed, a support widget)

Unmasked furniture systematically pulls every statistic toward generic browser/OS defaults, not
the brand's actual palette. When a live site is inspectable, prefer reading computed CSS colour
values directly over pixel sampling — it sidesteps masking entirely for elements you can select in
devtools, though page furniture (ads, embeds) still needs excluding from any pixel-based capture
you also take.

## Percentile selection for "the accent colour"

When the pack needs to name a single accent swatch from a noisy sample (not just report band
statistics), select by percentile within the highest-chroma band (e.g. the 90th-percentile chroma
sample in that band) rather than an absolute chroma cutoff — an absolute threshold tuned on one
reference over- or under-selects on the next one with a different overall saturation level.

## Verify before use

Every semantic pair built from the measured primitives still needs the WCAG contrast gate run
independently (`doctrine/references/wcag-2.2-criteria.md`) — a faithfully measured reference can
itself contain a failing pair.
