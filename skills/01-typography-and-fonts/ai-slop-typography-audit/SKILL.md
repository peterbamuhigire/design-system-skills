---
name: ai-slop-typography-audit
description: Use when auditing an existing artefact for banned or convergent type, weak hierarchy, monotype systems, or unstated choices. Unlike visual-product-slop-audit, this inspects typography only; font selection owns the replacement design.
metadata:
  portable: true
  category: 01-typography-and-fonts
  compatible_with:
  - claude-code
  - codex
---

# AI-Slop Typography Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Reviewing an existing artifact (site, DOCX/PPTX/PDF, UI screen) for typographic slop.
- A deliverable "feels AI-generated" and you need to find and fix the tells.
- Gate-checking a product before it ships under the Chwezi name.

## Do Not Use When

- Choosing fonts from scratch — use `font-selection-and-pairing`.
- The artifact has no type, or fonts are fixed by a binding brand guideline.

## Required Inputs

| Input | Supplied by | Required? | Why |
|---|---|---|---|
| Rendered artefact and styles | Requester | yes | Enables visual and source inspection |
| Audience, medium, and voice | Brief or owner | yes | Tests contextual fitness |
| Current doctrine and banned list | Design engine | yes | Prevents stale findings |

- The artifact or its source (CSS/HTML, the document file, screenshots, or a style spec).
- The intended context and design voice (so the remediation maps to the right font category).

## Workflow

1. **Detect primary typefaces.** Read the CSS `font-family` stacks / document style / theme.
   Flag any banned face from `doctrine/references/ai-slop-banned-fonts.md` used as primary,
   and flag bare system stacks used alone.
2. **Detect secondary slop.** Flag Space Grotesk/Poppins/Montserrat/Nunito and standalone
   Source Sans used as the distinctive choice.
3. **Detect structural slop:** one font for everything; mid-weights only (no extremes);
   near-identical size steps; wide-tracked body; pure-black body text.
4. **Score** each finding (primary-font slop is critical; structural slop is major/minor).
5. **Remediate deliberately:** propose a non-slop pairing + scale for the artifact's category via
   `font-selection-and-pairing`; state the replacement and reason.
6. **Report** findings → fixes, with before/after.

## Anti-Patterns

- Swapping Inter for another single sans and calling it fixed.
- Removing a banned font but keeping monotype, timid weights, or wide-tracked body.
- Calling a face slop from personal taste alone; cite the current list or a documented convergence tell.
- Recommending an unlicensed or unavailable replacement; route the brief through selection and scan.
- Auditing only headings; inspect body, controls, data, errors, and responsive states too.

## Outputs

| Output | Consumer | Evidence / acceptance |
|---|---|---|
| Typography finding register | Designer and owner | Location, tell, severity, evidence, and rule |
| Gate verdict | Pre-launch QA | PASS, CONDITIONAL, or BLOCKED with rationale |
| Replacement brief | Typeface selector | Role, voice, hierarchy, and constraints |

- A findings list (each tagged critical/major/minor with the rule it breaks) and a stated,
  non-slop remediation ready to apply.

## Examples

- Use the worked example in `examples/` as the required findings-to-remediation model.

## Quality Standards

- Tie every finding to visible evidence and a current doctrine rule; taste alone is insufficient.
- Inspect display, body, data, and state text at representative sizes and widths.
- Block release for a banned primary face or faux typography until remediated and re-audited.

## Decision Rules

| Condition | Decision | Wrong-choice failure |
|---|---|---|
| Primary face is currently banned | Block and replace | Convergent type ships |
| Face is allowed but hierarchy is timid | Fail the system, not the family | Font swap is mistaken for design |
| Distinctiveness harms readability | Find another authored option | Novelty excludes users |
| Evidence is subjective dislike only | Record critique, not gate failure | Taste becomes doctrine |

## Capability Contract

Read and visual inspection are required. Review remains read-only unless remediation is requested. Search may inspect styles; rendering is preferred. Current-definition research routes to the doctrine-refresh skill.

## Degraded Mode

Without styles, audit the render and mark causes unverified. Without a render, return a checklist and do not issue a pass. If doctrine currency is uncertain, stop and route to refresh.

- `examples/typography-audit-filled.md` — a filled audit of a sample SaaS landing-page stylesheet
  (Inter body + Geist display + Space Grotesk accent over a bare system stack): each banned and
  secondary-slop face detected with the rule it breaks, scored critical/major/minor, then one
  deliberate non-slop remediation (Bricolage Grotesque 800 -> Hanken Grotesk 400, 03 Modern
  Product / Grotesque) mapped
  finding-by-finding with the before/after CSS.

## References

- `doctrine/references/ai-slop-banned-fonts.md`, `pairing-principles.md`,
  `type-scale-and-spacing.md`.
<!-- dual-compat-end -->
