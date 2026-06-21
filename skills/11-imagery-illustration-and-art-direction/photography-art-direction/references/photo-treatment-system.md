# Reference: The Photo Treatment System

A *treatment system* is the small set of concrete, repeatable rules that make every image —
shot, stock, or generated, from any source — look like it came from one art director. Without
it, imagery reads as a scrapbook. With it, a £0 stock frame and a commissioned shot sit
together as one brand. This is the lever that turns "an image" into *your* image.

State the treatment as **values, not adjectives.** "Warm and editorial" is a wish; the recipe
below is a spec.

---

## 1. The grade (colour & tone)

Define a single grade and apply it to everything. Specify, at minimum:

| Control | What to specify | Typical authored choice |
|---|---|---|
| **White balance** | Cool / neutral / warm, in Kelvin or a tint direction | Warm +200K for human/care brands; neutral for technical |
| **Black point** | Do shadows hit true black or lift to charcoal? | Lifted blacks (`#14171A`, not `#000`) = filmic, modern, less harsh |
| **Highlight rolloff** | Clip white or roll off to a soft near-white? | Soft rolloff (no blown highlights) reads premium, not snapshot |
| **Contrast curve** | Flat / medium / punchy | Medium-low S-curve; flat-ish midtones read editorial, not stock |
| **Saturation** | Full / muted / selective | Muted -10 to -20%; *desaturating slightly is the single fastest "un-stock" move* |
| **Accent tint** | A subtle colour cast tying images to the palette | e.g. a faint teal in shadows pulled from the brand teal |

A consistent grade is *the* signature. If you do only one thing, do this.

## 2. Grain & texture

Digital-clean is a slop tell — it is also the default of every AI generator. A whisper of grain
reads as physical, captured, human.

- **Grain:** 1–3% monochrome film grain over the final image. Enough to feel, not to see.
- **Avoid** plastic over-smoothing and HDR "clarity" — these are the waxy/hyper-glossy tell from
  `doctrine/references/ai-slop-taxonomy.md` (Visual tells). Push toward *texture*, never away.
- Optional: a very slight vignette (−5 to −10% at corners) to seat the subject — never a heavy
  Instagram vignette.

## 3. Monochrome / duotone (optional unifier)

When source images are wildly inconsistent (mixed stock, mixed eras), a **duotone** is the
strongest unifier: map shadows→brand-dark, highlights→brand-light. Everything instantly belongs.

- Duotone shadow/highlight pair should be two brand colours with a real luminance gap.
- Reserve full colour for *hero / product-truth* shots; duotone the supporting imagery. This
  also creates hierarchy (the colour image is the one that matters).

## 4. Cropping & focal point

Most of the "stock look" lives in a lazy, centred crop. Re-cropping is free art direction.

- **Off-centre the subject.** Place the focal point on a thirds intersection, not dead centre.
  Centre-punched + eyes-down-the-lens is the convergent default — avoid it.
- **Crop *into* the action.** Tight, decisive crops (a pair of hands, a face cut at the brow)
  read as authored; full-body-with-headroom reads as stock.
- **Intentional negative space.** Leave a deliberate quiet zone for the headline/overlay — this
  is design, not waste. Define the text-safe zone per layout.
- **Ratios — pick a deliberate set**, do not use whatever the file ships at:
  - Hero / banner: `16:9` or a cinematic `21:9` / `2:1`.
  - Editorial inline / card: `4:5` (portrait, more human) or `3:2`.
  - Square (OG/social/avatars): `1:1`, focal point checked at this crop too.
  - Always verify the focal point survives every ratio (responsive art-direction with
    `<picture>`/`srcset`, not one image squashed into all sizes).

## 5. Subject direction (what's *in* the frame)

- **Real, specific, mid-task** beats posed-and-smiling. Candid-of-a-real-moment > staged candid.
- **Gaze:** subject looking *at their task* or off-frame > staring into the lens.
- **Light:** available / natural light with real direction and shadow > flat studio fill. Hard
  light with intent beats safe soft light with none.
- **Imperfection is the signal:** a slightly messy desk, a real (not stock-perfect) face, a
  genuine environment. Perfection is the AI/stock tell; specificity is the human one.

## 6. Weight & technical (non-negotiable)

- Export **AVIF first, WebP fallback.** Quality ~60–70 for AVIF is usually invisible-loss.
- Keep every image inside the LCP weight budget in
  `doctrine/references/web-performance-budgets-2026.md` — the hero especially. A beautiful image
  that blows LCP is a UX failure, not a win.
- Provide responsive sources (`srcset` + `sizes`, or `<picture>` for true art-directed crops).
- **Alt text** per `doctrine/references/wcag-2.2-criteria.md`: meaningful for content images,
  empty (`alt=""`) for purely decorative ones. Never auto-generate vague alt.
- If text overlays the image, guarantee contrast (scrim/gradient/overlay) to the WCAG threshold.

---

## The treatment recipe template (fill this, reuse it)

```
TREATMENT: <brand name>
  Grade:      WB <warm/neutral/cool, +/-K> · blacks lifted to <#hex> · highlights soft-roll
              · contrast <low/med> S-curve · saturation <-N%> · shadow tint <#hex @ N%>
  Grain:      <N%> mono film grain · vignette <N%>
  Mono/duo:   <none | duotone shadows <#hex> → highlights <#hex>, applied to: <which images>>
  Crop:       focal off-centre (thirds) · crop into action · text-safe zone: <where>
  Ratios:     hero <16:9|2:1> · inline <4:5|3:2> · square <1:1>
  Subject:    <one sentence: who, doing what, light, gaze, mood>
  Export:     AVIF q<NN> + WebP · within LCP budget · responsive srcset · alt policy stated
```

Run *every* candidate image through this recipe. If it can't be made to fit, it's the wrong
image — replace it, don't ship it raw.
