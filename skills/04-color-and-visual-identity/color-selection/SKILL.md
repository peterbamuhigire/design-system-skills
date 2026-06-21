---
name: color-selection
description: Select optimal color palettes for websites using brand colors and color theory. Use when users need to define their website's color scheme, generate complementary palettes, ensure accessibility compliance, or refine existing colors for better visual impact and industry alignment.
---

# Color Selection
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Select optimal color palettes for websites using brand colors and color theory. Use when users need to define their website's color scheme, generate complementary palettes, ensure accessibility compliance, or refine existing colors for better visual impact and industry alignment.
- The user needs an implementation-facing skill rather than a general discussion.

## Do not use when
- The prerequisite upstream context is missing and the task is not yet execution-ready.
- Another narrower skill is the clear better fit for the exact subtask.

## Required inputs
- Project context, current files, and any constraints that affect implementation.
- Upstream artifacts produced by earlier skills when this skill is part of a pipeline.

## Workflow
1. Read only the relevant project inputs and preserved guidance before acting.
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.

## Quality standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-patterns
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not generate generic output that ignores the actual project context.

## Outputs
- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## References
- Start with `references/legacy-guidance.md` when you need the preserved detailed instructions from the previous skill version.
- Read only the specific files under `references/` that match the current task instead of loading the whole directory.
- Use bundled tools in `scripts/` when they cover the task more reliably than redoing the work manually.

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

For a deeper colour theory skill that goes beyond website-specific palette selection (full colour models, OKLCH scale generation, archetype mapping), use the `color-theory` skill in the parent skills repository.
