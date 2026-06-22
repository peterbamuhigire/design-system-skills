---
name: logo-and-wordmark-design
description: Use when designing, drawing, or specifying the actual LOGO and WORDMARK as a buildable system — mark construction on a geometry/grid, custom lettering or wordmark cuts, lockups (primary/stacked/horizontal/monogram), clear-space and minimum-size rules, a responsive logo set, a favicon + app-icon system (iOS/Android/web), monochrome/reversed/dark-mode variants, and a misuse sheet. Routes here whenever the ask is "draw/construct/spec the mark", "make a logo grid", "build the favicon and app-icon set", "give me the lockups and clear-space", or "what are the logo do-nots". The distinctiveness lever is Janoff's interactive wit (a small surprise, like the FedEx arrow) and encoding the product's USP into the mark. Defers brand strategy/colour/type tie-in and the full style-guide to brand-visual-identity; defers typeface selection to font-selection-and-pairing and palette to color-system-and-palette.
status: active
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Logo and Wordmark Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Constructing a mark on an explicit geometry/grid (circle/square modules, golden or
  unit-grid construction, optical correction) and writing down the rules that reproduce it.
- Drawing or specifying a **wordmark / custom lettering**: which letters are modified, the
  spacing/kerning discipline, the one distinguishing letterform detail that makes it ownable.
- Producing the **lockup family**: primary, horizontal, stacked, monogram/glyph-only, and the
  rules for switching between them.
- Setting **clear-space**, **minimum sizes**, and a **responsive logo** ladder (full lockup →
  reduced wordmark → monogram → favicon).
- Building the **favicon + app-icon system** (web `favicon.svg`/ICO, iOS/iPadOS, Android
  adaptive, maskable PWA, monochrome/tinted) from the monogram.
- Specifying **monochrome / reversed / dark-mode** variants and the **misuse sheet** (the
  do-nots that protect the mark).
- Using **interactive wit / a small surprise** (FedEx arrow, I♥NY) and **USP-encoding** as the
  device that earns memorability — not literal depiction.

## Do Not Use When

- The ask is the whole identity system (strategy, colour+type tie-in, photography, voice,
  mini style-guide) — use `brand-visual-identity` and return here for the mark's construction
  and the favicon/app-icon system. This skill is the *mark-construction specialist* under it.
- The ask is only choosing typefaces — use
  `../../01-typography-and-fonts/font-selection-and-pairing`, then return here to draw or
  specify the wordmark cut.
- The ask is only the palette / contrast — use `../color-system-and-palette`, then bind the
  logo's colour variants here.
- You are auditing existing UI/marketing imagery for generative-AI artefacts (warped or
  misspelled marks, melted glyphs) — run `../../00-cross-cutting-ops-qa-a11y/visual-product-slop-audit`
  first, then design the clean replacement here.
- A binding client logo guideline already exists — follow and record it; apply only the
  responsive/favicon/variant extensions it lacks.

## Required Inputs

