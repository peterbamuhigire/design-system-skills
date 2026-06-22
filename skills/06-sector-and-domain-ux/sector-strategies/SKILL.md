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
- Designing for a specific industry/vertical (tour & travel, corporate/consulting, portfolio,
  education, e-commerce, professional services, NGO/charity) and you need the sector's trust cues,
  content priorities, and visual direction — not a generic template.
- You need to make a site read as *authentically of its sector* while deliberately avoiding the
  convergent "every-X-site-looks-the-same" look (apply the `ANTI-HOMOGENEITY-PRINCIPLE.md`).
- Choosing the visual/UX strategy for a sector before the build (pairs with `distinctive-by-design`).

## Do not use when
- The sector is **healthcare**, **legal/fintech**, or **e-commerce** — those have dedicated deeper
  skills (`healthcare-ui-design`, `legal-sector-ui-ux`, `fintech-and-financial-product-ui`,
  `ecommerce-and-checkout-ux`); use this for the sectors they don't cover, or for cross-sector strategy.
- You already have the sector direction and just need to execute UI craft → `practical-ui-design`,
  `webapp-gui-design`; or brand/identity → `brand-visual-identity`.

## Required inputs
- The sector/vertical, the audience, and what they actually check before trusting (the trust cues).
- The brand or a deliberate type+colour direction (never a banned font; no default-sector palette).
- The one distinctive move that will keep this site from the sector's homogeneous default.

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

