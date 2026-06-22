# 02 (RE-AUDIT) — Coverage & Taxonomy after the book-informed v2 plan

**Engine:** `C:\wamp64\www\design-system-skills`
**Prior re-audit:** `docs/audits/post-phase-1/02-coverage-and-taxonomy-reaudit.md` → **71 / 100** (52 skills, 13 groups + cross-cutting)
**v2 plan scored against:** `docs/plans/hardening-june/PLAN-v2-book-informed.md` (Tracks A–E)
**Gap list cross-checked:** `docs/initial-analysis/04-gap-analysis-new-skills.md` (68-skill P0/P1/P2 plan)
**Inventory now:** **81 skills** across **13 numbered groups + 1 cross-cutting** (excludes `_TEMPLATE`).
**Date:** 2026-06-22
**Verdict:** the P1 wave is real and lands depth in every previously-starved group; the four thin-seed groups (03/10/11/12) and starved-08 from the prior audit are materially resolved. The taxonomy is now near-complete on coverage, and the two NEW doctrine references strengthen the doctrine moat. The single remaining structural defect is **group 04 (15 skills) is now genuinely overloaded** and is the one mandatory decomposition. Score reflects "stocked + doctrine-deepened, with one overloaded drawer."

---

## 1. What changed since the 71-line (the delta driver)

**Headcount: 52 → 81 (+29 skills).** The prior re-audit's central complaint — "fixed skeleton with half its muscle; 08/10/11/12 at seed depth, four drawers hold only a seed" — is the thing this wave was built to close.

Per-group delta vs the prior re-audit's table:

| Group | Prior (52) | Now (81) | Δ | What landed |
|---|---:|---:|---:|---|
| 00 cross-cutting | 6 | **11** | +5 | `design-critique-and-review-facilitation`, `inclusive-and-assistive-design`, `design-ethics-and-anti-dark-patterns`, `ux-remediation-and-redesign` (Track B net-new), `product-design-audit` |
| 01 typography | 4 | **6** | +2 | `variable-fonts-and-opentype-features`, `fluid-responsive-typography` |
| 02 color/brand | 6 | **7** | +1 | `logo-and-wordmark-design` |
| 03 layout | 2 | **4** | +2 | `composition-and-visual-hierarchy`, `editorial-and-long-form-layout` |
| 04 web-and-ui | 11 | **15** | +4 | `component-states-and-interaction-fidelity`, `onboarding-and-first-run-design`, `trust-credibility-and-social-proof`, `email-and-newsletter-design` |
| 05 ux-process | 4 | **7** | +3 | `heuristic-evaluation-and-design-critique`, `journey-mapping-and-service-design`, `demo-driven-design-process` (Track B P2 net-new) |
| 06 sector UX | 3 | **5** | +2 | `ecommerce-and-checkout-ux`, `fintech-and-financial-product-ui` |
| 07 mobile | 3 | **5** | +2 | `app-store-presence-and-aso`, `touch-gesture-and-haptics` |
| 08 motion | 1 | **2** | +1 | `micro-interactions-and-feedback` |
| 09 design-systems | 3 | **4** | +1 | `figma-and-tooling-workflow` |
| 10 content | 2 | **3** | +1 | `voice-tone-and-content-style-guide` |
| 11 imagery | 2 | **4** | +2 | `illustration-style-and-systems`, `ai-image-generation-art-direction` |
| 12 data-viz | 2 | **3** | +1 | `chart-selection-and-encoding` |
| 13 presentations/docs | 3 | **5** | +2 | `xlsx-and-financial-model-presentation` (Track B net-new), `design-storytelling-and-case-studies` (Track B P2 net-new) |
| **TOTAL** | **52** | **81** | **+29** | |

**The 4 net-new (book-justified) skills are all on disk:** `ux-remediation-and-redesign` (00), `xlsx-and-financial-model-presentation` (13), `demo-driven-design-process` (05), `design-storytelling-and-case-studies` (13). Track B is complete.

