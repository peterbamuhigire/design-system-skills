# Existing Groups RE-AUDIT — Post-v2-Plan — Design-System-Skills Engine

**Date:** 2026-06-22
**Auditor scope:** All **81 `SKILL.md`** files across **14 groups** (00–13), a sample of their
`references/` and `examples/` subtrees, `doctrine/design-doctrine.md`, and the doctrine
`references/` set (now **12 files**, +2 since the prior audit: `creative-selection-and-taste.md`,
`interaction-anti-patterns.md`).
**Baseline compared against:** `docs/audits/post-phase-1/03-existing-groups-reaudit.md` — **51
skills, 14 groups, aggregate 63/100** (the audit taken when **17 skills lacked any example** and
`distinctive-by-design` shipped zero refs / zero before-after).
**Bar (unchanged, ruthless):** Top-0.1% global — Pentagram / Apple / Awwwards SOTD / D&AD.
90–100 rivals them · 75–89 excellent pro · 60–74 solid but visibly short · 40–59 competent ·
<40 skeletal. Default band 45–65; 70+ requires extraordinary, specific justification.

> **Method.** Doctrine + the two NEW doctrine references read in full. SKILL.md files read across
> all 14 groups; the new P1/P2 skills (`demo-driven-design-process`,
> `heuristic-evaluation-and-design-critique`, `voice-tone-and-content-style-guide`,
> `ecommerce-and-checkout-ux`, `chart-selection-and-encoding`, `figma-and-tooling-workflow`,
> `editorial-and-long-form-layout`, `logo-and-wordmark-design`, `touch-gesture-and-haptics`,
> `ai-image-generation-art-direction`, etc.) read end-to-end; the surviving legacy shells re-read
> at the head to confirm whether the boilerplate was removed. `distinctive-by-design`'s NEW
> `before-after-distinctive.md` (the *Cadence* hero) read end-to-end. A repo-wide grep fixed the
> exact remaining shell set ("reusable judgment", "Evidence Produced", "matches this domain") and
> verified the book attributions (Podmajersky, Kocienda, Maioli, Neil, Tognazzini, Cleveland–McGill)
> and the C2PA/Figma-variables/Dev-Mode claims.

---

## Headline: the engine crossed from "good-and-uneven" to "**broad, good, and example-complete** — with the same hard legacy core still visible." The v2 plan closed the prior audit's two flagship gaps and added a strong new skill tier; it did **not** re-author the old boilerplate shells.

The prior audit's defining split — a strong NEW tier vs an untouched legacy-shell tier — **persists**,
but the engine moved decisively on three fronts:

1. **Every one of the 81 skills now ships a worked example.** This is the single biggest change and
   it closes the prior audit's #1 systemic gap. The prior audit scored 63 *with 17 skills having no
   example at all*; that count is now **zero**. Each skill directory carries a populated `examples/`
   file — verified by directory walk, not assertion (the deck group alone ships 8 worked variants;
   tokens ships `tokens.json` + `semantic-mapping.md`; docx/pdf/imagery each ship real artifacts).
2. **`distinctive-by-design` — the soul skill — now has its before/after.** The prior audit's #2
   open gap ("preaches distinctiveness it never demonstrates") is closed: `before-after-distinctive.md`
   takes one real screen (the *Cadence* EM-status-update SaaS hero) from convergent slop (Inter,
   indigo→blue gradient, centred card grid, ✨ badge) to an authored version (asymmetric editorial
   split in Bricolage Grotesque, grounded in Vignelli) with the full human-craft checklist run. It
   is one of the better worked examples in the engine. The skill *still* ships **zero own refs**
   (it leans entirely on doctrine refs), which keeps it just under the world-class line — but the
   "tells-not-shows" charge no longer holds.
