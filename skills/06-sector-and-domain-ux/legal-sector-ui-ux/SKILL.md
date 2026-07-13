---
name: legal-sector-ui-ux
description: Use when a lawyer, law firm, chambers, solicitor, barrister, or legal consultancy website needs ethical trust signals, practice-area structure, attorney profiles, or intake UX. Do not use for legal advice or generic sector selection; verify current jurisdictional advertising/privacy rules.
metadata:
  portable: true
  category: 06-sector-and-domain-ux
  compatible_with:
  - claude-code
  - codex
---

# Legal Sector UI/UX
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->

## Use when
- Building or redesigning a website for a law firm, solo lawyer, solicitor, barrister, or legal consultant — use this instead of the generic `06-sector-and-domain-ux/sector-strategies`.
- Designing practice-area pages (family, criminal, corporate, immigration, etc.) and need practice-specific tone, client-psychology framing, and a confidential-consult intake CTA.
- Building attorney profile pages, credentials/bar-admission blocks, case-result or testimonial sections, and other trust/credibility signals for a credibility-critical service.
- Wording or laying out legal calls-to-action that must carry the attorney–client disclaimer and respect bar-association advertising rules (no guarantees, no unverifiable "best/specialist" claims).
- Planning law-firm local SEO (jurisdiction pages, practice-area + city targeting, attorney schema).

## Do not use when
- The site is not a legal-services business — use the matching sector skill (e.g. `healthcare-ui-design`, `fintech-and-financial-product-ui`, `ecommerce-and-checkout-ux`) or the generic `sector-strategies`.
- You only need cross-sector trust/social-proof patterns with no legal-ethics or bar-rule constraints — pull from the trust-credibility-and-social-proof guidance directly.
- The job is pure palette/contrast or type-system work — defer to `02-color-brand-and-visual-identity/color-system-and-palette` (this skill calls into it for the trust-signal palette and WCAG gate).

## Required inputs

| Input | Source | Evidence |
|---|---|---|
| Jurisdiction, practice areas, audience, and intake boundaries | Firm owner and legal/ethics reviewer | Verified services, barred claims, disclaimers, and conflict process |
| Lawyer credentials and trust evidence | Authorised firm records | Names, admissions, experience, memberships, and permission to publish |
| Privacy, accessibility, and lead-routing requirements | Legal/privacy/operations | Consent, sensitive-data limits, retention, and response ownership |
- Firm details: jurisdiction(s), practice areas, attorney roster with real credentials/bar admissions, and any governing bar-association advertising rules.
- Brand and visual constraints (existing identity, or the trust-signal palette from `color-system-and-palette`) and the standard build-pipeline context.
- Real trust assets where available: case results, testimonials, accreditations, plus the required attorney–client disclaimer text.

## Workflow
1. Read only the relevant project inputs and preserved guidance before acting.
2. Choose the smallest set of references needed for the current job.
3. Produce the implementation, configuration, or guidance this skill owns.
4. Validate that the result stays compatible with the rest of the repository workflow.

## Decision Rules

| Condition | Choice | Wrong-choice failure |
|---|---|---|
| Visitor has an urgent/high-stakes matter | Clear scope, jurisdiction, contact route, and expectation | Vague conversion copy delays appropriate help |
| Claim cannot be substantiated or is restricted | Omit or qualify after ethics review | Superlatives/testimonials create misleading advertising risk |
| Intake may reveal privileged/sensitive facts | Collect minimum screening data before secure follow-up | Open forms invite unnecessary exposure and false confidentiality assumptions |

## Capability Contract

- Must inspect authorised credentials and current jurisdictional rules; review is read-only unless website remediation is requested.
- May edit in-scope content/design, but may not provide legal advice, invent outcomes/credentials, contact leads, or publish claims without firm approval.

## Degraded Mode

- If jurisdiction, credentials, disclaimer, or intake/privacy rules are unverified, stop publication and return a content blocker register.
- Without current regulatory research, use neutral factual language and mark compliance review pending. Recover a challenged claim by removing it, preserving evidence, and routing it to the named ethics owner.

## Quality Standards
- Outputs must be implementation-ready and internally consistent.
- Preserve existing behavior unless the task explicitly requires a change.
- Avoid host-specific path assumptions so the skill remains portable.

## Anti-patterns

- Guaranteed-outcome or "best lawyer" claims. Correction: use verifiable scope, experience, and evidence.
- Stock gavels and scales as the whole identity. Correction: build distinction from real people, place, expertise, and authored typography.
- Intake forms that solicit a full case narrative before conflict/privacy safeguards. Correction: collect minimum screening data.
- Testimonials without permission or required disclaimers. Correction: verify provenance and jurisdictional conditions.
- Ambiguous attorney-client relationship language. Correction: state that contact does not itself establish representation.
- Do not hardcode `.claude/skills` or another single install path.
- Do not skip validation against upstream or downstream dependencies.
- Do not generate generic output that ignores the actual project context.

## Outputs

| Output | Consumer | Evidence and acceptance |
|---|---|---|
| Legal website direction and content architecture | Firm, content, design | Practice areas, profiles, trust evidence, intake, disclaimers, and exclusions are explicit |
| Ethics/privacy/accessibility gate | Firm approver and QA | Claims, credentials, consent, forms, jurisdiction, and representative journeys are verified |
- Implementation guidance, configuration, generated artifacts, or concrete follow-on steps.

## References
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter; legal sites must read as authored and trustworthy, never templated.
- `doctrine/references/ai-slop-taxonomy.md` — convergent-default tells to avoid in a credibility-critical sector.
- `references/ethics-constraints.md`, `references/content-templates.md`, `references/local-seo.md` (this folder) — bar-association advertising rules, attorney profile/practice-area structure, and law-firm local SEO.
- Sibling skills: `06-sector-and-domain-ux/sector-strategies` (the generic sector skill this one overrides), `02-color-brand-and-visual-identity/color-system-and-palette` (trust-signal palette + WCAG gate).
- Start with `references/legacy-guidance.md` for the preserved detailed guidance; read only the files under `references/` that match the current task.

## Examples
- `examples/law-firm-screen-worked.md` — a worked family-law practice-area page spec: client-psychology framing, non-default trust palette and a non-banned type pairing, authority/credibility signals sequenced after reassurance, plain-English process, and a practice-specific confidential-consult CTA with the required attorney–client disclaimer.

## Notes
- Treat this `SKILL.md` as the portable execution layer for both Claude Code and Codex.
- Preserve existing project behavior unless the current task explicitly requires a change.
<!-- dual-compat-end -->
