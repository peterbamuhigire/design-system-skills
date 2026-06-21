# 05 — Per-Output-Type Readiness Audit

**Engine:** `C:\wamp64\www\design-system-skills`
**Doctrine reviewed:** `doctrine/design-doctrine.md` (v0.1.0) + 8 reference files
**Inventory reviewed:** 37 skills across groups 01–06, plus their `references/`, `sections/`, and `templates/` payloads
**Date:** 2026-06-21
**Question:** Given ONLY this engine's current skills + doctrine, could it guide an agent to produce work that rivals top global studios (Apple / Pentagram / award winners) — per output type?

**Scoring bar (ruthless):** 90–100 rivals Apple/Pentagram/award winners · 75–89 excellent pro · 60–74 solid but visibly short · 40–59 competent/amateur · <40 skeletal. Default band 45–65. A 70+ requires extraordinary justification.

---

## How to read this audit

The engine's **horizontal foundations are genuinely strong**: typography (selection, pairing, scale, embedding, licensing, slop policing), colour (`color-system-and-palette` — Albers/Itten/OKLCH, WCAG hard gate, deliberate dark-mode remap), layout (`layout-grid-and-spacing` — Müller-Brockmann/Tschichold/Vignelli/Lupton, optical alignment), the anti-slop charter, and the `distinctive-by-design` pre-flight. These lift the *floor* of every output type above the AI mean.

What repeatedly caps the *ceiling* is the same recurring shortfall: **the engine teaches design judgement and governance, not production-systems craft or platform-frontier execution.** It states choices, audits slop, and gates quality — but it rarely carries an output type all the way to the bleeding edge (Apple-award motion/haptics, Material 3 Expressive, design-token infrastructure, DOCX/PDF rendering mechanics, logo *generation*). That gap is what keeps almost everything in the 55–70 band.

---

## 1. Marketing website / landing page — **66 / 100**

**What carries it:** This is one of the engine's best-served types. `distinctive-by-design` forces one committed idea and kills the convergent hero; `layout-grid-and-spacing` supplies real asymmetry/focal-point discipline; `color-system-and-palette` and `font-selection-and-pairing` give an authored type+colour system; `sector-strategies` adds 10 vertical template packs (each with `design-tokens.md`, `component-patterns.md`, branding + conversion files) plus an explicit `ANTI-HOMOGENEITY-PRINCIPLE.md`; `ux-psychology`, `motion-design`, and `visual-product-slop-audit` round it out. A landing page built through this stack would look authored, not templated.

**Biggest gaps:**
- **No conversion-rate / CRO craft as a discipline** — hero message testing, social-proof architecture, offer framing, scroll choreography, and form-conversion are only touched obliquely (sector `*-conversion.md` files), not owned by a real skill.
- **No editorial/marketing *layout* skill** — `webapp-gui-design` explicitly defers marketing pages elsewhere, but there is no dedicated long-scroll narrative-page skill (storytelling sections, scrollytelling, full-bleed art direction).
- **Imagery/art-direction is reactive, not generative** — the slop audit rejects bad imagery but nothing teaches commissioning/art-directing a photographic or illustration system for a hero.

**To reach world-class:** a HARDENED `landing-page-art-direction` skill (scroll narrative, hero art direction, CRO patterns), and a real `conversion-design` skill. With those it could plausibly reach the low 80s.

---

## 2. Web application (SaaS dashboard / product UI) — **70 / 100**

**What carries it:** The single most complete vertical. `webapp-gui-design` is substantial (app shell, TanStack tables, RHF+Zod forms, modal/drawer, loading/error/empty states, dark mode, uploads, multi-tenant, a real a11y sweep, plus a 10-file PHP/Tabler section pack). It is reinforced by `interaction-design-patterns` (Tidwell, 45+ patterns), `practical-ui-design` (HSB/OKLCH colour, type scale, button/form rules), `premium-ui-ux-design` (gate + SRS spec mode), `form-ux-design`, `ai-agent-ux`, `enterprise-ux-process`, `design-audit`, and `data-visualization` for dashboards.

**Biggest gaps:**
- **No design-token / component-system infrastructure** — tokens are *named as a deliverable* in `production-quality-handoff` but no skill teaches token taxonomy, naming, state matrices, or a component-spec standard. World-class SaaS ships a real system, not screens.
- **Exploratory/interactive dashboards** — `data-visualization` is textbook-strong on *explanatory* static charts but silent on brushing, filtering, drill-down, cross-filter, real-time/streaming, and dashboard composition/topology.
- **Frontier interaction polish** — command palettes, optimistic-everything, multiplayer/presence, keyboard-first power-user surfaces are not addressed at Linear/Vercel level.