3. **24+ new P1/P2 skills, almost all book-sourced and current-2026, form a genuinely strong tier.**
   `demo-driven-design-process` fully operationalises Kocienda's creative-selection loop
   (algorithm-vs-heuristic test, fidelity ring, "live on it", 41-blues lesson) — and it is backed by
   a new doctrine ref of the same quality. `voice-tone-and-content-style-guide` operationalises
   Podmajersky's six-row Voice Chart + Tone Map + lexicon governance. `heuristic-evaluation-and-design-critique`
   runs Nielsen + Tognazzini with a real severity-capture protocol. `ecommerce-and-checkout-ux` is a
   strict anti-dark-pattern retail playbook. `chart-selection-and-encoding` splits the Cleveland–McGill
   selection decision out cleanly. `figma-and-tooling-workflow` is explicitly current Figma
   (variables/modes, Dev Mode, branching) and refuses Sketch/XD. `logo-and-wordmark-design`,
   `touch-gesture-and-haptics`, `editorial-and-long-form-layout`, `ai-image-generation-art-direction`
   (which **closes the C2PA/provenance gap** the prior audit flagged as the last surviving 2026 hole)
   round it out. These are the engine's better tier — well-routed, deduplicated against siblings,
   doctrine-anchored.

### What did NOT change (and still costs points under the strict bar)

- **The boilerplate shell survives in ~8 legacy SKILL.md heads.** Grep is exact. Eight skills still
  open with the auto-generated *"The task needs reusable judgment, domain constraints…"* Use-When
  and/or the *"Evidence Produced"* table at the top of the SKILL.md body:
  `interaction-design-patterns`, `practical-ui-design`, `form-ux-design`, `motion-design`,
  `data-visualization`, `healthcare-ui-design`, `design-audit`, `webapp-gui-design`. They now have
  examples bolted on, but the **entrypoint is still a slop signal in an anti-slop engine** — the
  first thing the reader sees is filler. `interaction-design-patterns` is the worst: ~50 lines of
  pure generated boilerplate sit *above* the real Tidwell content.
- **Five "matches this domain" variant stubs persist** (`brand-style-guide`, `color-selection`,
  `ux-psychology`, `legal-sector-ui-ux`, `sector-strategies`) — now exampled, but the SKILL.md
  framing is still the generated variant.
- **The "specs-not-render" ceiling holds.** Decks still build no PPTX (route to human); mobile and
  several UI skills are gates/specs, not generators. Correct for a design engine, but it caps the
  top end.

---

## Group-by-group

### Group 00 — Cross-cutting Ops / QA / A11y — **66/100**  *(prior 65, +1)*

