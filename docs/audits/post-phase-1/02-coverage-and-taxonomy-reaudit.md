# 02 (RE-AUDIT) — Coverage & Taxonomy after Phase 1

**Engine:** `C:\wamp64\www\design-system-skills`
**Baseline scored:** `docs/initial-analysis/02-coverage-and-taxonomy.md` → **48 / 100** (37 skills, 6 groups)
**Gap list cross-checked:** `docs/initial-analysis/04-gap-analysis-new-skills.md` (68-skill P0/P1/P2 plan)
**Inventory now:** **52 skills** across **13 numbered groups + 1 cross-cutting** (excludes `_TEMPLATE`).
**Date:** 2026-06-21
**Verdict:** the restructure is real and the disqualifying P0 gaps are closed. Taxonomy is now sound; **coverage is still mid-build** (P1/P2 backlog large, four groups thin). New score reflects structure-fixed-but-thinly-stocked.

---

## 1. What actually changed (Phase 0 + Phase 1)

**Phase 0 — restructure (the 48→delta driver):** the 6-drawer cabinet became the proposed **14-drawer** one, exactly per the baseline's §4 plan:

| # | Group on disk | Skills |
|---|---|---:|
| 00 | cross-cutting-ops-qa-a11y *(co-activates)* | 6 |
| 01 | typography-and-fonts | 4 |
| 02 | color-brand-and-visual-identity | 6 |
| 03 | layout-grid-and-composition | 2 |
| 04 | web-and-ui-design | 11 |
| 05 | ux-process-research-and-psychology | 4 |
| 06 | sector-and-domain-ux | 3 |
| 07 | mobile-ios-android-cross-platform | 3 |
| 08 | motion-and-interaction | 1 |
| 09 | design-systems-tokens-and-theming | 3 |
| 10 | content-design-and-ux-writing | 2 |
| 11 | imagery-illustration-and-art-direction | 2 |
| 12 | data-viz-and-dashboards | 2 |
| 13 | presentations-and-documents | 3 |
| — | **TOTAL** | **52** |

Honesty fixes landed: "02 Document Formatting" (which was decks) is gone — group 13 is now honestly **Presentations & Documents** with real doc skills; "05 Layout-and-Data-viz" is split into **03 Layout** and **12 Data Viz**; brand+colour fused into honest **02**; accessibility/tokens/content/imagery now have **named homes with real skills**, not empty drawers.

**Two honest consolidations to note in the count (not skill loss):**
- The baseline's 7–8 `deck-*` skills were collapsed into one **`deck-system`** skill that owns the shared deck-craft discipline and routes purposes via variants. This is *better* taxonomy (one discipline, not eight near-duplicates) but means group 13's headcount looks smaller than the baseline's "8 decks."
- `brand-alignment` (a baseline 04 skill) is no longer present as a standalone folder — consolidated into the brand cluster. Net originals carried forward + new = the 52 on disk.

**Phase 1 — infill:** 23 net-new P0 skills added, 10 existing hardened. Net-new skills observed on disk include: `accessible-color-and-contrast`, `dark-mode-and-theming`, `responsive-and-adaptive-layout`, `navigation-and-information-architecture`, `landing-page-and-conversion-design`, `empty-error-and-loading-states`, `ux-research-and-usability-testing`, `wireframing-and-prototyping`, `cross-platform-design-parity`, `design-tokens-and-naming`, `component-library-architecture`, `design-handoff-and-dev-spec`, `ux-writing-and-microcopy`, `error-empty-and-system-messaging`, `photography-art-direction`, `iconography-system-design`, `dashboard-and-data-product-design`, `docx-report-and-document-formatting`, `pdf-proposal-and-bankable-document-design`, `accessibility-wcag-2-2-compliance`, `internationalization-and-rtl-design`, `performance-as-ux-and-core-web-vitals`, `design-qa-and-pre-launch-review`.

---

## 2. Taxonomy re-score — **71 / 100**  (Δ **+23** vs 48)

Scored on the same ruthless bar (default 45–65; 70+ needs extraordinary justification). 70+ is earned here **only** because the restructure is not cosmetic — every structural defect the baseline itemised (§3.1–3.9) is materially fixed, and the fixes are backed by real routable skills, not empty folders. It does **not** go higher because coverage depth is still mid-build and four groups are starved.

