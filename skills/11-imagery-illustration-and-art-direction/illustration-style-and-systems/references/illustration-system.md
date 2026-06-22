# Reference: The Illustration System

Illustration is the most **ownable** imagery a brand has, and therefore the most-faked. Treat it
the way the engine treats type and icons: a constructed system with stated rules, not clip-art
commissioned one frame at a time. The test of the whole system is simple — **crop the logo off;
would a viewer still recognise the work as yours?** If not, you have competence without a
signature, which this engine classes as slop (`doctrine/design-doctrine.md` §0/§2).

This reference is the canonical rule-set the skill cites. Numbers are illustrative defaults; the
point is that *you state concrete values*, never adjectives alone.

---

## 1. The five style attributes (state each concretely, before drawing)

Per the anti-slop non-negotiable #1 (`doctrine/design-doctrine.md` §2), name the choice first.
Every drawing in the set must obey all five. "Friendly and modern" is not a spec; the following is.

| Attribute | What to decide (concretely) | Example statement |
|---|---|---|
| **Line** | Present/absent. If present: weight (px at base size), uniform vs variable/tapered, terminal (round/butt), join (round/miter), and **clean-geometric vs hand-wobble**. Whether outline colour is fixed (e.g. near-black) or tinted per fill. | *"2.5px variable-weight line, round terminals, slight hand-wobble, outline = ink-900, never pure black."* |
| **Shape** | Geometric vs organic; corner-radius language; the **primitive set** forms are built from; fill style (flat / two-tone shaded / textured / gradient within a defined ramp). | *"Organic rounded forms built from 3 primitives (pill, leaf, disc); flat fill + one offset shadow tone; 6px min corner."* |
| **Colour** | A **constrained ramp** drawn from the brand palette — how many tints, the light/shadow logic, accent rule. Never the full rainbow; never default flat-vector primaries. | *"5-step ramp from the brand teal + 1 warm accent; shadow = same hue −20% L; one accent used ≤10% of any frame."* |
| **Perspective / space** | **Pick one and hold it across the whole set**: flat front-on, fixed isometric (state the angle, e.g. 30°), or naive layered depth. Mixed perspective is an instant "assembled" tell. | *"Flat front-on only; depth implied by overlap + the single shadow tone, never by isometric."* |
| **Texture / finish** | clean-vector / grain / halftone / paper / brush. **The finish is often where the ownable signature lives.** State the grain spec or that it is clean. | *"Light 8% film-grain overlay on fills only, not on line; gives a printed-not-rendered feel."* |

Write these as one paragraph before production. If you can't, you're not ready to draw.

---

## 2. The ownable motif (the one signature move)

The doctrine prefers the choice "a templating tool would never have produced" (§0). Generic flat
vector has **no** motif — which is exactly why it converges to slop. Pick **one** strong,
repeatable, distinctive move and apply it everywhere; restraint plus one move beats five hedged
choices. Candidates:

- A **signature line treatment** — a consistent imperfect wobble, an open-terminal gap, a
  double-line, a single-weight-break rule.
- A **recurring shape grammar** — every form resolves to the same 2–3 primitives; a repeated motif
  shape (e.g. a specific leaf, arc, or notch) seeded into many frames.
- A **single accent texture** — one grain/halftone/paper finish that no clean-vector competitor has.
- A **consistent broken-grid / off-axis composition** — a recurring compositional tic.
- A **character of light** — one fixed light direction and one shadow tone used as identity.

Document the motif and show it recurring in ≥3 frames. The motif is what survives the logo crop.

---

## 3. Spot vs scene, and the density ladder

- **Spot art** — small inline illustrations (empty states, feature tiles, onboarding steps, error
  pages, list items). Reductive: **one idea per spot**, low detail density, must read at thumbnail
  size. Often a single character or object on a plain ground.
- **Scene art** — larger hero/editorial compositions. Carries narrative: multiple characters,
  environment, depth, the full texture.

They **share DNA** (identical line/shape/colour/perspective/finish attributes) but **scale detail
with size** via a stated **density ladder** — what drops out as the illustration shrinks:

| Size band | Background | Texture/grain | Characters | Detail |
|---|---|---|---|---|
| Spot ≤120px | none / single shape | dropped | ≤1 | silhouette-clear only |
| Inline 200–480px | simple ground | optional | 1–2 | medium |
| Hero / scene full-bleed | full environment | full | 2–5 | full, with foreground/background layers |

The ladder is what keeps a spot from being a muddy shrink of the hero (the illustration cousin of
the naive-icon-downscale smell).

---

## 4. Character / object construction rules

So any illustrator extends the set **on-model**:

