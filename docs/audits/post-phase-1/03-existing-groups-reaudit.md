# Existing Groups RE-AUDIT — Post-Phase-1 — Design-System-Skills Engine

**Date:** 2026-06-21
**Auditor scope:** All **51 `SKILL.md`** files across **14 groups** (00–13), their `references/`
and `examples/` subtrees, `doctrine/design-doctrine.md`, and all 10 `doctrine/references/*.md`.
**Baseline compared against:** `docs/initial-analysis/03-existing-groups-audit.md` — 37 skills, 6
groups, aggregate **58/100**.
**Bar (unchanged, ruthless):** Top-0.1% global — Pentagram / Apple / Awwwards SOTD / ADA / D&AD.
90–100 rivals them · 75–89 excellent pro · 60–74 solid but visibly short · 40–59 competent ·
<40 skeletal. Default band 45–65; 70+ requires extraordinary, specific justification.

> **Method.** Doctrine + all 10 references read in full. SKILL.md files read across the lead
> auditor + a parallel reviewer (groups 00/01), with worked-example files opened directly for
> calibration (≥1 per group; the OKLCH, landing, table-states, deck, docx, iOS, microcopy
> examples read end-to-end). A repo-wide grep for the two legacy boilerplate-shell signatures
> ("The task needs reusable judgment, domain constraints" and the "Evidence Produced" migration
> table) was used to fix the exact remaining-stub set.

---

## Headline: the engine moved from "great doctrine, competent skills" to "great doctrine, **good-and-uneven** skills." Phase 1 closed three of the four systemic gaps — for the skills it touched.

The split the baseline diagnosed (world-class doctrine over a merely-competent skill layer) has
**materially narrowed**, but in a **bimodal** way:

- **Phase-1-authored / rewritten skills are genuinely good** (a real 65–74 tier now exists with
  *justification*, not just assertion): they operationalize 2026 standards, carry their own
  reference files, and ship **real worked examples** (named brief → applied artifact → checklist
  run). `color-system-and-palette`, `accessible-color-and-contrast`, `dark-mode-and-theming`,
  `responsive-and-adaptive-layout`, `design-tokens-and-naming`, `landing-page-and-conversion-design`,
  `empty-error-and-loading-states`, `deck-system`, `ios-ui-ux-design`, `docx-…`, and the typography
  pair are the new spine.
- **Pre-Phase-1 migrated skills are largely untouched** and still carry the **auto-generated
  boilerplate shell** ("Use When → The task needs reusable judgment…", "Evidence Produced" table)
  with **no examples**. The grep is exact: **7 skills still carry the shell** —
  `design-audit`, `form-ux-design`, `interaction-design-patterns`, `practical-ui-design`,
  `healthcare-ui-design`, `motion-design`, `data-visualization` — plus the `ux-psychology` /
  `sector-strategies` / `legal-sector-ui-ux` "matches this domain" variant stubs. For several of
  these the *body below the shell* is deep (motion, data-viz, healthcare), so the slop-signal
  entrypoint is now the main defect rather than thin content.

### The four systemic weaknesses, re-scored

1. **Examples drought → largely CLOSED.** **34 of 51 skills now ship a real worked example**
   (64–332 lines; verified non-stub). The OKLCH palette (full ramp + measured contrast matrix),
   the Tallymark landing spec, the every-state table component, the 8 deck variants, the
   default-vs-designed DOCX before/after, the iOS "Send Payment" screen — these are exactly the
   "show, don't just tell" artifacts the baseline said were *entirely absent*. **The single
   disqualifying gap is no longer disqualifying.** The 17 without examples are precisely the
   untouched legacy skills.
2. **Boilerplate-stub entrypoints → HALVED but not gone.** The worst offenders were deleted or
   rewritten; ~10 remain (7 shell + 3 "matches this domain"). Still a slop signal in an
   anti-slop engine, now concentrated in the older Group-04/05/06/08/12 skills.
3. **Missing 2026 standards → CLOSED at the doctrine + new-skill layer.** OKLCH is now **fully
   operationalized** (L/C/H channel recipe, stop tables, gamut + neutral handling, a worked ramp
   with hexes). **APCA-design / WCAG-certify** split is encoded with its own ref. **WCAG 2.2**
   (24px target, dragging, redundant entry, accessible auth) is a whole new cross-cutting group.
   **View Transitions, spring physics (`linear()`), container queries, fluid `clamp()`,
   variable-font axes, Liquid Glass (chrome-only), SF Symbols 7, haptics, Material 3** all now
   appear with references. The baseline's entire "missing 2026" list is substantially answered —
   *except* C2PA/provenance, which I did not find operationalized.
