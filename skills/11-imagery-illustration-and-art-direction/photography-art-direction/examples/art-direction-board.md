# Worked Example: Art-Direction Board — "BrightSoma Clinics"

A complete, real art-direction brief for a sample brand. Reusable as a template — fill the
brackets for your own brand. Every value here is concrete (a spec, not adjectives), per
`references/photo-treatment-system.md` and `references/anti-stock-direction.md`.

**Brand:** BrightSoma Clinics — community health-tech, East Africa. Positioning: *competent,
warm, local, real* — the opposite of glossy Western telehealth stock.
**Audience:** clinic owners, patients, public-health partners.
**The one feeling the imagery must carry:** *"real people getting real care, calmly."*

---

## 1. Photographic intent (the one sentence — stated first)

> *Real Ugandan clinicians and patients mid-task, in actual clinic environments, lit by
> available daylight, framed close and slightly off-centre, calm and competent — never
> triumphant, never posed, never glossy.*

This sentence is the test every candidate image must pass. If a frame contradicts it, it's out.

## 2. Sourcing ladder decision (stated, per doctrine §2)

| Surface | Tier chosen | Reason |
|---|---|---|
| Homepage hero, "our clinics," patient stories | **Tier 1 — original shoot** | Truth-claim surfaces showing *real* people/places; cannot be stock or AI (surface rule, `anti-stock-direction.md` §2) |
| Blog / supporting / partner pages | **Tier 3 — premium stock, made un-stock** | Mid-budget; rescued by hard crop + grade + duotone |
| Abstract concept headers (e.g. "data privacy") | **Tier 4 — AI-generated** | No subject, conceptual, surface permits it, must pass the reject gate |
| (Never) | Free stock people on a truth surface | The "shovelware" backlash trap — banned here |

## 3. Treatment recipe (the system — applied to *every* image)

```
TREATMENT: BrightSoma Clinics
  Grade:      WB warm +200K · blacks lifted to #15171A · highlights soft-roll (no clipping)
              · contrast low S-curve · saturation -15% · shadow tint #1E6F6A (brand teal) @ 8%
  Grain:      2% mono film grain · vignette -6%
  Mono/duo:   supporting/blog images → duotone shadows #15171A → highlights #F4F1EA
              (full colour reserved for hero + real patient stories = the hierarchy signal)
  Crop:       focal off-centre on thirds · crop into the action (hands, faces cut at brow)
              · text-safe zone: lower-left quiet third for headline
  Ratios:     hero 2:1 · inline editorial 4:5 · square 1:1 (focal re-checked at each crop)
  Subject:    real clinician/patient mid-task · available daylight, directional · gaze on the
              task, not the lens · genuine environment, slight real-world mess kept
  Export:     AVIF q65 + WebP · hero within LCP budget (web-performance-budgets-2026.md)
              · responsive <picture> for true crops · alt: meaningful; decorative headers alt=""
```

## 4. Crop & focal direction (worked)

- **Hero:** nurse at a reception desk, framed at 2:1, her hands + tablet on the right third,
  the quiet left third for the headline. She looks at the tablet, not the camera. Crop cuts the
  ceiling out entirely — no headroom, no "office establishing shot."
- **Patient story (4:5):** patient's face cut at the brow, warm window light from frame-left,
  shallow depth so the busy background falls soft. Off-centre, looking off-frame.
- **Square (OG/social):** re-crop the hero so the tablet+hands cluster survives at 1:1; never
  squash the 2:1 into a square.

## 5. AI-image direction block (for the Tier-4 concept headers)

**Surface:** "Data privacy" section header — abstract, no people, AI permitted.

**Prompt:**
> *A close, documentary still-life of a clinic intake form and a phone on a wooden desk by a
> window, soft warm available daylight from the left, 35mm, shallow depth of field, off-centre
> composition, natural texture, slightly imperfect, muted warm grade, fine film grain.*

**Negative (attached):**
```
NEGATIVE: waxy skin, plastic, hyper-glossy, HDR over-clarity, extra fingers, fused hands,
dead eyes, melted background, dissolving objects, floating objects, impossible shadows,
gibberish text, garbled signage, warped/misspelled logos, mismatched lighting, glowing blue HUD,
holographic interface, lens-flare skyline, stock smile, isolated on white
```

**Accept / reject gate run (this candidate):**
- [x] No waxy/plastic surfaces — pass
- [x] Background coherent (a real desk, no melt) — pass
- [x] No baked-in gibberish text on the form (form is blurred, no legible nonsense) — pass
- [x] No floating objects / impossible shadows — pass
- [x] No hands/limbs in frame to malform — pass (still-life chosen *because* hands are AI's tell)
- [x] No logos to warp — pass
- [x] Lighting consistent (single window source) — pass
- [x] Not on the §1 cliché list — pass
- **Verdict: ACCEPT** → then re-graded by hand into the BrightSoma recipe (saturation -15%,
  teal shadow tint, 2% grain) and cropped 2:1. Generation was the start, not the ship.

> *Note:* the still-life was deliberately chosen over an AI image of "a person" precisely to
> dodge the hands/face tells from `doctrine/references/ai-slop-taxonomy.md`. Where AI is used,
> direct it onto subjects it can actually render cleanly.

## 6. Do / Don't board

| Do | Don't |
|---|---|
| Real clinicians mid-task, daylight | Headset call-centre agent (cliché kill-list) |
| Hands cut into the action, off-centre | Centre-punched, eyes down the lens |
| Muted warm grade + grain on everything | Raw ungraded stock, ten different looks |
| Duotone the supporting set for unity | Random colour images as a scrapbook |
| AI only for object/concept stills, vetted | AI "team of doctors" on the about page |

## 7. Decision record (the one-line stamp, per doctrine §2)

> *Hero: Tier 1 original shoot (truth surface); treatment = BrightSoma recipe; full colour as
> hierarchy. Privacy header: Tier 4 AI still-life, passed the reject gate, re-graded by hand.*

No image on this brand ships without a line like this.
