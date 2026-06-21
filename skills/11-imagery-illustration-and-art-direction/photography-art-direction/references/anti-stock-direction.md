# Reference: Anti-Stock Direction & AI-Image Handoff

Stock photography is not banned — *unconsidered* stock is. The same is true of AI imagery.
The failure is shipping an image **unauthored**: straight off the library or straight out of the
generator, recognisable as such. This reference is the kill-list, the sourcing ladder, the
"make stock un-stock" moves, and the AI-image direction handoff with its reject gate.

Grounded in `doctrine/design-doctrine.md` §0 (looks-human-made) and §2 (state the choice;
sourcing-authority asymmetry), and `doctrine/references/ai-slop-taxonomy.md` (the visual tells
and the "shovelware assets" backlash risk).

---

## 1. The cliché kill-list (reject on sight)

These are the convergent, training-data-saturated images that scream "nobody art-directed this":

- **The smiling handshake** / deal-closed-in-a-boardroom.
- **The headset call-centre agent**, mid-laugh, looking at a screen we can't see.
- **The diverse team laughing around a laptop / at a salad** in a too-clean office.
- **Isolated-on-pure-white** product or person with no environment, no story.
- **Lens-flare skyline / generic glass tower** standing in for "business."
- **Hands on a keyboard glowing with blue HUD nonsense** standing in for "technology / AI."
- **Pointing at a floating chart / touching a holographic interface.**
- **The perfect-teeth fake-candid** — posed to look spontaneous, fooling no one.
- **Doctor-folds-arms-with-stethoscope** / lawyer-with-gavel / any profession-as-costume.
- **Generic purple→blue gradient with sparkles** as a stand-in for an image (slop by the
  product/interface tells in `ai-slop-taxonomy.md`).

If a candidate is on this list, it is rejected — not graded, not cropped. Replaced.

---

## 2. The sourcing ladder (prefer top, descend only with reason)

| Tier | Use when | Risk |
|---|---|---|
| **1. Original shoot** | Budget exists; brand-defining surfaces; people/places that are *actually yours* | Cost/time — but the only fully authored option |
| **2. Commissioned / editorial** | A specific look you can brief a photographer or buy from an editorial library | Cost; still must be graded into the system |
| **3. Premium stock, used non-obviously** | Mid-budget; supporting imagery | Cliché risk — *must* be cropped + graded to stop reading as stock |
| **4. AI-generated (where permitted)** | No subject access, conceptual/abstract, the surface *allows* it, and it can pass the reject gate | High slop risk; legal/rights questions; never for "real people / real claims" |
| **5. Free stock** | Last resort, low-stakes surface | Highest cliché saturation — the §1 list lives here |

**Surface rule:** never put AI-generated or obvious stock people on a surface that makes a
**truth claim** (a real customer testimonial, a "our team," a medical/financial outcome). That is
the "shovelware assets" backlash trap from `ai-slop-taxonomy.md` §2.

---

## 3. How to make stock *un-stock* (Tier 3 rescue)

A decent stock frame can be made to look authored:

1. **Crop hard.** Cut into the action; off-centre the subject; kill the headroom. A tight crop
   destroys the "stock composition" instantly (see `photo-treatment-system.md` §Cropping).
2. **Grade it into the system.** Apply the brand grade — desaturate slightly, lift blacks, add
   grain. The single fastest tell-killer.
3. **Duotone the supporting set.** If it still reads generic, duotone it into the palette;
   reserve full colour for the one true hero.
4. **Combine / overlay** with a brand graphic element, texture, or type so it becomes a
   *composition*, not a borrowed photo.
5. **Pick the un-obvious frame** from the set — never the first/most-licensed result. The image
   everyone else also bought is the one that looks like stock.

If after all five it still reads as stock, it was the wrong pick — go back up the ladder.

---

## 4. AI-image direction handoff

AI imagery is admissible **only** when: the surface permits it (§2 surface rule), a human
re-grades/crops it into the treatment system, and it passes the reject gate below. Per doctrine
§2, the generator's *own* default aesthetic is **never** the authority for the look — we
art-direct *away* from its mean, exactly as we do with banned default fonts.

### The prompt (direct it like a photographer, not a slot machine)
Specify, concretely:
- **Subject + action** (specific, mid-task, not posed): *"a community nurse checking a tablet at
  a clinic reception, mid-task, not looking at camera."*
- **Lens & framing:** *"35mm, eye-level, shallow depth of field, subject off-centre."*
- **Light:** *"available daylight from a window, soft directional, warm."*
- **Mood & realism:** *"documentary, candid, natural skin texture, slightly imperfect."*
- **Grade hint** matching the treatment recipe (warm, muted, lifted blacks, fine grain).

### The negative-constraint list (always attach)
Keyed directly to the `ai-slop-taxonomy.md` visual tells:
```
NEGATIVE: waxy skin, plastic skin, hyper-glossy, HDR over-clarity, over-smoothed faces,
extra fingers, extra limbs, fused hands, malformed hands, dead/uncanny eyes, too-symmetrical
face, melted background, dissolving objects, floating objects, impossible shadows,
gibberish text, garbled signage, warped/misspelled logos, mismatched lighting, lens-flare
skyline cliché, glowing blue HUD, holographic interface, stock-photo smile, isolated on white
```

### The accept / reject gate (run on every generated frame)
Reject if **any** is true (these are the `ai-slop-taxonomy.md` Visual tells):
- [ ] Waxy / plastic / hyper-glossy skin or surfaces.
- [ ] Melted, incoherent, or dissolving background detail.
- [ ] Illegible / gibberish text or signage baked in.
- [ ] Floating objects, impossible shadows, broken physics.
- [ ] Anatomically impossible features (fingers, limbs, joints, fused hands).
- [ ] Misspelled / warped logos or brand marks.
- [ ] Uncanny face — dead eyes, "off" asymmetry, or too-smooth symmetry.
- [ ] Mismatched lighting across what should be one scene.
- [ ] Lands on any §1 cliché.

Pass only if it clears all of the above **and** can be graded/cropped into the treatment
recipe. Then a human re-grades and re-crops it — generation is the start, not the ship.

---

## 5. One-line decision record (state it, per doctrine §2)

> *"<surface>: sourcing tier <N> because <reason>; treatment = <recipe ref>; <if AI> passed the
> reject gate, re-graded by hand."*

No image ships without this sentence. An unstated image choice is a reflexive default — exactly
what the Anti-Slop Charter exists to stop.
