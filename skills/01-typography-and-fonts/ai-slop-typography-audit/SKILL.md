---
name: ai-slop-typography-audit
description: Use when auditing an existing website, document, deck, or UI for AI-slop typography — detecting banned fonts (Inter, Roboto, Arial, Open Sans, Lato, bare system stacks) and the secondary escape fonts (Space Grotesk, Poppins, Montserrat, Nunito, standalone Source Sans), single-font monotype, timid weights/sizes, and wide-tracked body. Produces a findings list and a deliberate remediation.
status: active
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

- The artifact or its source (CSS/HTML, the document file, screenshots, or a style spec).
- The intended context (so the remediation maps to the right font group).

## Workflow

1. **Detect primary typefaces.** Read the CSS `font-family` stacks / document style / theme.
   Flag any banned face from `doctrine/references/ai-slop-banned-fonts.md` used as primary,
   and flag bare system stacks used alone.
2. **Detect secondary slop.** Flag Space Grotesk/Poppins/Montserrat/Nunito and standalone
   Source Sans used as the distinctive choice.
3. **Detect structural slop:** one font for everything; mid-weights only (no extremes);
   near-identical size steps; wide-tracked body; pure-black body text.
4. **Score** each finding (primary-font slop is critical; structural slop is major/minor).
5. **Remediate deliberately:** propose a non-slop pairing + scale for the artifact's group via
   `font-selection-and-pairing`; state the replacement and reason.
6. **Report** findings → fixes, with before/after.

## Anti-Patterns

- Swapping Inter for another single sans and calling it fixed.
- Removing a banned font but keeping monotype, timid weights, or wide-tracked body.

## Outputs

- A findings list (each tagged critical/major/minor with the rule it breaks) and a stated,
  non-slop remediation ready to apply.

## Examples

- `examples/typography-audit-filled.md` — a filled audit of a sample SaaS landing-page stylesheet
  (Inter body + Geist display + Space Grotesk accent over a bare system stack): each banned and
  secondary-slop face detected with the rule it breaks, scored critical/major/minor, then one
  deliberate non-slop remediation (Bricolage Grotesque 800 → Hanken Grotesk 400, Group 3) mapped
  finding-by-finding with the before/after CSS.

## References

- `doctrine/references/ai-slop-banned-fonts.md`, `pairing-principles.md`,
  `type-scale-and-spacing.md`.
<!-- dual-compat-end -->
