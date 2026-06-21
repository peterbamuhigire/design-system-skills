---
name: legal-sector-ui-ux
description: Legal sector website design for law firms. Use instead of generic sector-strategies when building websites for lawyers, law firms, solicitors, barristers, or legal consultants. Covers practice-area-specific design direction, client psychology for legal services, ethical advertising constraints (bar association rules), attorney profile pages, trust signals for legal, local SEO for law firms, and conversion for legal intake. Works alongside all standard build pipeline skills.
status: active
metadata:
  portable: true
  category: 06-sector-and-domain-ux
  compatible_with:
    - claude-code
    - codex
---

# Legal Sector UI/UX
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

## Use when
- The task matches this domain: Legal sector website design for law firms. Use instead of generic sector-strategies when building websites for lawyers, law firms, solicitors, barristers, or legal consultants. Covers practice-area-specific design direction, client psychology for legal services, ethical advertising constraints (bar association rules), attorney profile pages, trust signals for legal, local SEO for law firms, and conversion for legal intake. Works alongside all standard build pipeline skills.
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
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter; legal sites must read as authored and trustworthy, never templated.
- `doctrine/references/ai-slop-taxonomy.md` — convergent-default tells to avoid in a credibility-critical sector.
- `references/ethics-constraints.md`, `references/content-templates.md`, `references/local-seo.md` (this folder) — bar-association advertising rules, attorney profile/practice-area structure, and law-firm local SEO.
- Sibling skills: `03-web-and-ui-design/sector-strategies` (the generic sector skill this one overrides), `04-color-and-visual-identity/color-system-and-palette` (trust-signal palette + WCAG gate).
- Start with `references/legacy-guidance.md` for the preserved detailed guidance; read only the files under `references/` that match the current task.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.

