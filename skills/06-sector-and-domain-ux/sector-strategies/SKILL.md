---
name: sector-strategies
description: Industry-specific website design strategies and templates. Use when building websites for different business sectors (tour & travel, corporate & consulting, personal & portfolio, education, healthcare, e-commerce, professional services, hobbyist creators, nonprofit/charity/NGO, law firms/legal) to ensure the site reflects sector-specific design psychology, trust cues, and visual identity. Choose your sector → customize template → get industry-authentic design that doesn't look AI-generated.
status: active
metadata:
  portable: true
  category: 06-sector-and-domain-ux
  compatible_with:
    - claude-code
    - codex
---

# Sector Strategies
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Industry-specific website design strategies and templates. Use when building websites for different business sectors (tour & travel, corporate & consulting, personal & portfolio, education, healthcare, e-commerce, professional services, hobbyist creators, nonprofit/charity/NGO, law firms/legal) to ensure the site reflects sector-specific design psychology, trust cues, and visual identity. Choose your sector → customize template → get industry-authentic design that doesn't look AI-generated.
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
- `doctrine/design-doctrine.md` — the Mission ("the moat is looking human-made") and Anti-Slop Charter; sector authenticity is one route to authored, non-convergent design.
- `doctrine/references/ai-slop-taxonomy.md` — the convergent-default tells each sector strategy must avoid.
- `ANTI-HOMOGENEITY-PRINCIPLE.md` (this folder) — why sector templates inform but never dictate the final tokens.
- Sibling skills: `03-web-and-ui-design/distinctive-by-design` (commit one distinctive idea per build), `03-web-and-ui-design/legal-sector-ui-ux` and `03-web-and-ui-design/healthcare-ui-design` (deeper sector skills), `04-color-and-visual-identity/color-system-and-palette`.
- Start with `references/legacy-guidance.md` for the preserved detailed sector matrix; read only the files under `references/` and `templates/` that match the current task.

## Examples
- `examples/sector-strategy-worked.md` — a fully reasoned worked strategy for one sector (fintech): trust cues, visual/aesthetic direction, content priorities, and the single anti-homogeneity move that keeps it distinctive. Read it to see how a sector template informs but does not dictate the final design.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

