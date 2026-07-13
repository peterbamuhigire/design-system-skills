---
name: sector-strategies
description: Use when a website needs an evidence-based sector direction for travel, consulting, education, nonprofit, professional services, portfolio, or another industry without a dedicated skill. Do not use for legal, healthcare, fintech, or ecommerce UX; route those regulated/specialist sectors to their skills.
metadata:
  portable: true
  category: 06-sector-and-domain-ux
  compatible_with:
  - claude-code
  - codex
---

# Sector Strategies
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

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

| Input | Source | Evidence |
|---|---|---|
| Sector, offer, audience, geography, and buying context | Client brief and research | Specific segment, alternatives, trust barriers, and decision journey |
| Authentic proof and available assets | Client/operations records | Projects, people, results, locations, testimonials, and permissions |
| Regulatory, accessibility, and conversion constraints | Domain owner and delivery team | Verified claims, required disclosures, lead route, and target devices |
- The sector/vertical, the audience, and what they actually check before trusting (the trust cues).
- The brand or a deliberate type+colour direction (never a banned font; no default-sector palette).
- The one distinctive move that will keep this site from the sector's homogeneous default.

## Workflow
1. Read only the relevant project inputs and preserved guidance before acting.
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.

## Decision Rules

| Condition | Choice | Wrong-choice failure |
|---|---|---|
| A dedicated regulated-sector skill exists | Route to it and retain this only for broader context | Generic advice misses safety/legal constraints |
| Sector trust depends on tangible proof | Lead with authentic evidence and process | Generic visual tropes imitate category without credibility |
| Organisation spans sectors | Prioritise audience/job and create bounded service branches | Mixing every sector cue creates incoherent identity |

## Capability Contract

- Must inspect real sector/client evidence; strategy review is read-only unless implementation is requested.
- May produce in-scope direction but may not invent proof, make regulated claims, purchase assets, or publish without client authority.

## Degraded Mode

- If sector, audience, offer, or proof is missing, stop final direction and return labelled hypotheses plus research needs.
- Without current regulatory evidence, avoid compliance claims and route to the relevant domain owner. Recover a generic direction by replacing category clichés with verified client-specific proof and rerunning comparison.

## Quality Standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-patterns

- Selecting colours from sector stereotype alone. Correction: derive palette from brand position, context, and accessibility.
- Using generic stock imagery as proof. Correction: prioritise real people, work, place, and outcomes.
- Copying one template across unrelated sectors. Correction: adapt information hierarchy to the buying/task journey.
- Inventing statistics, clients, or testimonials. Correction: use authorised evidence or transparent placeholders.
- Applying this generic router to regulated healthcare, finance, or legal decisions. Correction: activate the dedicated domain skill.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not generate generic output that ignores the actual project context.

## Outputs

| Output | Consumer | Evidence and acceptance |
|---|---|---|
| Sector strategy brief | Client, content, design | Audience, trust model, hierarchy, proof, visual direction, and exclusions are explicit |
| Authenticity and quality gate | Approver and QA | Claims/assets trace to sources and sector-specific journeys pass accessibility/conversion review |
- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## References
- `doctrine/design-doctrine.md` — the Mission ("the moat is looking human-made") and Anti-Slop Charter; sector authenticity is one route to authored, non-convergent design.
- `doctrine/references/ai-slop-taxonomy.md` — the convergent-default tells each sector strategy must avoid.
- `ANTI-HOMOGENEITY-PRINCIPLE.md` (this folder) — why sector templates inform but never dictate the final tokens.
- Sibling skills: `04-web-and-ui-design/distinctive-by-design` (commit one distinctive idea per build), `06-sector-and-domain-ux/legal-sector-ui-ux` and `06-sector-and-domain-ux/healthcare-ui-design` (deeper sector skills), `02-color-brand-and-visual-identity/color-system-and-palette`.
- Start with `references/legacy-guidance.md` for the preserved detailed sector matrix; read only the files under `references/` and `templates/` that match the current task.

## Examples
- `examples/sector-strategy-worked.md` — a fully reasoned worked strategy for one sector (fintech): trust cues, visual/aesthetic direction, content priorities, and the single anti-homogeneity move that keeps it distinctive. Read it to see how a sector template informs but does not dictate the final design.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
<!-- dual-compat-end -->