| Criterion | Weight | Baseline | Now | Rationale for the new score |
|---|---|---|---|---|
| **Collective exhaustiveness** | 25 | 9 | **20/25** | Every previously-homeless domain now has a group *and* at least one real skill: accessibility + i18n + performance + QA (00), tokens/components/handoff (09), content/UX-writing (10), imagery/iconography (11), data-viz split out (12), real doc formatting (13). The −5 is honest: groups 09/10/11/12 each hold only their P0 seed (2–3 skills), and named-but-unbuilt concerns remain (illustration systems, AI-image direction, 3D, motion depth, sector verticals, mobile gesture/ASO, ethics/inclusive/email/voice). A home existing ≠ the domain being covered. |
| **Mutual exclusivity** | 20 | 8 | **16/20** | 03's grab-bag is decomposed into 04/05/06/08 + cross-cutting; the three audits are consolidated into 00 (`design-audit`, `visual-product-slop-audit` + a11y/QA) — no longer scattered. Clean boundaries now. −4: group 04 still carries 11 skills mixing core UI craft with AI-native UX (`ai-agent-ux`, `ai-output-design`) and state/nav/landing patterns — it is the next decomposition candidate; minor content-vs-craft overlap between 10's `error-empty-and-system-messaging` and 04's `empty-error-and-loading-states` (intentional pairing, but a boundary to watch). |
| **Balance / sizing** | 15 | 4 | **9/15** | Gini greatly improved: the old 03 held 43% (16/37); the new top group (04) holds 21% (11/52) and most groups sit at 2–6. Still −6: group **08 = 1 skill** (single `motion-design`), and **03/10/11/12 = 2 each** are starved seeds; 04 at 11 is heavy. Distribution is healthy-ish but not yet even. |
| **Scalability to 75–100** | 20 | 9 | **15/20** | The 14-drawer structure pre-allocates a labelled slot for every planned skill in the gap list, so the remaining 53 skills *infill* rather than force a re-org — the baseline's core complaint is resolved. −5: group 04 will need an internal split (or a 05/06 sibling) before it absorbs its remaining P1s and stays one-screen navigable; the structure scales, but 04 is the pressure point. |
| **Naming clarity & honesty** | 10 | 5 | **9/10** | The two actively-misleading names are gone: 13 is honestly Presentations **& Documents** (with DOCX/PDF skills present), and Layout vs Data-viz are separate honest groups. `00-cross-cutting` correctly signals co-activation. −1: group 04 "web-and-ui-design" is a slightly broad label for what is now foundations+states+nav+landing+AI-UX. |
| **Doctrine alignment** | 10 | 13→cap13 | **13/10→cap 13** | Still the engine's best asset and now *strengthened*: anti-slop audits consolidated in 00, the distinctive-by-design gate retained in 04, and the CLAUDE.md router enforces dynamic glob-based discovery so new anti-slop skills appear with no registration. Capped contribution applied. |
| **Total** | 100 | 48 | **71** | The cabinet now has the right drawers, honestly labelled, each with at least its keystone skill — but four drawers hold only a seed and one drawer (04) is overloaded. Structure: solved. Stocking: half-done. |

**One-line verdict:** the restructure is genuine and earns the 70-line — 14 honestly-named, balanced-enough drawers with real skills in every previously-empty one — but with 08/10/11/12 still at seed depth and the full P1/P2 backlog outstanding, this is a fixed-skeleton with half its muscle, not yet a world-class body.

---

## 3. P0 gap closure — **24 / 24 CLOSED (100%)**

The gap list (`04-gap-analysis-new-skills.md`) carries **24 P0 items**. Cross-checked against skills on disk:

| # | P0 skill (gap list) | Target group | On disk? |
|---|---|---|---|
| 4 | dark-mode-and-theming | 02 | ✅ |
| 5 | accessible-color-and-contrast | 02 | ✅ |
| 8 | responsive-and-adaptive-layout | 03 | ✅ |
| 12 | navigation-and-information-architecture | 04 | ✅ |
| 13 | landing-page-and-conversion-design | 04 | ✅ |
| 14 | empty-error-and-loading-states | 04 | ✅ |
| 18 | ux-research-and-usability-testing | 05 | ✅ |
| 20 | wireframing-and-prototyping | 05 | ✅ |
| 27 | cross-platform-design-parity | 07 | ✅ |
| 34 | design-tokens-and-naming | 09 | ✅ |
| 35 | component-library-architecture | 09 | ✅ |
| 36 | design-handoff-and-dev-spec | 09 | ✅ |
| 40 | ux-writing-and-microcopy | 10 | ✅ |
| 41 | error-empty-and-system-messaging | 10 | ✅ |
| 44 | photography-art-direction | 11 | ✅ |
| 45 | iconography-system-design | 11 | ✅ |
| 50 | dashboard-and-data-product-design | 12 | ✅ |
| 53 | pitch-deck-narrative-and-craft | 13 | ✅ *(satisfied by `deck-system`, which explicitly owns narrative arc / slide economy / builds / presenter craft and routes deck purposes by variant — consolidation, not omission)* |
| 54 | docx-report-and-document-formatting | 13 | ✅ |
| 55 | pdf-proposal-and-bankable-document-design | 13 | ✅ |
| 59 | accessibility-wcag-2-2-compliance | 00 | ✅ |
| 60 | internationalization-and-rtl-design | 00 | ✅ |
| 61 | performance-as-ux-and-core-web-vitals | 00 | ✅ |
| 62 | design-qa-and-pre-launch-review | 00 | ✅ |

