---
name: color-selection
description: Use when generating a starting website palette from brand hues, imagery, audience, mood, or colour harmony. Unlike color-system-and-palette, this selects candidate colours; semantic roles, ramps, dark themes, and final contrast contracts are downstream.
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
  - claude-code
  - codex
---

# Color Selection
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use when
- You need to *generate* a starting palette from scratch — a project with weak or no brand-colour direction, and you must arrive at a primary hue, harmony, and candidate swatches.
- You have reference imagery (hero photo, product shots) and want the photography to live *inside* the palette via duotone/brand-hue tinting (the imagery-first Flux method).
- A brief exists with a mood word, audience, and target viewer action, and you need to translate it into a hue + harmony (mono / analogous / complementary / split-complementary / triadic / tetradic).
- You need to fight templated AI-default colour (indigo→blue gradients, stock Tailwind, neon-on-dark) by sourcing colour from brand and imagery instead.

## Do not use when
- The palette already exists and you need semantic roles, tonal ramps, dark-mode remap, or the hard WCAG contrast gate — that is the system sibling `02-color-brand-and-visual-identity/color-system-and-palette`. Generate here, then hand off.
- You only need to theme/restyle an existing palette across light/dark — see `dark-mode-and-theming`.
- You only need to verify or repair contrast on fixed colours — see `accessible-color-and-contrast`.
- Strong locked brand colours already dictate the palette and no generation is needed.

## Required inputs

| Input | Supplied by | Required? | Why |
|---|---|---|---|
| Brand colours or source imagery | Client or brief | recommended | Provides an authored anchor |
| Audience, mood, sector, and action | Strategy brief | yes | Guides harmony and emphasis |
| Existing equity and prohibited colours | Brand owner | conditional | Avoids identity loss |
- A brief: the mood word, the audience, and the action you want the viewer to take.
- Any existing brand colours or constraints (one locked hue is enough to anchor generation).
- Reference imagery if available — the hero/product photos that should be tinted toward the brand hue.
- Answers to the four diagnostic questions: any colour constraints? is the guidance complete? what feel? what action?

## Workflow
1. Read only the relevant project inputs and preserved guidance before acting.
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.

## Quality standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.
- Stop selection when neither a brand/imagery anchor nor an authorised strategic choice exists.

## Anti-patterns
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not generate generic output that ignores the actual project context.
- Do not copy a fashionable gradient or framework default; anchor the palette in brief or imagery.
- Do not fix contrast by replacing the brand hue first; move along its tonal scale.

## Outputs

| Output | Consumer | Evidence / acceptance |
|---|---|---|
| Candidate palette and rationale | Brand and web designers | Anchor, mood, harmony, and values recorded |
| Imagery treatment and balance rule | Art direction and layout | Tint/duotone and 60/30/10 usage demonstrated |
| Handoff constraints | Colour-system workflow | Roles, contrast risks, and prohibited uses stated |

- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## Decision Rules

| Condition | Decision | Wrong-choice failure |
|---|---|---|
| Strong brand colour exists | Build harmony around it | Existing equity is discarded |
| Imagery leads the experience | Extract or tint toward one defensible hue | Photography and UI feel unrelated |
| Calm field is required | Use monochromatic or analogous harmony | Excess colour competes for attention |
| Strong focal action is required | Use a restrained complementary accent | Every surface shouts equally |

## Capability Contract

Read and colour calculation are required. Image sampling and rendering are preferred. Editing requires authorisation; do not change master assets or claim final accessibility before semantic testing.

## Degraded Mode

If required evidence or tooling is unavailable, use the scoped fallback below and mark the result unverified.
Without imagery or brand direction, return two differentiated candidates and the decision needed to choose. Without contrast tooling, mark pairs provisional and hand off to the colour-system gate.

## Examples
- `examples/palette-generation-worked.md` — a full palette *generation* for a named brief
  (Texas barbecue restaurant): brisket-bark anchor → *smoked* mood → analogous-plus-warm-accent
  harmony → candidate palette (OKLCH + hex) → 60-30-10 framing → a quick WCAG sanity check, then a
  clean hand-off to the system sibling. Stays in the generation lane; the ramps/roles/hard gate are
  the sibling's job.

## References
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter (state the colour choice and its anchor first; the sourcing-authority asymmetry rule — AI picks are evidence of what to avoid, never authority for what to use).
- `doctrine/references/ai-slop-taxonomy.md` — the convergent colour defaults to reject (indigo/purple→blue gradient, stock Tailwind palette, glassmorphism, neon-on-dark).
- **Sibling — `02-color-brand-and-visual-identity/color-system-and-palette`.** That skill is the colour *system* (semantic roles, tonal ramps, dark-mode remap, the hard WCAG gate) and the default entry skill for colour. **This skill is palette *generation*** — the imagery-first / brand-hue Flux method for arriving at a starting palette. Generate the palette here, then hand it to `color-system-and-palette` to derive roles, ramps, and the contrast gate. Use them together; do not merge.
- Start with `references/legacy-guidance.md` for preserved detailed guidance; read only the files under `references/` that match the task, and use `scripts/palette_generator.py` when it covers the work reliably.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

---

## Flux process: imagery-first colour selection

For projects without strong brand-colour direction, the Flux Academy process (Ran Segall et al., *The Complete Guide for Choosing Colors*) is the workhorse method. Load `references/flux-process.md` for the full workflow. Key moves:

1. **Define the brief** — mood word, audience, viewer action.
2. **Four diagnostic questions** — constraints? all the guidance? what feel? what action?
3. **Pick the primary hue** from mood + audience. If imagery exists, **tint the imagery toward the brand hue** (duotone) so the photography lives inside the palette rather than on top of it.
4. **Choose the harmony** — monochromatic / analogous / complementary / split-complementary / triadic / tetradic — using the brief-to-harmony decision table.
5. **Generate scales** — 10 steps for primary, 10 for neutrals (slightly tinted toward primary), 3–5 for the accent.
6. **Apply 60/30/10** — neutrals 60%, primary 30%, accent 10% (a balance gauge, not a literal three-colour rule).
7. **WCAG AA verification** — body 4.5:1, large/UI 3:1. To fix a failure, **move shade up/down the scale, never re-pick the hue** — preserves brand identity.
8. **Build base first, accents last.** No accent colour in non-CTA areas.

The Flux worked example (a black-and-white "girl with balloons" reference photo, tinted purple → navy-purple hero / mid-purple chrome / magenta accent / off-white surfaces) is captured in the reference. Use the imagery-first algorithm for any client website that needs to feel cohesive rather than templated.

For a deeper colour-system skill that goes beyond website-specific palette selection (semantic roles, perceptual OKLCH/CIELAB ramp generation, the WCAG contrast gate, and the dark-mode remap), hand off to the sibling `02-color-brand-and-visual-identity/color-system-and-palette` in this engine. (The former cross-engine `color-theory` skill did not migrate; its concerns are covered by `color-system-and-palette` plus `doctrine/design-doctrine.md` §2.)
<!-- dual-compat-end -->