Grew from 6 → 11 skills, and the additions are strong: `design-ethics-and-anti-dark-patterns`,
`inclusive-and-assistive-design`, `design-critique-and-review-facilitation` (Kocienda-grounded "no
critique without a concrete artifact"), `product-design-audit`, and `ux-remediation-and-redesign`
(Maioli-grounded detect→triage→fix→re-validate). All exampled. The new `interaction-anti-patterns.md`
doctrine ref (Neil + Maioli, updated to WCAG 2.2) gives these audits a shared behavioural checklist —
a real upgrade. Drag: `design-audit` **still carries the boilerplate shell + "Evidence Produced"
table**, and the five-plus audit/critique skills overlap each other more than a world-class engine
would tolerate (design-audit vs product-design-audit vs visual-product-slop-audit vs design-qa).
**Standout:** `design-critique-and-review-facilitation`. **Weakest:** `visual-product-slop-audit`
(81L, thin mirror of the taxonomy) — or `design-audit` for the surviving shell.

### Group 01 — Typography & Fonts — **62/100**  *(prior 60, +2)*

Two new skills lift it: `fluid-responsive-typography` (clamp() + locks) and
`variable-fonts-and-opentype-features` (axes, `font-feature-settings`, a dashboard type system) —
both exampled, both answering named 2026 gaps. `font-selection-and-pairing` remains the spine.
The three plumbing skills (`premium-font-scan`, `font-embedding-and-licensing`,
`ai-slop-typography-audit`) are now exampled but remain thin procedural wrappers; the slop-audit
skill still lacks font-inference-from-screenshot. **Standout:** `variable-fonts-and-opentype-features`.
**Weakest:** `font-embedding-and-licensing` (68L plumbing).

### Group 02 — Color, Brand & Visual Identity — **67/100**  *(prior 68, −1)*

Still the OKLCH-operationalised standout (`color-system-and-palette` + worked ramp + measured
contrast; `accessible-color-and-contrast` with the APCA-vs-WCAG split; `dark-mode-and-theming`
remap-not-invert). The new `logo-and-wordmark-design` is a genuinely good buildable-mark skill
(grid construction, lockup family, favicon/app-icon system, Janoff interactive-wit lever) with a
worked aperture-mark spec. The −1 is honest, not punitive: `color-selection` is now openly redundant
with `color-system-and-palette` (a deletion candidate the routing itself admits), and `brand-style-guide`
still carries the "matches this domain" framing — two soft spots dilute an otherwise top group.
**Standout:** `color-system-and-palette`. **Weakest:** `color-selection`.

### Group 03 — Layout, Grid & Composition — **66/100**  *(prior 65, +1)*

The two prior skills (`layout-grid-and-spacing`, `responsive-and-adaptive-layout`) are joined by two
strong new ones: `composition-and-visual-hierarchy` (focal point, eye-path, Gestalt, with a
before/after composition) and `editorial-and-long-form-layout` (measure, reading rhythm, drop
caps/pull-quotes/sidenotes, the web-reading partner to the DOCX skill). All four authored, exampled,
no shells — one of the cleanest groups. **Standout:** `editorial-and-long-form-layout`.
**Weakest:** `layout-grid-and-spacing` (solid but the most generic of the four).

### Group 04 — Web & UI Design — **63/100**  *(prior 62, +1)*

Still the largest (15 skills) and the most **bimodal** group in the engine — but the v2 plan added a
strong NEW cohort and resolved the prior audit's dangling forward-references: the three sibling
skills the prior audit flagged as *missing* now **exist and are good** — `onboarding-and-first-run-design`,
`trust-credibility-and-social-proof`, and `ecommerce-and-checkout-ux` (in group 06). Plus
`component-states-and-interaction-fidelity` and `email-and-newsletter-design`. And
**`distinctive-by-design` now has its before/after** (+ a strengthened body), lifting the soul skill.
Against that, the legacy core is **unchanged**: `interaction-design-patterns`, `practical-ui-design`,
`form-ux-design`, `webapp-gui-design` all **still open with the boilerplate shell** and now merely
have examples bolted on; `premium-ui-ux-design` still *asserts* premium (13 refs, but the worked
example is a "direction", not a rendered screen). The band barely moves because the new wins are
dragged by ~5 unimproved shell skills. **Standout:** `distinctive-by-design` (73) — now with its
example. **Weakest:** `interaction-design-patterns` (57) — the most egregious surviving shell, ~50
boilerplate lines above the real Tidwell content.

### Group 05 — UX Process, Research & Psychology — **62/100**  *(prior 58, +4)*

The biggest mover among the carried-over groups, on the back of two excellent NEW process skills.
`demo-driven-design-process` is the engine's best new skill — it fully operationalises the new
`creative-selection-and-taste.md` doctrine ref (Kocienda): the algorithm-vs-heuristic test, the
fidelity ring + non-goals, "live on it", convergence-by-subtraction, the 41-blues lesson as the
named argument against outsourcing taste to a metric *or* an AI pick — with a real four-round
iteration log. `heuristic-evaluation-and-design-critique` (Nielsen 10 + Tognazzini, 0–4 severity,
worked evaluation) and `journey-mapping-and-service-design` are also strong. The carried-over
`ux-psychology` is **still the "matches this domain" stub** (now exampled but unreauthored) and
`enterprise-ux-process` is process-not-craft. **Standout:** `demo-driven-design-process` (one of
two or three best skills in the engine). **Weakest:** `ux-psychology`.

### Group 06 — Sector & Domain UX — **60/100**  *(prior 57, +3)*

Two genuinely strong new sector skills lift the floor: `ecommerce-and-checkout-ux` (strict
anti-dark-pattern retail: guest-first, total-cost transparency, real scarcity, symmetric returns)
and `fintech-and-financial-product-ui` (with a worked send-money screen). `healthcare-ui-design`
remains the deepest single domain skill (15 refs, clinical thresholds, HIPAA/FHIR) but **still
carries the boilerplate shell + "Evidence Produced"**, and `legal-sector-ui-ux` + `sector-strategies`
remain the "matches this domain" stubs (sector-strategies is still structurally a "choose
sector → customise template" factory). **Standout:** `ecommerce-and-checkout-ux`.
**Weakest:** `sector-strategies`.

### Group 07 — Mobile (iOS / Android / Cross-platform) — **64/100**  *(prior 63, +1)*

The prior-audit rewrite of `ios-ui-ux-design` (Liquid Glass chrome-only, SF Symbols 7, AX5, haptics)
holds, and two new skills deepen the group: `touch-gesture-and-haptics` (thumb-zone ergonomics,
gesture vocabulary, WCAG 2.5.1/2.5.7 single-pointer fallbacks, iOS/Android haptic semantics) and
`app-store-presence-and-aso` (store-listing asset spec). All exampled. Android remains lighter on
M3-Expressive specifics than iOS is on its 2026 set. **Standout:** `ios-ui-ux-design`.
**Weakest:** `app-store-presence-and-aso` (useful but the most peripheral to *design* craft).

### Group 08 — Motion & Interaction — **63/100**  *(prior 62, +1)*

The single-skill group is now two: the carried-over `motion-design` (springs + View Transitions
present, but **still the boilerplate shell + "Evidence Produced" header** — the prior audit's exact
complaint, unaddressed) is joined by the strong new `micro-interactions-and-feedback` (anatomy:
trigger→rules→feedback→loops, with inoculation notes and a worked toggle-switch spec). The new skill
is cleaner than the legacy one it sits beside. **Standout:** `micro-interactions-and-feedback`.
**Weakest:** `motion-design` (deep body, slop-signal shell head).

### Group 09 — Design Systems, Tokens & Theming — **66/100**  *(prior 65, +1)*

The three-tier token backbone (`design-tokens-and-naming` + `component-library-architecture` +
`design-handoff-and-dev-spec`) is joined by `figma-and-tooling-workflow` — explicitly *current*
Figma (variables with modes for theming/breakpoints, component properties/variants, styles-vs-variables,
Dev Mode handoff, branching/publishing), refusing Sketch/XD/Axure by name, with a worked Figma-setup
example. Clean routing, no overlap, all exampled. One of the most coherent groups. **Standout:**
`design-tokens-and-naming`. **Weakest:** `component-library-architecture` (74L SKILL.md — leanest of
the four, leans hard on its example).

### Group 10 — Content Design & UX Writing — **65/100**  *(prior 63, +2)*

The two prior skills gain a strong upstream parent: `voice-tone-and-content-style-guide` operationalises
Podmajersky's six-row Voice Chart × product-principle columns + ratified tiebreaker, the Tone Map
across the user lifecycle, and lexicon governance — and cleanly delegates *textual AI-slop detection*
to the research engine rather than duplicating it (a sharp boundary). `ux-writing-and-microcopy` and
`error-empty-and-system-messaging` both carry reasoned before/after rewrites. Solid; short of
world-class only on localised-voice depth. **Standout:** `voice-tone-and-content-style-guide`.
**Weakest:** `ux-writing-and-microcopy` (good, but the most conventional of the three).

### Group 11 — Imagery, Illustration & Art Direction — **63/100**  *(prior 60, +3)*

The prior audit's "last surviving 2026 gap" — **C2PA / provenance — is now closed**:
`ai-image-generation-art-direction` makes AI imagery a directed/gated/post-processed/**provenance-checked**
act (training-data rights, C2PA, indemnity, truth-claim surfaces, when-NOT-to-use), keyed to the
sourcing-authority asymmetry rule. `illustration-style-and-systems` adds a real style-system spec.
`iconography-system-design` and `photography-art-direction` carry over. All exampled. The group still
doesn't reach named-studio art-direction depth, but the systemic hole is gone. **Standout:**
`ai-image-generation-art-direction`. **Weakest:** `photography-art-direction`.

### Group 12 — Data-Viz & Dashboards — **64/100**  *(prior 64, ±0)*

`chart-selection-and-encoding` is a clean new addition — the *upstream* data-type×message→chart
routing (pie→sorted bar, dual-axis ban, zero-baseline honesty, non-colour cues), explicitly ceding
the Cleveland–McGill perceptual ranking and decluttering craft to `data-visualization`. The split is
well-drawn. But `data-visualization` itself **still carries the boilerplate shell + "Evidence
Produced" table** and is still on the single-2015-Knaflic spine (no scrollytelling/uncertainty); it
is the anchor that keeps the group from rising. `dashboard-and-data-product-design` carries over
strong. **Standout:** `dashboard-and-data-product-design`. **Weakest:** `data-visualization`
(content-rich, shell-headed, dated spine).

### Group 13 — Presentations & Documents — **63/100**  *(prior 62, +1)*

The 8-decks→1 consolidation holds (`deck-system` + 8 worked variants), DOCX/PDF formatting carry
over, and two new skills deepen it: `design-storytelling-and-case-studies` (with a worked KesiLex
onboarding case study) and `xlsx-and-financial-model-presentation` (KPI/model-summary exhibit — a
real artifact, ties cleanly to the finance engine). Remaining defect unchanged: `deck-system` still
routes the actual PPTX build to the human. **Standout:** `xlsx-and-financial-model-presentation`
(genuinely fills a presentation-of-numbers gap). **Weakest:** `deck-system` (builds no PPTX).

---

## Group ranking (post-v2-plan, weakest → strongest)

| Group | Score | Δ vs prior | One-line verdict |
|---|---:|---|---|
| 06 Sector & Domain UX | 60 | +3 | Strong new ecommerce/fintech; deep healthcare + two "matches this domain" stubs still drag. |
| 01 Typography | 62 | +2 | Two strong new fluid/variable-font skills; three plumbing skills stay thin. |
| 05 UX Process & Psychology | 62 | +4 | `demo-driven-design-process` (Kocienda) is a top-tier addition; `ux-psychology` stub persists. |
| 04 Web & UI | 63 | +1 | Soul skill now exampled, dangling P1 refs resolved; ~5 legacy shells unchanged. |
| 08 Motion | 63 | +1 | Strong new micro-interactions skill beside the still-shell-headed `motion-design`. |
| 11 Imagery / Art Direction | 63 | +3 | C2PA/provenance gap now closed via the AI-image skill. |
| 13 Presentations & Documents | 63 | +1 | Storytelling + XLSX deepen it; deck still builds no PPTX. |
| 12 Data-Viz & Dashboards | 64 | ±0 | Clean new chart-selection split; `data-visualization` shell + dated spine cap it. |
| 07 Mobile | 64 | +1 | Touch/haptics + ASO deepen a strong iOS/Android/parity spine. |
| 10 Content Design | 65 | +2 | Podmajersky Voice Chart system now anchors microcopy/error siblings. |
| 02 Color, Brand & Identity | 67 | −1 | Still OKLCH standout + new logo skill; redundant `color-selection` + brand stub dilute. |
| 00 Cross-cutting QA/A11y | 66 | +1 | New ethics/inclusive/critique/remediation spine; `design-audit` shell + audit overlap. |
| 03 Layout & Composition | 66 | +1 | Four authored, exampled, shell-free skills — one of the cleanest groups. |
| 09 Design Systems & Tokens | 66 | +1 | Coherent token backbone + current-Figma workflow; no overlap, all exampled. |

---

## NEW aggregate skill-depth score — **64/100**  ·  delta vs prior **63** = **+1**

**Computation.** Skill-count-weighted mean across the 81 scored skills (group counts:
00=11, 01=6, 02=7, 03=4, 04=15, 05=7, 06=5, 07=5, 08=2, 09=4, 10=3, 11=4, 12=3, 13=5) lands at
**~64/100** — squarely in the "solid but visibly short of world-class" band. The same harsh,
no-grade-inflation rubric is applied.

**Why it rose — the gains are real and the prior audit's two flagship gaps are closed.**

- **The examples drought is fully closed: 0/81 skills now lack a worked example** (prior: 17 of 51).
  This was the prior audit's *single biggest* recommendation and it is done across the board, with
  verified-real artifacts (the *Cadence* before/after, the four-round demo-iteration log, the Voice
  Chart guide, the send-money screen, the Figma-setup spec, the XLSX exhibit, the 8 deck variants).
- **`distinctive-by-design` — the soul skill — now demonstrates what it preaches.** Its before/after
  is one of the better worked examples in the engine; the prior audit's #2 open gap is closed.
- **The new P1/P2 tier is strong and book-sourced.** Two new doctrine refs of high quality
  (`creative-selection-and-taste.md` from Kocienda; `interaction-anti-patterns.md` from Neil+Maioli,
  WCAG-2.2-aligned) anchor a cohort of genuinely good skills (demo-driven process, voice/tone system,
  heuristic evaluation, honest e-commerce, chart-selection, current-Figma, logo system, touch/haptics,
  editorial layout). The C2PA/provenance gap and the dangling forward-references the prior audit
  flagged are both **resolved**.

**Why it is only +1, not more.** The strict bar punishes three things the v2 plan did **not** touch:

1. **The legacy boilerplate shells were not re-authored — only exampled.** Eight SKILL.md files still
   open with the auto-generated "reusable judgment" Use-When and/or "Evidence Produced" table
   (`interaction-design-patterns`, `practical-ui-design`, `form-ux-design`, `motion-design`,
   `data-visualization`, `healthcare-ui-design`, `design-audit`, `webapp-gui-design`), plus five
   "matches this domain" variant stubs. Adding an example to a skill whose *entrypoint is filler*
   does not fix the entrypoint — and a templated shell is itself a slop signal in an anti-slop
   engine. The denominator also grew (51→81), so 30 strong new skills averaged against an unchanged
   ~13-skill weak legacy core nets only a small rise.
2. **The "specs-not-render" ceiling holds.** Decks build no PPTX; most UI/mobile skills gate or spec
   rather than generate. Defensible for a design engine, but it caps the top end — no skill reaches
   the 75+ "excellent pro" band, and the engine's best (`color-system-and-palette` 74,
   `distinctive-by-design` 73, `demo-driven-design-process` ~72) sit just below it.
3. **Residual depth gaps survive on the carried-over anchors.** `data-visualization` is still on a
   single-2015-book spine; `premium-ui-ux-design` still asserts rather than renders premium; the
   group-00 audits still overlap; `color-selection` is now openly redundant.

**Net.** The doctrine remains the engine's best asset, now reinforced by two strong book-sourced
references. The skill layer is **broad (81 skills), example-complete (100%), and bimodal**: a real
65–74 tier of new, book-grounded, current-2026 skills sits over an unchanged ~13-skill legacy core
that still wears its generated shell. The fastest remaining route to 70+ is the same unglamorous job
the prior audit named — now narrowed to one task: **re-author the ~8 boilerplate-shell SKILL.md
heads (and the 5 "matches this domain" stubs) so their entrypoints match the quality of their bodies
and their examples.** That is finishing the v2 job on the skills v2 skipped — not a new-skill task.
