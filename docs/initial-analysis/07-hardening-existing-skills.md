# 07 — Hardening the Existing Skills

**Engine:** `C:\wamp64\www\design-system-skills`
**Inventory hardened here:** the **37 existing** skills across 6 groups (excludes `_TEMPLATE`).
**Companion docs:** `02-coverage-and-taxonomy.md` (the group structure), `04-gap-analysis-new-skills.md` (net-**new** skills). This doc is about making the skills that **already exist** deep enough to drive world-class output; it does not propose new skills.
**Date:** 2026-06-21
**Verdict:** the engine has an outstanding *doctrine* and a handful of genuinely deep skills, but **~17 of 37 skills are thin** — either generic migration-boilerplate (`Use when / Do not use / Workflow / Quality standards`) with the real content parked in a `references/legacy-guidance.md`, or single-file craft skills with **zero worked examples**. Across the whole engine the **2026 standards layer is stale**: WCAG **2.2** named in only 5 files (and never as a numbered-criteria checklist), **INP** in 1, **container queries** in 1, **view transitions / cascade layers** in **0**, OKLCH present but never as a generation algorithm, and the mobile platform skills predate **Liquid Glass** (iOS 26) and **Material 3 Expressive**.

---

## 1. How "hardened" is scored

A world-class (top-studio-bar) skill needs five things. Each existing skill is rated against them:

| Axis | What "world-class" requires |
|---|---|
| **A. Decision spine** | A specific, opinionated workflow with named frameworks, numbers, and a gate — not a generic "read inputs → apply → output" shell. |
| **B. Reference depth** | Companion `references/*.md` holding the spec tables, checklists, and standards the SKILL.md cites — so the SKILL stays short and the depth is loadable on demand. |
| **C. Worked example** | At least one *applied* artifact: a before/after, a real token set, a real type scale, a sample spec, a filled-in audit. This is the single most-missing thing in the engine. |
| **D. 2026 standards** | Current criteria baked in: WCAG **2.2** (by number), Core Web Vitals **2026** (LCP < 2.5s, **INP < 200ms**, CLS < 0.1), OKLCH, container queries, cascade layers, view transitions, fluid `clamp()` type, HIG/Liquid Glass, Material 3 Expressive, variable-font axes. |
| **E. Right size** | Neither a grab-bag that should split, nor a stub that should merge. |

**The engine-wide tells, in one glance:**

| Tell | Where |
|---|---|
| **Migration-boilerplate SKILL** (generic 57-line shell; real content in `references/legacy-guidance.md`) | `brand-alignment`, `brand-style-guide`, `color-selection`, `legal-sector-ui-ux`, `sector-strategies`, `ux-psychology` — and partially `practical-ui-design` |
| **Zero reference files / zero examples** | `font-selection-and-pairing`, `ai-slop-typography-audit`, `premium-font-scan`, `font-embedding-and-licensing`, `distinctive-by-design`, `motion-design`, `brand-visual-identity`, `color-system-and-palette`, `layout-grid-and-spacing`, `visual-product-slop-audit` |
| **No worked example anywhere** | **All 37.** Not one skill ships a filled-in specimen, before/after, or applied token set. |
| **Stale standards** | engine-wide (see §2) |

---

## 2. The 2026 standards gap (cross-cutting — fix once, cite everywhere)

A keyword sweep of every `*.md` under `skills/` (word-boundary, deduped):