- **Strategy hand-off from `brand-visual-identity`** (or gather it first): the one-word
  essence, adjective set, and the *not-to-be-confused-with* competitor list. Distinctiveness is
  relative — you cannot construct an ownable mark without naming the field it stands apart from
  (Neumeier, *The Brand Gap*; Janoff: "do your homework — know the competition and where the
  mark will be seen").
- **The product's USP / differentiator in one sentence** — the thing the mark should *encode*,
  not decorate (Janoff: the Apple rainbow stripes *were* the Apple II's colour-on-TV story).
- **The surface set the mark must survive**: 16 px favicon → app icon → UI → sign/print →
  single-colour/embroidered. Janoff's rule: a strong mark sheds the wordmark, survives
  reduction, and crosses languages with no translation required.
- The brand name's exact spelling/casing, and whether a custom mark is to be **drawn** or an
  existing one **systematised**.
- Approved type (for the wordmark cut's skeleton) and the owned signature colour, if already
  fixed upstream.

## Workflow

1. **Idea before execution — name the ONE device first.** Decide the single distinctive idea
   the mark carries *before* drawing anything. Janoff: "going straight to the computer is often
   devoid of an idea… the idea should come first, the execution follows" — a direct restatement
   of the doctrine's anti-slop rule (don't reach for the tool to "get something on screen";
   `doctrine/design-doctrine.md` §2). The device is one of:
   - **Interactive wit / a small surprise** — a hidden or dual-reading detail the viewer
     *discovers* (the FedEx arrow in the negative space; I♥NY's substitution). A mark that
     carries a small surprise gets remembered. It must be *earned through one device*, never a
     literal picture of the product (Janoff: "visualise it metaphorically, perhaps subliminally
     — certainly not literally").
   - **USP-encoding** — the mark's defining feature *is* the differentiator (stripes =
     colour-on-TV). State the USP, then make the geometry carry it.
   Pick by **conviction, not by test** — a signature mark is a heuristic/taste decision with no
   objective arrow, so it is resolved by demo + taste, never outsourced to a metric or an AI
   recommend-list (`doctrine/references/creative-selection-and-taste.md`, the "41 shades of
   blue" rule; doctrine §2 sourcing-authority asymmetry).

2. **Silhouette iteration.** Draw the essence *every which way* — many quick variants — until
   the simplest form that still carries the device appears. Janoff: "When in doubt, leave it
   out"; clients arrive with "laundry lists of must-haves — a recipe for failure." A clear
   message is singular. Converge to one, then refine (the demo→feedback→next-demo loop,
   `creative-selection-and-taste.md`). **Never an AI-generated mark** — they carry the
   warped/fused/misspelled-glyph tell and read as every other logo
   (`doctrine/references/ai-slop-taxonomy.md` §Visual tells).

3. **Construct the mark on a grid.** Fix the geometry so it is reproducible from rules, not
   from a single exported PNG: construction modules, key ratios, stroke contrast, optical
   corrections (overshoot on round forms, optical centring, joint thinning). Full method in
   `references/mark-construction.md`. Rand's discipline: simple, distinctive, reproducible at
   any size, in one colour, from memory.

4. **Draw / specify the wordmark.** If lettering is custom, state which glyphs are modified and
   why, the kerning and tracking discipline, the cap-height/x-height relationship, and the one
   distinguishing detail. If set from an approved face, name it (from
   `font-selection-and-pairing`) and record the customisation (tightened spacing, a redrawn
   terminal). The wordmark's skeleton should agree with the brand's display type — one voice.

5. **Build the lockup family.** Specify: **primary** lockup, **horizontal** and **stacked**
   variants, **monogram/glyph-only**, and the alignment/relationship rules (mark-to-wordmark
   gap in mark-units, shared baseline or optical alignment, relative scale). Vignelli's
   discipline: a small governed set used consistently, not a sprawl of one-offs.

6. **Clear-space and minimum sizes.** Define clear-space in **units of the mark itself** (e.g.
   = cap-height, or = the monogram's width), never in px. Set minimum legible sizes per lockup,
   verified at the **favicon end** — the scale-relater test (Janoff): does the mark still read
   as itself, not a smudge, at 16 px?

7. **Responsive logo ladder.** Define the breakpoint-driven swap: full lockup → reduced
   wordmark (detail dropped) → monogram → favicon glyph. State the trigger size for each step.
   This is the same load-shedding discipline as "edit for less" — drop detail the small size
   cannot carry rather than shrinking everything uniformly.

8. **Favicon + app-icon system.** Derive the whole icon set from the monogram, not from a
   squashed lockup. Full matrix (web `favicon.svg` + ICO fallback, iOS/iPadOS, Android adaptive
   foreground/background + safe zone, maskable PWA, monochrome/tinted, Safari mask) in
   `references/app-icon-and-favicon-system.md`. Verify the maskable safe zone and the 16 px
   render.

9. **Colour, mono, reversed, dark variants.** Bind the owned signature colour
   (`../color-system-and-palette`) and specify: full-colour, single-colour positive, reversed,
   and dark-mode variants — each verified legible on its surface. A mark that only works in
   full colour is not finished (Janoff: works in one colour, from memory).

10. **Misuse sheet + Construction Gate.** Write the do-nots (no recolour, no stretch, no
    outline, no swoosh, no drop-shadow, no rotate, no set-on-busy-photo-without-scrim, no
    substitute typeface) and run the **Construction Gate** below. Structure the deliverable
    against `examples/aperture-mark-and-lockup-spec.md`.

## The Construction Gate (quality gate — run before sign-off)

1. **Device present and earned:** the one distinctive idea (wit/surprise or USP-encoding) is
   actually carried by the geometry — not bolted on, not literal.
2. **Reproducible from rules:** grid, ratios, and optical corrections are written down; a
   skilled hand could redraw the mark from the spec alone (Rand).
3. **Reduction-proof:** monogram is legible at 16 px favicon; the maskable safe zone holds.
4. **Variant-complete:** full-colour, single-colour, reversed, and dark variants all exist and
   are legible on their surfaces.
5. **Lockup-governed:** primary/horizontal/stacked/monogram + clear-space (in mark-units) +
   min-size are all specified; no ungoverned one-off.
6. **Memory test:** could someone redraw the essence after looking away? If not, sharpen one
   element — it is not yet ownable (Janoff & Rand; brand-visual-identity Consistency Gate).
7. **No AI-mark tells:** no warped, fused, or misspelled glyphs; no melted detail; no uncanny
   near-symmetry (`ai-slop-taxonomy.md`).

If any item fails, fix before sign-off — do not ship a half-built mark.

## Anti-Patterns

- **Going straight to the render with no idea** — fussing a corner before the device exists
  (Janoff: "tech is an idea-killer").
- **AI-generated marks** — warped, fused, or misspelled letterforms; melted detail; the
  highest public-backlash slop tell for a brand (`ai-slop-taxonomy.md`).
- **Literal depiction** — drawing a picture of the product instead of encoding its USP through
  one device (a coffee cup for a coffee app, a leaf for any "eco" brand).
- **The "laundry list" mark** — every must-have crammed in; complexity is the enemy of memory.
- **Exported-PNG-as-spec** — a single image with no grid, ratios, clear-space, or variants;
  unreproducible and ungoverned.
- **Full-colour-only mark** — no mono/reversed/dark; dies on a sign, a fax, or a dark UI.
- **Favicon by squashing the lockup** instead of deriving a purpose-built monogram glyph.
- **Picking the mark by A/B test or an AI tool's suggestion** — a taste decision outsourced to
  a metric is the asymmetry-rule error (`creative-selection-and-taste.md`; doctrine §2).

## Outputs

A **mark + lockup specification** (the buildable spec, 1–3 pages) containing:
- The stated device (interactive wit / small surprise, or USP-encoding) and why it fits.
- Mark construction: grid, modules, key ratios, optical corrections.
- Wordmark: face/custom cut, modified glyphs, spacing discipline.
- Lockup family: primary / horizontal / stacked / monogram + relationship rules.
- Clear-space (in mark-units) + minimum sizes (favicon-verified).
- Responsive logo ladder (swap thresholds).
- Favicon + app-icon matrix (web/iOS/Android/maskable/monochrome).
- Colour / single-colour / reversed / dark variants.
- Misuse sheet + a filled Construction Gate.

## Examples

- `examples/aperture-mark-and-lockup-spec.md` — a full worked mark+lockup spec for an invented
  but realistic brand ("Aperture", a privacy-first photo-archive app): the chosen device
  (USP-encoded interactive wit), grid construction, wordmark cut, lockup family, clear-space,
  responsive ladder, favicon/app-icon matrix, variants, misuse sheet, and a filled Construction
  Gate. Mirror its shape, not its values.

## References

- `references/mark-construction.md` (this folder) — geometry/grid construction, modular and
  ratio systems, optical correction, the wordmark-cut method, and how to encode wit/USP into
  form. Read before step 3.
- `references/app-icon-and-favicon-system.md` (this folder) — the full favicon + iOS/Android/
  web/maskable/monochrome icon matrix, safe zones, and the 16 px reduction test. Read before
  step 8.
- Sibling: `../brand-visual-identity` — the parent identity system this mark plugs into
  (strategy, colour+type tie-in, voice, Consistency Gate). Pair, don't duplicate: that skill
  owns the *system*; this one owns the *mark's construction and the icon set*.
- `../color-system-and-palette` (owned colour + contrast); `../../01-typography-and-fonts/font-selection-and-pairing`
  (the wordmark's skeleton); `../../00-cross-cutting-ops-qa-a11y/visual-product-slop-audit`.
- `doctrine/design-doctrine.md` — Mission (§0, the moat is looking human-made) and the
  Anti-Slop Charter (§2, sourcing-authority asymmetry: human design authority only).
- `doctrine/references/creative-selection-and-taste.md` — pick the mark by conviction + the
  demo→feedback loop, not by metric/AI ("41 shades of blue").
- `doctrine/references/ai-slop-taxonomy.md` — warped/misspelled-mark tells and the visual
  checklist used in the Construction Gate.
- Human design authority: **Rob Janoff** (interactive wit / a small surprise; encode the USP;
  "when in doubt, leave it out"; scale-relater; survives reduction in one colour); **Paul Rand**
  (simple, distinctive, reproducible, earns meaning through use); **Massimo Vignelli** (a small
  governed set, used consistently); **Marty Neumeier**, *The Brand Gap* (differentiation first).
  **No AI-tool recommendation is cited as authority.**
<!-- dual-compat-end -->