**The 2 new doctrine references are present** at `doctrine/references/`: `creative-selection-and-taste.md` (Kocienda demo-loop / production-method) and `interaction-anti-patterns.md` (Neil + Maioli bad-UX catalogue). These are the highest-leverage items in the plan (cited by `distinctive-by-design`, the critique/process skills, and the group-00 audits), and they raise the doctrine criterion materially over the prior audit.

**Track D P1 wave is essentially fully built:** every named P1 in Track D appears on disk — micro-interactions, touch/haptics, onboarding, trust/social-proof, composition, editorial layout, journey-mapping, heuristic-eval, critique-facilitation, fintech, ecommerce, ASO, variable-fonts, fluid-type, illustration, ai-image, chart-selection, email, inclusive, ethics, figma-workflow.

---

## 2. Taxonomy re-score — **78 / 100**  (Δ **+7** vs 71)

Scored on the same ruthless bar (default 45–65; 70+ needs extraordinary justification). The +7 is earned, not inflated: the prior audit's two biggest deductions were (a) four starved seed-groups + one starved (08), losing points on *balance* and *exhaustiveness*, and (b) coverage depth being mid-build. Both are now substantially closed by a +29 wave that put genuine P1 depth into every thin group AND added two doctrine refs that deepen the engine's actual moat. It does **NOT** cross 80 because one defect the prior audit explicitly flagged — group 04 overload — got **worse** (11 → 15), and a handful of P1/P2 differentiators plus the inoculation-notes housekeeping remain open.

| Criterion | Weight | Prior | Now | Rationale for the new score |
|---|---|---|---|---|
| **Collective exhaustiveness** | 25 | 20 | **22/25** | Every group now carries P0 keystone **plus** its core P1 depth, not just a seed: 03 has composition+editorial; 08 has micro-interactions; 10 has voice/tone; 11 has illustration+ai-image; 12 has chart-encoding; 00 added critique/inclusive/ethics/remediation. The "a home existing ≠ the domain covered" complaint is largely answered. −3 is honest: P2 differentiators still absent (3d/webgl, scroll-storytelling, page-transitions, multilingual-non-latin type, print/production, gov-ngo + education sector, mobile-foldables, governance/versioning, multi-brand theming, sustainable-ux, conversational-ui — the last correctly *deferred* per Track E). |
| **Mutual exclusivity** | 20 | 16 | **15/20** | Boundaries remain clean across 00/03/05/08–13. **−5 (worse by 1):** group 04 at 15 skills now spans foundations (`practical-ui-design`, `premium-ui-ux-design`, `webapp-gui-design`), AI-native UX (`ai-agent-ux`, `ai-output-design`), state/nav/landing/onboarding/trust patterns, the `distinctive-by-design` doctrine gate, AND `email-and-newsletter-design` — which is a distinct *channel* (Email output type) sitting awkwardly in a web/UI drawer. The intentional 04↔10 messaging pairing persists (`empty-error-and-loading-states` vs `error-empty-and-system-messaging`). The grab-bag risk the prior audit named has materialized in 04. |
| **Balance / sizing** | 15 | 9 | **11/15** | Big improvement at the bottom: 08 is no longer 1 (now 2), and the four 2-skill seeds are now 3–4 each. Gini at the low end is fixed. **−4:** the *top* got heavier — 04 is now **15/81 = 19%**, more skills than the prior whole-engine top share, and 2.1× the next-largest group (00 and 05 at 7→11/7). Distribution is bimodal: a fat 04 + healthy middle. The imbalance moved from "starved tail" to "overloaded head." |
| **Scalability to 75–100** | 20 | 15 | **17/20** | At 81 the engine is now *inside* the 75–100 target band, and the 14-drawer structure absorbed the entire P1 wave without a re-org — the core scalability thesis held. **−3:** group 04 has now hit the pressure point the prior audit predicted; it cannot absorb further skills (e.g. more AI-UX, more conversion patterns) without an internal split. Scaling further requires the 04 decomposition first. |
| **Naming clarity & honesty** | 10 | 9 | **9/10** | Honest labels retained; new skill names are precise. −1 unchanged: "04 web-and-ui-design" is now an even broader umbrella for foundations + states + nav + landing + onboarding + trust + AI-UX + email — the label undersells the sprawl. |
| **Doctrine alignment** | 10 | 13→cap 13 | **13/10→cap 13** | Strengthened again and now the clearest score-mover: the **two new doctrine references** (`creative-selection-and-taste.md` = the missing production method; `interaction-anti-patterns.md` = the bad-UX catalogue) give the anti-slop / distinctive-by-design moat a *method* and a *failure taxonomy* it lacked, both cited cross-engine. Capped contribution applied (already at ceiling). −0 within cap; the only open doctrine housekeeping is the Track-A "inoculation notes" (explicit do-NOT-adopt lines for glassmorphism / fixed red-blue semantics / bounce easing) which could not be verified as landed in the named skills. |
| **Total** | 100 | 71 | **78** | Coverage is now genuinely stocked top-to-bottom and the doctrine moat is deeper — but one drawer (04) is overloaded and is the single mandatory fix before the engine can be called world-class-balanced. |