| Standard | Files mentioning it | World-class expectation | Verdict |
|---|---|---|---|
| **WCAG 2.2** (by name) | 5 | Named, and present as a **numbered-criteria checklist** | **STALE** — never a checklist |
| WCAG 2.2 §2.5.8 target size (24px) | 2 | In every interactive skill | **MISSING** |
| WCAG 2.2 §2.4.11 focus-not-obscured | 0 | In every interactive skill | **ABSENT** |
| WCAG 2.2 §3.3.7 redundant entry / §3.3.8 accessible auth | 0 | In form/auth skills | **ABSENT** |
| **INP** (Interaction to Next Paint) | 1 | Primary responsiveness metric since 2024 | **STALE** (still FID-era) |
| Core Web Vitals thresholds (LCP/CLS) | ~7 | LCP < 2.5s, INP < 200ms, CLS < 0.1 | partial / no INP |
| **OKLCH** | 8 | A **generation algorithm**, not just a name-drop | present-but-shallow |
| **Container queries** (`@container`) | 1 | A core 2026 responsive primitive | **ABSENT** |
| **CSS cascade layers** (`@layer`) | 0 | Token/override architecture | **ABSENT** |
| **View Transitions API** | 0 | Standard page/element motion | **ABSENT** |
| Fluid type `clamp()` | 2 | Default responsive type method | **THIN** |
| `prefers-reduced-motion` | 13 | (good) | OK |
| **Liquid Glass** (iOS 26) | 1 | The current Apple design language | **ABSENT in iOS skill** |
| **Material 3 / Material You** (dynamic colour) | named, no spec | Tonal-palette generation, dynamic colour | **THIN** |
| Predictive back (Android) | 1 | Standard since Android 14/15 | **THIN** |

**The single highest-leverage move in this whole plan** is to create **two doctrine-level cross-cutting references** and have the interactive skills cite them rather than each re-deriving:

- **`doctrine/references/wcag-2.2-criteria.md`** — every A/AA criterion that bites UI work, *by number*, each with a one-line "what it means here" and a pass test. Must call out the four **new-in-2.2** ones: **2.4.11** focus not obscured, **2.4.13** focus appearance, **2.5.7** dragging movements, **2.5.8** target size ≥ 24px, **3.2.6** consistent help, **3.3.7** redundant entry, **3.3.8** accessible authentication. Plus the carried-over contrast (1.4.3 / 1.4.11), focus-visible (2.4.7), and reflow (1.4.10).
- **`doctrine/references/web-performance-budgets-2026.md`** — Core Web Vitals **2026** (LCP < 2.5s, **INP < 200ms**, CLS < 0.1) with the field-vs-lab distinction, the INP-replaces-FID note, the modern-framework CLS gotchas (font-swap, lazy images without dimensions, injected banners), and a per-output budget table (marketing site vs web-app vs deck-export).

Every web/app/form/audit/mobile skill then gains one bullet: *"Gate against `doctrine/references/wcag-2.2-criteria.md` and `web-performance-budgets-2026.md`."* This is also why the governance gate (`governance/design-quality-gate.md`) should grow an explicit **"Accessibility (WCAG 2.2)"** and **"Performance (CWV 2026)"** block — today it only says "sufficient contrast."

---

## 3. Priority ranking — what to harden first

Scored on **leverage** (how many outputs it touches × how far below the bar it sits × how foundational it is). P0 = harden first; these ten give the biggest jump to world-class.

### P0 — the ten that move the needle most

| # | Skill | Why it's P0 | Headline fix |
|---|---|---|---|
| 1 | **`color-system-and-palette`** | Default colour entry for *every* artifact; excellent prose but **OKLCH is named, never operationalised**, no ramp/role token example, no dark-mode worked remap. | Add an OKLCH ramp-generation algorithm + a **real token set** worked example (light+dark). |
| 2 | **`font-selection-and-pairing`** | Default type entry for *every* artifact; strong workflow but **zero reference of its own and no worked pairing/scale specimen**. | Add 6–8 worked pairings + a real modular scale specimen + variable-font axes. |
| 3 | **`layout-grid-and-spacing`** | Default layout entry; great principles, **no spacing-token table, no grid spec sheet, no container-query / fluid-`clamp()` 2026 layer**. | Add a token/grid reference + a before/after recomposition + container queries. |
| 4 | **`design-audit`** | The engine's flagship QA gate; **WCAG 2.2 named but not by-criterion, CWV not 2026, no container-query dimension, no sample report**. | Wire in the two new cross-cutting refs + ship a **filled-in sample audit**. |
| 5 | **`ios-ui-ux-design`** | Whole platform; **predates Liquid Glass (iOS 26); no HIG-2026 spec table, no worked SwiftUI screen**. | Add `ios-hig-2026.md` + Liquid Glass + a worked screen spec. |
| 6 | **`android-ui-ux-design`** | Whole platform; **Material 3 named without a spec; no Material You dynamic-colour, no predictive-back, no worked Compose screen**. | Add `material3-expressive.md` + dynamic colour + a worked screen spec. |
| 7 | **`data-visualization`** | Deep on Knaflic narrative but **thin on chart-spec tables, encoding standards, accessible/colour-blind palettes, and a real chart redline**. | Add a chart-type spec reference + an accessible-encoding ref + a before/after redline. |
| 8 | **`visual-product-slop-audit`** | A doctrine-critical audit that is **skeletal: 66 lines, 0 references, 0 examples**. | Build its `references/` (tells checklist + remediation) + a before/after. |
| 9 | **`brand-visual-identity`** | Best-written identity skill but **0 references and no worked mini-style-guide specimen** to anchor downstream artifacts. | Add a worked mini-style-guide + logo-system spec reference. |
| 10 | **`motion-design`** | Cross-platform motion; solid but **all inline, no reusable motion-token table, no View Transitions API, no SwiftUI/Compose spring tokens**. | Add a motion-token table + View Transitions + platform spring tokens. |

