# Existing Groups RE-AUDIT — Post-v2-Plan — Design-System-Skills Engine

**Date:** 2026-06-22
**Auditor scope:** All **81 `SKILL.md`** files across **14 groups** (00–13), their `references/`
and `examples/` subtrees, `doctrine/design-doctrine.md`, and all 12 `doctrine/references/*.md`
(incl. the two NEW refs: `creative-selection-and-taste.md`, `interaction-anti-patterns.md`).
**Baseline compared against:** `docs/audits/post-phase-1/03-existing-groups-reaudit.md` — **51 skills,
14 groups, aggregate 63/100** (which itself was +5 over the original 58).
**Bar (unchanged, ruthless):** Top-0.1% global — Pentagram / Apple / Awwwards SOTD / D&AD.
90–100 rivals them · 75–89 excellent pro · 60–74 solid but visibly short · 40–59 competent ·
<40 skeletal. Default band 45–65; 70+ requires extraordinary, specific justification. No
grade inflation; the same rubric the prior audit applied, applied again.

> **Method.** Doctrine + both NEW references read in full. All 81 SKILL.md files read across the
> lead auditor + parallel reviewers (one fork per group-cluster, each inheriting the full rubric +
> prior-audit context), with worked-example files opened directly for calibration (the distinctive
> before/after, the demo-driven iteration log, the OKLCH ramp, the ecommerce/checkout spec, the
> voice-and-tone guide, the ai-image C2PA gate, among others). Two repo-wide greps anchored the
> structural claims: the legacy boilerplate-shell signatures ("reusable judgment" Use-When + the
> "Evidence Produced" migration table) and the "matches this domain" stub variant.

---

## Headline: the engine is now **uniformly example-backed and substantially book-grounded** — a real "good-and-even" 64-tier — but the **legacy boilerplate shells were patched with examples, not re-authored**, which is the single thing holding it out of the high-60s.

The prior audit diagnosed a **bimodal** engine: a genuinely-good 65–74 Phase-1 tier sitting beside
~10 untouched boilerplate-shell legacy skills and **17 skills with no worked example at all**. The
v2 plan closed the largest of those gaps decisively, but left the most embarrassing one only
half-finished.

### The four prior open defects, re-scored

1. **Examples drought → FULLY CLOSED.** **All 81 skills now ship a worked example** — verified
   real (named brief → applied artifact → checklist run), not lorem, line-counts confirmed
   non-stub. The prior audit's 17-skill no-example set is gone. This is the single biggest,
   most-creditable delta in the engine and it is genuine.
2. **`distinctive-by-design` — the soul skill — → FIXED.** It now ships `examples/before-after-distinctive.md`
   (126L): the "Cadence" SaaS hero, where BEFORE and AFTER carry the **same words** and the entire
   delta is authorship — one stated decision grounded in Vignelli, then the full 8-item Human-Craft
   checklist run against the AFTER. The engine's flagship finally *shows* the distinctiveness it
   preaches. It rises 73 → **76**.
3. **Dangling P1 references → RESOLVED.** `trust-credibility-and-social-proof`,
   `onboarding-and-first-run-design`, and `ecommerce-and-checkout-ux` now all **exist** (and are
   good), so `landing-page-and-conversion-design`'s routing is real, not forward-promised.