**To reach world-class:** the missing `design-tokens-and-systems` skill + an interactive-dashboard hardening. The 70 is justified by genuine breadth, but the token/system gap is what blocks the 80s.

---

## 3. iOS app (SwiftUI, HIG-compliant, Apple Design Award bar) — **57 / 100**

**What carries it:** `ios-ui-ux-design` plus four substantial reference files (`swiftui-design`, `swiftui-pro-patterns`, `ios-uikit-advanced`, `advanced-interactions` — ~1,400 lines total) show modern, correct API usage (NavigationStack, `@Observable`, `ContentUnavailableView`, compositional layout, diffable data sources, touch coalescing/prediction, UIKit Dynamics, iPad multitasking). The state-matrix discipline and the SF Pro platform-font caveat are handled well. This is a solid, ship-a-good-product reference.

**Biggest gaps (vs the award bar):**
- **No haptics system, no SF Symbols animation** — both are table-stakes for award winners and appear nowhere. Haptics is the "invisible UI" every winning app layers in.
- **No Live Activities / Dynamic Island / Lock-Screen widgets** — these are now surface-zero on iOS and are entirely absent.
- **Motion is mechanical, not art-directed** — the docs cover the Animatable protocol but not gesture-driven, momentum-aware fluid transitions, spring tuning for a luxury feel, or iOS 26/Liquid-Glass direction. No App Store screenshot craft.

**To reach world-class:** an iOS `sensory-and-motion` hardening (haptic design system, SF Symbols animation, gesture momentum), plus a Live-Activities/widgets skill. Production-grade today (~60); ~30 against the award bar.

---

## 4. Android app (Material 3 Expressive bar) — **58 / 100**

**What carries it:** `android-ui-ux-design` plus eight reference files (`design-philosophy`, `animation-and-polish`, `composable-patterns`, `data-tables`, `layout-and-components`, `navigation-and-performance`, `responsive-adaptive`, `skill-deep-dive` — ~3,200 lines). Navigation architecture, `WindowSizeClass` adaptivity, performance (stability, `remember`, `derivedStateOf`, lazy lists, Coil), dense business-report table patterns, and the Roboto-as-system-only caveat are all professional-grade.

**Biggest gaps (vs the Expressive bar):**
- **Pre-dates Material 3 Expressive (2024–25)** — no expressive motion timing, no morphing/shape transitions, no dynamic-color-in-motion choreography. The animation guidance is 2–3 years behind the current bar.
- **No Predictive Back** — Material 3's flagship navigation gesture (Android 13+) is absent end to end.
- **No foldable/large-screen playbook, no edge-to-edge immersive guidance, no haptics** — adaptivity stops at `WindowSizeClass`; hinge/continuity and immersive surfaces are unaddressed.

**To reach world-class:** a Material-3-Expressive hardening (expressive motion + shapes + dynamic color), a Predictive-Back + edge-to-edge skill, and a foldable playbook. Production-grade today (~65); ~35 against the Expressive bar.

---

## 5. Cross-platform mobile (RN / Flutter) — **22 / 100**

**What carries it:** Almost nothing in-engine. The mobile group is two native stubs (iOS/Android). React Native appears only as a former sibling reference; Flutter is absent entirely. Motion timing and interaction patterns are platform-portable in principle, and the foundations (type/colour/layout) apply.

**Biggest gaps:**
- **No React Native skill, no Flutter skill** — no Expo, navigation, native-module, offline-sync, or platform-divergence guidance; no widget/render-model coverage (Flutter's Skia/Impeller, RN's bridge/Fabric).
- **No cross-platform design strategy** — when to share vs. diverge per platform, how to honour both HIG and Material from one codebase, adaptive components.
- **No parity/QA discipline** for "feels native on both."

**To reach world-class:** dedicated `react-native-design` and `flutter-design` skills plus a cross-platform-parity skill. This is the engine's weakest output type — effectively skeletal.

---

## 6. Business / consulting document (report, BRD/SRS) as DOCX/PDF — **30 / 100**

**What carries it:** The foundations help a document *look* considered — type pairing, colour, the `layout-grid-and-spacing` note on document grids and baseline rhythm, `data-visualization` for exhibits, and `font-embedding-and-licensing` covering DOCX/PDF embed+subset mechanics. `premium-ui-ux-design` has an SRS spec-mode for *requirements* writing.