### P1 — high value, second wave

`practical-ui-design` · `webapp-gui-design` · `form-ux-design` · `interaction-design-patterns` · `healthcare-ui-design` · `color-selection` · `brand-style-guide` · `ai-agent-ux` · `ai-output-design` · the **8 `deck-*` skills** (hardened as a group — see §5).

### P2 — fill out / fix sizing

`ai-slop-typography-audit` · `font-embedding-and-licensing` · `premium-font-scan` · `distinctive-by-design` · `ux-psychology` · `brand-alignment` · `legal-sector-ui-ux` · `sector-strategies` · `enterprise-ux-process`.

---

## 4. Per-skill hardening spec

Conventions: **REF** = reference file to add (path relative to the skill folder); **EX** = worked example to add; **STD** = 2026 standard to inject; **SIZE** = split/merge call.

### Group 01 — Typography & Fonts *(4 skills — all single-file, all 0 refs, all 0 examples)*

This group has the best prose-to-content ratio but is **entirely exemplar-free**. The doctrine `references/` (pairing, type-scale, banned, groups) carry the rules; what's missing is **applied specimens**.

**`font-selection-and-pairing`** *(P0)*
- **REF** `references/worked-pairings.md` — 6–8 named display+body pairings, one per context (editorial-authoritative, developer-technical, startup-product, long-form body, deck, dashboard, civic/healthcare, luxury), each with the contrast rationale, x-height match note, and the OFL baseline + premium upgrade.
- **REF** `references/variable-fonts-and-opentype.md` — variable axes (`wght`, `opsz`, `wdth`, `slnt`, `GRAD`), optical sizing, and which OpenType features to switch on per context (tabular vs old-style numerals, ligatures, stylistic sets). *(Currently the engine treats fonts as static.)*
- **EX** `examples/specimen-developer-technical.md` — a full applied specimen: chosen pair, the modular scale (ratio, every step in px/rem), weights, line-heights, tracking, and a rendered sample paragraph + heading stack.
- **STD** name the variable-font axes and `font-optical-sizing: auto`; reference fluid `clamp()` scale handoff to layout.

**`ai-slop-typography-audit`** *(P2)*
- **REF** `references/audit-findings-rubric.md` — the critical/major/minor scoring table mapped to each banned tell, with the exact remediation per tell.
- **EX** `examples/before-after-audit.md` — a real slop'd CSS `font-family` block + the scored findings list + the deliberate remediation (the doctrine `examples/` may already host a candidate — link or move it).

**`font-embedding-and-licensing`** *(P2)*
- **REF** `references/embedding-cookbook.md` — copy-paste-correct snippets per format: `@font-face` woff2 + `font-display: swap` + variable-font `@font-face` with `font-weight: 100 900`; python-docx/python-pptx embed+subset invocation; PDF generator embed flags; the XLSX "deliver-as-PDF" fallback. *(Today the SKILL describes these in prose only.)*
- **EX** `examples/web-variable-font-embed.md` — a working variable-font `@font-face` + fallback stack + measured file-size delta.

