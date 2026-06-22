# Reference: AI-Image Direction & the Reject/Accept Gate

The method for directing an AI image model so the output looks **authored, not slop**, and the gate
that keeps un-authored frames off Chwezi surfaces. AI imagery is not banned — *unconsidered,
un-gated, un-integrated* AI imagery is. The failure is shipping a generation **as it fell out of the
model**: the convergent mean, recognisable as such.

Grounded in `doctrine/design-doctrine.md` §0 (looks-human-made), §2 (state the choice; the
sourcing-authority asymmetry — the generator's own defaults are *evidence of what to avoid*, never
authority for what to use), and `doctrine/references/ai-slop-taxonomy.md` (the visual tells and the
"shovelware assets" backlash risk). Pairs with `photography-art-direction/references/anti-stock-
direction.md` (the photo sourcing ladder + treatment recipe this output must land in) and the
`visual-product-slop-audit` tells checklist (the product-wide gate this is built to pass).

---

## 1. Is AI imagery even allowed here? (the gate before the gate)

Decide *before* prompting. AI imagery is admissible **only** when ALL hold:

- **The surface makes no truth claim.** Never generate people/scenes for a surface that asserts
  something *real*: a customer testimonial, "our team / our clinic," a named place, a medical /
  financial / outcome claim, a real product the buyer will receive. Generating there is the
  **"shovelware assets" backlash trap** (`ai-slop-taxonomy.md` §2) — the public failure that triggers
  the loudest reaction. Those surfaces go to a real shoot (`photography-art-direction`, Tier 1).
- **The use is conceptual / abstract / background / illustrative**, where no real subject is being
  represented — concept headers ("data privacy"), abstract textures, stylised key art, decorative
  backgrounds that carry mood not fact.
- **The model's licensing permits it** for this commercial use (see §4).
- **It can pass the reject gate (§5) AND be integrated into the treatment recipe (§6).**

If any fails, **do not generate** — route up the sourcing ladder. State the decision either way (§7).

| Surface | AI allowed? | Why |
|---|---|---|
| Real customer / team / clinic / outcome | **No** | Truth claim — shovelware trap |
| Concept header, abstract texture, stylised key art, mood background | **Yes (gated)** | No real subject asserted |
| Product the buyer actually receives | **No** | Misrepresents the real thing |
| Conceptual hero where a *symbolic* (not real) subject is fine | **Maybe** | Only if clearly non-literal and gated |

---

## 2. The prompt — direct it like a photographer/illustrator, not a slot machine

Adjective-piles ("beautiful, professional, high-quality, 4k, trending, award-winning") yield the
**convergent mean** — the exact slop the Mission tells us to escape. Direct concretely instead:

- **Subject + specific action** (mid-task, not posed): *"a market trader arranging produce on a stall
  at dawn, mid-motion, not looking at camera."*
- **Medium / lens + framing:** for photo-real — *"35mm, eye-level, shallow depth of field, subject
  off-centre, slight motion blur in the hands."* For illustration — name a **committed style with a
  point of view** (e.g. *"flat editorial vector, limited 3-colour palette, visible grain"*), never
  "digital art," which averages every style into the no-author blend (§5, A-blend tell).
- **Light:** name the source + direction + quality — *"available daylight from camera-left, soft,
  warm,"* not "good lighting."
- **Mood + realism cues:** *"documentary, candid, natural skin texture with visible pores, slightly
  imperfect, real-world wear on surfaces."* These actively fight the plastic default-render.
- **Grade hint** matching the treatment recipe (`photo-treatment-system.md`): *"warm, slightly
  desaturated, lifted blacks, fine grain"* — so the output lands closer to the brand look.

**Commit to one point of view.** The single strongest anti-slop move in a prompt is naming a
specific, defensible aesthetic — the choice a templating tool would never make (doctrine §0).

---

## 3. The negative-constraint list (always attach)

Keyed directly to the `ai-slop-taxonomy.md` visual tells. Paste and tune per model:

```
NEGATIVE: waxy skin, plastic skin, hyper-glossy, HDR over-clarity, over-smoothed faces,
airbrushed skin, poreless skin, extra fingers, extra limbs, fused hands, malformed hands,
doubled teeth, dead eyes, glassy catchlights, too-symmetrical face, mannequin affect,
melted background, dissolving objects, bleeding edges, floating objects, missing contact shadow,
impossible shadows, gibberish text, garbled signage, warped logo, misspelled logo, invented
brand mark, mismatched lighting, cut-out composite edges, creamy uniform bokeh, golden-hour-on-
everything, uniform-frequency texture, lens-flare skyline cliché, glowing blue HUD, holographic
interface, stock-photo smile, isolated on white, generic purple-blue gradient, AI sparkle
```

Tune by surface: for illustration, add `no-author style-blend, averaged digital-art mush`; for
product/UI imagery, emphasise the small-text and gauge garbling terms.

---

## 4. Provenance & licensing caution (check before you embed)

Embedding/publishing an AI image is a **rights act**, not just an aesthetic one:

- **Commercial-use rights.** Confirm the model's terms permit *commercial* output for this use. Free /
  research tiers often do not. Output you cannot license, you cannot ship.
- **Training-data provenance & indemnity.** Some providers offer commercial **indemnity** (they back
  you against IP claims on the output); many do not. Higher-stakes / public surfaces should prefer a
  model that does, and the decision should be recorded. Treat un-indemnified output as higher risk.
- **No real person or real trademark.** Do not generate a recognisable real individual, a real
  customer's likeness, or a real brand's protected mark/logo (warped or not — A6 tell *and* a legal
  risk).
