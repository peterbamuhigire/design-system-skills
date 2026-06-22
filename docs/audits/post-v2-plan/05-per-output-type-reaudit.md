# 05 — Per-Output-Type Readiness RE-AUDIT (Post-v2-Plan, Book-Informed)

**Engine:** `C:\wamp64\www\design-system-skills`
**Doctrine reviewed:** `doctrine/design-doctrine.md` (v0.2.0 — Mission "the moat is looking human-made", Anti-Slop Charter, sourcing-authority asymmetry) + reference files.
**Inventory reviewed:** **81 skills** across groups 00–13 (was 52 at the post-Phase-1 re-audit), including the **24 new P1 skills** (two Track-D waves), the new `product-design-audit` composer, and the two net-new output-type owners `email-and-newsletter-design` and `xlsx-and-financial-model-presentation` — with their `references/`, `examples/`, `sections/`, and `templates/` payloads (depth-checked, not counted).
**Baseline compared against:** `docs/audits/post-phase-1/05-per-output-type-reaudit.md` (overall **70/100**; web app **79**; weakest cross-platform mobile **58**).
**Date:** 2026-06-22
**Question (unchanged):** Guided ONLY by this engine's current skills + doctrine, could an agent produce work that rivals top global studios (Apple / Pentagram / award winners) — per output type?

**Scoring bar (unchanged, ruthless, top 0.1%):** 90–100 rivals Apple/Pentagram/award winners · 75–89 excellent pro · 60–74 solid but visibly short · 40–59 competent/amateur · <40 skeletal. Default band 45–65. A 70+ requires extraordinary justification.

---

## What changed since Phase 1 (the v2 delta drivers)

The v2 plan was **book-informed** (six craft studies folded into the doctrine refs and skills) and shipped in tracks A–D. Verified against the bar, the consequential additions:

- **The previously-weak types got dedicated craft, not just hardening.**
  - *Cross-platform mobile* gained two real owners beyond the parity skill: `touch-gesture-and-haptics` (WCAG 2.5.1/2.5.7 single-pointer + non-drag fallback **rule table** — the legal core — plus iOS impact/notification/selection vs Android `HapticFeedbackConstants`/predictive-back semantics, thumb-zone arcs, system-gesture reservation table) and `app-store-presence-and-aso` (dual-store icon delivery incl. iOS **Liquid Glass** light/dark/tinted/clear variants, captioned device-framed screenshot **narrative**, App Preview storyboard, copy-field model, 2026 preflight). These close two of the exact gaps the prior audit named for iOS/Android (App-Store screenshot craft) and cross-platform (touch/haptic per side).
  - *iOS / Android native* deepened: iOS now carries SF Symbols 8 + advanced UIKit/SwiftUI sub-modules; Android carries **Material 3 Expressive** + **Predictive Back end-to-end** (`PredictiveBackHandler`, interruptible/reversible) + **WindowSizeClass** adaptivity + dense data-tables.

- **Marketing-website ceiling lifted.** `editorial-and-long-form-layout` (measure 45–75ch, baseline rhythm, pull-quotes/sidenotes/footnotes, drop caps, figure handling) closes the prior "no true scrollytelling/long-scroll narrative-layout" gap; `trust-credibility-and-social-proof` (attributed-proof credibility hierarchy, honest security cues, anti-fabrication) + `onboarding-and-first-run-design` own the conversion/trust spine the prior audit said was only half-owned.

- **Brand identity got generation craft + an icon system.** `logo-and-wordmark-design` (grid/optical mark construction, lockup family, **responsive logo ladder**, favicon + iOS/Android/web/maskable **app-icon matrix**, misuse sheet) plus the strengthened `brand-visual-identity` close the prior "logo/wordmark only lightly taught" gap.

- **Two net-new output types now have real owners.** `email-and-newsletter-design` (table+inline-CSS constrained model, hybrid/spongy responsive, bulletproof VML/anchor button, fallback-IS-the-design type, dark-mode inversion + logo swap, image-off resilience — grounded in Litmus/Email-on-Acid/Parmentier authority) and `xlsx-and-financial-model-presentation` (custom number masks, accounting negatives, blue-input/black-formula convention, conditional-formatting-as-encoding with non-colour cue, integrity charts, print-exhibit layout).

