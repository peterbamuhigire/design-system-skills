# 02 - Coverage and Taxonomy Re-Audit

**Date:** 2026-06-22
**Engine:** `C:\wamp64\www\design-system-skills`
**Inventory:** 82 active skills across 15 active groups, excluding `skills/_TEMPLATE`.
**Score:** **86 / 100** (prior post-v2 score: 78)

## Verdict

The taxonomy fix landed. The old overloaded group 04 is no longer the structural blocker:

- `04-web-and-ui-design` is now a focused UI-craft/foundations group with 9 skills.
- `14-conversion-and-web-page-patterns` now owns landing, navigation/IA, onboarding, trust, and
  empty/error/loading page states.
- `email-and-newsletter-design` moved to `13-presentations-and-documents`, which is the right
  channel/output-type home.

The taxonomy is now strong enough for the current 75-100 skill target band. The stale active
cross-links left by the split have been cleaned. Remaining deductions are from thin future-facing
groups and P2 differentiator gaps rather than from the core drawer structure.

## Current group inventory

| Group | Skills | Status | Note |
|---|---:|---|---|
| 00 cross-cutting ops / QA / a11y | 12 | Healthy | Large by design; owns audit, a11y, QA, ethics, remediation, and living slop-doctrine refresh. |
| 01 typography and fonts | 6 | Healthy | Good coverage; three plumbing skills still have no own refs. |
| 02 color, brand, visual identity | 7 | Healthy | Strong OKLCH/contrast/logo spine; active cross-links are current. |
| 03 layout, grid, composition | 4 | Healthy | Composition and editorial layout closed the old thin-group gap. |
| 04 web and UI design | 9 | Healthy | Split succeeded; now foundations, UI craft, AI UX, forms, interaction. |
| 05 UX process, research, psychology | 7 | Healthy | Strong demo-driven and remediation loop. |
| 06 sector and domain UX | 5 | OK | Healthcare/legal/fintech/ecommerce/generic sector coverage. |
| 07 mobile iOS/Android/cross-platform | 5 | OK | Good presentation-layer mobile; implementation depth remains external. |
| 08 motion and interaction | 2 | Thin but acceptable | No longer skeletal; still needs page transitions/scroll choreography. |
| 09 design systems, tokens, theming | 4 | OK | Strong token/handoff base; governance/versioning still P2. |
| 10 content design and UX writing | 3 | OK | Voice/tone landed; content-structure/readability remains P2. |
| 11 imagery, illustration, art direction | 4 | Healthy | C2PA/AI image and illustration slop gaps closed. |
| 12 data-viz and dashboards | 3 | OK | Chart-selection split is clean; analytical exhibits remain P2. |
| 13 presentations and documents | 6 | Healthy | Deck, DOCX, PDF, XLSX, email, storytelling now share an output group. |
| 14 conversion and web page patterns | 5 | Healthy | The old web/UI sprawl now has its own honest drawer. |

## What improved since the prior audit

| Prior issue | Current result |
|---|---|
| Group 04 had 15 skills and mixed foundations, page patterns, conversion, AI UX, and email. | Resolved. Group 04 has 9 skills; group 14 owns conversion/page patterns; email moved to group 13. |
| Email was misfiled under web/UI. | Resolved. It is now in presentations/documents as a channel/output artifact. |
| Thin groups 03, 10, 11, 12, and 08 needed P1 depth. | Mostly resolved. All have P1 owners; 08 remains intentionally small. |
| P1 wave might have been plan prose rather than disk reality. | Resolved. The named P1 skills exist and ship examples. |

## Score rationale

| Criterion | Score | Rationale |
|---|---:|---|
| Collective exhaustiveness | 22 / 25 | Core P0/P1 presentation-layer coverage is now broad and usable. P2 gaps remain: 3D/WebGL, print/production, scroll storytelling, foldables, public-sector/education UX, sustainable UX, and analytical exhibits. |
| Mutual exclusivity | 19 / 20 | The 04/14 split fixed the biggest boundary problem and active routing links now point to the right sibling homes. Some overlap remains in audits/remediation and color-selection vs color-system. |
| Balance and sizing | 14 / 15 | No active non-template group is wildly oversized. Group 08 is still thin at 2 skills, but no longer starved. |
| Scalability to 75-100 skills | 18 / 20 | The 15-group structure can absorb remaining P2s. It will need a decision before adding render-pipeline implementation skills. |
| Naming clarity | 10 / 10 | Group names are honest and active `SKILL.md` sibling links now point to current homes. |
| Doctrine alignment | 3 / 10 counted as bonus discipline | Anti-slop, WCAG 2.2, performance budgets, creative-selection, and anti-pattern doctrine are current and cross-cited; scored conservatively here to keep the total arithmetic honest. |

**Total:** **86 / 100**

## Remaining taxonomy work

1. Decide whether render-pipeline implementation becomes a new group or a formal handoff to other
   engines.
2. Add only P2 skills that change output readiness, not more near-duplicates.

## Bottom line

The taxonomy is no longer the bottleneck. It is balanced enough for current use and for a modest v3.
The next audit lift will come from deciding the render boundary and adding high-leverage P2 depth,
not from another broad P1-style expansion.
