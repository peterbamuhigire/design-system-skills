# Reference: Visual & Product Tells Checklist

A concrete, tickable checklist for the `visual-product-slop-audit` workflow. It operationalises
`doctrine/references/ai-slop-taxonomy.md` — read that taxonomy first for the *why* and the five
categories; this file is the *how* you run during an audit. Every tell here traces to the taxonomy
(category cited inline). When a tell fires, tag the finding **critical / major / minor** and decide
**remake vs remediate** per the SKILL workflow.

Provenance: derived from `ai-slop-taxonomy.md` (§Visual & video tells, §Product / interface tells,
§The 5 categories) and the doctrine Mission ("the moat is looking human-made"). Last reviewed
2026-06.

---

## A. Image / visual tells (per asset)

Run against every AI-generated or AI-assisted image, key art, thumbnail, hero, avatar, or icon.
Source: taxonomy §Visual & video tells; categories 1 (social-media slop) & 2 (corporate/advertising
"shovelware assets").

| # | Tell | What to look for | Default severity |
|---|---|---|---|
| A1 | **Waxy / hyper-glossy skin** | Plasticky sheen, pores erased, airbrushed-uniform texture, "rendered" not photographed | major → **critical** if public-facing face |
| A2 | **Melted / incoherent backgrounds** | Detail dissolves; objects bleed into each other; architecture that doesn't resolve on zoom | major |
| A3 | **Gibberish / illegible text in-image** | Baked-in signage, packaging, book spines, UI text that is non-words or warped glyphs | **critical** (instantly legible as AI) |
| A4 | **Floating objects / broken physics** | Impossible shadows, no contact shadow, objects unsupported, reflections that don't match | major |
| A5 | **Impossible anatomy** | Extra/missing fingers or limbs, fused hands, missing joints, doubled teeth, mismatched ears | **critical** |
| A6 | **Warped / misspelled logos & brand marks** | Distorted wordmark, wrong letterforms, off-geometry icon, invented brand glyphs | **critical** (legal + trust risk) |
| A7 | **Uncanny faces** | Dead eyes, glassy catchlights, too-smooth symmetry, asymmetry that reads "off," mannequin affect | **critical** if a person fronts the brand |
| A8 | **Mismatched lighting in a composite** | Subject and background lit from different directions / colour temps; cut-out edges | major |

### A9. Current 2026 AI-image tells (newer-model failure surface — INJECTED)

Modern diffusion/transformer image models (late-2025/2026 generations) have largely fixed the
*classic* six-finger artifact, so the tells have **migrated**. These are the current, higher-fidelity
giveaways — still squarely taxonomy categories 1 & 2, just subtler:

- **A9a — Plastic "default-render" lighting & bokeh.** Uniform soft studio light, creamy
  background blur, golden-hour-on-everything. The image is *technically clean* but has the
  convergent AI house style — exactly the "convergent AI mean" the Mission tells us to escape.
  Severity: **major** (it is the new corporate slop — passes a casual glance, fails a designer's).
- **A9b — Texture-too-perfect / detail-too-even.** Fabric weave, skin pores, foliage, gravel
  rendered at uniform frequency with no real-world noise, dust, wear, or focal falloff. Reads as
  "stock-AI." Severity: major.
- **A9c — Micro-anatomy & accessory errors.** Hands now *look* right at thumbnail size but break on
  zoom: teeth count, earring asymmetry, watch faces, eyeglass hinges, jewellery that merges with
  skin, hair strands fused into the scalp. Severity: **critical** at hero scale, major at small.
- **A9d — Garbled fine text & UI chrome.** Headline text may be correct now, but small text,
  watermarks, keyboard keys, screen UI, dial gauges, license plates degrade into pseudo-glyphs.
  Severity: **critical** if it's product/UI imagery.
- **A9e — Physically-impossible reflections & continuity.** Mirror/glass/water reflections that
  don't match the subject; patterns (tiles, brickwork, stripes) that drift or re-tile illogically;
  shadow directions inconsistent within one frame. Severity: major.
- **A9f — Style-blend "no-author" aesthetic.** The image is an averaged mush of illustration styles
  with no committed point of view — competent, generic, attributable to no human hand. This is the
  Mission's core target: it looks made by *nobody*. Severity: major (it is the moat-failure even
  when no hard artifact is present).
- **A9g — Watermark ghosts / provenance gaps.** Faint stock/model watermark remnants; no C2PA /
  content-credential metadata where authored work would carry it. Severity: minor (signal, not proof)
  but escalate if the asset is public-facing.

> Rule of thumb (2026): the obvious artifact is gone; **the tell is now the *absence of authored
> specificity*** — perfect, even, styleless competence. Audit for "would a named designer have made
> this exact choice?" If the honest answer is no, it is slop even with zero hard anomalies.

---

## B. Product / interface tells (per feature)

Run against any UI screen or product feature that embeds or surfaces generative AI.
Source: taxonomy category 5 ("feature cramming" / "the AI hammer looking for a nail") and §Product /
interface tells.

| # | Tell | What to look for | Default severity |
|---|---|---|---|
| B1 | **AI where nav/search was faster** | A chat/summary bolted on a flow a search bar or two clicks already solved | major |
| B2 | **Ungrounded chatbot can invent commitments** | No guardrails; bot can state prices, returns, policy, legal, availability it cannot honour | **critical** |
| B3 | **No verifiability / grounding / undo** | Generative output with no source, no citation, no confidence cue, no edit/undo/adjust affordance | major → critical for high-stakes domains |
| B4 | **Decorative "AI" badges & gradients** | Sparkle icon, "AI ✨" label, purple-to-blue gradient used as decoration with no user benefit | major (it is design theatre) |
| B5 | **AI-feature cramming** | Multiple generative features stacked because they're impressive, not because users asked | major |
| B6 | **Hallucination surfaced as fact** | Model output presented with authority and no "may be wrong" framing in a consequential context | **critical** |

---

## C. Severity & disposition (how to close each finding)

| Severity | Definition | Disposition |
|---|---|---|
| **Critical** | Public-facing visual anomaly, warped/misspelled logo, hallucinating bot, impossible anatomy on a brand face | **Remake / replace** (image) or **remove / ground** (feature). Block ship. |
| **Major** | Convergent AI house style, melted detail, decorative AI theatre, "no-author" aesthetic | Remake or art-direct (image); remove or justify with stated user benefit (feature). |
| **Minor** | Provenance gaps, small even-texture issues not at focal point | Note + remediate in next pass; not a ship blocker alone. |

**Remake vs remediate (from SKILL.md):** anomalous AI imagery is **remade or replaced**
(art-directed, real photography/illustration) — *never* spot-patched (you do not "fix" a six-finger
hand, A5, or a styleless render, A9f). Product slop is **removed or grounded**, not redecorated.

**Human-craft alternative (the Mission test):** for every finding, state what a skilled designer
would ship instead — a specific, authored, non-templated choice. A finding is not closed until the
alternative is named.

---

## D. Cross-references

- `doctrine/references/ai-slop-taxonomy.md` — the source taxonomy (categories, the *why*).
- `doctrine/design-doctrine.md` §0 Mission — "the moat is looking human-made."
- Sibling audits: `ai-slop-typography-audit` (type-specific tells, `ai-slop-banned-fonts.md`);
  digital-research engine `anti-ai-slop` (written-copy tells).
- Worked example: `../examples/slop-audit-filled.md`.