4. **Redundancy → CLOSED.** The 8 byte-identical deck skills are consolidated into **one
   `deck-system`** with the 8 purposes preserved as `variant-*` examples. The 5 overlapping
   color/brand skills are rationalized (`brand-alignment` removed; clear "do not use when →"
   routing between `color-system-and-palette` and `accessible-color-and-contrast`).

**Still open:** (a) ~10 boilerplate shells; (b) `distinctive-by-design` — the soul skill — *still*
ships **zero own refs and zero before/after**, preaching distinctiveness it never demonstrates;
(c) several skills reference **P1/P2 siblings that do not yet exist** (`trust-credibility-and-social-proof`,
`onboarding-and-first-run-design`, `ecommerce-and-checkout-ux`) — dangling forward-references;
(d) the deck group still **builds no actual PPTX** (routes execution to the human), though `docx-`
and `pdf-` siblings are now real; (e) no C2PA/provenance.

---

## Group-by-group

### Group 00 — Cross-cutting Ops / QA / A11y — **65/100**  *(NEW — no baseline)*

A strong, genuinely new spine that did not exist before. Six skills, all authored (no thin
content), all with worked examples; the WCAG-2.2 skill operationalizes the 2.2-specific criteria
(target size, dragging, redundant entry, accessible auth) rather than restating them, and
co-activation routing is clean. Drag on the band: `design-audit` still carries the boilerplate
shell + "Evidence Produced" table; the audits overlap each other and the doctrine more than a
world-class engine would tolerate.

| Skill | Score | Refs | Examples | Notes |
|---|---:|---|---|---|
| accessibility-wcag-2-2-compliance | 70 | 2 | Yes (audit sheet, 73L) | Operationalizes the 9 new 2.2 SCs as build-then-audit; clean delegation to the contrast skill; worked audit sheet. Short of 75: no per-framework (SwiftUI/Compose) worked component, leans on the doctrine ref. |
| design-qa-and-pre-launch-review | 64 | 1 | Yes (184L filled review) | Real composed gate (a11y+slop+perf); good filled example. Still carries the legacy "Evidence Produced" table. |
| performance-as-ux-and-core-web-vitals | 63 | 1 | Yes (budget sheet) | Treats CWV as a design constraint with a real budget sheet; thin on INP-specific remediation patterns. |
| internationalization-and-rtl-design | 60 | 2 | Yes (RTL before/after) | Logical-properties + translation-expansion; worked RTL flip. Thinner than the color/type new skills. |
| design-audit | 58 | 4 | Yes (141L filled) | Usable 10-dimension rubric + a filled sample (a baseline ask, now met). But **still the boilerplate shell**; overlaps `visual-product-slop-audit` + doctrine; AI-slop still under-weighted. |
| visual-product-slop-audit | 58 | 1 | Yes (filled, 78L) | Now has a worked filled audit (baseline had none). Still a thin mirror of `ai-slop-taxonomy.md`; no diffusion-artifact/C2PA generative tells. |

### Group 01 — Typography & Fonts — **60/100**  *(baseline 56, +4)*

The doctrine's sharpest area; the skills are now better-supported. `font-selection-and-pairing`
gained a `pairing-catalog.md`, a `type-scale-recipes.md` (with **fluid `clamp()` + variable-font
axes** — a named baseline gap), and a real applied example. The other three remain thin
procedural wrappers with no own examples — `premium-font-scan` and `font-embedding-and-licensing`
are essentially unchanged plumbing; `ai-slop-typography-audit` is cleaner but still lacks
screenshot/OCR font-inference and a before/after.