**One-line verdict:** the v2 wave converted a fixed-skeleton-with-half-its-muscle into a stocked, doctrine-deepened engine inside the 75–100 band — but it solved the starved tail by piling the head, leaving group 04 (15) as the one overloaded drawer that must be split before this clears 80.

---

## 3. Prior thin-group concerns — resolution status

The 71-line flagged **08/03/10/11/12 thin/starved** and **04 overloaded**. Status now:

| Prior concern | Prior | Now | Resolved? |
|---|---:|---:|---|
| 08 motion **STARVED (1)** | 1 | 2 | **Partially** — no longer starved (micro-interactions added); still the smallest drawer. The two P2s (page-transitions, scroll-storytelling) remain open, so 08 is "thin-OK," not deep. |
| 03 layout **THIN (2)** | 2 | 4 | **Resolved** — composition + editorial landed; only P2 print/production owed. |
| 10 content **THIN (2)** | 2 | 3 | **Resolved (P1)** — voice/tone landed; only P2 content-structure/readability owed (Track C rescope). |
| 11 imagery **THIN (2)** | 2 | 4 | **Resolved** — illustration + ai-image landed; only P2 3d/webgl + data-illustration owed. |
| 12 data-viz **THIN (2)** | 2 | 3 | **Resolved (P1)** — chart-selection landed; only P2 analytical-exhibit owed. |
| 04 **HEAVY (11)** | 11 | **15** | **NOT resolved — worse.** This is now the engine's primary structural debt. |

**Net:** 5 of 6 prior thin-group concerns resolved; the 6th (04 overload) regressed and is now the headline issue.

---

## 4. Per-group sizing now — healthy / thin / overloaded

| Group | Count | Status | Note |
|---|---:|---|---|
| 00 cross-cutting | 11 | **Healthy (full)** | a11y, i18n, perf, QA, critique, inclusive, ethics, remediation + 3 audits. Co-activation pattern intact. Largest *legitimately*, because it is the cross-cutting catch-all by design — but watch it: if it keeps absorbing, split audits vs ops/qa vs a11y/ethics. |
| 01 typography | 6 | **Healthy** | + variable-fonts + fluid-type; P2 multilingual-non-latin owed. |
| 02 color/brand | 7 | **Healthy** | + logo-and-wordmark; P2 brand-voice/verbal owed. |
| 03 layout | 4 | **Healthy** | + composition + editorial; P2 print owed. |
| 04 web-and-ui | **15** | **OVERLOADED** | **Split recommended (see §5).** 19% of the engine; mixes foundations + states + nav + landing + onboarding + trust + AI-UX + email. |
| 05 ux-process | 7 | **Healthy** | + heuristics + journey-mapping + demo-driven; P2 behavioral-design owed. |
| 06 sector UX | 5 | **OK** | + fintech + ecommerce; P2 gov-ngo + education sector owed. |
| 07 mobile | 5 | **OK** | + ASO + gesture/haptics; P2 foldables owed. |
| 08 motion | **2** | **Thin-OK** | + micro-interactions; smallest drawer; P2 page-transitions + scroll-storytelling owed. |
| 09 design-systems | 4 | **OK** | + figma-workflow; P2 governance/versioning + multi-brand theming owed. |
| 10 content | **3** | **OK (P1 done)** | + voice/tone; P2 content-structure/readability owed. |
| 11 imagery | 4 | **Healthy** | + illustration + ai-image; P2 3d/webgl + data-illustration owed. |
| 12 data-viz | **3** | **OK (P1 done)** | + chart-selection; P2 analytical-exhibit owed. |
| 13 presentations/docs | 5 | **Healthy** | + xlsx + storytelling/case-studies; P2 whitepaper + template-master owed. |

