# Control-plane adoption

This engine adopts the shared ten-engine contract from
`C:\wamp64\www\skills-web-dev\docs\engine-control-plane.md`. Design doctrine
remains authoritative for typography, colour, layout, UI/UX, document and
presentation appearance, visual assets, and anti-slop rules.

## Local roles and commands

| Role | Responsibility | Required evidence |
|---|---|---|
| Design planner | Define audience, hierarchy, constraints, tokens, and acceptance states. | Design decision record. |
| Brand guardian | Check identity, typeface, colour, tone, and cross-surface consistency. | Typeface/brand decision. |
| Accessibility reviewer | Check contrast, focus, readability, motion, and assistive use. | Contrast and accessibility results. |
| Visual-finish reviewer | Inspect rendered output at required sizes and fix implementation drift. | Rendered comparison and findings. |

Route thin commands `design-audit`, `visual-qa`, `finish-gate`, and `handoff`
to existing skills. `scripts/validate_design_delivery_evidence.py` is the
deterministic evidence adapter for rendered delivery manifests. A command may
recommend a typeface or token but may not
override design doctrine's banned-font and evidence rules.

## Hook and release contract

- `preflight` records surface, audience, output format, viewport/page sizes,
  brand constraints, and required render path.
- `context` loads canonical design doctrine, tokens, font manifest, prior
  reference, and known implementation constraints.
- `before_write` checks asset provenance, font licensing, scope, reversibility,
  and cross-engine ownership.
- `after_write` renders the artifact and runs typeface, contrast, layout,
  overflow, responsive, and asset-manifest checks as applicable.
- `release` requires typeface decision, rendered output, contrast result,
  asset manifest, and an explicit implementation or document-tooling handoff.
- `stop` preserves source/reference state, unresolved visual findings, missing
  renders, and the next owner.

Missing renders or contrast evidence are `NOT ASSESSED`, not PASS. The
anti-slop checklist remains a hard release gate.

## Human approval adapter

Live design-system and agent-interface changes are detailed in
[`approval-enforcement.md`](approval-enforcement.md) and catalogued in
[`approval-adapter.json`](approval-adapter.json). The checkpoint interaction
must expose correction, rejection, escalation, and rollback before approval.