**Biggest gaps:**
- **No DOCX/PDF document-formatting skill exists at all.** Group 02 ("document-formatting") is mislabelled — it contains *only* 8 PPTX deck skills. There is zero coverage of multi-page document structure: master/left-right pages, running headers/footers, ToC, footnotes/endnotes, cross-references, appendices, multi-page table continuation, print margins/bleed, or body-text leading for print.
- **No long-form information architecture for documents** (as opposed to slides) — section systems, numbering, figure/table captioning, callout/pull-quote systems.
- **No rendering pipeline** — nothing on producing the actual `.docx`/`.pdf` to a professional standard (the engine assumes hand-off).

**To reach world-class:** a real `business-document-formatting` skill (DOCX/PDF structure + print typography) and a `long-form-report-architecture` skill. McKinsey-grade *written* deliverables are currently unreachable from this engine. This is the most consequential single gap.

---

## 7. Proposal / pitch (deck + document) — **62 / 100**

**What carries it:** The deck half is strong. Eight `deck-*` skills (initial-pitch, strategy, ai-strategy, campaign-proposal, credentials, monthly/quarterly/annual review) apply serious persuasion science — Minto's Pyramid, Duarte's Big Idea/Sparkline, Klaff STRONG, Sant NOSE, Hatton — with per-slide visual-direction discipline, action titles, RAG status systems, bookended cover/closing design, and Group-3 type pairing. `data-visualization` supplies the exhibits.

**Biggest gaps:**
- **The "document" half of "deck + document" is missing** — the same DOCX/PDF gap as type 6. A pitch *document* / leave-behind / signed proposal in Word/PDF has no formatting skill.
- **No PPTX rendering mechanics** — the deck skills are markdown content+narrative blueprints that all end in "paste into PowerPoint/Canva/Google Slides." Nothing produces a polished `.pptx` (masters, layouts, real chart objects, speaker-notes export). Award-grade decks live or die on execution craft the engine hands off.
- **Data-viz-in-deck depth** — chart-type-for-data-relationship and projection legibility are only lightly covered inside the deck skills.

**To reach world-class:** a `pptx-production` skill (masters/layouts/chart objects) and the shared `business-document-formatting` skill for the document leg. The content/persuasion layer is already excellent (low-80s on narrative alone); execution and the document leg drag the blended score to 62.

---

## 8. Brand / visual identity system — **58 / 100**

**What carries it:** `brand-visual-identity` is well-grounded (Paul Rand, Vignelli, Neumeier): essence + adjective set + "not-to-be-confused-with" anchor, logo *usage* (lockups, clear-space, min size, mono/dark), photography/illustration/iconography rules, voice-of-the-visuals, and a Consistency Gate with a memory test. `brand-style-guide` produces a client deliverable; `color-system-and-palette` and `font-selection-and-pairing` supply rigorous colour and type; `brand-alignment` handles fit.

**Biggest gaps:**
- **Logo *generation* is deferred entirely** — the skill gate-keeps and specifies an existing/commissioned mark but never teaches designing one (mark geometry, wordmark type selection, simplification discipline). Pentagram-level work is fundamentally about *making* the mark.
- **No identity *architecture*** — parent/sub-brand/endorsed relationships, brand systems across a portfolio, naming systems.
- **No extended applications** — environmental/signage, motion-identity rules, foil/embroidery/die-cut specs, and no Figma asset-library/export management for the identity.

**To reach world-class:** harden `brand-visual-identity` with logo-design craft + identity architecture + extended applications, and add a brand-asset/Figma-management skill. Strong on governance and application; short on generation and ecosystem — capped in the high 50s.

---

## 9. Data product / dashboards / data-viz — **64 / 100**

**What carries it:** `data-visualization` is the engine's deepest single discipline — the full Knaflic framework (context-first, chart-selection decision tree, the 6-move declutter, preattentive attributes, gestalt, narrative), a 20-item model checklist, an anti-pattern table (no pie/donut/3D/secondary-axis), grey-base+one-accent colour with colourblind safety, plus `responsive-mobile-charts`, `analytics-dashboard-decision-story`, and `svg-css-js-implementation` references. Genuinely textbook-grade for *explanatory* data storytelling.

**Biggest gaps:**
- **Explanatory only — no exploratory/interactive** — brushing, filtering, drill-down, cross-filter, dynamic queries, and real-time/streaming are absent. A "data product" is usually interactive.
- **No dashboard composition/topology** — KPI-card systems, chart nesting, multi-chart grouping, and the dashboard grid are deferred to `layout-grid-and-spacing` and fall between the two skills.
- **Thin perceptual science + no geospatial / advanced time-series** — Weber's law, deeper pre-attentive timing, choropleth/flow maps, forecast confidence bands, and anomaly framing are not covered.