**Healthy:** 00, 01, 02, 03, 05, 11, 13. **OK (P1 complete, P2 owed):** 06, 07, 09, 10, 12. **Thin-OK:** 08. **Overloaded:** 04.

---

## 5. Group-04 split recommendation (the one mandatory action)

Group 04 at 15 is no longer one-screen navigable and mixes three discernible clusters. Recommended decomposition into two (or three) honest drawers:

- **04 web-and-ui-design (foundations & craft)** — keep: `practical-ui-design`, `premium-ui-ux-design`, `webapp-gui-design`, `distinctive-by-design`, `form-ux-design`, `interaction-design-patterns`, `component-states-and-interaction-fidelity`, `empty-error-and-loading-states`. (≈8)
- **NEW 04b — conversion-patterns-and-page-types** (or fold into a renamed group): `landing-page-and-conversion-design`, `navigation-and-information-architecture`, `onboarding-and-first-run-design`, `trust-credibility-and-social-proof`. (≈4)
- **AI-native UX** (`ai-agent-ux`, `ai-output-design`) — strong candidate for its own small group or for co-locating with conversational-ui when that P2 ships.
- **`email-and-newsletter-design`** is mis-placed in a web/UI drawer — it is a distinct **Email** output channel. Move to cross-cutting (00) or a channels group; it does not belong under "web-and-ui."

This split also relieves the mutual-exclusivity (−5) and scalability (−3) deductions and is the cheapest path to crossing 80.

---

## 6. Gap-skill build progress & remaining backlog

**Of the 68 gap-list skills: ~52 are now built** (24 P0 + ~24 Track-D P1 + the 4 Track-B book-justified net-new that map onto gap items such as #56 xlsx). The remaining **~16 are P2 differentiators** plus a few deferred items.

**Remaining open (P2 unless noted):**
- 01: multilingual-and-non-latin-type
- 02: brand-voice-and-verbal-identity
- 03: print-and-production-layout
- 05: behavioral-design-and-persuasion-ethics
- 06: gov-ngo-and-public-sector-ux, education-and-elearning-ux
- 07: mobile-adaptive-and-foldables
- 08: page-transitions-and-choreography, scroll-and-parallax-storytelling
- 09: multi-brand-and-white-label-theming, design-system-governance-and-versioning
- 10: content-modeling/structure-and-readability (Track C rescope)
- 11: 3d-webgl-and-immersive-visuals, data-illustration-and-infographics
- 12: analytical-report-and-exhibit-design
- 13: editorial-and-whitepaper-design, template-and-master-system-design
- 00: sustainable-and-green-ux; conversational-and-voice-ui **(correctly DEFERRED per Track E — do not build from the misfiled book)**

**Track-A housekeeping still open:** the explicit "inoculation notes" (do-NOT-adopt lines for glassmorphism-as-best-practice, fixed red/blue semantics + shadow-only dark elevation, and `ease-*-back` bounce vs `motion-design` ζ≥0.7) could not be confirmed landed in the named target skills — verify and add if missing.

**P0 closure:** remains 24/24 (100%) — unchanged from the prior audit; no regressions.

---

## 7. Bottom line

- **Taxonomy: 78/100, Δ +7 vs 71.** Coverage is now stocked top-to-bottom and inside the 75–100 target band; the two new doctrine refs deepen the moat.
- **5 of 6 prior thin-group concerns resolved**; the 6th — group 04 overload (11→15) — regressed and is the single mandatory fix.
- **The one action that unlocks 80+:** split group 04, and relocate the mis-placed `email-and-newsletter-design`.
