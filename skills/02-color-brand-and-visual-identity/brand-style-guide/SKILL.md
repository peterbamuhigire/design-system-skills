---
name: brand-style-guide
description: Produces a client-facing brand style guide deliverable (docs/brand-style-guide.md). Use after brand-strategy and design-system are complete. Covers logo usage rules, colour palette card (hex/RGB/CMYK), typography specimen, spacing system, photography style, voice and tone guide, and component usage examples. This document is delivered to the client as a premium project deliverable.
status: active
metadata:
  portable: true
  category: 02-color-brand-and-visual-identity
  compatible_with:
    - claude-code
    - codex
---

# Brand Style Guide
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Produces a client-facing brand style guide deliverable (docs/brand-style-guide.md). Use after brand-strategy and design-system are complete. Covers logo usage rules, colour palette card (hex/RGB/CMYK), typography specimen, spacing system, photography style, voice and tone guide, and component usage examples. This document is delivered to the client as a premium project deliverable.
- The user needs domain-specific strategy, writing, or planning in this area.

## Do not use when
- Another skill is clearly narrower and better matched to the request.
- The task is unrelated to this domain or needs direct implementation instead.

## Required inputs
- Business context, target audience, and the artifact or decision being developed.
- Any existing materials, constraints, or supporting references already available.

## Workflow
1. Read the current business context and the concrete task to solve.
2. Use only the relevant detailed guidance and references for the request at hand.
3. Produce the strategy, writing, or framework output this skill is responsible for.
4. Check the result for clarity, realism, and handoff readiness.

## Quality standards
- Outputs must be specific, usable, and grounded in the available evidence.
- Recommendations should support follow-on execution instead of staying abstract.
- The result should remain consistent with the broader repository system.

## Anti-patterns
- Do not produce generic framework dumps with no decision made.
- Do not invent facts to complete the output.
- Do not ignore the actual audience, offer, or business constraints.

## Outputs
- Strategy notes, writing deliverables, framework outputs, or implementation-facing recommendations.

## References
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter; the style guide must record *deliberate, stated* choices, not defaults.
- `doctrine/references/ai-slop-banned-fonts.md` and `doctrine/references/font-groups-and-usage.md` — verify the typography specimen names an approved, non-banned face before it ships to the client.
- `doctrine/references/pairing-principles.md`, `doctrine/references/type-scale-and-spacing.md` — typography pairing and the spacing/type scale the specimen documents.
- Sibling skills: `04-color-and-visual-identity/color-system-and-palette` (palette card hexes + WCAG), `04-color-and-visual-identity/brand-visual-identity`, `01-typography-and-fonts/font-selection-and-pairing`.
- Start with `references/legacy-guidance.md` and `references/style-guide-template.md` for the deliverable structure; read only the files under `references/` that match the task.

## Examples
- `examples/mini-style-guide-worked.md` — a worked compact brand style-guide deliverable for a
  sample roaster (Köya): logo usage, colour palette (hex + OKLCH + roles), an approved Fraunces +
  Public Sans typography specimen with scale, spacing system, photography note, and a do/don't.
  Use it as the calibration target for specificity and the stated-choice discipline.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

