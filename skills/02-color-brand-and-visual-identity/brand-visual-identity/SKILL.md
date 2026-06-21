---
name: brand-visual-identity
description: Use when building, defining, or refreshing a DISTINCTIVE visual identity system for a product, company, or deliverable — logo usage and lockups, the colour+type tie-in, spacing/photography/illustration style, the "voice of the visuals", and a mini style-guide. Routes here whenever the ask is "make this brand recognisable / ownable / not look like every other startup", or when assembling the visual rules that govern a website, app, deck, or document suite. Defers typeface choice to font-selection-and-pairing and palette construction to color-system-and-palette, and ties them into one cohesive, unmistakably-authored identity.
status: active
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Brand Visual Identity
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Defining a new brand's visual identity from scratch: logo, colour, type, imagery, and the
  rules that bind them into one system.
- Refreshing or auditing an existing identity that has drifted into generic "startup sameness"
  — stock gradients, an interchangeable geometric-sans wordmark, swappable hero illustration.
- Producing a mini style-guide / brand sheet that downstream artifacts (site, app, deck, DOCX
  suite) must obey for consistency.
- Deciding logo placement, lockups, clear-space, and minimum sizes for a specific surface.

## Do Not Use When

- The task is only choosing typefaces — use `font-selection-and-pairing` and return here to
  tie the choice into the identity.
- The task is only constructing or correcting a colour palette / contrast — use
  `color-system-and-palette` and return here for the system-level tie-in.
- The task is auditing imagery/UI for generative-AI artefacts (warped logos, uncanny photos) —
  run `skills/03-web-and-ui-design/visual-product-slop-audit` first, then design the
  replacement here.
- A binding client brand guideline already exists — follow it, record it, and apply only the
  consistency gate.

## Required Inputs

