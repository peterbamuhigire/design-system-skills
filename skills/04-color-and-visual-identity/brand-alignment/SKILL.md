---
name: brand-alignment
description: Ensures every website element — layout, messaging, navigation, imagery, CTAs — reflects the client's brand identity and speaks clearly to their ideal customer. Use before and during page building to validate that the site feels intentional, cohesive, and trustworthy.
status: active
metadata:
  portable: true
  category: 04-color-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Brand Alignment
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Ensures every website element — layout, messaging, navigation, imagery, CTAs — reflects the client's brand identity and speaks clearly to their ideal customer. Use before and during page building to validate that the site feels intentional, cohesive, and trustworthy.
- The work needs a quality gate or standard applied across other outputs.

## Do not use when
- The task is unrelated to this standard or quality lens.
- A more specific execution skill should own the work instead.

## Required inputs
- The content, interface, or artifact being reviewed or improved.
- Any brand, audience, regional, or conversion context that affects the judgment.

## Workflow
1. Read the artifact and the decision context before applying rules.
2. Use only the parts of the preserved guidance that matter to the current task.
3. Review or revise the work using this skill as a focused quality lens.
4. Return actionable changes or acceptance criteria instead of abstract theory.

## Quality standards
- Recommendations must be concrete enough to apply immediately.
- Changes should improve consistency, usability, or credibility without flattening the brand.
- The standard should support downstream implementation rather than slow it down.

## Anti-patterns
- Do not apply every rule mechanically when only a subset is relevant.
- Do not give generic critique with no change implications.
- Do not override project reality with taste-based preferences alone.

## Outputs
- Revisions, review findings, acceptance criteria, or quality guidance tied to the artifact under review.

## References
- `doctrine/design-doctrine.md` — the Mission ("the moat is looking human-made") and Anti-Slop Charter; brand alignment is the check that every element is an intentional, stated choice.
- `doctrine/references/ai-slop-taxonomy.md` — the convergent-default tells that signal "no brand thought went in here."
- Sibling skills: `04-color-and-visual-identity/brand-style-guide` (the recorded brand system this skill validates against), `04-color-and-visual-identity/color-system-and-palette`, `03-web-and-ui-design/distinctive-by-design`.
- `references/trust-architecture-checklist.md` (this folder) when validating proof, legitimacy, and credibility requirements.
- Start with `references/legacy-guidance.md` for preserved detailed guidance; read only the files under `references/` that match the task.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

