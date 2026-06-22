---
name: distinctive-by-design
description: Use BEFORE building any UI, website, landing page, app screen, dashboard, pitch deck, or rendered artifact — the pre-flight discipline that makes the work look like the product of highly skilled human hands rather than an AI or template default. Forces ONE committed distinctive idea (a signature typeface, an unexpected layout, a custom motif, a real photographic/illustrative point of view), real weight/size/space extremes, intentional asymmetry and a clear focal point, and craft details (custom bullets, considered empty states, micro-interactions, real content). Forbids the convergent defaults — Inter/Geist, indigo gradients, glassmorphism, uniform card grids, centered-everything, decorative AI badges — and forbids justifying any choice by "an AI tool recommends it." Run this first; it gates the build.
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
    - claude-code
    - codex
---

# Distinctive By Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

> The engine's soul skill. The Mission is blunt: *the moat is looking human-made.* Sameness is
> free and worthless; deliberate, crafted distinctiveness is what sells. This skill is the
> master designer's pre-flight — the moves you make **before** the first line of markup so the
> finished thing could not have fallen out of a template.

<!-- dual-compat-start -->
## Use When

- You are about to build, theme, or restyle **any** rendered surface: a website, landing page,
  web/app UI screen, dashboard, marketing page, or a slide/document with a visual identity.
- A new project is starting and the "default look" hasn't been decided — the moment of maximum
  leverage, before the convergent mean sets in.
- You catch yourself reaching for the safe, generic version "just to get something on screen."
- A draft already exists but reads as templated and you need to author a real point of view into it.

## Do Not Use When

- The task is *auditing* an already-built artifact for slop tells — use
  `visual-product-slop-audit` (this skill is the proactive twin; that one is the retrospective).
- The only decision in front of you is the typeface pairing — go straight to
  `01-typography-and-fonts/font-selection-and-pairing` (then return here to set the layout idea).
- A binding client brand system already dictates type, colour, and layout — honour it, record
  it, and apply only the craft-detail and focal-point steps that don't conflict.

## Required Inputs

