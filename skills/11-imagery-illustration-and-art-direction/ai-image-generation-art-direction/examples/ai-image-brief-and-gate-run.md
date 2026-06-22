# Worked Example: AI-Image Brief + Gate Run — "Maduuka"

A complete, real AI-image direction case for a sample brand. Reusable as a template — fill the
brackets for your own. Every value is concrete (a spec, not adjectives), per
`references/ai-image-direction-and-gate.md`, `doctrine/design-doctrine.md` (Mission §0; Charter §2),
and `doctrine/references/ai-slop-taxonomy.md` (the visual tells + shovelware backlash risk).

**Brand:** Maduuka — a platform for small East-African merchants (dukas / market stalls).
Positioning: *practical, local, warm, real* — the opposite of glossy fintech stock.
**Surface:** the blog header for an article *"Keeping stock when cash is tight"* — a **conceptual**
header, not a customer or product claim.
**The one feeling the image must carry:** *"the texture of real small-trade — busy, human, unpolished."*

---

## 1. Allowed-surface decision (the gate before the gate — §1)

| Question | Answer |
|---|---|
| Does the surface make a **truth claim** (real customer / team / place / outcome)? | **No** — it is a conceptual article header, no real person/merchant is being asserted |
| Is the use conceptual / illustrative / mood-carrying? | **Yes** — it sets the scene for an idea |
| Does the model licence permit this commercial use? | **Yes** — paid tier, commercial rights confirmed, provider offers output indemnity |
| Can it pass the reject gate + integrate into the treatment recipe? | To be tested (§5–§6) |

**Decision: AI imagery permitted (gated).** Had this been "meet our merchants" or a named real duka,
AI would be **forbidden** (shovelware trap, `ai-slop-taxonomy.md` §2) → route to a Tier-1 shoot via
`photography-art-direction`.

## 2. Intent sentence (stated first — Charter §2)

> *A busy market stall at dawn, produce being arranged by hands mid-motion, available warm daylight
> from the side, framed close and off-centre, documentary and unpolished — never glossy, never posed.*

Every candidate must pass this sentence. A glossy, centred, "professional" frame contradicts it → out.

## 3. The prompt (directed, not adjective-piled — §2)

```
A market trader's hands arranging tomatoes and greens on a wooden stall at dawn, mid-motion,
not looking at camera, 35mm, eye-level, shallow depth of field, subject off-centre, available
warm daylight from camera-left (soft, directional), documentary candid style, natural skin
texture with visible pores, real-world wear on the wood and crates, slight motion blur in the
hands, warm slightly-desaturated grade with lifted blacks and fine grain.
```

## 4. Negative-constraint list (attached — §3)

```
NEGATIVE: waxy skin, plastic skin, hyper-glossy, HDR over-clarity, over-smoothed faces,
extra fingers, fused hands, malformed hands, dead eyes, too-symmetrical face, melted background,
dissolving objects, floating objects, missing contact shadow, gibberish text, garbled signage,
warped logo, mismatched lighting, creamy uniform bokeh, golden-hour-on-everything, uniform-
frequency texture, lens-flare cliché, glowing blue HUD, stock-photo smile, isolated on white,
generic purple-blue gradient, AI sparkle, no-author style-blend
```

---

## 5. Gate run on two candidates (§5)

### Candidate A — REJECTED

| Gate item | Result |
|---|---|
| Waxy / plastic / hyper-glossy skin (A1) | **FAIL** — the hands and tomatoes have a plastic, poreless sheen |
| Gibberish text / garbled signage (A3) | **FAIL** — a price card on the stall reads as warped pseudo-glyphs |
| Texture-too-even (A9b) | **FAIL** — the wood grain repeats at uniform frequency, no real wear |
| No-author style-blend (A9f) | **FAIL** — golden-hour-on-everything, creamy bokeh; the convergent AI house style, "made by nobody" |
| Closing question: *would a named designer have made this exact choice?* | **No** |

**Disposition: REJECT — remake, do not patch.** Three hard tells (A1, A3, A9b) plus the moat-failure
(A9f). Re-prompt with stronger texture/wear cues and a committed documentary point of view; tighten
the negative list (`HDR over-clarity, creamy bokeh, golden-hour` are already in — increase weight /
re-roll). Per `ai-slop-taxonomy.md`, a garbled-signage public header is exactly the shovelware risk.

### Candidate B — ACCEPTED (as a post-processing candidate)

| Gate item | Result |
|---|---|
| Skin / surface texture (A1, A9b) | Pass — visible pores, real wood wear, non-uniform detail |
| Text / signage (A3, A9d) | Pass — no baked-in text in frame (hands + produce only; crop avoids the price card) |
| Anatomy incl. zoom (A5, A9c) | Pass — hands correct at hero scale and on zoom; no watch/ring defects |
| Lighting / reflections (A8, A9e) | Pass — single consistent warm side-light, no impossible reflections |
| Default-render light & bokeh (A9a) | Pass — light is directional and a little harsh, not the creamy default |
| No-author style-blend (A9f) | Pass — committed documentary look with a clear point of view |
| Closing question | **Yes** — a documentary photographer could have framed this |

**Disposition: ACCEPT as a candidate → post-process (§6).** Then ship.

## 6. Post-processing applied (§6)

1. Re-graded into the Maduuka recipe: warm, −12% saturation, blacks lifted, contrast curve matched.
2. Added fine film grain to lock in the non-even texture.
3. Re-cropped tighter and off-centre; produce fills lower third, negative space top-left for the
   article title (safe text zone, contrast-checked per `wcag-2.2-criteria.md`).
4. No micro-anatomy repair needed; checked teeth/jewellery n-a (no face/accessories in frame).
5. Exported AVIF, 1600px, 78 KB — inside the LCP budget (`web-performance-budgets-2026.md`).
6. `alt`: *"Hands arranging tomatoes and greens on a market stall at dawn."*

## 7. Provenance + one-line decision record (§4, §7)

> *Blog header "Keeping stock when cash is tight": AI imagery permitted because it is a conceptual,
> non-claim header (no real merchant asserted); model [Flux-pro v1.1], commercial rights & output
> indemnity checked; passed the reject gate (candidate B); re-graded/cropped into the Maduuka
> treatment recipe; C2PA content-credentials retained; no watermark ghosts.*

No generated image ships without this sentence — an unstated generation is a reflexive default,
exactly what the Anti-Slop Charter (`doctrine/design-doctrine.md` §2) exists to stop.