- Who the brand is *for* and *against*: audience, the category it competes in, and the two or
  three competitors it must NOT be confused with. Distinctiveness is relative; you cannot be
  ownable without naming the field you stand apart from (Neumeier, *The Brand Gap* — "a brand
  is not what *you* say it is, it's what *they* say it is"; differentiation is the first job).
- One-word brand essence and 3–5 adjectives (e.g. "austere, precise, warm") that every visual
  decision is tested against.
- The surface set the identity must survive: favicon → billboard, light/dark, print/screen,
  embroidered/single-colour.
- Any existing assets, and whether a logo already exists or must be commissioned/designed.

## Workflow

1. **Fix the strategy before any mark.** Write the one-word essence and the adjective set, and
   the "not-to-be-confused-with" list. Every later choice is justified against these — this is
   the human-authority anchor that stops the identity converging on the category mean
   (doctrine Mission: *the moat is looking human-made*; `doctrine/design-doctrine.md` §0).

2. **Logo / wordmark — make it ownable, not generated.**
   - Prefer a **wordmark or monogram built from real, correct letterforms** over an abstract
     blob. If a custom mark is drawn, it must be drawn deliberately — Paul Rand's discipline:
     the mark earns meaning through use, so it must be *simple, distinctive, and reproducible*
     at any size, in one colour, and from memory.
   - **Never ship an AI-generated mark.** Generative marks carry the slop tells — warped or
     misspelled letterforms, fused glyphs, melted detail, near-symmetry that reads as "off"
     (`doctrine/references/ai-slop-taxonomy.md` §Visual tells; category 2, "misspelled logos /
     uncanny promo art" is the highest public-backlash risk for a brand).
   - Specify the system, not one image: primary lockup, secondary/stacked lockup, monogram,
     clear-space (defined in units of the mark itself), and **minimum legible size** verified at
     the favicon end. Vignelli's discipline applies: a small, governed set of elements used
     consistently, not a sprawl of one-off variants.

3. **Tie in colour.** Do the palette work in `color-system-and-palette`, then bind it: assign
   roles (brand / ink / surface / accent / state), and choose **one** signature colour the
   brand can own — not a purple→blue gradient, which is the single most recognisable identity
   slop signal (doctrine §2). State why this colour fits the essence.

4. **Tie in type.** Do the pairing in `font-selection-and-pairing`, then bind it: the display
   face is part of the *identity's voice*, not just headings. Record where the wordmark's
   letterforms and the running type agree or deliberately contrast (a wordmark may be custom
   while body uses the paired body face — say so).

5. **Define the supporting visual language** — these are what separate an authored identity
   from a template:
   - **Spacing & geometry:** a consistent spacing rhythm and corner/edge language (sharp vs
     soft) applied everywhere. Cross-ref `skills/05-layout-grid-and-data-viz` for the grid.
   - **Photography style:** state the rules — framing, colour grade, subject treatment, whether
     people are real. **Reject uncanny / waxy / impossible-physics AI imagery** as brand
     content (`ai-slop-taxonomy.md` §1–2).
   - **Illustration / iconography style:** one coherent system (line weight, corner radius,
     perspective) — not a marketplace of mismatched stock icons.
   - **Motion (if any):** one or two signature behaviours, not decoration.

6. **Write the voice-of-the-visuals.** One short paragraph + a do/don't pair that tells any
   future contributor *how the brand behaves visually* — the gap Neumeier names between strategy
   and execution. This is the rule a templating tool can never infer.

7. **Produce the mini style-guide deliverable** (see Outputs) and run the **Consistency Gate**.
   Structure the system against `references/identity-system-spec.md`; for a complete worked
   instance, see `examples/identity-mini-guide.md`.

## The Consistency Gate (quality gate — run before sign-off)

A distinctive identity that is applied inconsistently reads as accidental, not authored.
The full checklist lives in `references/brand-consistency-gate.md` (this folder); the summary:

1. Logo: correct lockup, clear-space, and minimum size on every surface; single-colour and
   dark-mode variants exist and are legible.
2. Colour: roles honoured; the signature colour is actually carried through; no off-system
   gradient or stray accent crept in.
3. Type: the identity pairing is used; no slop "escape" font substituted downstream.
4. Imagery: every photo/illustration passes the AI-slop visual checklist
   (`doctrine/references/ai-slop-taxonomy.md`) — reject and remake any that don't.
5. The result passes the **memory test**: could someone redraw the essence of this identity
   after looking away? If not, it is not yet ownable — sharpen one element.

If any item fails, fix before sign-off — do not ship a half-applied system.

## Anti-Patterns

- **Stock-gradient logo / "AI badge" aesthetic** used as identity instead of a real mark.
- **AI-generated wordmarks** with warped, fused, or misspelled letterforms.
- **Interchangeable startup sameness:** geometric-sans wordmark + purple-blue gradient +
  generic 3D-blob hero — swap the name and nothing changes. That is the convergent mean the
  doctrine exists to defeat.
- Designing a logo with no system around it (no clear-space, no min size, no mono variant).
- Citing an AI tool's "brand suggestions" as authority. Approvals trace **only** to human design
  authority; an AI's own picks are exactly what the next wave converges on (doctrine §2,
  sourcing-authority asymmetry).
- Five hedged "safe" choices instead of one strong, defensible one (doctrine §0).

## Outputs

A **mini style-guide** (one to three pages) containing:
- Brand essence + adjective set + the not-to-be-confused-with list.
- Logo: lockups, clear-space, minimum size, colour/mono/dark variants, misuse examples.
- Colour roles + signature colour (deferring construction to `color-system-and-palette`).
- Type roles (deferring selection to `font-selection-and-pairing`).
- Photography / illustration / iconography style rules.
- The voice-of-the-visuals paragraph + one do/don't pair.
- A completed Consistency Gate checklist.

## Examples

- `examples/identity-mini-guide.md` — a full worked mini brand identity ("Sonda"): strategy,
  logo system, colour tie-in, type tie-in, supporting visual language, voice-of-the-visuals,
  an applied one-screen style-guide, and a filled Consistency Gate. Mirror its shape, not its
  values.

## References

- `references/identity-system-spec.md` (this folder) — the canonical structure every layer of
  the identity system must fill; read it before producing the mini style-guide.
- `references/brand-consistency-gate.md` (this folder) — the sign-off checklist run in step 7.
- `references/trust-architecture-checklist.md` (this folder) — when the brand surfaces must
  carry proof/legitimacy (legal, consulting, healthcare, financial, high-stakes sectors).
- `doctrine/design-doctrine.md` — Mission (§0, the moat is looking human-made), the Anti-Slop
  Charter (§2), and the sourcing-authority asymmetry rule (human design authority only).
- `doctrine/references/ai-slop-taxonomy.md` — corporate/advertising slop (misspelled logos,
  uncanny assets) and the visual tells checklist.
- Sibling skills: `../color-system-and-palette` (palette construction & contrast) and
  `../../01-typography-and-fonts/font-selection-and-pairing` (typeface selection & pairing);
  `../../05-layout-grid-and-data-viz` (grid/spacing); `../../03-web-and-ui-design/visual-product-slop-audit`.
- Human design authority grounding the approach: Paul Rand (a mark is simple, distinctive,
  reproducible, and earns meaning through use); Massimo Vignelli (discipline — a small governed
  set of elements, used consistently); Marty Neumeier, *The Brand Gap* (differentiation first;
  a brand is what *they* say it is). **No AI-tool recommendation is cited as authority.**
<!-- dual-compat-end -->