**`premium-font-scan`** *(P2)*
- **REF** `references/manifest-schema.md` — the exact `MANIFEST.md` field schema (family, files, licence, embed-permitted, redistribute-permitted, source) so scans are deterministic. **SIZE:** keep separate — it is correctly scoped.

---

### Group 02 — Document Formatting (8× `deck-*`) *(P1, harden as a SYSTEM)*

All eight are competent narrative-framework skills (Minto, Duarte Sparkline, Klaff STRONG, Hatton) but they share three pain points: **(a) the framework refs are duplicated across folders** (`presentation-frameworks.md` / `pitch-psychology.md` / `storytelling.md` appear in multiple skills); **(b) no PPTX *visual* spec** — no slide-master token system, table/chart styling, or accessibility; **(c) zero worked decks.**

**SIZE — MERGE the shared layer, keep the 8 SKILLs.** Create a shared **`skills/02-document-formatting/_deck-system/`** (a `references/`-style sibling, not a skill) and point all 8 SKILLs at it:

- **REF** `_deck-system/presentation-frameworks.md`, `pitch-psychology.md`, `storytelling.md` — **single canonical copy** of each (de-dupe from the 8 folders).
- **REF** `_deck-system/slide-master-spec.md` — the PPTX visual system the 8 decks all assume but none specify: 16:9 dims, the brand colour **token** set, the type hierarchy (display/headline/body/caption sizes in pt), the **8 master layouts** (title, headline+bullets, data table, card grid 3-up / 2+1 / 2×2, large-number hero, 3-phase timeline, two-column before/after), safe margins, and the baseline grid.
- **REF** `_deck-system/metrics-visualisation-spec.md` — table styling (header row, alternating shade, padding, number alignment/format), the chart kit (trend line, platform bar, composition stacked bar, slope/before-after, waterfall budget) with axis/label/gridline rules, and **colour-blind-safe** + non-colour-redundant traffic-light encoding (the red/amber/green pattern fails ~8% of users today).
- **REF** `_deck-system/deck-accessibility.md` — slide contrast (esp. text on dark/photo fills), chart alt-text, reading order, min on-screen type size.
- **EX** `_deck-system/worked-examples/quarterly-review-anonymised.md` — one **fully built, anonymised** deck (a Kampala SME) showing the SCR/Minto spine, the applied master layouts, and a redline of three common mistakes.
- **STD** add a PPTX font **embed+subset** step (cross-ref `font-embedding-and-licensing`) and the colour-blind-safe palette to every deck.

Per-deck SKILL edits stay light: each keeps its narrative spine and a "sector framing" note (healthcare ethics, ecommerce AOV/conversion, NGO impact) and cites `_deck-system` for everything visual.

---

### Group 03 — Web & UI Design *(16 skills — the most uneven group)*

**Foundational craft**

**`design-audit`** *(P0)*
- **REF** `references/wcag-2.2-modern-criteria.md` — the audit checklist for **2.4.11, 2.4.13, 2.5.7, 2.5.8, 3.2.6, 3.3.7, 3.3.8** plus 1.4.3/1.4.11/2.4.7/1.4.10 (or cite the new doctrine ref from §2).
- **REF** `references/core-web-vitals-2026.md` — INP-replaces-FID, the three 2026 thresholds, modern-framework CLS patterns (or cite the doctrine ref).
- Add a **container-query** check to the layout dimension and **agentic-UI slop tells** (no tool transparency, hidden cost, missing approval state) to the AI-slop dimension.
- **EX** `examples/sample-audit-report.md` — a filled-in audit of a real-ish product: scored findings across all 10 dimensions, severity matrix populated, remediations.

**`practical-ui-design`** *(P1)* — content is largely in `references/skill-deep-dive.md`; promote it.
- **REF** `references/fluid-typography-clamp.md` (modular fluid scale via `clamp()` across breakpoints), `references/oklch-palette-generation.md` (the interpolation algorithm), `references/contrast-checklist.md` (WCAG 2.2 AA + APCA note).
- **EX** it already has a Major-Third scale + 8pt token table inline — **extract to** `examples/token-set.md` and make it a complete, copy-paste design-token file (colour roles, spacing, type, radius, shadow) in CSS custom properties **on `@layer`**.
- **SIZE — MERGE candidate** with `premium-ui-ux-design` (both own colour+type+spacing fundamentals; premium becomes the refinement/gate layer).