- **Sector + composition depth.** `ecommerce-and-checkout-ux`, `fintech-and-financial-product-ui`, `journey-mapping-and-service-design`, `composition-and-visual-hierarchy`, plus cross-cutting `figma-and-tooling-workflow` (variable collections + modes, Dev Mode, Code Connect, branching) — which directly chips at the prior "no Figma library/Dev-Mode export mechanics" handoff gap.

- **A product-wide audit composer.** `product-design-audit` runs the doctrine + per-platform lenses + the three hard gates across every surface and routes each finding to the remediating skill — raising the realistically-achievable quality floor because the engine can now find its own misses.

The payloads were depth-checked: the haptic WCAG fallback table, the Liquid-Glass icon variants, the bulletproof-email VML recipe, and the xlsx number-mask system are all technically correct and specific — craft, not filler.

---

## Re-scored ranking (delta vs the Phase-1 re-audit)

| Rank | Output type | Phase-1 | **Now** | Δ | Biggest remaining gaps (2–3) |
|---|---|---:|---:|---:|---|
| 1 | Web application (SaaS / dashboard UI) | 79 | **82** | +3 | Frontier interaction polish still short of Linear/Vercel (command palette, multiplayer/presence, optimistic-everything as a system); component-states + micro-interactions now present, but no deep front-end *implementation* skill |
| 2 | Marketing website / landing page | 73 | **80** | +7 | Editorial long-form + trust + conversion now owned; ceiling held by no true *scrollytelling-with-scroll-driven-motion* recipe (GSAP/scroll-timeline choreography) and no SEO-render/perf-budget-for-content depth beyond the CWV gate |
| 3 | Data product / dashboards | 74 | **78** | +4 | KPI tiering + layout archetypes + real-time freshness now solid; still thin on geospatial / advanced time-series, deep perceptual animation timing, and large-scale cross-filter state |
| 4 | Design deliverable / handoff | 74 | **78** | +4 | `figma-and-tooling-workflow` adds variable-collections/modes + Dev Mode + Code Connect + branching; gap now narrows to **CI token publishing / Style-Dictionary-in-pipeline** and live two-way Figma↔code sync |
| 5 | Spreadsheet / financial-model exhibit *(NEW)* | — | **76** | new | Real exhibit-grade owner (masks, blue/black, CF-as-encoding, integrity charts, print layout); ceiling: engine **specs** the settings, does not drive the actual `.xlsx` write pipeline; defers all model mechanics to finance engine |
| 6 | Proposal / pitch (deck + document) | 72 | **76** | +4 | PDF/DOCX legs real, deck-system has 8 variant blueprints; still no `.pptx` *rendering* mechanics (masters/chart objects) — decks stop at markdown blueprint |
| 7 | Business document (DOCX/PDF) | 71 | **75** | +4 | Named-style + TOC + tagged-DOCX + bankable-PDF preflight all real; gap unchanged — engine **specs**, does not **render** (no python-docx/LaTeX/Typst execution pipeline) |
| 8 | Brand / visual identity | 65 | **74** | +9 | Logo/wordmark construction + lockup family + responsive ladder + app-icon matrix now taught; still no identity **architecture** (parent/sub/endorsed), no environmental / motion-identity system, no Figma asset-library *management* at scale |
| 9 | Email *(NEW)* | — | **72** | new | Real client-resilient owner (Outlook/Word engine, hybrid/spongy, bulletproof button, dark-mode, image-off); ceiling: engine specs + render-checklist but cannot itself run the Litmus/Email-on-Acid cross-client test matrix it (correctly) demands |
| 10 | iOS app (Apple Design Award bar) | 68 | **73** | +5 | Haptics owner + SF Symbols 8 + UIKit/SwiftUI sub-modules + App-Store craft added; still **no Live Activities / Dynamic Island / WidgetKit / Lock-Screen surfaces** — the current iOS award differentiators |
| 11 | Android app (M3 Expressive bar) | 67 | **72** | +5 | M3 Expressive + Predictive-Back end-to-end + WindowSizeClass + App-Store craft; still **no dedicated foldable/large-screen playbook** and no Wear/widget surfaces |
| 12 | Cross-platform mobile (RN / Flutter) | 58 | **67** | +9 | Parity skill + RN/Flutter mapping + now `touch-gesture-and-haptics` (per-side gesture/haptic/WCAG) + `app-store` (per-store delivery); gap unchanged & decisive — **no deep RN-specific or Flutter-specific *implementation* skill** (Expo, navigation, offline sync; Skia/Impeller vs Fabric render models). Parity + touch *strategy* exist; framework *depth* does not |