4. **Residual 2026 gaps → MOSTLY CLOSED.** **C2PA/provenance** is now operationalized
   (`ai-image-generation-art-direction`: Content Credentials, indemnity, training-data rights,
   truth-claim-forbids-AI-people). iOS advanced to **SF Symbols 8** and **Material 3 Expressive**.
   The book sourcing landed where the v2 plan promised: **Kocienda creative-selection**
   (design-critique, demo-driven, storytelling's "THE FENCE"), **Maioli triage** (ux-remediation),
   **Neil/Tognazzini** anti-patterns (heuristic-evaluation, the new `interaction-anti-patterns.md`),
   **Cleveland–McGill** encoding (chart-selection/data-viz), **Podmajersky Voice Chart**
   (voice-tone-and-content-style-guide), **Janoff/Rand/Vignelli/Neumeier** (logo-and-wordmark).

### What still holds the line (and caps the score)

1. **The legacy shells were NOT re-authored — examples were bolted onto them.** The grep is exact
   and unchanged from the prior audit's set: **7 SKILL.md still carry the full boilerplate shell**
   ("The task needs reusable judgment…" Use-When + "Evidence Produced" table) — `design-audit`,
   `practical-ui-design`, `form-ux-design`, `interaction-design-patterns`, `healthcare-ui-design`,
   `motion-design`, `data-visualization`. A further **~5 SKILL.md keep the "Evidence Produced"
   table alone** (`design-critique`, `design-qa`, `performance-as-ux`, `product-design-audit`,
   `webapp-gui-design`), and **5 keep the "matches this domain" stub** (`brand-style-guide`,
   `color-selection`, `ux-psychology`, `legal-sector-ui-ux`, `sector-strategies`). A generated
   shell in an explicitly **anti-slop** engine is itself a slop signal — so several deep-bodied
   skills (`practical-ui-design`, `data-visualization`, `healthcare-ui-design`) actually **lose a
   point or two** under the same harsh bar despite gaining examples, because their peers were
   re-authored and they were not.
2. **Stale sibling paths** in the legacy stubs (`03-web-and-ui-design/…`, `04-color-and-visual-identity/…`)
   are dangling references — the groups were renumbered but the stub bodies weren't.
3. **`deck-system` still generates no PPTX** — output is "ready to build," routing the actual
   assembly to the human. The DOCX/PDF/XLSX siblings now produce real styled artifacts; the deck
   group still partly offloads execution.
4. **Many strong new skills ship only one own reference file** — enough to anchor, but it is the
   thing keeping most of them in the 63–70 band rather than higher.
5. **`color-selection`** (50, 9 refs, redundant with `color-system-and-palette` which it routes
   to) remains a deletion candidate; the audit family still overlaps more than world-class.

---

## Group-by-group

### Group 00 — Cross-cutting Ops / QA / A11y — **64/100**  *(prior 65; grew 6→11)*

Grew with a genuinely strong, **book-grounded** spine: `product-design-audit` (whole-product,
multi-platform, every finding routed to its remediating skill), `ux-remediation-and-redesign`
(operationalizes Maioli's *Fixing Bad UX* — triage matrix, red-route severity, the
diagnose→triage→redesign→re-validate loop), `design-critique-and-review-facilitation` (the deepest
application of `creative-selection-and-taste.md` in the engine), `design-ethics-and-anti-dark-patterns`,
and `inclusive-and-assistive-design`. All five new skills are authored, routed, exampled — **no
"reusable judgment" shell among them.** The band holds flat (−1) only because `design-audit` still
wears the full shell, five skills keep the "Evidence Produced" table, the audit family overlaps,
and two new examples (ethics/inclusive, 29L) are dense-but-lean.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| product-design-audit | 71 | 3 | Yes (191L) | **NEW. Standout.** Multi-platform composing audit, every finding routed to the exact remediating skill, three hard gates cap score. Under 75: "Evidence Produced" table + heavy sibling composition. |
| ux-remediation-and-redesign | 70 | 2 | Yes (143L) | **NEW.** Maioli triage matrix (red-route × effort-impact × MoSCoW), loop-not-waterfall, cross-walks `interaction-anti-patterns.md`; worked Aurora 41→88. No shell. |
| accessibility-wcag-2-2-compliance | 70 | 2 | Yes (73L) | **±0.** Build-then-audit on the 9 new 2.2 SCs; Liquid Glass/Dynamic Type a11y folded in. No per-framework worked component. |
| design-critique-and-review-facilitation | 69 | 1 | Yes (144L) | **NEW.** Demo-grounded crit, algorithm/heuristic lens, single decider, 41-blues-not-vote, "live on it." Held by 1 ref + an "Evidence Produced" table. |
| design-ethics-and-anti-dark-patterns | 66 | 1 | Yes (29L) | **NEW.** 7 deceptive-pattern families → honest swap each; regulator note. Lean example; SKILL→file name mismatch (`ethics-audit-worked.md` vs `-filled.md`). |
| inclusive-and-assistive-design | 65 | 1 | Yes (29L) | **NEW.** Microsoft persona-spectrum, exclusion audit, above-the-floor accommodations. Lean 29L example. |
| design-qa-and-pre-launch-review | 64 | 1 | Yes (184L) | **±0.** Real signed go/no-go gate (slop+a11y+perf). Still the "Evidence Produced" table; overlaps the audits. |
| performance-as-ux-and-core-web-vitals | 63 | 1 | Yes (137L) | **±0.** CWV-as-constraint + budget sheet; "Evidence Produced" table; thin on INP remediation. |
| visual-product-slop-audit | 60 | 1 | Yes (78L) | **+2.** Now carries the 2026 AI-image tells ("absence of authored specificity," not six fingers). Still a thin taxonomy mirror; no C2PA. |
| internationalization-and-rtl-design | 60 | 2 | Yes (73L) | **±0.** Logical-properties + expansion + worked RTL flip. Thinner than the color/type spine. |
| design-audit | 59 | 5 | Yes (169L) | **+1.** 447L deep body (the anti-pattern cross-walk lands here) + worked filled audit, **but STILL the full "reusable judgment" shell AND "Evidence Produced" table** — the prior audit's exact unaddressed defect. |

**Standout:** `product-design-audit` (71). **Weakest:** `design-audit` (59 — deep body, only group-00 skill still wearing the full generated shell).

### Group 01 — Typography & Fonts — **63/100**  *(prior 60; grew 4→6, +3)*

Two excellent technical additions close the prior audit's named "fluid clamp / variable-font axes"
gap. `variable-fonts-and-opentype-features` is now the deepest type-mechanics skill in the engine.
The four carried-over skills are unchanged in body but **now all ship worked examples** (the prior
gap), lifting the plumbing trio modestly without re-authoring them.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| variable-fonts-and-opentype-features | 68 | 2 | Yes (137L) | **NEW. Standout.** Tabular-vs-proportional numerals correctness rule (the common data-UI bug), real small caps, one-`ssNN`-with-intent, variable-as-perf. Sharp, non-overlapping. |
| fluid-responsive-typography | 67 | 1 | Yes (147L) | **NEW.** Real `clamp()` derivation (slope/intercept, not magic numbers), WCAG 1.4.4/1.4.10 zoom-safe, `cqi`, capped measure. Closes the prior gap. |
| font-selection-and-pairing | 66 | 2 | Yes (147L) | **±0.** The type spine — pairing catalog + scale recipes + worked Maduuka scale. Still a router over the doctrine. |
| ai-slop-typography-audit | 58 | 0 | Yes (146L) | **+1.** Now a worked filled audit. Still no own refs, no font-inference-from-screenshot. |
| font-embedding-and-licensing | 54 | 0 | Yes (199L) | **+3.** Real worked embedding spec; body still a thin compression of two doctrine refs. |
| premium-font-scan | 53 | 0 | Yes (94L) | **+1.** Unchanged `fonts/<group>/`+MANIFEST plumbing; now exampled. |

**Standout:** `variable-fonts-and-opentype-features` (68). **Weakest:** `premium-font-scan` (53 — plumbing, now exampled).

### Group 02 — Color, Brand & Visual Identity — **66/100**  *(prior 68; grew 6→7, −2)*

`logo-and-wordmark-design` is one of the best new skills in the engine. The OKLCH/contrast/dark-remap
spine is intact (`color-system-and-palette` 74 still the engine's top single skill). The band edges
**down 2** because the group grew by adding one strong skill while **two "matches this domain" stubs
survive unreauthored** (`brand-style-guide`, `color-selection`) — examples bolted on, bodies still
generated boilerplate — which the harsh count-weighted bar punishes as dilution.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| color-system-and-palette | 74 | 2 | Yes (102L) | **±0.** Operationalized OKLCH recipe + worked ramp w/ hexes + measured contrast + APCA/WCAG split. The engine's most complete color skill. |
| logo-and-wordmark-design | 73 | 2 | Yes (169L) | **NEW. Standout.** Janoff/Rand/Vignelli/Neumeier-grounded; idea-before-execution anti-AI-mark rule; favicon/app-icon matrix; 7-item Construction Gate; conviction-not-test (41-blues). |
| accessible-color-and-contrast | 70 | 2 | Yes (97L) | **±0.** APCA-vs-WCAG done right (design vs certify), full pair×pair matrix, CVD ramps + non-colour-cue rule. |
| dark-mode-and-theming | 66 | 1 | Yes (147L) | **±0.** Remap-not-invert, elevation-flip, re-certify dark independently; real token-pair example. |
| brand-visual-identity | 65 | 3 | Yes (136L) | **±0.** Strategy-first, ownability test, worked mini-identity; now pairs with the new logo skill. No motion-system depth. |
| brand-style-guide | 54 | 3 | Yes (114L) | **±0.** Real template + worked mini-guide, **but still the "matches this domain" boilerplate stub** body — unreauthored. |
| color-selection | 50 | 9 | Yes (87L) | **±0. Weakest.** Still the "matches this domain" stub; redundant with `color-system-and-palette` (admits the routing). Deletion candidate. |

**Standout:** `color-system-and-palette` (74) / `logo-and-wordmark-design` (73). **Weakest:** `color-selection` (50).

### Group 03 — Layout, Grid & Composition — **66/100**  *(prior 65; grew 2→4, +1)*

Now the most **uniformly strong** group — all four skills authored, no shells, all exampled, tightly
cross-routed. `composition-and-visual-hierarchy` is deeply Swiss-canon-grounded (Tschichold/
Müller-Brockmann/Vignelli/Lupton/Arnheim) and operationalizes the halation optics rule + glassmorphism
inoculation. Band rises only +1 because none breaks into the high-60s — excellent pro, not
Pentagram-rivalling.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| composition-and-visual-hierarchy | 69 | 2 | Yes (143L) | **NEW. Standout.** Halation optics, hierarchy-from-extremes, eye-path, asymmetry/tension, figure-ground, whitespace-as-rank; worked before/after w/ CSS + glassmorphism inoculation. |
| responsive-and-adaptive-layout | 67 | 2 | Yes (183L) | **±0.** Container queries + clamp() + intrinsic; kills the "collapses to one stacked column" tell. |
| editorial-and-long-form-layout | 65 | 1 | Yes (199L) | **NEW.** Measure/baseline-rhythm/drop-caps/pull-quotes/sidenotes; the web partner to the group-13 doc skills. Single ref. |
| layout-grid-and-spacing | 64 | 2 | Yes (144L) | **±0.** Concrete grid spec with numbers; still abstract on print-grid baseline cases. |

**Standout:** `composition-and-visual-hierarchy` (69). **Weakest:** `layout-grid-and-spacing` (64 — group floor).

### Group 04 — Web & UI Design — **65/100**  *(prior 62; grew 11→15, +3)*

The engine's largest group, and its bimodality has **narrowed substantially**. The three biggest
prior demerits are resolved: (1) **`distinctive-by-design` now demonstrates** its discipline with a
real same-words before/after — the engine's most glaring "tells-not-shows" hole is filled; (2) the
**dangling P1 references are gone**; (3) **`premium-ui-ux-design` and `ai-output-design` now have
worked examples**, recovering the points the no-example rule docked. Four new skills (trust,
onboarding, component-states, email) are all genuinely good, book-grounded, non-redundant. What still
holds it down: **three legacy boilerplate shells survive verbatim** — so `practical-ui-design`
actually **drops 4** despite gaining an example, because its peers were re-authored and it was not.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| distinctive-by-design | 76 | 0 own | Yes (126L) | **+3.** The flagged gap is **closed**: "Cadence" before/after, same words, authorship-only delta, grounded in Vignelli, full 8-item checklist run. A true "show, don't tell" exemplar. Under 80 only because it ships no own `references/` dir. |
| trust-credibility-and-social-proof | 72 | 1 | Yes (138L) | **NEW.** Honest-persuasion ethics (attribution mandatory, zero fabrication), credibility hierarchy, trust-signal catalog, Neil/Maioli anti-patterns. Worked clinic-SaaS spec. |
| landing-page-and-conversion-design | 71 | 2 | Yes (134L) | **+1.** Section spine + honest-conversion ethics + WCAG/perf-as-conversion. **Dangling refs now RESOLVED** — routing is real. |
| onboarding-and-first-run-design | 70 | 1 | Yes (157L) | **NEW.** Value-before-auth (Neil B1), empty-state-as-onboarding, sparing-coachmark (C4 trap), TTV; worked first-run flow. |
| empty-error-and-loading-states | 69 | 1 | Yes (176L) | **+1.** Every reachable state of one real fintech table authored up front; cleanly split from the new component-states sibling. |
| premium-ui-ux-design | 68 | 13 | Yes (115L) | **+5.** Prior "no worked screen" demerit **fixed** — full worked Collections-workspace direction. 13 refs finally anchored by an artifact. |
| component-states-and-interaction-fidelity | 68 | 2 | Yes (126L) | **NEW.** Per-component state matrix + transition table (not just endpoints), focus-visible to 2.4.7/2.4.11/1.4.11, reduced-motion. |
| ai-output-design | 66 | 6 | Yes (179L) | **±0.** Sharp/current (Macfadyen 2025, no-confidence-%, inline sources); prior "no example" demerit **fixed**. No shell. |
| email-and-newsletter-design | 66 | 1 | Yes (62L) | **NEW.** The constrained email model (tables/inline-CSS, Outlook-Word engine, VML bulletproof button, fallback-IS-the-design). Held by the thinnest example in group (62L). |
| webapp-gui-design | 65 | 3 | Yes (250L) | **+1.** Strongest code skill (Next.js/Radix, four-state rule, worked app-shell). Still the "Evidence Produced" table; generic visual defaults. |
| navigation-and-information-architecture | 64 | 2 | Yes (192L) | **±0.** Solid IA + worked sitemap; not yet world-class on large faceted nav. |
| practical-ui-design | 62 | 2 | Yes (129L) | **−4.** Strong rules body + worked before/after, **but still the verbatim boilerplate shell + "Evidence Produced" table.** A templated shell in the flagship UI skill costs more now its peers were re-authored. |
| form-ux-design | 60 | 6 | Yes (285L) | **+2.** Deep refs + worked sign-up spec (WCAG 3.3.7/3.3.8/2.5.8), but **shell + table survive verbatim**. |
| interaction-design-patterns | 59 | 0 own | Yes (166L) | **+2.** Tidwell digest + worked invoice-editor example, but the **auto-generated shell + "Evidence Produced" table are still at the top**, no own refs. Clearest surviving stub-entrypoint. |
| ai-agent-ux | 58 | 5 | Yes (344L) | **+4.** Router shell, but generic verbatim gone + longest worked example in group (344L Ledger copilot). Still a thin top-level surface. |

**Standout:** `distinctive-by-design` (76). **Weakest:** `interaction-design-patterns` (59).

### Group 05 — UX Process, Research & Psychology — **63/100**  *(prior 58; grew 4→7, +5)*

Three genuinely strong new skills anchor it, all book-grounded and example-backed. The one persistent
drag is `ux-psychology`, still the untouched "matches this domain" stub (example bolted on, body
verbatim filler, stale `03-web-and-ui-design` sibling paths). Process-heavy for a *design* engine, but
that's structural, not a defect introduced here.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| demo-driven-design-process | 72 | 2 | Yes (182L) | **NEW. Standout.** Genuinely operationalizes Kocienda creative-selection: algorithm-vs-heuristic classifier, fidelity-ring + non-goals, "live on it," 41-blues guard — all *applied*. The worked 4-demo iteration log (convergence-by-subtraction, A/B rejected on the spot) is one of the best examples in the engine. Does what distinctive-by-design now does: shows the method running. |
| heuristic-evaluation-and-design-critique | 69 | 2 | Yes (172L) | **NEW.** Nielsen-10 + Tognazzini, severity 0–4 (freq×impact×persistence), independent-then-merge, cross-walks `interaction-anti-patterns.md` A1–E3. Digests rather than extends the canon. |
| journey-mapping-and-service-design | 65 | 2 | Yes (116L) | **NEW.** Evidence-based personas, JTBD, frontstage/backstage blueprint → ranked opportunities; strong anti-patterns. Not world-class on large service ecosystems. |
| ux-research-and-usability-testing | 63 | 2 | Yes (77L) | **+1.** Research-to-decision spine, method selector, sharp anti-patterns. Example thinnest in group. |
| wireframing-and-prototyping | 62 | 1 | Yes (109L) | **+1.** Fidelity ladder + branch-complete wireflow; hands off the loop to demo-driven. Single ref. |
| enterprise-ux-process | 58 | 7 | Yes (102L) | **±0.** Rigorous 9-phase methodology; process not visual craft. WCAG **2.1** still (others moved to 2.2). |
| ux-psychology | 52 | 3 | Yes (103L) | **±0. Weakest.** Still the "matches this domain" stub — verbatim-generic body, stale `03-web-and-ui-design` paths. Good example cannot lift a skeletal body. |

**Standout:** `demo-driven-design-process` (72). **Weakest:** `ux-psychology` (52).

### Group 06 — Sector & Domain UX — **61/100**  *(prior 57; grew 3→5, +4)*

Two strong new sector skills carry the band. The headline finding: the two legacy stubs the prior
audit flagged — `sector-strategies`, `legal-sector-ui-ux` — were **NOT re-authored** (still
"matches this domain", stale sibling paths, examples bolted on). Worse, `healthcare-ui-design` —
the deepest domain skill in the engine — **STILL carries the full boilerplate shell**, the prior
audit's exact unaddressed complaint.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| ecommerce-and-checkout-ux | 70 | 1 | Yes (194L) | **NEW. Standout.** Surface-by-surface spine (PLP→PDP→cart→checkout→payment→post-purchase) + 13-item anti-dark-pattern checklist that refuses coercive variants with honest swaps; guest-first, total-cost transparency, WCAG 2.5.8; runs distinctive-by-design as a gate. Exceptionally complete + ethically rigorous. 1 ref. |
| fintech-and-financial-product-ui | 65 | 1 | Yes (145L) | **NEW.** Reversibility/blast-radius classification, tabular-figures-first, fee/FX disclosure before commit, East-African mobile-money (M-Pesa/MoMo/USSD), anti-homogeneity ("refuse the fintech blue"). Single ref. |
| healthcare-ui-design | 62 | 15 | Yes (168L) | **−2.** Deepest domain knowledge (HIPAA/FHIR, clinical thresholds, 15 refs) **but STILL the full boilerplate shell** — slipping under the no-shell harshness despite the new worked screen. |
| legal-sector-ui-ux | 54 | 4 | Yes (184L) | **−1. Not re-authored.** Still "matches this domain" + stale `03-web-and-ui-design`/`04-color-and-visual-identity` paths; decent refs + real example bolted on a generic shell. |
| sector-strategies | 53 | 1 | Yes (100L) | **±0. Weakest.** Still the "choose sector → customize template" factory with a pure boilerplate body; anti-homogeneity gate lives in a *separate* file, **not operationalized in the SKILL.md**. |

**Standout:** `ecommerce-and-checkout-ux` (70). **Weakest:** `sector-strategies` (53).

### Group 07 — Mobile (iOS / Android / Cross-platform) — **66/100**  *(prior 63; grew 3→5, +3)*

The new skills are genuinely specialist. `ios-ui-ux-design` is now even more current than the prior
audit credited — **SF Symbols 8** (not 7), Liquid Glass chrome-only, Dynamic Type to AX5. Two strong
new skills: `touch-gesture-and-haptics` operationalizes the WCAG 2.5.1/2.5.7 single-pointer/non-drag
rule table (a real gap nothing else covered), and `app-store-presence-and-aso` treats the store
listing as a composed conversion surface. No shells anywhere.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| ios-ui-ux-design | 68 | 8 | Yes (111L) | **+1.** Liquid Glass chrome-only, **SF Symbols 8**, AX5, haptics semantics, worked "Send Payment." Defers code to a dev skill (a gate). |
| touch-gesture-and-haptics | 66 | 1 | Yes (111L) | **NEW. Standout.** WCAG 2.5.1/2.5.7 gesture-alternative rule table as the legal core; thumb-zone arcs, system-gesture reservation, iOS+Android haptic map. Fills a real gap. 1 ref. |
| app-store-presence-and-aso | 65 | 1 | Yes (166L) | **NEW.** Store listing as one authored surface — icon delivery (masks/safe-zone/Liquid Glass variants), narrative screenshot order, copy char-limits, localization. 1 ref. |
| android-ui-ux-design | 62 | 4 | Yes (130L) | **+2.** Now explicitly **Material 3 Expressive** + predictive-back + HCT brand-seed. Lighter on expressive-component depth than iOS on its 2026 set. |
| cross-platform-design-parity | 62 | 2 | Yes (88L) | **+1.** "Unify meaning, diverge mechanism," current Liquid Glass/SF-Symbols-8 vs M3-Expressive. Not world-class on large multi-surface systems. |

**Standout:** `touch-gesture-and-haptics` (66) / `ios-ui-ux-design` (68). **Weakest:** `android-ui-ux-design` / `cross-platform-design-parity` (62).

### Group 08 — Motion & Interaction — **64/100**  *(prior 62; grew 1→2, +2)*

The new `micro-interactions-and-feedback` is excellent and lifts the floor: the **ζ ≥ 0.7 no-bounce
spring rule** directly inoculates against the `ease-*-back` AI animation fingerprint;
optimistic-feedback-with-rollback, semantic haptics, reduced-motion replacement. `motion-design`
keeps its deep 370L body **but still carries the verbatim boilerplate shell** — the prior audit's
exact unaddressed complaint, now more glaring beside a cleanly-authored sibling.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| micro-interactions-and-feedback | 68 | 1 | Yes (136L) | **NEW. Standout.** Per-control feedback layer, ζ≥0.7 no-bounce, optimistic+rollback, semantic haptics, worked toggle; cleanly defers the global law to motion-design. |
| motion-design | 62 | 3 | Yes (111L) | **±0.** Deep body (springs, View Transitions, GPU rules, reduced-motion) **but STILL the full boilerplate shell** + no scroll-driven `animation-timeline`. |

**Standout:** `micro-interactions-and-feedback` (68). **Weakest:** `motion-design` (62).

### Group 09 — Design Systems, Tokens & Theming — **66/100**  *(prior 65; grew 3→4, +1)*

All authored, all example-backed, coherent, no overlap, no shells. `design-tokens-and-naming` is the
backbone (three-tier, multi-brand/dark mapping, Style Dictionary export, ships a real `tokens.json`).
The new `figma-and-tooling-workflow` is a useful explicitly-2026-Figma skill that defers token
*decisions* upstream.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| design-tokens-and-naming | 68 | 2 | Yes (64L + tokens.json 173L) | **+1.** Three-tier architecture, dark/multi-brand role mapping, real tokens.json. Just shy on token-versioning/governance-at-scale. |
| design-handoff-and-dev-spec | 64 | 2 | Yes (178L) | **±0.** Concrete measured-redline handoff sheet; practical. |
| figma-and-tooling-workflow | 64 | 1 | Yes (164L) | **NEW.** Variables+modes, component properties, styles-vs-variables seam, Dev Mode. 1 ref; operates tokens, doesn't extend the model. |
| component-library-architecture | 63 | 2 | Yes (173L) | **±0.** Worked variant/state matrix (button) + atomic structure. |

**Standout:** `design-tokens-and-naming` (68). **Weakest:** `component-library-architecture` (63).

### Group 10 — Content Design & UX Writing — **66/100**  *(prior 63; grew 2→3, +3)*

The new `voice-tone-and-content-style-guide` is the strongest single addition — it operationalizes
**Podmajersky's six-aspect Voice Chart** with a *ratified tiebreaker* (settles disputes, not just
describes voice), the Ben-David Voice Guide, a lifecycle Tone Map, and terminology governance. It's
the upstream system the other two skills already cited as a missing dependency, now real.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| voice-tone-and-content-style-guide | 70 | 1 | Yes (146L) | **NEW. Standout.** Podmajersky Voice Chart + ratified tiebreaker + Ben-David Voice Guide + lifecycle Tone Map + terminology governance. Clears 70 on rigor + the ratification mechanism. 1 own ref. |
| ux-writing-and-microcopy | 65 | 3 | Yes (158L) | **+1.** Voice-declared-first, verb+object CTA rules, reasoned before/after; now consumes the voice skill. |
| error-empty-and-system-messaging | 64 | 2 | Yes (169L) | **+1.** Error-message formula + placement taxonomy + real error-copy library; pairs with the states skill. |

**Standout:** `voice-tone-and-content-style-guide` (70). **Weakest:** `error-empty-and-system-messaging` (64).

### Group 11 — Imagery, Illustration & Art Direction — **65/100**  *(prior 60; grew 2→4, +5)*

**The prior audit's one surviving 2026 gap — C2PA/provenance — is now closed.** The new
`ai-image-generation-art-direction` treats generation as a directed/gated/post-processed/**provenance-
checked** act (C2PA, indemnity, training-data rights, truth-claim-forbids-AI-people). The new
`illustration-style-and-systems` explicitly kills corporate-Memphis/blob-people slop. All authored,
all exampled.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| ai-image-generation-art-direction | 68 | 1 | Yes (108L) | **NEW. Standout.** Closes the C2PA gap; slop-tell reject gate, negative-constraint prompting, truth-claim-forbids-AI-people, post-process-to-de-slop, when-NOT-to-use. The sourcing-asymmetry rule applied to image models. 1 ref. |
| photography-art-direction | 64 | 2 | Yes (107L) | **+5.** Treatment-system (grade/grain/duotone/crop), anti-stock-cliché kill list, authored image-POV rule; C2PA now handled by sibling. |
| illustration-style-and-systems | 63 | 1 | Yes (144L) | **NEW.** Illustration as constructed system + ownable motif; explicit corporate-Memphis/blob-people kill. 1 ref, not yet named-studio depth. |
| iconography-system-design | 62 | 1 | Yes (145L) | **+1.** Grid/stroke/optical-correction spec + worked icon set. Competent, unchanged in substance. |

**Standout:** `ai-image-generation-art-direction` (68). **Weakest:** `iconography-system-design` (62).

### Group 12 — Data-Viz & Dashboards — **64/100**  *(prior 64; grew 2→3, ±0)*

The new `chart-selection-and-encoding` is a clean split: it owns the upstream data-type × message →
chart-type routing + honest-encoding gate, explicitly handing the **Cleveland–McGill perceptual
ranking** and decluttering craft to `data-visualization`. The band doesn't move because
`data-visualization` — the most content-complete single skill — **still carries the full boilerplate
shell** and its prior single-2015-book-spine / no-scrollytelling / no-uncertainty gaps persist.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| dashboard-and-data-product-design | 65 | 2 | Yes (141L) | **±0.** KPI hierarchy + cross-filter + streaming-freshness UX, worked dashboard spec. Clean page-above-the-chart split. |
| data-visualization | 65 | 5 | Yes (129L) | **−2.** Exhaustive (Knaflic+Tufte+Gestalt+preattentive+chart tree, 545L) and now exampled, **but STILL the boilerplate shell**; single-book-spine / scrollytelling / uncertainty gaps unaddressed. |
| chart-selection-and-encoding | 64 | 1 | Yes (152L) | **NEW.** Message-type → chart-type routing, honest-encoding gate (zero-baseline, dual-axis ban), accessibility, clean Cleveland-McGill handoff. 1 ref; overlaps the sibling by design. |

**Standout:** `dashboard-and-data-product-design` / `chart-selection-and-encoding`. **Weakest:** `data-visualization` (65 — deep body, unreauthored shell).

### Group 13 — Presentations & Documents — **64/100**  *(prior 62; grew 3→5, +2)*

The group now formats real DOCX/PDF/**XLSX** artifacts — the new `xlsx-and-financial-model-presentation`
genuinely produces exhibit-grade spreadsheets. The new `design-storytelling-and-case-studies` opens
with a sharp "THE FENCE" citing `creative-selection-and-taste.md` (narrative must never replace the
working demo or decorate slop). The one persistent structural defect: `deck-system` still routes the
*actual build* to the human — **no PPTX generation**.

| Skill | Score | Refs | Example | Notes (Δ) |
|---|---:|---|---|---|
| xlsx-and-financial-model-presentation | 66 | 2 | Yes (138L) | **NEW. Standout.** Exhibit-grade .xlsx as a designed artifact — number masks, conditional-format-as-encoding + non-colour cue, blue-input/black-formula, print exhibits. Genuinely produces a styled artifact (unlike decks). |
| docx-report-and-document-formatting | 65 | 3 | Yes (95L + 120L) | **+1.** Named-style hierarchy/TOC/letterhead/embedding/accessible tags + sharp default-vs-designed before/after. Real produced artifact. |
| design-storytelling-and-case-studies | 64 | 2 | Yes (102L) | **NEW.** Six named structures (Freytag/Three-Act/Pixar/Kishōtenketsu/Contrast/Peak-End), user-as-protagonist, "THE FENCE" anti-slop guard citing creative-selection. Thinner example. |
| pdf-proposal-and-bankable-document-design | 63 | 3 | Yes (66L + 86L) | **+1.** Worked cover + exhibit-page layout, bankable framing, print-ready checklist. Real artifact. |
| deck-system | 63 | 3 | Yes (8 variants, 208–332L) | **±0.** Consolidates 8→1 with rich variant blueprints. **Still builds no PPTX** — the human assembles. |

**Standout:** `xlsx-and-financial-model-presentation` (66). **Weakest:** `deck-system` / `pdf` (63).

---

## Group ranking (post-v2-plan, weakest → strongest)

| Group | Score | Δ vs prior | One-line verdict |
|---|---:|---|---|
| 06 Sector & Domain UX | 61 | +4 | Strong new ecommerce/fintech; two stubs + healthcare's full shell still unreauthored. |
| 01 Typography | 63 | +3 | Excellent new variable-fonts + fluid-type; the plumbing trio now exampled but unchanged. |
| 05 UX Process & Psychology | 63 | +5 | demo-driven (72) operationalizes Kocienda; `ux-psychology` stub still drags. |
| 08 Motion | 64 | +2 | New micro-interactions inoculates the spring fingerprint; `motion-design` keeps its shell. |
| 12 Data-Viz & Dashboards | 64 | ±0 | Clean Cleveland-McGill split; `data-visualization` shell + single-book-spine unaddressed. |
| 13 Presentations & Documents | 64 | +2 | Now formats real DOCX/PDF/XLSX; deck still builds no PPTX. |
| 00 Cross-cutting QA/A11y | 64 | −1 | Strong book-grounded new spine (product-audit 71, Maioli remediation); `design-audit` shell + tables. |
| 11 Imagery / Art Direction | 65 | +5 | C2PA closed; corporate-Memphis killed; all authored. |
| 04 Web & UI | 65 | +3 | Soul skill now SHOWS; dangling refs resolved; 3 legacy shells still survive. |
| 02 Color, Brand & Identity | 66 | −2 | OKLCH spine intact + strong new logo skill; two "matches this domain" stubs dilute. |
| 03 Layout & Composition | 66 | +1 | Now uniformly strong — Swiss-canon composition skill, no shells. |
| 07 Mobile | 66 | +3 | SF Symbols 8 / M3 Expressive / gesture-haptics WCAG table; all authored. |
| 09 Design Systems & Tokens | 66 | +1 | Coherent three-tier backbone + real tokens.json + modern-Figma skill. |
| 10 Content Design | 66 | +3 | Podmajersky Voice Chart with a ratified tiebreaker; the missing upstream, now real. |

---

## NEW aggregate engine score — **64/100**  ·  delta vs prior **63** = **+1**

**Computation.** Three independent weightings converge: the **skill-level count-weighted mean across
all 81 skills = 64.5**; the **group-score count-weighted mean = 64.5**; the **simple mean of the 14
group scores = 64.5**. All round to **64/100** — out of "competent" and solidly into "**solid but
visibly short of world-class**," one band below the 75 "excellent pro" line. The same harsh,
no-grade-inflation rubric is applied; the +1 is earned, not assumed.

**Why it rose +1 and not more — the v2 plan did real work, and most of it is creditable:**

- **The examples drought is FULLY closed.** All 81 skills now ship a verified-real worked example
  (the prior audit had 17 with none). This is the single biggest delta and it is genuine.
- **The soul skill now proves its thesis.** `distinctive-by-design`'s same-words "Cadence"
  before/after is the best single new artifact in the engine; the prior audit's most glaring
  "tells-not-shows" hole is filled.
- **The book sourcing translated directly into score.** Every skill that rose into the 68–76 tier
  is book-grounded: Kocienda (demo-driven 72, design-critique 69), Maioli (ux-remediation 70),
  Podmajersky (voice-tone 70), Janoff/Rand (logo 73), the Swiss canon (composition 69),
  Cleveland-McGill (chart-selection), Neil/Tognazzini (heuristic-eval, the new anti-patterns ref).
  The two new doctrine refs are **genuinely operationalized**, not decorative.
- **The named 2026 gaps closed:** C2PA/provenance, SF Symbols 8, Material 3 Expressive, the
  gesture-alternative WCAG table, the ζ≥0.7 spring-fingerprint inoculation.
- **The dangling P1 references are resolved** — three previously-promised siblings now exist and
  are good.

**Why it is still 64 and not 70+ — four things hold the line, all consistent with the strict bar:**

1. **The v2 plan added examples to the legacy stubs without re-authoring the stubs.** The exact
   prior boilerplate-shell set survives verbatim — **7 SKILL.md with the full "reusable judgment"
   shell**, ~5 more with the "Evidence Produced" table, 5 with the "matches this domain" stub. A
   generated shell in an explicitly anti-slop engine is itself a slop signal, and several deep
   skills (`practical-ui-design` −4, `data-visualization` −2, `healthcare-ui-design` −2) **drop
   points** because their peers were re-authored and they were not. This is the single biggest
   thing capping the aggregate — and it is the same finding as the prior audit, only now more
   glaring because the examples around it improved.
2. **The new skills are mostly single-reference.** A large share of the 24 new P1 skills ship one
   own `references/` file — enough to anchor a worked example, not enough to reach the high-60s.
   The score rose by *breadth* (every skill now exampled) far more than by any skill reaching
   world-class.
3. **Structural offloads persist:** `deck-system` still generates no PPTX; stale renumbered sibling
   paths dangle inside the legacy stubs; `color-selection` remains a redundant deletion candidate.
4. **The ceiling didn't move.** The top skill is still `color-system-and-palette` at 74; only
   `distinctive-by-design` (76) crosses into the mid-70s. Nothing approaches the 90s the bar
   reserves for Pentagram/Apple — the engine got *broader and more even*, not *taller*.

**Net.** The engine has converted the prior audit's **bimodal "good-and-uneven"** profile into a
**tight "good-and-even" 64-tier**: the floor rose (every skill exampled, the worst new content
book-grounded), the worst structural gaps closed (soul skill, C2PA, dangling refs), and the new
doctrine refs are real. But the **fastest remaining route to 70+ is the same unglamorous job the
prior audit named and the v2 plan skipped: rewrite the ~12 legacy boilerplate-shell skills**
(`design-audit`, `practical-ui-design`, `form-ux-design`, `interaction-design-patterns`,
`healthcare-ui-design`, `motion-design`, `data-visualization`, plus the `brand-style-guide` /
`color-selection` / `ux-psychology` / `legal-sector-ui-ux` / `sector-strategies` stubs), **strip the
"Evidence Produced" tables, fix the stale sibling paths, add PPTX generation, and deepen the
single-ref new skills with a second reference.** The plan added a strong new storey to the building;
it has not yet repaired the cracked rooms on the ground floor it already knew about.