**`distinctive-by-design`** *(P2)* — strong discipline, **0 refs, 0 examples**.
- **REF** `references/distinctive-moves-catalogue.md` — the menu of *one strong idea* moves (signature type treatment, broken-grid hero, single ownable colour, custom motif, art-directed imagery) each with a do/don't.
- **EX** `examples/before-after-distinctive.md` — a templated hero → the same hero after one committed distinctive decision.

**`webapp-gui-design`** *(P1)* — already deep (React/Next + PHP/Tabler).
- **REF** `references/server-components-and-streaming.md` (RSC, Suspense boundaries, streaming for INP/LCP), `references/container-queries-responsive-components.md` (`@container` over media queries for components).
- **STD** INP-first interaction budget; cite the two doctrine refs.

**`interaction-design-patterns`** *(P1)* — deep (Tidwell, 6 section files).
- **REF** `references/wcag-2.2-pattern-gates.md` mapping each pattern family to the criteria it must satisfy (target size on actions, focus-not-obscured on overlays/sticky bars, dragging-alternative on reorder).
- **STD** viewport `viewport-fit=cover` + `env(safe-area-inset-*)` note for full-bleed patterns.

**`premium-ui-ux-design`** *(P1)* — deep refs already.
- **REF** `references/ios-liquid-glass-2026.md`, `references/material-you-dynamic-color.md`, `references/accessibility-gate-checklist.md` (tie the premium 0–10 gate to WCAG 2.2 by number).
- **SIZE:** see merge note under `practical-ui-design`.

**`motion-design`** *(P0)* — solid but all inline, no reusable tokens.
- **REF** `references/motion-token-table.md` — canonical duration×easing pairs (100/200/300/500ms × the named cubic-beziers) as reusable tokens for Web/iOS/Android; `references/view-transitions-api.md` (cross-document + same-document VT); `references/platform-spring-tokens.md` (SwiftUI `.spring` and Compose `spring` stiffness/damping values).
- **EX** `examples/motion-tokens.css` — the table rendered as CSS custom properties + a `prefers-reduced-motion` block.
- **SIZE:** optionally split the platform sections into `references/motion-{web,ios,android}.md`; keep one SKILL.

**Process / psychology**

**`enterprise-ux-process`** *(P2)* — deep (18 files, Synechron maturity model).
- **REF** `references/regulatory-compliance-by-sector.md` — phase-4/9 audit gates for HIPAA, GDPR, PCI-DSS, legal-privilege (cross-cite healthcare/legal skills rather than re-derive).
- **STD** Phase-9 accessibility scope = WCAG 2.2 AA test plan (cite doctrine ref).

**`ux-psychology`** *(P2)* — real content sits in a 547-line `references/legacy-guidance.md`.
- **SIZE — SPLIT the legacy file** into loadable units: `references/gestalt.md`, `nielsen-heuristics.md`, `norman-levels.md`, `cognitive-load.md`, `affordance-4-stage.md`. The SKILL.md is otherwise generic boilerplate — rewrite its Workflow to actually route to these.
- **EX** `examples/affordance-applied.md` — the 4-stage affordance discipline applied to one real form + one chat/agent approval flow.

**AI-native UX**

**`ai-agent-ux`** *(P1)* — good nested refs (agentic-ui, ux-patterns).
- **REF** `references/tool-call-transparency.md` (which tool ran, why it failed, latency/cost metadata, audit trail), `references/streaming-errors-recovery.md` (mid-stream failure, interrupt, retry), `references/agent-cost-and-quota-ui.md`.
- **STD** WCAG 2.2 **2.5.8** target size + **2.4.11** focus-not-obscured on approval/permission buttons.