**All 24 P0 gaps are closed.** This includes every disqualifying gap the gap analysis named: accessibility, dark mode, design tokens, dev handoff, doc formatting (DOCX/PDF), state design, i18n/RTL, performance-as-UX, UX research, prototyping, conversion/landing, navigation/IA, component architecture, UX writing, iconography, photo art-direction, dashboards, and design QA. The "world-class credibility" floor is met.

> Note on `xlsx-and-financial-model-presentation` (#56) — that is a **P1**, not P0; group 13 currently has DOCX + PDF + decks but no XLSX skill yet. Correctly out of P0 scope.

---

## 4. What remains — P1/P2 backlog (≈44 of 68 gap skills still open)

P0 is done (24). The gap list totals 68 proposed skills; **~44 P1/P2 remain unbuilt.** Major outstanding clusters:

**P1 still open (high value, expected of a top studio):**
- 01: variable-fonts-and-opentype, fluid-responsive-typography
- 02: logo-and-wordmark-design
- 03: editorial-and-long-form-layout, composition-and-visual-hierarchy
- 04: onboarding-and-first-run, trust-credibility-and-social-proof, component-states-and-interaction-fidelity
- 05: journey-mapping-and-service-design, heuristic-evaluation-and-design-critique
- 06: fintech-and-financial-product-ui, ecommerce-and-checkout-ux
- 07: touch-gesture-and-haptics, app-store-presence-and-aso
- 08: micro-interactions-and-feedback
- 09: figma-and-tooling-workflow
- 10: voice-tone-and-content-style-guide
- 11: illustration-style-and-systems, ai-image-generation-art-direction
- 12: chart-selection-and-encoding
- 13: xlsx-and-financial-model-presentation
- 00: design-critique-and-review-facilitation, inclusive-and-assistive-design, design-ethics-and-anti-dark-patterns, email-and-newsletter-design

**P2 still open (differentiators/depth):** multilingual-non-latin-type, brand-voice-and-verbal-identity, print-and-production-layout, behavioral-design-and-persuasion-ethics, gov-ngo + education sector UX, mobile-adaptive-and-foldables, page-transitions-and-choreography, scroll-and-parallax-storytelling, multi-brand-and-white-label-theming, design-system-governance-and-versioning, content-modeling-and-information-design, 3d-webgl-and-immersive-visuals, data-illustration-and-infographics, analytical-report-and-exhibit-design, editorial-and-whitepaper-design, template-and-master-system-design, sustainable-and-green-ux, conversational-and-voice-ui.

---

## 5. Per-group sizing now — healthy vs thin

| Group | Count | Status | Note |
|---|---:|---|---|
| 00 cross-cutting | 6 | **Healthy** | a11y, i18n, perf, QA + 2 audits — strongest infill; co-activation pattern correct. |
| 01 typography | 4 | **OK (seed-stable)** | unchanged; no P0 owed. P1 variable-fonts/fluid-type still owed. |
| 02 color/brand | 6 | **Healthy** | dark-mode + accessible-contrast added on top of brand/colour base. |
| 03 layout | **2** | **THIN** | only layout-grid + responsive; owes editorial/composition (P1). |
| 04 web-and-ui | 11 | **Heavy** | overloaded; next decomposition candidate, but well-stocked. |
| 05 ux-process | 4 | **OK** | research + prototyping added; owes journey-mapping/heuristics (P1). |
| 06 sector UX | 3 | **THIN** | no new P0 (all P1/P2); fintech/ecomm still owed. |
| 07 mobile | 3 | **THIN-ish** | cross-platform-parity added to ios/android; owes gesture/ASO (P1). |
| 08 motion | **1** | **STARVED** | single `motion-design`; the most under-built group on disk. |
| 09 design-systems | 3 | **Adequate (P0 complete)** | tokens + components + handoff — all three P0s present; P1/P2 governance owed. |
| 10 content | **2** | **THIN** | both P0s present (microcopy + messaging); P1 voice/tone owed. |
| 11 imagery | **2** | **THIN** | both P0s present (photo + icons); illustration/AI-image (P1) owed. |
| 12 data-viz | **2** | **THIN** | dashboard (P0) + data-viz; chart-encoding (P1) owed. |
| 13 presentations/docs | 3 | **Adequate (P0 complete)** | deck-system + docx + pdf — all P0s; xlsx/whitepaper/templates owed. |

**Healthy:** 00, 02, 04 (over-full), and P0-complete 09/13.
**Thin/starved:** **08 (1)**, and the 2-skill seeds **03, 10, 11, 12**; **06/07** under-built on the P1 axis.

The pattern is consistent: every group now has its **P0 keystone(s)**, but the four net-new/split groups (10, 11, 12 and motion's 08) carry only seeds, and the P1 layer that gives a group "studio depth" is the next build wave.