| Skill | Score | Refs | Examples | Notes (Δ vs baseline) |
|---|---:|---|---|---|
| font-selection-and-pairing | 66 | 2 | Yes (applied-type-scale) | **+4.** Pairing catalog + scale recipes (clamp/variable axes) + worked Maduuka scale. Real spine. Still a router over the doctrine; no x-height/contrast diagnostic. |
| ai-slop-typography-audit | 57 | 0 | No | **+2.** Tighter detection + severity scoring. Still no own refs/examples, no font-inference-from-screenshot, before/after only *described*. |
| premium-font-scan | 52 | 0 | No | **±0.** Unchanged `ls fonts/<group>/` + MANIFEST plumbing. No quality-vetting rule. |
| font-embedding-and-licensing | 51 | 0 | No | **+1.** Still a compression of two doctrine refs; subsetting toolchain only named, not worked. |

### Group 02 — Color, Brand & Visual Identity — **68/100**  *(baseline "Group 04" 56, +12 — biggest gain)*

The standout Phase-1 result. **OKLCH is now fully operationalized** — `oklch-ramp-construction.md`
(L/C/H channels, stop tables, gamut, low-chroma neutrals) plus a **worked example with real
hexes and a measured light+dark contrast matrix and a retune-on-fail loop**. **APCA-design /
WCAG-certify** is split out with `apca-vs-wcag.md`; colour-blind-safe ramps (Okabe–Ito / IBM /
Viridis) get their own ref. `dark-mode-and-theming` is a real role re-bind (not inversion) with a
token-pair example. The redundancy is gone (`brand-alignment` removed; clear routing). The exact
two baseline criticisms — "OKLCH named not operationalized" and "WCAG 2 only, no APCA" — are
both fully answered.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| color-system-and-palette | 74 | 2 | Yes (OKLCH worked) | **+6.** Operationalized OKLCH recipe + worked ramp w/ hexes + measured contrast + APCA/WCAG split. The most-improved skill; just shy of world-class (single worked anchor; categorical scales still punted to G12). |
| accessible-color-and-contrast | 70 | 2 | Yes (contrast matrix) | **NEW.** APCA-vs-WCAG done correctly (design vs certify), full pair×pair matrix example, CVD ramps + non-colour-cue rule. Strong. |
| dark-mode-and-theming | 66 | 1 | Yes (light-dark token pair) | **NEW.** Remap-not-invert, elevation-flip, accent lightening, re-certify dark independently. Real token-pair example. |
| brand-visual-identity | 65 | 3 | Yes (mini-guide) | **±0.** Strategy-first, ownability test; now a worked mini-identity. Still no logo-construction technique / motion-system depth. |
| brand-style-guide | 54 | 3 | Template only | **+2.** Real template; body still generic; no worked specimen. |
| color-selection | 50 | 9 | No | **±0.** Now clearly redundant with `color-system-and-palette` (routing admits it); kept for the `flux-process.md`/generator. Candidate for deletion. |

### Group 03 — Layout, Grid & Composition — **65/100**  *(baseline "Group 05" 64 partial, +1)*

`layout-grid-and-spacing` now has a **worked grid spec with measurements** (`grid-template-worked.md`,
144L) — the exact baseline gap. The new `responsive-and-adaptive-layout` is a genuinely strong
2026 skill: **container queries, fluid `clamp()`, intrinsic layout, mobile-first breakpoint
strategy** with a worked responsive-grid template. Both authored, no shells.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| responsive-and-adaptive-layout | 67 | 2 | Yes (responsive grid) | **NEW.** Container queries + clamp() + intrinsic; kills the "collapses to one stacked column" slop tell. Strong. |
| layout-grid-and-spacing | 64 | 2 | Yes (worked grid w/ numbers) | **+3.** Now has the concrete grid spec the baseline demanded. Still abstract on print-grid baseline cases. |

### Group 04 — Web & UI Design — **62/100**  *(baseline "Group 03" 60, +2)*