- **Content credentials (C2PA).** Where the model emits provenance metadata, **keep it** — it is the
  honest signal that this is generated. Do not strip it to pass the work off as a photograph.
- **No laundering.** Never present AI output as a genuine photo of a genuine subject. That is both a
  slop failure (the truth-claim ban, §1) and a trust failure.
- **Watermark hygiene.** Strip stray model/stock **watermark ghosts** (A9g tell) — but that is
  cleanup of an artifact, *not* removal of legitimate provenance metadata above.

Sourcing-authority reminder (doctrine §2): the model's *recommended* look is **never** the authority
for our look — it is the convergence we art-direct away from. An AI nod is not an endorsement.

---

## 5. The accept / reject gate (run on EVERY candidate frame)

Reject if **any** box is true. Classic tells (`ai-slop-taxonomy.md` §Visual tells):

- [ ] **Waxy / plastic / hyper-glossy** skin or surfaces (A1).
- [ ] **Melted / incoherent / dissolving** background detail; objects bleeding together (A2).
- [ ] **Illegible / gibberish text** or signage baked in (A3).
- [ ] **Floating objects, impossible shadows, broken physics** (A4).
- [ ] **Impossible anatomy** — extra/fused fingers, missing joints, doubled teeth, mismatched ears (A5).
- [ ] **Warped / misspelled / invented logo** or brand mark (A6).
- [ ] **Uncanny face** — dead eyes, "off" asymmetry, too-smooth symmetry, mannequin affect (A7).
- [ ] **Mismatched lighting** across what should be one scene; cut-out composite edges (A8).
- [ ] Lands on a **cliché stand-in** — lens-flare skyline, glowing-blue HUD, holographic UI,
      stock-photo smile, isolated-on-white, purple→blue sparkle gradient.

**2026 migrated tells** — the classic six-finger artifact is largely fixed in late-2025/2026 models,
so audit for the subtler giveaways (`ai-slop-taxonomy.md`; `visual-tells-checklist.md` §A9):

- [ ] **Plastic "default-render" light & bokeh** — uniform soft studio light, creamy blur,
      golden-hour-on-everything. Technically clean, convergent AI house style (A9a).
- [ ] **Texture-too-perfect / detail-too-even** — fabric, skin, foliage at uniform frequency, no
      real-world noise/dust/wear/focal falloff (A9b).
- [ ] **Micro-anatomy & accessory errors on zoom** — teeth, earrings, watch faces, eyeglass hinges,
      jewellery merging into skin, hair fused into scalp (A9c). Correct at thumbnail, broken at hero.
- [ ] **Garbled fine text / UI chrome / gauges** — small text, keyboard keys, screen UI, dials,
      plates degrade to pseudo-glyphs even when a headline is correct (A9d).
- [ ] **Impossible reflections & re-tiling** — mirror/glass/water reflections that don't match;
      tiles/brick/stripes that drift or re-tile illogically (A9e).
- [ ] **No-author style-blend** — averaged mush of styles, competent, generic, attributable to no
      human hand. "Made by nobody" (A9f). **This is the core moat-failure — reject even with zero
      hard anomalies.**

> **The 2026 rule of thumb:** the obvious artifact is gone; the tell is now the **absence of authored
> specificity** — perfect, even, styleless competence. The closing question on every frame:
> *"Would a named designer have made this exact choice?"* If the honest answer is no, it is slop.

**Pass** only if it clears *all* of the above **and** can be graded/cropped/integrated into the
treatment recipe (§6). A pass is a *candidate for post-processing*, never a ship.

---

## 6. Post-processing & integration (generation is the start, not the ship)

A passed frame is raw material. Make it *yours*:

1. **Re-grade into the treatment recipe** — apply the brand grade (desaturate slightly, lift blacks),
   match the contrast curve. The fastest tell-killer for the plastic default-render (A9a).
2. **Add real-world grain / noise** — kills the too-even texture (A9b) that screams "stock-AI."
3. **Re-crop hard** — off-centre the subject, kill the default centre-punch composition, crop into
   the action, leave intentional negative space for text (`photo-treatment-system.md` §Cropping).
4. **Repair micro-anatomy & zoom errors** (A9c) — fix or paint out the teeth/earring/watch/hair
   defects, or re-crop to exclude them. If the defect is *load-bearing* (a hand on a hero), **remake,
   don't patch** — you do not spot-fix a structurally broken frame.
5. **Composite with brand elements** — texture, type, a graphic mark — so it reads as a *composition*,
   not a borrowed generation.
6. **Strip watermark ghosts**, keep legitimate C2PA provenance (§4).
7. **Accessibility & weight** — meaningful `alt` text (decorative → empty alt,
   `doctrine/references/wcag-2.2-criteria.md`), contrast for any overlaid text, and final weight
   inside the LCP budget (`doctrine/references/web-performance-budgets-2026.md`).

If after all this it still reads as "a generation," it failed — go back up the sourcing ladder.

---

## 7. The one-line decision record (state it, per doctrine §2)

> *"<surface>: AI imagery permitted because <non-claim/conceptual reason>; model <name + version>,
> commercial rights & indemnity checked; passed the reject gate (§5); re-graded/cropped into
> <treatment recipe ref>; provenance <C2PA kept / n-a>."*

No generated image ships without this sentence. An unstated generation is a reflexive default —
exactly what the Anti-Slop Charter (`doctrine/design-doctrine.md` §2) exists to stop.