- **Proportion system** — head-to-body ratio (e.g. 1:6 realistic, 1:4 friendly-stylised — but
  **never** the corporate-Memphis tiny-head/giant-limbs caricature), and hand/foot treatment
  (simplified mitten, articulated, or implied).
- **Anatomy / joint logic** — how limbs bend and connect (consistent elbow/knee logic, no noodle
  arms), and whether figures **have faces** and what the face language is (dot eyes + minimal
  mouth, full features, etc.) — stated and uniform.
- **Diversity with dignity** — depict **real human variation** in skin, body, age, ability, dress.
  Do **not** use the faceless-everyone dodge; removing identity to "be inclusive" is the
  corporate-Memphis cop-out, not inclusion. Show people as specific and real.
- **Objects from the same primitives** — inanimate objects are built from the *same* primitive set,
  line weight, and finish as the characters, so a phone and a person clearly come from one hand.

---

## 5. The consistency kit (build, don't improvise)

Audit the whole inventory **side by side** before refining any single frame — one line weight, one
shape language, one perspective, one colour ramp, one finish. Then build a small reusable kit:

- **Characters** — a cast drawn on-model, reusable across frames.
- **Objects** — common props (phone, box, chart, plant) on-system.
- **Backgrounds / grounds** — a few reusable environment layers.
- **Accent shapes / motif elements** — the signature motif as drop-in pieces.

New illustrations are **assembled from the kit on-system**, not improvised from scratch. This is
what stops a growing set from drifting into the mixed-marketplace look.

---

## 6. Illustration vs photography (the decision rubric)

Cross-check `photography-art-direction`. State the call **per surface** in the spec.

**Illustration wins when:**
- The idea is **abstract/conceptual** with no literal subject (privacy, automation, "how it
  works", security, data flow).
- You need **schematic explanation** — showing a process or relationship clearly.
- The tone is **playful, editorial, or craft-forward**, or you want warmth without literal people.
- You want to **own a look** photography cannot give — a signature drawn language no stock matches.
- You want to **avoid the cost and cliché of stock people** on a non-truth surface.

**Photography wins when:**
- The surface makes a **truth claim** — real people, real places, real product, real results.
- It is a **credibility/trust** surface where "is this real?" is the user's question.
- Authenticity and specificity matter more than interpretation.

**Never** illustrate a truth claim (drawing "happy customers" instead of showing them misleads);
**never** use raw stock where a signature illustration would own the look better.

---

## 7. AI-assisted illustration (gated, never the default author)

AI may assist **only**: (a) toward a *defined* system, (b) on surfaces that permit it (never
truth/people surfaces), (c) when a human re-draws/cleans the output onto the motif.

- The **sourcing-authority asymmetry rule** (`doctrine/design-doctrine.md` §2): an AI tool's *own*
  default illustration style is the corporate-Memphis ocean it was trained on. It is **never** the
  authority for the look — it is the convergent mean we art-direct **away** from. Use AI as a
  rendering hand inside *your* stated system, not as the style-setter.
- **Prompt** the stated attributes + motif explicitly; **negative-constrain** the slop tells.
- **Reject gate** (`doctrine/references/ai-slop-taxonomy.md` §Visual tells): melted/incoherent
  detail, gibberish/illegible text baked in, warped or misspelled logos, anatomically impossible
  hands (six fingers, fused limbs), mismatched lighting, and — specific to illustration — the
  default blob-people regurgitation. Anything that fails is redrawn or rejected, never shipped
  "because it's close." This is the highest public-backlash risk (taxonomy §2, "shovelware assets").

---

## 8. Accessibility & export

- **Alt text** conveys the illustration's *point*, not "an illustration"; decorative → empty alt.
- **Never colour-alone** for meaning (WCAG 2.2 **1.4.1**) — pair with shape/label.
- **Text over illustration** must meet contrast (`doctrine/references/wcag-2.2-criteria.md`); keep a
  deliberate quiet zone or scrim under overlaid text.
- **Ship as optimised SVG** where the work stays vector — small weight, infinite scale, themeable
  via `currentColor`/CSS variables; strip editor cruft and normalise the viewBox. Rasterise (AVIF/
  WebP) only complex textured scenes, and keep weight inside the LCP budget
  (`doctrine/references/web-performance-budgets-2026.md`).

---

## Provenance

Derived from the Chwezi Design Doctrine (Mission §0, Anti-Slop Charter §2) and the AI-slop
taxonomy. Paired with `photography-art-direction` (when to photograph) and
`iconography-system-design` (the reductive functional cousin). Numbers are illustrative defaults;
the binding rule is that concrete values are *stated*, and the corporate-Memphis default is
*refused*.