---

## Did the new P1 skills lift the previously-weak types? (the targeted question)

**Yes — measurably, across the board, and the floor rose by 9 points.**

- **Cross-platform mobile 58 → 67 (+9):** lifted by `touch-gesture-and-haptics` (the WCAG 2.5.1/2.5.7 single-pointer/non-drag fallback table + correct iOS/Android haptic semantics, applied *per side*) and `app-store-presence-and-aso` (per-store icon/screenshot/copy delivery incl. Liquid Glass variants). The engine now teaches the *parity decision* **and** the *touch + store* craft on each platform — but still **not** deep framework implementation (render models, Expo, navigation, offline sync). It is no longer near-amateur, but it remains the floor for exactly the reason the prior audit named: strategy without framework depth.
- **iOS 68 → 73 / Android 67 → 72 (+5 each):** the App-Store screenshot-craft gap (called out for both in Phase 1) is now closed by a real owner; Android's Predictive-Back is now end-to-end and WindowSizeClass covers adaptive sizing; touch/haptic detail is now owned. They clear into the **excellent-pro** band's lower edge. They do not reach the award ceiling because the platform-frontier *signature* surfaces remain absent — Live Activities / Dynamic Island / WidgetKit on iOS, a foldable/large-screen playbook on Android.
- **Conversion / trust (marketing website) 73 → 80 (+7):** `trust-credibility-and-social-proof` (honest attributed-proof hierarchy) + `onboarding-and-first-run-design` + `editorial-and-long-form-layout` together close the prior "CRO owned but narrative-layout missing, trust only half-owned" gap. This is now the **strongest non-web-app surface** and the second type to clear 75.

The two web-cluster P1 skills (`component-states-and-interaction-fidelity`, `micro-interactions-and-feedback`) also nudged the web app from 79 → 82 by supplying the state-matrix + feedback fidelity the prior audit said was "not at Linear/Vercel level."

---

## Overall output readiness — **75 / 100** (Δ **+5** vs 70)

Computed as the mean of the twelve re-scored types (≈75.3; the ten prior types alone average ≈76.4, lifted by every one rising 3–9 points, and the two new types enter at a healthy 76 and 72). The v2 plan moved the engine from "solid-to-excellent, three types in the excellent band" to "**excellent-pro is now the modal band: seven of twelve types clear 75**, the amateur band (<60) is empty, and the floor rose from 58 to 67."

**Why not higher:** the bar is end-to-end *world-class*, and the engine still **specs rather than renders** the last execution mile in the same places, now joined by the two new types' own version of it:
- no `.pptx` / `.docx` / `.pdf` / `.xlsx` **generation pipeline** (it designs the artifact, it does not drive the file);
- no deep **RN / Flutter implementation** skill (the single reason cross-platform stays the floor);
- no **Live Activities / Dynamic Island / WidgetKit** (iOS) or **foldable** (Android) platform-frontier surfaces;
- no **CI token publishing / two-way Figma↔code** sync (the remaining handoff mile);
- and email/xlsx, while now real owners, still hand off the actual cross-client test run and the spreadsheet write to tooling outside the engine.
These are "**build the artifact**," not "**design the artifact**," gaps — which is why even the leaders sit at 80–82 rather than 85+.

**Now-weakest output type:** **Cross-platform mobile (RN / Flutter) at 67/100** — still the floor despite a +9 jump and two new supporting skills, because the engine now teaches the parity decision, the per-side touch/haptic craft, and per-store delivery, but **not** deep framework *implementation* (render models, Expo, navigation, offline sync). It is the one type whose remaining gap is squarely "build," and it would be the highest-leverage target for a v3.

> **Caveat on method (unchanged):** scores assess what an agent could produce *guided only by this engine's current skills + doctrine*, against the named world-class bar — end-to-end readiness per output type, not the (high) quality of the foundations in isolation. The two new types (email, spreadsheet exhibit) are scored on the same rubric. No skill files were modified for this audit.
