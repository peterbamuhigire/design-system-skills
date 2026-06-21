---
name: color-system-and-palette
description: Use when choosing colours or building a colour system for ANY artifact — a website or landing page, an app/web UI, a dashboard, a DOCX/PPTX/PDF deck or report, or a brand identity. Selects a deliberate, non-slop palette anchored in a real brand or concept, derives tonal ramps and semantic roles, gates every pair on WCAG contrast, and remaps deliberately for dark mode. This is the default entry skill for colour in the design engine.
status: active
metadata:
  portable: true
  category: 04-color-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Color System And Palette
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- About to choose colours or theme any artifact: website/landing page, app or web UI,
  dashboard, DOCX/PPTX/PDF report or deck, or a new brand identity.
- A colour decision is needed and the work risks defaulting to the AI-slop look
  (indigo/purple→blue gradients, the stock Tailwind palette, glassmorphism, neon-on-dark).
- Reviewing or refreshing an existing artifact's colours, or adding a dark mode.

## Do Not Use When

- A binding client brand guideline already mandates exact colours — follow it, record the
  hexes and roles, and skip selection (but still run the contrast gate and the dark-mode remap).
- The task is only typography — use `01-typography-and-fonts/font-selection-and-pairing`.
- The task is chart/data-viz colour encoding specifically — start here for the base palette,
  then hand the categorical/sequential scales to `05-layout-grid-and-data-viz`.

## Required Inputs

- Artifact type and medium (web / UI / DOCX / PPTX / PDF), and whether dark mode is required.
- A real anchor: the brand, product, place, material, or concept the palette must express
  (e.g. a logo colour, a physical material, a regional or sector reference) — not a vibe word.
- The audience/context register (editorial-authoritative, developer-technical, startup-product)
  and the smallest text size and thinnest UI stroke the colours must survive.

## Workflow

1. **Find a real anchor before picking any hex.** Derive the palette from something that
   actually exists — a brand mark, a product material, a place, a printed reference, a named
   designer's or artist's work. State the anchor and the primary hue *before* generating the
   artifact, exactly as typography states the typeface first (per the Mission in
   `doctrine/design-doctrine.md` §0 and the Anti-Slop Charter §2.1). A palette with no anchor
   is how slop happens.

2. **Reject the convergent defaults explicitly.** Do not ship the indigo/violet→blue gradient,
   the unedited Tailwind default scale, frosted-glass panels as the identity, or neon accents
   on near-black. These are the colour equivalent of opening in Inter — see
   `doctrine/references/ai-slop-taxonomy.md`. If the anchor genuinely lands near one of these,
   shift hue, desaturate, or warm/cool it until it no longer reads as the stock look, and say so.

3. **Build the ramp by perceptual steps, not by lightening toward white.** Take the anchor hue
   and generate a tonal ramp (roughly 50–900) where each step is an even *perceptual* lightness
   move, holding or subtly rotating hue and adjusting chroma so mid-tones don't go muddy and
   light tints don't go chalky. This is Albers' lesson in *Interaction of Color* — a colour is
   judged by its neighbours, so tune the ramp in context, not in isolation. Itten's contrast
   types (hue, light–dark, saturation, warm–cool) name the levers; pick the one the artifact
   needs. Prefer a perceptually-uniform space (OKLCH / CIELAB) over naive HSL, whose "equal"
   steps are perceptually uneven.

4. **Assign semantic roles, not raw hexes.** Map ramp positions to roles: `surface` (and
   raised/sunken surfaces), `text` (primary + muted), `border`, `accent` (the brand voice),
   and the status set `success / warning / error / info`. Components reference roles, never
   literal colours, so the system can be retuned or remapped in one place.

5. **Hold the 60-30-10 distribution.** ~60% a quiet dominant (usually surface), ~30% a
   secondary, ~10% the accent that carries the brand. The accent earns its scarcity — colour
   everywhere is colour nowhere. One confident accent beats a rainbow of hedged ones (Mission §0).

6. **Gate every foreground/background pair on WCAG — this is a hard gate, not advice.**
   Body and small text ≥ **4.5:1**; large text (≥24px, or ≥18.66px bold) and meaningful UI
   components/icons/focus rings ≥ **3:1** (WCAG 2.x 1.4.3 / 1.4.11). Any pair that fails is
   rejected and the ramp step is retuned until it passes — no exceptions for "it looks fine."

7. **Never put pure black on white, or pure white on a saturated field.** `#000` on `#fff`
   over-contrasts and vibrates (haloing/eye strain); use a near-black with a trace of the brand
   hue (e.g. a very dark desaturated version of the anchor). Likewise prefer a near-white,
   slightly warm or cool surface over `#fff`. This is perceptual colour science, not taste.

8. **Make dark mode a deliberate remap, not an inversion.** Do not invert lightness. Dark
   surfaces want *lower* chroma and a near-dark grey carrying the brand hue (not `#000`);
   accents usually need to be *lightened and slightly desaturated* to stay legible and keep the
   same semantic meaning at 3:1/4.5:1. Re-run the contrast gate (step 6) for the dark roles
   independently — passing in light mode does not imply passing in dark.

9. **State the system and hand off.** Output the named roles, the ramp, the distribution rule,
   and the recorded contrast results. Hand categorical/sequential data scales to
   `05-layout-grid-and-data-viz`.

## Anti-Patterns

- The indigo/purple→blue hero gradient, glassmorphism-as-identity, or neon-on-near-black.
- Shipping the default Tailwind palette (or any tool's stock swatches) unedited.
- Justifying a colour because "an AI tool / generator recommends it" — AI picks are evidence of
  what to *avoid*, never authority for what to use (`doctrine/design-doctrine.md` §2, the
  sourcing-authority asymmetry rule). Authority traces to human colour science and named
  designers — Albers, Itten, foundry/brand systems — not to a model's convergent default.
- `#000` on `#fff`; eyeballing contrast instead of measuring it; treating 4.5:1 as a target
  to barely clear rather than a floor.
- Dark mode by lightness inversion, with full-chroma accents and `#000` surfaces.
- A different literal hex sprinkled per component instead of a small set of semantic roles.

## Outputs

- A stated colour decision (anchor + primary hue + reason), the tonal ramp, the semantic role
  map, the 60-30-10 distribution, recorded WCAG results for light and dark, and a clean handoff
  to data-viz colour.

## References

- `doctrine/design-doctrine.md` — Mission §0 (the moat is looking human-made; authored over
  convergent), Anti-Slop Charter §2 (state the choice first; the sourcing-authority asymmetry
  rule).
- `doctrine/references/ai-slop-taxonomy.md` — the convergent-default tells to reject.
- Human authority (not citable in-repo, named for provenance): Josef Albers, *Interaction of
  Color*; Johannes Itten, *The Art of Color* (the seven colour contrasts); WCAG 2.x success
  criteria 1.4.3 and 1.4.11.
<!-- dual-compat-end -->
