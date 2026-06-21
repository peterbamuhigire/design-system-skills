---
name: font-selection-and-pairing
description: Use when choosing typefaces for ANY artifact that contains type - a website, a DOCX/PPTX/PDF report or proposal, a software/app UI screen, a pitch deck, or marketing page. Selects a deliberate, non-slop display+body pairing matched to artifact context, design voice, functional role, and licence constraints; states the choice and reason before output; and runs the anti-slop checklist. This is the default entry skill for typography in the design engine.
status: active
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
    - claude-code
    - codex
---

# Font Selection And Pairing
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- About to generate, theme, or restyle any artifact that contains type: website/landing page,
  DOCX/PPTX/PDF/report/proposal/business-plan/SRS, app or web UI, dashboard, or pitch deck.
- A typeface decision is needed and the work risks defaulting to an AI-slop font.
- Reviewing or refreshing an existing artifact's typography.

## Do Not Use When

- The work has a binding client brand guideline that already mandates fonts - follow it,
  record it, and skip selection, but still apply pairing/scale hygiene.
- The task is purely embedding/loading an already-chosen font - use
  `font-embedding-and-licensing`.
- The task is auditing an existing artifact for slop - use `ai-slop-typography-audit`.

## Required Inputs

- Artifact type and output format: web, DOCX, PPTX, PDF, XLSX, UI, mobile, or app shell.
- Context and audience: formal/institutional, editorial/literary, product/grotesque,
  technical/data/code, friendly/humanist, expressive/artistic, script/cursive, or body/UI.
- Functional role: display, body, UI, code/data, or accent.
- Any brand constraints, and the device/size range the type must survive.

## Workflow

1. **Classify the artifact** via `doctrine/references/font-groups-and-usage.md` using:
   artifact context -> design voice -> functional role -> licence/availability.
2. **Verify the font folder taxonomy:** before scanning on a new device or after a pull, ensure
   the eight required `fonts/<category>/` directories from `fonts/README.md` exist. Create any
   missing category folder without deleting or moving local font files.
3. **Scan for premium files:** run the `premium-font-scan` logic against the matching
   `fonts/<category>/` folder. If a permitted premium family is present and would look better,
   prefer it; else take the named OFL baseline.
4. **Pick a pairing** using `doctrine/references/pairing-principles.md`: display + body,
   category contrast, weight extremes, compatible x-heights, and no mood conflict. For ready,
   named, context-sorted pairings, use `references/pairing-catalog.md`.
5. **State the choice before producing anything:** name the display face, the body face, the
   category, and a one-line reason tied to this artifact's context.
6. **Run the anti-slop checklist** below. If any item fails, fix before proceeding.
7. **Set the type scale** per `doctrine/references/type-scale-and-spacing.md`: ratio >=1.25,
   real jumps, inverse line-height, and weight extremes. For concrete px/rem scales, fluid
   `clamp()` versions, and variable-font axes, use `references/type-scale-recipes.md`.
8. **Hand off to `font-embedding-and-licensing`** for the format-correct load/embed.

## The Anti-Slop Checklist

1. Typeface(s) named explicitly with a one-line contextual reason - stated before output.
2. None on the banned list (`ai-slop-banned-fonts.md`), including secondary escape fonts.
3. A deliberate display+body pairing, not one font for everything.
4. Licence permits the intended use, including embedding (`licensing-and-embedding.md`).
5. Loaded/embedded correctly for the format, subsetting on for DOCX/PPTX (`embedding-by-format.md`).
6. A sensible fallback set after, never instead of, the chosen font.

If the checklist cannot be satisfied, say so and ask. Never silently fall back to Inter or a
bare system stack.

## Anti-Patterns

- Picking a font "to start" and never stating it.
- Reaching for Space Grotesk/Poppins/Montserrat as the safe distinctive choice.
- Treating `08-body-ui-workhorses` as a complete identity instead of the body layer.
- Using `07-script-cursive-handwritten` for paragraphs, forms, tables, dashboards, or UI labels.
- One typeface for headings, body, labels, and buttons.
- Timid mid-weights and near-identical sizes.

## Outputs

- A stated typographic decision: display + body + category + reason.
- A completed anti-slop checklist.
- The type scale and a clean handoff to embedding.

## Examples

- `examples/applied-type-scale.md` - a real px/rem type scale for a named brief: the stated
  pairing + reason, the full scale, the fluid `clamp()` version, variable-font axis settings,
  and the anti-slop checklist run end to end.

## References

- `doctrine/design-doctrine.md`, and the references it indexes: `ai-slop-banned-fonts.md`,
  `font-groups-and-usage.md`, `pairing-principles.md`, `type-scale-and-spacing.md`.
- `fonts/README.md` - required eight-category folder taxonomy and new-device setup command.
- `references/pairing-catalog.md` - named, context-sorted display+body pairings.
- `references/type-scale-recipes.md` - concrete px/rem scales, fluid `clamp()`, variable-font axes.
<!-- dual-compat-end -->