The largest group (11 skills) and the most **bimodal** in the engine. The three NEW skills are
excellent and example-backed; the legacy core (`practical-ui-design`, `interaction-design-patterns`,
`webapp-gui-design`, `form-ux-design`, `premium-ui-ux-design`, `ai-output-design`, `ai-agent-ux`)
is **almost entirely untouched** — boilerplate shells, **no examples**, no new 2026 craft. The
band barely moves because the new wins are dragged down by ~7 unimproved older skills, and the new
skills carry **dangling references** to P1 siblings that don't yet exist.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| distinctive-by-design | 73 | 0 | **No** | **+1.** The soul skill — now a fully-fleshed pre-flight + human-craft checklist. **Still zero refs, zero before/after**; it *forbids* the templated hero it never *shows* reauthored. The engine's most glaring "tells-not-shows" hole. |
| landing-page-and-conversion-design | 70 | 2 | Yes (Tallymark spec) | **NEW.** Section spine + honest-conversion ethics (dark-pattern→honest-swap) + WCAG/perf as conversion; a real, named, checklist-applied worked spec. Held back: references 3 non-existent P1 siblings. |
| empty-error-and-loading-states | 68 | 1 | Yes (every-state table) | **NEW.** Every reachable state of one real fintech table authored up front; exactly the "states as first-class" exemplar the baseline wanted. |
| navigation-and-information-architecture | 64 | 2 | Yes (sitemap/nav spec) | **NEW.** Solid IA + worked sitemap; not yet world-class on large-scale faceted nav. |
| practical-ui-design | 66 | 2 | **No** | **−2.** Strong rules body survives, but **boilerplate shell + still no worked example**; net erosion vs baseline 68 under the same harsh bar. |
| ai-output-design | 66 | 6 | No | **−2.** Still sharp/current (Macfadyen 2025), but no full chat→canvas worked spec and shell header; baseline 68 doesn't hold without an example. |
| webapp-gui-design | 64 | 3 | No | **±0.** Strongest code skill (Next.js/Radix, four-state rule). Still visually generic defaults; "Evidence Produced" table; no example. |
| premium-ui-ux-design | 63 | 13 | No | **−3.** "Premium" still asserted via adjectives, **not demonstrated** — 13 refs but **no worked screen**. The baseline 66 was generous; under the no-example rule it slips. |
| form-ux-design | 58 | 6 | No | **±0.** Deep cross-platform refs, but boilerplate shell, no worked exemplar form, nothing on passkeys/OTP/inline-AI. |
| interaction-design-patterns | 57 | 0 | No | **−3.** Pure auto-generated shell at the top (the filler "reusable judgment" Use-When); a Tidwell digest with no own refs/examples. The clearest untouched-stub in the group. |
| ai-agent-ux | 54 | 5 | No | **+2.** Router shell over child refs; no top-level worked agent surface, no approval-diff/interrupt patterns surfaced. |

### Group 05 — UX Process, Research & Psychology — **58/100**  *(baseline ~58, +0)*

Two NEW process skills with worked examples lift the floor, but the two carried-over skills
(`ux-psychology`, `enterprise-ux-process`) are the legacy "matches this domain" / deep-but-process
stubs and did not improve. Process, not visual craft — the right tools on the wrong axis for a
*design* engine, as the baseline noted.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| ux-research-and-usability-testing | 62 | 2 | Yes (plan+synthesis) | **NEW.** Real research-plan→synthesis worked artifact; competent, not world-class. |
| wireframing-and-prototyping | 61 | 1 | Yes (wireflow) | **NEW.** Worked wireflow; solid mid-fidelity discipline. |
| enterprise-ux-process | 58 | 7 | No | **±0.** Rigorous 9-phase ops methodology; process not visual craft; no example. |
| ux-psychology | 52 | 3 | No | **−6.** Still the "matches this domain" boilerplate variant over a legacy dump; no bias→pattern table, no example. The same skeleton the baseline flagged. |

### Group 06 — Sector & Domain UX — **57/100**  *(baseline "Group 03" sector skills 54–64)*

Bimodal: `healthcare-ui-design` remains the deepest domain skill in the engine (clinical
thresholds, HIPAA/FDA/HL7 FHIR, working code) but **still carries the boilerplate shell + no
example**. `legal-sector-ui-ux` and `sector-strategies` remain the **slop-prone "matches this
domain" stubs** the baseline flagged — `sector-strategies` is still structurally a
"choose sector → customize template" factory whose anti-homogeneity gate is named but not
operationalized in the SKILL.md.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| healthcare-ui-design | 64 | 15 | No | **±0.** Deepest domain knowledge; boilerplate shell + "Evidence Produced"; no worked screen. Safety > craft, still. |
| legal-sector-ui-ux | 55 | 4 | No | **±0.** Boilerplate stub saved by decent refs; no top-firm trust-pattern teardown. |
| sector-strategies | 53 | 1 | No | **−1.** "Matches this domain" stub over `legacy-guidance.md`; slop-factory risk persists; anti-homogeneity gate not operationalized in-skill. |