**`ai-output-design`** *(P1)* — deep five-principles skill.
- **REF** `references/error-recovery-patterns.md` (failed generation, partial-output preservation, state rollback, offline/sync-loss), `references/source-freshness.md` (staleness indicators for web-grounded output).
- **STD** target size + focus-visible on inline-refinement controls and citation superscripts.

**Audits**

**`visual-product-slop-audit`** *(P0 — most under-built skill in the engine)*
- **REF** `references/visual-tells-checklist.md` (each generative tell — waxy skin, melted bg, gibberish text, extra fingers, warped/fused logo glyphs, uncanny faces, impossible lighting — with a diagnostic test), `references/product-interface-tells.md` (AI-hammer feature cramming, ungrounded chatbot, decorative-AI gradient/badge), `references/remediation-workflows.md` (retouch vs reshoot vs real-photography decision tree).
- **EX** `examples/before-after-slop.md` — a slop'd hero image + key-art remade, annotated.

**Verticals**

**`healthcare-ui-design`** *(P1)* — deep (16 refs, HIPAA-aware).
- **REF** `references/wcag-2.2-clinical-criteria.md` (2.4.11 on alert banners, 2.5.8 for tremor/geriatric users), `references/error-tolerance-life-critical.md` (dual-verify, wrong-patient prevention, medication-order undo/rollback), `references/alarm-fatigue-audit.md` (alerts-per-screen budget, non-colour cues), `references/fda-21cfr11-esignature-ui.md`.
- **SIZE:** merge the overlapping `clinical-workflows-ui.md` + `dashboards-analytics-ui.md`.

**`legal-sector-ui-ux`** *(P2)* — boilerplate SKILL; real content in 3 refs + `legacy-guidance.md`. The description promises e-discovery/privilege but the refs don't deliver it.
- **REF** `references/privilege-and-discovery-ui.md` (document markup, redaction, attorney-work-product labeling, secure attorney-client comms indicators, conflict-of-interest disclosure).
- **EX** `examples/law-firm-page-audit.md` — an intake/profile page scored against the bar-ethics constraints.
- **SIZE:** **EXPAND** (currently ~57-line SKILL) to parity with healthcare, *or* fold into `sector-strategies/templates/legal/`. Recommend expand — it is a credibility-critical vertical.

**`sector-strategies`** *(P2)* — 87 files, but the SKILL is generic boilerplate and several templates are stubs (`README` marks healthcare/ecommerce/education/professional-services 🚧).
- **Action:** complete the stub templates; add per-sector `wcag-2.2-checklist.md` + `core-web-vitals-targets.md`.
- **EX** `templates/_worked-example/` — one sector built end-to-end (HTML/CSS + a performance + a11y result).
- **SIZE:** point the healthcare and legal sector templates at the deep `healthcare-ui-design` / `legal-sector-ui-ux` skills (authority) instead of duplicating.

---

### Group 04 — Colour & Visual Identity *(5 skills — split between deep and boilerplate)*

**`color-system-and-palette`** *(P0 — top of the whole list)* — excellent prose; **OKLCH named but no algorithm, 0 refs, 0 token example**.
- **REF** `references/oklch-ramp-algorithm.md` — the concrete recipe: pick anchor → set L steps (perceptual) → hold/rotate H → chroma curve to avoid muddy mids / chalky tints → the 50–900 output; plus the dark-mode remap rules (lower chroma, lift+desaturate accents, re-gate contrast).
- **REF** `references/semantic-role-map.md` — the canonical role set (surface/raised/sunken, text/muted, border, accent, success/warning/error/info) as **token names**.
- **EX** `examples/token-set-light-dark.md` — a **real** anchored palette → full OKLCH ramp → role map → recorded WCAG results for **both** modes, as copy-paste CSS custom properties.
- **STD** OKLCH as the working space; CWV-irrelevant but cite the WCAG 2.2 contrast ref.

**`color-selection`** *(P1)* — boilerplate SKILL but a good Flux section + `scripts/palette_generator.py` + `references/flux-process.md`.
- **EX** `examples/flux-worked-palette.md` — promote the in-prose "girl with balloons → purple duotone" walkthrough into a standalone before/after with the actual hexes and the 60/30/10 application.
- **SIZE:** keep distinct from `color-system-and-palette` (generation vs system) — the SKILL already argues this well; just de-boilerplate the Workflow.

