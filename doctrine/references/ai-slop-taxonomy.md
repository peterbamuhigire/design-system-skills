# Reference: The AI-Slop Taxonomy (what we are fighting)

"AI slop" is a recognised category of **digital waste**: low-effort, mass-produced AI content
deployed at scale to extract clicks, cash, or attention by prioritising **volume over
substance**. Unlike disinformation, its motive is usually extraction, not deception. This engine
exists to keep Chwezi products on the *opposite* side of this line — see the doctrine Mission
("the moat is looking human-made").

This reference scopes the taxonomy to the parts the **design engine** owns (visual, product,
interface). The **textual** tells (preambles, buzzword salad, vague attribution) are a *writing*
concern owned by the `digital-research-engine` (`anti-ai-slop` / `ai-slop-audit`) — cross-cite,
don't duplicate.

---

## The 5 categories (design-relevant emphasis in **bold**)

1. **Social-media slop** — engagement-bait & "brainrot": hyper-surreal emotionally-manipulative
   imagery (the "Shrimp Jesus" genre), automated looping AI visuals with robotic voiceover.
   *Design relevance:* never ship kitsch, uncanny, or manipulative AI imagery as brand content.
2. **Corporate & advertising slop ("shovelware assets")** — unpolished generative assets in
   public marketing: **misspelled logos, mismatched/uncanny promo art, deformed key-art
   thumbnails** (e.g. 19 smudged faces on a *12 Angry Men* tile). *Highest design risk for
   Chwezi* — this is the failure that triggers public backlash.
3. **Submission slop** — mass-generated books/papers/applications flooding gatekeepers
   (LLM prompt left in the text; scrambled pseudonyms). *Mostly a content concern → research
   engine.*
4. **Slop news / programmatic-SEO "pink slime"** — text for bots not humans; semantic
   hollowness. *Content concern → research engine; design only ensures the page doesn't look
   templated.*
5. **Product & interface slop ("feature cramming")** — forcing generative AI into UIs where it
   hurts UX. **The "AI hammer looking for a nail"** (a chatbot where a search bar was faster);
   hallucinating support bots inventing policies. *Squarely the design engine's job — see the
   audit skill.*

---

## Visual & video tells (the audit checklist)

If any of these appear, the asset is slop — reject or remake:

- **Waxy / hyper-glossy skin**, plasticky textures.
- **Melted or incoherent background detail**; objects that dissolve into each other.
- **Illegible text / gibberish signage** baked into the image.
- **Floating objects**, impossible shadows, broken physics.
- **Anatomically impossible features** — extra fingers/limbs, missing joints, fused hands.
- **Misspelled or warped logos / brand marks.**
- **Uncanny faces** — dead eyes, asymmetry that reads as "off," too-smooth symmetry.
- **Mismatched lighting** across a composite that should be one scene.

## Product / interface tells

- An AI feature (summary, chat) inserted where **standard navigation or search was faster**.
- A chatbot deployed without guardrails that can **invent commitments** (returns, prices, legal).
- Generative output surfaced **without verifiability, grounding, or an undo/adjust affordance**.
- "AI" badges and gradients used as decoration with no real user benefit.

## Why slop floods everything (so we resist the pull)

The cost of generation has dropped to near-zero, so quality gatekeepers collapse and programmatic
ad networks reward pure volume. The economic gravity is *toward* slop. Chwezi's deliberate
counter-position — crafted, distinctive, human-looking work — is precisely what becomes scarce
and therefore valuable.

---

## Counter-doctrinal "best practices" — taught by the literature, REJECTED here

The UI/UX book canon (see `docs/book-study/`) contains advice that was once standard but
contradicts this engine's doctrine. Skills must **not** adopt these even though respected books
teach them — inoculate against them explicitly:

- **Glassmorphism as a default surface treatment** (taught by *Fundamentals of Creating a Great
  UI/UX*). It is a convergent AI-slop tell (see the taxonomy above) and usually fails contrast.
  Use deliberate, legible surfaces; reserve translucency for genuine platform materials (iOS
  Liquid Glass *chrome only*), never as decoration.
- **Fixed red/green or red/blue colour semantics + shadow-only dark-mode elevation** (taught by
  *Mobile Design Pattern Gallery*). We use **OKLCH semantic roles** and **lightness-based**
  elevation in dark mode (see `dark-mode-and-theming`), and **never colour-alone** signalling
  (WCAG 1.4.1) — always pair colour with icon/shape/text.
- **`ease-*-back` / bouncy overshoot interpolators** (taught by *App Design Apprentice*). These
  contradict `motion-design`'s **damping-ratio ζ ≥ 0.7 (no bounce)** rule. Use spring physics in
  the no-bounce band; honour `prefers-reduced-motion`.
- **Hover-reveal / hover-as-primary-invitation and drag-as-hero interactions** (taught by
  *Designing Web Interfaces*, 2009). Desktop-only; they have **no touch equivalent**. Provide a
  visible, tap-operable affordance first; hover is an enhancement, never the only path.

If a skill's source material recommends one of the above, it must state the rejection and the
doctrine-correct alternative.

---

## How the engine uses this

- The **`visual-product-slop-audit`** skill (`skills/00-cross-cutting-ops-qa-a11y/`) runs these
  checklists against imagery, UI, and product features.
- The **`ai-slop-typography-audit`** skill covers the type-specific tells
  (`ai-slop-banned-fonts.md`).
- Together with the Mission and the banned-font list, this is the engine's definition of "what
  we must never ship."