### Group 07 — Mobile (iOS / Android / Cross-platform) — **63/100**  *(baseline "Group 06" 49, +14 — second-biggest gain)*

The baseline's *weakest* group is now mid-pack. `ios-ui-ux-design` was substantively rewritten:
**Liquid Glass (chrome-only rule), SF Symbols 7, Dynamic Type to AX5, Core Haptics semantics**,
8 references (incl. dedicated `hig-liquid-glass.md`, `ios-sensory-and-haptics.md`), and a worked
"Send Payment" screen spec. Android gets Material-3 primitives + a worked screen; a new
`cross-platform-design-parity` skill with a worked one-screen parity spec is genuinely useful. The
baseline's entire mobile-2026 gap list (haptics, Dynamic Island-adjacent, M3, gesture, Liquid
Glass beyond a one-liner, worked flow) is largely answered.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| ios-ui-ux-design | 67 | 8 | Yes (screen spec) | **+16.** Liquid Glass chrome-only, SF Symbols 7, AX5, haptics semantics, worked screen. Major rewrite. Still defers code to a dev skill (a gate, not a generator). |
| android-ui-ux-design | 60 | 4 | Yes (screen spec) | **+12.** M3 primitives + worked screen. Lighter on M3 **Expressive** specifics and predictive-back than iOS is on its 2026 set. |
| cross-platform-design-parity | 61 | 2 | Yes (parity spec) | **NEW.** Real "design once, honour both platforms" parity spec; sensible decision rules. |

### Group 08 — Motion & Interaction — **62/100**  *(baseline "motion-design" 57, +5)*