- **Artifact + context + audience.** What is it, who reads it, and what is the one feeling it
  should leave? ("authoritative editorial," "developer tool that respects my time," "a product
  that feels confident and a little daring.")
- **The real content.** At least the genuine headline, the genuine first paragraph, and the
  genuine primary action. You cannot design distinctiveness around lorem ipsum — placeholder
  text produces placeholder design.
- **One reference of human authority** you will pair against (a foundry specimen, a named
  designer's system, a page from the design literature) — never an AI tool's recommendation.

## The Discipline (Workflow)

### 1. Commit to ONE strong distinctive idea — then subordinate everything to it
Pick a single organising decision and let it govern the whole artifact. Exactly one of:

- **A signature typeface** carrying the personality (display face that *means* something here),
  paired per `doctrine/references/pairing-principles.md` — cross categories, contrast weight
  extremes, match x-heights, never one font for everything.
- **An unexpected layout** — break the symmetric centre. An off-centre hero, a deliberate
  diagonal, an asymmetric two-column split where the content column is the *narrow* one, a grid
  the eye can't predict.
- **A custom motif** — a repeating shape, rule, marker, or graphic device that recurs and
  becomes the artifact's fingerprint (a hand-considered divider, a bracket system, a numbering
  style).
- **A real photographic or illustrative point of view** — one consistent, authored image
  language with a stated rule, never stock-grab + AI-fill collage. (Reject every visual tell in
  `doctrine/references/ai-slop-taxonomy.md`: waxy skin, melted backgrounds, gibberish signage,
  warped logos, uncanny faces.)

Restraint plus this one strong choice beats five hedged safe ones. The doctrine is explicit:
when two options are equally clean, prefer the one that looks *authored*.

### 2. Use real extremes — weight, size, space
Timidity is the slop signature. The mid-weight, near-uniform, evenly-padded page reads as
machine-default.

- **Weight:** push extremes — 100/200 against 800/900, never 400 against 600
  (`doctrine/references/pairing-principles.md` §5).
- **Size:** make hierarchy *obvious*. A real jump from heading to body (ratio ≥ 1.25, often far
  more for a hero), not three sizes that are almost the same.
- **Space:** let one thing breathe and pack another. Generous, intentional whitespace around the
  focal point; deliberate density where it earns attention. Uniform padding everywhere is a tell.

### 3. Compose tension — asymmetry, a focal point, a path for the eye
- Establish **one** clear focal point. If everything shouts, nothing is heard.
- Introduce **intentional asymmetry** — balance by weight and contrast, not by centring
  everything. Vignelli's grids are rigorous *because* they place tension deliberately, not
  because they centre by default (`doctrine/references/pairing-principles.md` sources: Vignelli).
- Give the eye a **path**: where it lands, where it goes second, where the action sits. Design
  the sequence, don't leave it to a default flow.

### 4. Add the craft details that only a human bothers with
These are the fingerprints of skilled hands. Do at least three:

- **Custom bullets / markers** — not the browser disc; a considered glyph, rule, or numbered
  system tied to the motif.
- **Considered empty, loading, and error states** — real copy, in voice, not "No data."
- **Micro-interactions** with intent — a hover, a focus ring, a transition that has a reason and
  a consistent easing/duration (route motion through `08-motion-and-interaction/motion-design`).
- **Real content, never lorem** — genuine headlines, genuine labels, genuine numbers.
- **Optical adjustments** — align to the eye, not the bounding box; correct the gaps the machine
  leaves equal but the eye reads as unequal.

### 5. State your ONE distinctive decision and WHY — before building
Write it down, out loud, before any markup:

> **"This artifact's distinctive decision is ___, because ___ (tied to THIS context/audience),
> grounded in ___ (named human design authority)."**

The *why* must trace to human design authority — a foundry, a named designer, the design
literature (Bonneville, Vignelli, Segall; `doctrine/references/pairing-principles.md`).
**The asymmetry rule is absolute:** you may never justify a choice with "an AI tool recommends
it." An AI tool's picks are exactly what the next wave of AI output converges on — adopting them
launders slop one step removed. AI-vendor sources are admissible **only as evidence of what to
avoid** (`doctrine/design-doctrine.md` §2). If a human-justified choice happens to coincide with
an AI recommend-list, note the convergence risk — never treat the AI nod as endorsement.

### 6. Run the human-craft signature checklist, then build
Only after every box is checked do you write markup.

## Human-Craft Signature Checklist (run every time, before building)

1. **One distinctive idea named and committed** — signature type / unexpected layout / custom
   motif / authored image POV — not a hedge of several half-decisions.
2. **Decision stated with a contextual reason**, grounded in **named human design authority**;
   zero reliance on "an AI tool suggests it."
3. **Real weight extremes** (100/200 vs 800/900), **real size jumps**, **intentional space** —
   no timid mid-weights, no near-uniform sizes, no uniform padding.
4. **Intentional asymmetry and a single clear focal point** with a designed eye-path — not
   centred-everything, not an even card grid.
5. **At least three craft details present** — custom markers, considered empty/error states,
   purposeful micro-interactions, optical alignment.
6. **Real content throughout** — no lorem ipsum, no "No data," no placeholder labels.
7. **No convergent default present** (see Anti-Patterns) — type, colour, layout, and badges all
   pass.
8. **No slop visual tell** from `doctrine/references/ai-slop-taxonomy.md` in any image or icon.

If any item cannot be satisfied (no real content yet, no authority to cite, no time to author a
real choice), **say so and ask** — never silently ship the convergent default.

## Anti-Patterns (the convergent defaults to push away from)

- **Type:** Inter, Geist, Roboto, or the "safe distinctive" escapes (Poppins, Montserrat,
  Space Grotesk) reached for reflexively; one font for headings, body, labels, and buttons.
- **Colour:** the indigo / purple-to-blue gradient, the same teal-on-dark SaaS palette, neon-on-
  near-black as a personality substitute.
- **Surface:** glassmorphism, frosted blur panels, and soft drop-shadows used as decoration with
  no information purpose.
- **Layout:** uniform rounded card grids, everything centred, hero-with-two-buttons, the
  three-feature-icon row — symmetry as a default rather than a choice.
- **"AI" theatre:** sparkle/AI badges, gradients, and chatbot bolt-ons used as decoration with no
  user benefit (`doctrine/references/ai-slop-taxonomy.md` §Product/interface tells).
- **Process:** designing around lorem ipsum; picking a look "to start" and never stating it;
  justifying any choice by an AI tool's recommendation (forbidden by the asymmetry rule).
- **Timidity:** hedging five safe choices instead of committing one strong one; mid-weights and
  near-identical sizes that erase hierarchy.

## Outputs

- A written **one-line distinctive-decision statement** (what + why + human authority), produced
  *before* any markup.
- A completed **human-craft signature checklist**.
- A clear handoff to the build with the focal point, asymmetry, type pairing, motif/image rule,
  and the three+ craft details specified — so what gets built is authored, not defaulted.

## Examples

- `examples/before-after-distinctive.md` — one real screen (the *Cadence* SaaS landing hero)
  taken from the convergent AI-slop default (Inter everywhere, indigo→blue gradient, centred
  uniform card grid, ✨ AI badge) to an authored version built on **one stated distinctive
  decision + why** (an asymmetric editorial split hero that shows the draft writing itself, set
  in Bricolage Grotesque, grounded in Vignelli), with the full human-craft signature checklist
  run against it. Read it to see the discipline applied end to end.

## References

- `doctrine/design-doctrine.md` — the Mission ("the moat is looking human-made"), the five
  non-negotiables, and the sourcing-authority asymmetry rule (§2).
- `doctrine/references/ai-slop-taxonomy.md` — the visual, product, and interface slop tells to
  push away from.
- `doctrine/references/pairing-principles.md` — the human design authority (Bonneville,
  Vignelli, Segall) grounding type, weight extremes, contrast, and deliberate composition.
- Sibling skills: `01-typography-and-fonts/font-selection-and-pairing` (the type decision),
  `00-cross-cutting-ops-qa-a11y/visual-product-slop-audit` (the retrospective twin),
  `08-motion-and-interaction/motion-design` (purposeful micro-interactions).
<!-- dual-compat-end -->