**`brand-visual-identity`** *(P0)* — best-authored identity skill, **but 0 refs and 0 worked specimen**.
- **REF** `references/logo-system-spec.md` (lockups, clear-space in mark-units, min-size, mono/dark variants, misuse) and `references/identity-consistency-gate.md` (promote the inline gate).
- **EX** `examples/mini-style-guide.md` — a complete worked mini-style-guide for one invented brand (essence + not-confused-with + logo system + signature colour + type roles + photography rules + voice paragraph) — the specimen downstream artifacts copy.

**`brand-style-guide`** *(P1)* — boilerplate SKILL; content in `references/legacy-guidance.md` + `style-guide-template.md`.
- **Action:** rewrite the generic Workflow to actually drive the `style-guide-template.md`; the template is the asset.
- **EX** `examples/filled-style-guide.md` — the template populated for one brand (ties to the `brand-visual-identity` specimen).

**`brand-alignment`** *(P2)* — generic boilerplate; real content in `references/legacy-guidance.md` + a `trust-architecture-checklist.md`.
- **Action:** rewrite Workflow to be a concrete element-by-element alignment audit (layout/messaging/nav/imagery/CTA vs the recorded brand system); cite `brand-style-guide` as the source of truth it validates against.

---

### Group 05 — Layout, Grid & Data-viz *(2 skills)*