One skill, substantially upgraded **below the shell**. The two sharpest baseline criticisms are
answered: it **no longer forbids springs** (new "Easing vs Spring" section with stiffness/damping
params + CSS `linear()`), and **View Transitions** now have a dedicated ref (`view-transitions.md`,
118L), alongside `spring-physics-and-easing.md` and a worked micro-interaction spec. The defect
that remains is the **auto-generated boilerplate shell at the top** of the SKILL.md and no
scroll-driven `animation-timeline` depth.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| motion-design | 62 | 3 | Yes (micro-interaction spec) | **+5.** Springs + View Transitions now present (baseline's two big misses); worked toggle spec. Held back by the boilerplate shell header and missing scroll-driven animation. |

### Group 09 — Design Systems, Tokens & Theming — **65/100**  *(NEW — no baseline)*

A coherent new group with a clear backbone. `design-tokens-and-naming` establishes the three-tier
primitive→semantic→component architecture, naming convention, multi-brand/dark mapping, and Style
Dictionary export — and routes cleanly into `component-library-architecture` (worked button-component
spec) and `design-handoff-and-dev-spec` (worked handoff sheet). All three authored, all with
examples.

| Skill | Score | Refs | Examples | Notes |
|---|---:|---|---|---|
| design-tokens-and-naming | 67 | 2 | Yes (semantic mapping) | Real three-tier architecture + export targets; the backbone the group leans on. |
| design-handoff-and-dev-spec | 64 | 2 | Yes (handoff sheet, 178L) | Concrete component handoff artifact; strong. |
| component-library-architecture | 63 | 2 | Yes (button spec, 173L) | Worked variant/state matrix for a real component. |

### Group 10 — Content Design & UX Writing — **63/100**  *(NEW — no baseline)*

Two authored skills, both with strong before/after worked examples (the slop→clear microcopy
rewrites carry *reasoning*, which is what makes a content skill transfer). Solid, not yet
world-class (no voice-system-at-scale or localized-voice depth).

| Skill | Score | Refs | Examples | Notes |
|---|---:|---|---|---|
| ux-writing-and-microcopy | 64 | 2 | Yes (before/after w/ reasoning) | Voice-declared-first, verb+object CTA rules, reasoned rewrites. |
| error-empty-and-system-messaging | 63 | 1 | Yes (error copy library) | Real error-copy library; pairs with the states skill. |

### Group 11 — Imagery, Illustration & Art Direction — **60/100**  *(NEW — no baseline)*

Two authored skills with worked specs (icon-set spec; art-direction board). Competent and
example-backed; the art-direction skill states an authored image-POV rule (good, anti-slop), but
neither reaches the named-studio art-direction depth, and **C2PA/provenance for AI imagery is
absent** — the one 2026 gap that survived Phase 1.

| Skill | Score | Refs | Examples | Notes |
|---|---:|---|---|---|
| iconography-system-design | 61 | 1 | Yes (icon-set spec) | Grid/stroke/optical-correction spec; real worked set. |
| photography-art-direction | 59 | 2 | Yes (art-direction board) | Authored image-POV rule (anti stock-grab); no C2PA/provenance check. |

### Group 12 — Data-Viz & Dashboards — **64/100**  *(baseline "data-visualization" 69)*

`data-visualization` remains the most content-complete single skill (Knaflic + Tufte + Gestalt +
preattentive + chart-selection tree), now with a `chart-worked-examples.md`. But it **still carries
the boilerplate shell + "Evidence Produced" table**, and the baseline's single-2015-book-spine /
no-scrollytelling / no-uncertainty / WCAG-2-only limits are unaddressed — so under the same harsh
bar it edges **down** from 69. The new `dashboard-and-data-product-design` (page-above-the-chart:
KPI tiering, cross-filter, real-time freshness UX) is a genuinely strong addition with a worked
dashboard spec.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| data-visualization | 67 | 5 | Yes (chart worked) | **−2.** Still exhaustive + now exampled, but boilerplate shell remains and the single-book-spine / scrollytelling / uncertainty / viridis / WCAG-3 gaps persist. |
| dashboard-and-data-product-design | 65 | 2 | Yes (dashboard spec) | **NEW.** KPI hierarchy + cross-filter + streaming-freshness UX; clean split from the chart skill. |

### Group 13 — Presentations & Documents — **62/100**  *(baseline "Group 02 Decks" 56, +6)*

The biggest *structural* fix in the engine: the **8 redundant deck skills are consolidated into one
`deck-system`** with the 8 purposes preserved as rich `variant-*.md` examples (208–332L each) — the
baseline's "one template ×8" redundancy is **resolved**. And the group finally **formats real
documents**: new `docx-…` and `pdf-…` skills with worked before/after and exhibit-layout examples.
The remaining defect: `deck-system` still routes the *actual build* to the human (no PPTX
generation), so as a "formatting" group it still partly offloads execution — though the DOCX/PDF
siblings now genuinely produce styled artifacts.

| Skill | Score | Refs | Examples | Notes (Δ) |
|---|---:|---|---|---|
| deck-system | 63 | 3 | Yes (8 variants) | **Consolidates 8 → 1.** Shared deck-craft + 8 worked variant blueprints; resolves the redundancy. Still builds no PPTX (human assembles). |
| docx-report-and-document-formatting | 64 | 3 | Yes (default-vs-designed + style table) | **NEW.** Real named-styles/TOC/embedding discipline + a sharp default-vs-designed before/after. |
| pdf-proposal-and-bankable-document-design | 62 | 3 | Yes (cover + exhibit layout) | **NEW.** Worked cover spec + exhibit page layout; bankable-document framing. |

---

## Group ranking (post-Phase-1, weakest → strongest)

| Group | Score | Δ vs baseline | One-line verdict |
|---|---:|---|---|
| 05 UX Process & Psychology | 58 | +0 | Two new exampled process skills lift the floor; the carried-over `ux-psychology` stub still drags. |
| 06 Sector & Domain UX | 57 | ~−1 | Deep healthcare + two slop-prone "matches this domain" stubs; anti-homogeneity gate still not operationalized. |
| 01 Typography | 60 | +4 | Selection skill now exampled w/ clamp/variable axes; the other three remain thin plumbing. |
| 11 Imagery / Art Direction | 60 | NEW | Authored + exampled; no C2PA — the one surviving 2026 gap. |
| 04 Web & UI | 62 | +2 | Bimodal: 3 strong NEW exampled skills vs ~7 untouched boilerplate-shell legacy skills; `distinctive-by-design` still shows nothing. |
| 08 Motion | 62 | +5 | Springs + View Transitions now present (the two big misses); boilerplate shell header remains. |
| 13 Presentations & Documents | 62 | +6 | 8 decks → 1; now formats real DOCX/PDF; deck still builds no PPTX. |
| 10 Content Design | 63 | NEW | Reasoned before/after rewrites; solid. |
| 07 Mobile | 63 | +14 | Was weakest; Liquid Glass/SF Symbols/haptics/M3 + worked screens. Huge lift. |
| 12 Data-Viz & Dashboards | 64 | ~−1 | Exhaustive data-viz (now exampled) but shell + single-book-spine unaddressed; strong new dashboard skill. |
| 00 Cross-cutting QA/A11y | 65 | NEW | New 2.2-operationalized spine; `design-audit` still a shell. |
| 03 Layout & Composition | 65 | +1 | Worked grid spec + a strong NEW responsive/container-query skill. |
| 09 Design Systems & Tokens | 65 | NEW | Coherent three-tier token backbone + exampled component/handoff skills. |
| 02 Color, Brand & Identity | 68 | +12 | The standout: OKLCH operationalized + worked ramp + APCA/WCAG split + dark remap. |

---

## NEW aggregate engine score — **63/100**  ·  delta vs baseline **58** = **+5**

**Computation.** Skill-count-weighted mean across the 51 scored skills (group counts:
00=6, 01=4, 02=6, 03=2, 04=11, 05=4, 06=3, 07=3, 08=1, 09=3, 10=2, 11=2, 12=2, 13=3) lands at
**~63/100** — out of the "competent/amateur" band and solidly into "**solid but visibly short of
world-class**." The same harsh, no-grade-inflation rubric is applied; the rise is earned, not
assumed.

**Why it rose +5 and not more.** Phase 1 did exactly what it set out to and the gains are real:

- **The examples drought — the baseline's single disqualifying gap — is closed for 34/51 skills**,
  with verified-real worked artifacts (the OKLCH ramp + contrast matrix, the Tallymark landing
  spec, the every-state table, the default-vs-designed DOCX, the iOS screen, the 8 deck variants).
- **2026 standards are operationalized**: OKLCH with a worked ramp, APCA-design/WCAG-certify,
  WCAG 2.2, View Transitions, spring physics, container queries, fluid `clamp()`, variable-font
  axes, Liquid Glass / SF Symbols / haptics / Material 3.
- **The two structural redundancies are gone** (8 decks → 1; the color/brand overlap rationalized),
  and **two whole missing layers were added** (cross-cutting QA/a11y; tokens/theming) plus
  content, imagery, dashboards, and real document formatting.

**Why it is still 63 and not 70+.** Four things hold the line, all consistent with the strict bar:

1. **The legacy skills were not re-authored.** ~10 skills still carry the **auto-generated
   boilerplate shell** ("reusable judgment" Use-When, the "Evidence Produced" table) and **17 have
   no example at all** — almost exactly the pre-Phase-1 set (`interaction-design-patterns`,
   `practical-ui-design`, `form-ux-design`, `premium-ui-ux-design`, `ai-output-design`,
   `webapp-gui-design`, `motion-design`, `data-visualization`, `healthcare-ui-design`,
   `design-audit`, `ux-psychology`, `sector-strategies`, `legal-sector-ui-ux`). A templated shell
   is itself a slop signal in an anti-slop engine; several of these *dropped* a point or two under
   the no-example rule even though their bodies are deep.
2. **`distinctive-by-design` — the soul skill — still ships zero own refs and zero before/after.**
   The engine's flagship still *tells* distinctiveness it never *shows*.
3. **P1/P2 skills are genuinely missing**, and several shipped skills carry **dangling references**
   to them (`trust-credibility-and-social-proof`, `onboarding-and-first-run-design`,
   `ecommerce-and-checkout-ux`), which is a real defect, not just absence.
4. **Residual 2026 gaps**: no **C2PA/provenance**; decks still build **no PPTX**; data-viz still on
   a single-2015-book spine with no scrollytelling/uncertainty; no scroll-driven `animation-timeline`.

**Net.** The doctrine is still the engine's best asset, but the skill layer is no longer "merely
competent" — a real 65–74 tier now exists *with* worked-example justification, and the worst stubs
and redundancies are gone. The fastest remaining route to 70+ is unglamorous: **rewrite the ~10
boilerplate-shell legacy skills and add their missing examples, give `distinctive-by-design` a real
before/after, resolve the dangling P1 references, and add C2PA + PPTX generation.** None of those is
a new-skill task — it is finishing the Phase-1 job on the skills Phase 1 skipped.