**To reach world-class:** an `interactive-dashboards` skill (exploration + composition) and a `geospatial-and-timeseries` extension. The static-storytelling core alone is low-80s; the interactive/topology gaps pull the data-*product* score to 64.

---

## 10. Design deliverable / handoff (tokens, specs, Figma-to-dev) — **34 / 100**

**What carries it:** `production-quality-handoff` (under `premium-ui-ux-design`) names the deliverables — token table, component inventory, state matrix, asset manifest, responsive + a11y notes — and `premium-ui-ux-specification-rules` turns premium UI into testable SRS requirements. Sector templates ship example `design-tokens.md` files showing token *shape*. The `webapp-gui-design` primitives register is a partial component inventory.

**Biggest gaps:**
- **No design-token skill as a craft** — tokens exist as a *deliverable mention*, never as a taught practice: no taxonomy/naming conventions, no tiering (primitive→semantic→component), no JSON/YAML export, no Style Dictionary / Tokens Studio / Supernova guidance, no versioning/deprecation.
- **Figma-to-dev handoff is entirely absent** — no spec format/traceability, no Figma library structure, no design→code export pipeline, no CI/CD token publishing.
- **No component-specification standard** — "component inventory" is named but there is no format for state matrices, prop definitions, usage rules, or per-component a11y specs; sector templates show flat CSS classes with no taxonomy guidance.

**To reach world-class:** dedicated `design-tokens-and-systems` and `figma-to-dev-handoff` skills plus a component-spec standard. This is the single largest systemic gap in the engine and the lowest non-cross-platform score.

---

## Readiness ranking

| Rank | Output type | Score | One-line ceiling-limiter |
|---|---|---:|---|
| 1 | Web application (SaaS / dashboard UI) | **70** | No design-token/component-system infrastructure; static-only dashboards |
| 2 | Marketing website / landing page | **66** | No CRO/art-direction skill; imagery is reactive not generative |
| 3 | Data product / dashboards / data-viz | **64** | Explanatory only — no interactive/exploratory or dashboard topology |
| 4 | Proposal / pitch (deck + document) | **62** | No PPTX rendering mechanics; the document leg is unsupported |
| 5 | Android app (Material 3 Expressive) | **58** | Pre-dates Expressive; no Predictive Back / foldables / haptics |
| 5 | Brand / visual identity system | **58** | Logo *generation* and identity architecture both deferred |
| 7 | iOS app (Apple Design Award bar) | **57** | No haptics / SF Symbols animation / Live Activities; motion not art-directed |
| 8 | Design deliverable / handoff (tokens, Figma-to-dev) | **34** | Tokens named as deliverable, never taught; Figma handoff absent |
| 9 | Business/consulting doc (DOCX/PDF) | **30** | No DOCX/PDF formatting skill exists at all (group 02 is decks-only) |
| 10 | Cross-platform mobile (RN / Flutter) | **22** | No React Native or Flutter skill; effectively skeletal |

**Weakest output type:** Cross-platform mobile (RN/Flutter) at **22/100** — no skill exists. The two most *consequential* gaps for the engine's stated business (premium client deliverables) are the DOCX/PDF business-document gap (**30**) and the design-token/handoff gap (**34**).

---

## Overall output readiness — **52 / 100**

Computed as the mean of the ten types (≈52), and consistent with the band: the engine is **competent-to-solid across most digital UI/visual output, with a strong horizontal foundation, but it is not yet world-class for any single output type** — nothing clears 75. Three structural shortfalls explain the ceiling everywhere:

1. **No production-systems layer** — design tokens, component specs, and Figma-to-dev handoff are named but not taught. This caps web-app, brand, and (definitionally) the handoff type.
2. **No document/render execution layer** — DOCX/PDF formatting is absent and the decks/PPTX stop at markdown hand-off. This caps the document and pitch types.
3. **Platform-frontier mobile is behind** — iOS lacks haptics/SF-Symbols-animation/Live-Activities; Android pre-dates Material 3 Expressive and Predictive Back; cross-platform is empty.

**Highest-leverage additions to lift the whole engine:** (a) `design-tokens-and-systems` + `figma-to-dev-handoff`; (b) `business-document-formatting` (DOCX/PDF) + `pptx-production`; (c) iOS sensory/motion + Android Material-3-Expressive hardenings, and `react-native-design` / `flutter-design`. These four moves would raise the weakest five types out of the amateur band and push the leaders (web app, landing page) into the excellent-pro 80s.

> **Caveat on method:** scores assess what an agent could produce *guided only by this engine's current skills + doctrine*, against the named world-class bar. They are not a judgement of the foundations' quality (which are high), but of *end-to-end readiness per output type*.
