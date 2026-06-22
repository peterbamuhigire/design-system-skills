# 05 - Per-Output-Type Readiness Re-Audit

**Date:** 2026-06-22
**Scope:** What an agent can produce when guided only by the current design-system skills and
doctrine.
**Score:** **78 / 100** (prior post-v2 score: 75)

## Verdict

Output readiness improved again after the final cleanup. The group-04 split makes web, conversion,
and email routing clearer, the reauthored active heads reduce friction for agents, and stale active
sibling paths no longer misroute output work. The score does not jump dramatically because the
remaining blockers are mostly execution-mile problems: the engine specifies artifacts well, but it
does not render files, run client matrices, publish tokens through CI, or implement
Flutter/SwiftUI/Compose code. React Native/Expo handoff is now stronger, but not a full app-build
owner.

## Output ranking

| Rank | Output type | Prior v2 | Current | Why it moved |
|---:|---|---:|---:|---|
| 1 | Web application / SaaS UI | 82 | **83** | Better routing after group split; component states, practical UI, webapp shell, AI UX, and micro-interactions compose cleanly. Still no deep front-end implementation owner. |
| 2 | Marketing website / landing page | 80 | **82** | Group 14 gives landing, trust, onboarding, nav/IA, and states a coherent home. Still missing scroll-storytelling/page-transition craft. |
| 3 | Design deliverable / handoff | 78 | **81** | Figma workflow, tokens, component specs, and handoff form a strong chain with cleaner routing. CI token publishing and two-way Figma/code sync remain outside scope. |
| 4 | Data product / dashboards | 78 | **79** | Dashboard, chart-selection, data-viz, and accessibility are well covered. Advanced time-series, geospatial, and large cross-filter systems remain thin. |
| 5 | Spreadsheet / financial-model exhibit | 76 | **78** | XLSX has a real exhibit owner. Actual workbook generation/model logic remains external. |
| 6 | Proposal / pitch | 76 | **78** | DOCX/PDF/deck/storytelling are stronger together under group 13. PPTX rendering remains absent. |
| 7 | Business document / DOCX-PDF | 75 | **77** | Stronger document cluster after email/XLSX/storytelling consolidation. No python-docx/Typst/LaTeX render pipeline. |
| 8 | Brand / visual identity | 74 | **76** | Logo, brand identity, style guide, color, and type now compose well. Identity architecture and large asset-library governance remain missing. |
| 9 | iOS app presentation layer | 73 | **75** | Current Apple presentation guidance remains solid: Liquid Glass constraints, SF Symbols 8, haptics, accessibility, app-store craft. Code surfaces remain external. |
| 10 | Android app presentation layer | 72 | **74** | Material 3 Expressive, predictive back, touch/haptics, and store craft are present. Foldables and Wear/widgets are missing. |
| 11 | Email | 72 | **74** | Correctly relocated to the documents/output group. Specs the hostile email environment well; does not run Litmus/Email-on-Acid matrices. |
| 12 | Cross-platform mobile / RN-Flutter | 67 | **72** | Parity, touch, haptics, store craft, and RN/Expo implementation-readiness gates are useful. Flutter/full-app implementation depth remains outside scope, so it remains the floor. |

**Blended readiness score:** 78 / 100.

## What improved

1. **Routing clarity improves output quality.** An agent now finds conversion/page-pattern work in
   group 14 instead of threading through an overloaded web/UI drawer.
2. **Email is now in the right output family.** It sits beside DOCX/PDF/XLSX/decks/storytelling
   instead of being treated as a web UI sibling.
3. **Web and marketing compositions are easier to assemble.** `webapp-gui-design`,
   `practical-ui-design`, `interaction-design-patterns`, `component-states-and-interaction-fidelity`,
   `landing-page-and-conversion-design`, `trust-credibility-and-social-proof`, and
   `onboarding-and-first-run-design` now have cleaner boundaries.
4. **The audit/fix loop is stronger.** `product-design-audit` can identify cross-surface issues and
   hand them to the right remediation skill.
5. **Stale active path references are gone.** Agent routing is now less likely to fall into old
   group names during output assembly.
6. **RN/Expo parity handoff is less thin.** Navigation shell, platform branches, state model,
   native APIs, permission states, list performance, release-build performance checks, and
   EAS/build-channel implications are now explicit.

## What still caps the score

- **No render pipeline:** no owned path for `.docx`, `.pdf`, `.pptx`, `.xlsx`, HTML email, or
  production front-end generation.
- **No full platform implementation layer:** iOS/Android/Flutter guidance remains
  presentation-layer guidance, and RN/Expo is now handoff-ready rather than a deep app-engineering
  owner.
- **No token publishing pipeline:** token structure and exports are covered, but CI publishing and
  governance/versioning are not deep enough.
- **No advanced motion/page storytelling depth:** group 08 is still thin, and marketing sites lack
  a true scroll/story choreography owner.

## Current best-supported outputs

The engine is strongest for **web application design**, **marketing/conversion sites**, **handoff
specs**, **data products**, and **document/spreadsheet/proposal presentation design**.

## Current weakest output

**Cross-platform mobile remains weakest at 72.** The design advice and RN/Expo handoff are now
better, but missing Flutter/full-app implementation keeps it below the native-platform and
web-output scores.

## Bottom line

The design engine is now output-ready for high-quality specs and design direction, with a few output
types already in the low-80s. It is not yet an end-to-end artifact production engine. Moving the
overall output score beyond the high-70s depends less on writing more design advice and more on
deciding whether this repo owns render/build execution or explicitly hands it to another engine.