**`layout-grid-and-spacing`** *(P0)* — strong Swiss-school principles; **0 refs, 0 token table, no 2026 layout layer**.
- **REF** `references/spacing-and-grid-tokens.md` — the 4/8pt scale as named tokens, container max-widths, gutter/margin sets per breakpoint, and the baseline-grid rule.
- **REF** `references/modern-css-layout-2026.md` — **container queries** (`@container` for component-level responsiveness), fluid `clamp()` spacing, CSS subgrid, and `@layer` for token/override order. *(This is the engine's main container-query/cascade-layer home — currently absent.)*
- **EX** `examples/before-after-recompose.md` — a uniform-card-grid slop layout recomposed with a focal point, intentional asymmetry, and uneven whitespace, shown with the spacing tokens.

**`data-visualization`** *(P0)* — deep on Knaflic narrative (503 lines) but **thin on hard chart specs and accessibility**.
- **REF** `references/chart-type-spec.md` — per chart type (line/bar/stacked/slope/scatter/area/small-multiple): when to use, axis/label/gridline/data-ink rules, number formatting, annotation pattern.
- **REF** `references/accessible-data-encoding.md` — colour-blind-safe categorical/sequential/diverging palettes (OKLCH-derived), non-colour redundancy (label/shape/pattern), chart alt-text and table-fallback, min text size.
- **EX** `examples/spaghetti-to-story.md` — a real "too many lines" chart redlined into a single highlighted-series explanatory chart, with the before/after image-or-SVG and the decluttering moves named.

---

### Group 06 — Mobile UI/UX *(2 skills — both thin platform stubs)*

**`ios-ui-ux-design`** *(P0)* — references SwiftUI/UIKit but **predates Liquid Glass (iOS 26); no HIG-2026 spec; no worked screen**.
- **REF** `references/ios-hig-2026.md` — current HIG: 44pt targets, safe-area/Dynamic-Island handling, SF Symbols usage, Dynamic Type ramp, **Live Activities**, lock-screen widgets, and the **Liquid Glass** material (translucency, vibrancy, blur, where it is and isn't appropriate).
- **REF** `references/swiftui-variable-fonts.md` (custom + variable font loading, optical sizing) and `references/ios-dark-mode.md`.
- **EX** `examples/worked-screen-spec.md` — one full screen (e.g. a settings or dashboard) specced: layout, every state (loading/content/empty/error/offline/permission-denied), Dynamic Type behaviour, VoiceOver order, target sizes.

**`android-ui-ux-design`** *(P0)* — Material 3 named without a spec.
- **REF** `references/material3-expressive.md` — Material 3 / **Material You**: dynamic colour from wallpaper, **tonal-palette generation**, expressive components, 48dp targets, edge-to-edge + `WindowInsets`, **predictive back** (`BackEventCompat` progress animation), adaptive nav (bottom-bar → rail → drawer by `WindowSizeClass`).
- **REF** `references/compose-state-and-animation.md` (StateFlow/`collectAsStateWithLifecycle`, `animate*AsState`, spring stiffness/damping tokens) and `references/android-dark-mode.md`.
- **EX** `examples/worked-screen-spec.md` — the parallel of the iOS worked screen, in Compose terms.

**SIZE (both):** keep as two platform skills, but cite the shared `motion-design` motion-token table and the doctrine WCAG ref so the platforms stay in sync.

---

## 5. Cross-cutting moves (do these once; they harden many skills at once)

1. **Create the two standards refs** (`doctrine/references/wcag-2.2-criteria.md`, `web-performance-budgets-2026.md`) and the **colour-blind-safe palette** ref — then cite from every interactive + data-viz + deck skill. *Highest leverage in the plan.*
2. **Grow `governance/design-quality-gate.md`** with explicit **WCAG 2.2** (by-criterion) and **CWV 2026** blocks; today it only says "sufficient contrast" and "consistent spacing."
3. **Establish a worked-examples convention.** Every skill gets an `examples/` folder; the `_TEMPLATE` should include an empty `examples/` and an "EX" prompt so the no-examples problem doesn't recur. **Not one of the 37 skills currently ships an applied specimen — this is the biggest single quality gap.**
4. **De-boilerplate the 7 migration-shell SKILLs** (`brand-alignment`, `brand-style-guide`, `color-selection`, `legal-sector-ui-ux`, `sector-strategies`, `ux-psychology`, partially `practical-ui-design`): replace the generic `Workflow/Quality standards` shell with a real decision spine that routes to the content already sitting in their `references/legacy-guidance.md`.
5. **De-duplicate the deck framework refs** into `02-document-formatting/_deck-system/` (§4).
6. **Add the modern-CSS layer once** (container queries, cascade layers, view transitions, fluid `clamp()`) in `layout-grid-and-spacing`, `motion-design`, `webapp-gui-design`, `practical-ui-design` — these four currently carry the web-platform weight and all four lack it.

---

## 6. Split / merge summary

| Action | Skill(s) | Rationale |
|---|---|---|
| **MERGE (shared layer)** | 8× `deck-*` → `_deck-system/` | De-dupe frameworks; add the missing PPTX visual + a11y spec once. |
| **MERGE (candidate)** | `practical-ui-design` + `premium-ui-ux-design` | Both own colour/type/spacing fundamentals; premium = refinement/gate layer. |
| **MERGE (sub-files)** | healthcare `clinical-workflows-ui` + `dashboards-analytics-ui` | Overlap. |
| **SPLIT (refs)** | `ux-psychology` legacy-guidance → 5 loadable files | 547-line monolith. |
| **SPLIT (optional)** | `motion-design` → `motion-{web,ios,android}.md` | Platform sections; keep one SKILL. |
| **EXPAND** | `visual-product-slop-audit`, `legal-sector-ui-ux` | Both far below their stated scope. |
| **COMPLETE** | `sector-strategies` stub templates | 🚧 healthcare/ecommerce/education/professional-services. |
| **KEEP AS-IS (size)** | all of group 01, `color-selection` vs `color-system-and-palette`, the two mobile skills | Correctly scoped; harden in place. |

---

## 7. Build order (one line)

**P0 (10):** the two doctrine standards refs → `color-system-and-palette` → `font-selection-and-pairing` → `layout-grid-and-spacing` → `design-audit` → `ios`/`android` → `data-visualization` → `visual-product-slop-audit` → `brand-visual-identity` → `motion-design`. **Then P1** (deck-system + the deep 03 skills + colour/brand boilerplate). **Then P2** (typography exemplars, process/psychology splits, vertical expansions). Every step ships **at least one worked example** — that single rule, applied across all 37, is what lifts the engine from "well-reasoned" to "world-class."
