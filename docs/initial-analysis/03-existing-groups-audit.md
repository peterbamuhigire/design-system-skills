# Existing Groups Audit — Design-System-Skills Engine

**Date:** 2026-06-21
**Auditor scope:** All 37 `SKILL.md` files across 6 groups, their `references/` subtrees, the doctrine (`doctrine/design-doctrine.md`), and all 8 `doctrine/references/*.md`.
**Bar:** Top-0.1% global. Reference standard = Pentagram, IDEO, Instrument, Metalab, Clay, Work & Co, Koto; Apple / Stripe / Linear / Vercel / Figma design; Awwwards SOTD / Apple Design Awards / D&AD winners.
**Scoring bands:** 90–100 rivals those · 75–89 excellent pro, minor gaps · 60–74 solid but visibly short of world-class · 40–59 competent/amateur · <40 skeletal. Default band 45–65; 70+ requires extraordinary, specific justification.

> **Method note.** The doctrine and references were read in full. The 37 skills were read across the auditor plus parallel reviewers, with ~13 skills additionally read directly by the lead auditor for calibration. Scores below are deliberately harsh per the brief.

---

## Headline finding: the doctrine is world-class; the skills are not

The single most important result of this audit is a **split between an exceptional doctrine layer and a merely-competent skill layer.**

- The **doctrine** (`design-doctrine.md` + 8 references) is genuinely top-tier opinionated design thinking: the "moat is looking human-made" Mission, the evidence-labelled banned-font list (`[AI]/[POP]/[SYS]`), the sourcing-authority **asymmetry rule** (AI vendors are evidence only for what to *ban*, never authority for what to *approve*), and the Bonneville/Vignelli/Segall-sourced pairing principles. This is sharper than most commercial type/brand guidance and is the engine's real asset.
- The **skills** mostly *route back to that doctrine* rather than adding craft of their own. Strip the doctrine and a large fraction of the SKILL bodies collapse to thin checklists.

### Four systemic weaknesses recur in every group

1. **Examples drought.** Across 37 skills there is **almost no worked example** — not one full generic→world-class before/after, no named-studio (Stripe/Linear/Vercel) teardown, no finished exemplar artifact. Every skill relies on the model *already* possessing elite taste rather than transferring it. This alone caps the engine far below the world-class bar.
2. **Generic boilerplate-stub entrypoints.** A large set of skills (`brand-alignment`, `brand-style-guide`, `color-selection`, `legal-sector-ui-ux`, `sector-strategies`, `ux-psychology`, `motion-design`, `data-visualization`, `interaction-design-patterns`, the mobile pair, and others) share an **identical auto-generated scaffold** ("Use When / Do Not Use When / Required Inputs / Workflow / Quality Standards / Anti-Patterns / Outputs" filled with vague filler) fronting their real content (often dumped into `references/legacy-guidance.md`). An identical templated shell is *itself a mild slop signal* in an anti-slop engine.
3. **Missing 2026 standards.** WCAG 2 AA contrast only — **no APCA / WCAG 3** anywhere (OKLCH is *named* but never operationalized: no formula, no worked ramp). No View Transitions API, no scroll-driven animation (`animation-timeline`), no container queries, no fluid `clamp()` type, no spring-physics motion (motion-design actively *forbids* it), no C2PA/provenance checks, no Material 3 Expressive, no Dynamic Island / Live Activities / haptics design.
4. **Redundancy.** Group 02 is one deck template instantiated 8× (byte-identical shared references). Group 04 has 5 overlapping color/brand skills. This is breadth-padding, not depth.

---

## Group 01 — Typography & Fonts — **56/100**

The engine's strongest *conceptually* (sits on the sharpest doctrine), but the skills themselves are thin procedural wrappers that re-route to `doctrine/references/`. **None have own reference files. None have worked examples.** The fatal gap: not one before/after, not one real pairing chosen for a named artifact, and no executable depth (no subsetting toolchain, no variable-font axis work, no `clamp()`/fluid type, no screenshot-based font forensics, no multi-script handling). They reliably *prevent* slop but do not, alone, *produce* world-class typography.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification (concrete deficiencies) |
|---|---:|---|---|---|---|---|
| font-selection-and-pairing | 62 | No | No | Yes (heavy) | Medium | Best of four; real 7-step spine. But a router over the doctrine: no worked pairing for an actual artifact, no x-height/contrast diagnostic procedure, no muddy-middle decision tree, no variable-font/optical-size guidance, no multi-script, no fluid-type. |
| ai-slop-typography-audit | 55 | No | No | Yes | Thin | Detection = keyword-match against the banned list; no font-inference-from-screenshot (OCR/visual), no `@font-face`/network inspection, no false-positive handling (brand-mandated Inter), **zero before/after despite promising it.** |
| premium-font-scan | 52 | No | No | Yes | Thin | A glorified `ls fonts/<group>/` + read-MANIFEST routine. No MANIFEST schema, no rule for which premium family wins, no font-quality vetting (hinting, weight coverage, italics). Mechanical plumbing. |
| font-embedding-and-licensing | 50 | No | No | Yes | Thin | Near-verbatim compression of two doctrine refs. No subsetting toolchain (`pyftsubset`/`glyphhanger`), no `unicode-range` splitting, no FOUT/FOIT/`size-adjust` guidance, no webfont-vs-desktop EULA edge cases. Verification step is "look at it." |

---

## Group 02 — Document Formatting (Decks) — **56/100**

Eight skills that generate **social-media-consultancy decks as markdown outlines** (Headline / Bullets / Speaker Notes / Visual Direction) — explicitly "paste into PowerPoint/Canva/Slides; no .pptx generated." Three structural problems define the group: **(1) the group is mislabelled "formatting" but formats nothing** — it never invokes the available `document-skills:pptx` tooling and offloads all visual execution to the human; **(2) heavy redundancy** — one identical skeleton plus byte-identical duplicated reference files (`presentation-frameworks.md` across 5 decks; `pitch-psychology.md`/`storytelling.md` across pairs); **(3) shallow + self-contradictory doctrine use** — every deck hardcodes "default to Group 3 — Bricolage + Hanken" for *all* decks, the opposite of the doctrine's "choose for THIS artifact" rule, and none specifies a real type scale, grid, or color system. The *content* discipline (Minto/Duarte/Klaff frameworks, complete-assertion headlines, presenter-ready notes, honesty norms) is genuinely good — but as **content briefs**, not world-class design.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification |
|---|---:|---|---|---|---|---|
| deck-initial-pitch | 66 | Yes (2, near-dup) | No | Boilerplate + contradicted | Deep persuasion / thin visual | Richest set — per-slide Persuasion Notes, hesitation scripts. But markdown only, never builds PPTX; generic Visual Direction; hardcoded font default. |
| deck-annual-review | 62 | Yes (1, dup) | No | Boilerplate | Deep content / thin design | Best narrative arc (Sparkline, 18 slides), strong honesty norms. Same ceiling: no artifact, generic visuals. |
| deck-quarterly-review | 60 | Yes (dup) | No | Boilerplate | Adequate | Solid keep/change/test + RACE; largely a longer monthly-report. Redundant skeleton; no PPTX. |
| deck-strategy-presentation | 59 | Yes (dup) | No | Boilerplate + contradicted | Medium | Clean Minto; cites "use visuals" data yet never produces the visuals. Overlaps initial-pitch. |
| deck-monthly-report | 57 | Yes (dup) | No | Boilerplate | Checklist-leaning | Competent reporting template; thin (10 slides), generic visuals, no artifact. |
| deck-campaign-proposal | 57 | Yes (2, near-dup) | No | Boilerplate | Medium | Near-duplicate of initial-pitch's persuasion machinery; no PPTX; generic mockup direction. |
| deck-credentials | 55 | Yes (2, dup) | No | Boilerplate | Checklist-leaning | Standard agency-credentials template; relies on duplicated refs; no distinctive layout system. |
| deck-ai-strategy-presentation | 54 | Yes (1, dup) | No | Boilerplate | Content-deep, design-shallow | Well-sourced (AI Marketing Canvas) but a fixed 14-slide fill-in form; cross-refs skills not in this engine; **slop-prone (fixed template).** |

---

## Group 03 — Web & UI Design — **60/100** (15 skills)

The largest and most consequential group. **Bimodal:** a few genuinely strong, engine-authored skills carry the band while the rest are derivative digests or boilerplate-stub entrypoints. Recurring gaps: **no worked examples anywhere**, no named-studio deconstructions, and missing 2026 web craft (View Transitions, scroll-driven animation, container queries, fluid `clamp()`, spring physics, C2PA). `distinctive-by-design` is the engine's soul skill and the only entry that earns 70+ — yet it ships **no examples of its own**, preaching distinctiveness without demonstrating it.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification |
|---|---:|---|---|---|---|---|
| distinctive-by-design | 72 | No | No | Yes (heavy, correct) | Deep, gated | Operationalizes the Mission: one committed idea, weight/size extremes, asymmetry rule, 8-item craft checklist, written decision before markup. But **zero refs, zero before/after** — never *shows* a templated hero reauthored; quality rests on model taste. |
| premium-ui-ux-design | 66 | Yes (15) | No | Yes (strong) | Broad orchestration + gate | Best-structured: visual-voice taxonomy, state list, 7-category blocking gate. But "premium" is asserted via adjectives/questions, **not demonstrated** — no generic→premium worked screen, no exemplar teardown, no optical/elevation specifics. Fee-band consultancy padding. |
| practical-ui-design | 68 | Yes (deep-dive) | Tables only | Yes (4 refs) | Deep rules-list | Strong content (HSB+OKLCH, mono palette tables, APCA, 8pt grid). But a rules compendium not authored craft; **internal contradiction** (deep-dive endorses one sans-serif system default, violating the doctrine it cites); no fluid type, no container queries. |
| ai-output-design | 68 | Yes (5) | Partial | Yes | Deep for scope | Sharp, current (Macfadyen 2025; correct "no confidence % on LLMs"; Perplexity/NotebookLM patterns; drop-in prompt block). Short of world-class: no full chat→canvas worked spec, no failure gallery, thin on streaming/multimodal. |
| healthcare-ui-design | 64 | Yes (15, deep) | Yes (code) | Yes | Deep | Deepest domain knowledge — clinical thresholds, HIPAA/FDA/ISO 62366/HL7 FHIR, alarm-fatigue rules, working code. But generic SaaS-blue palette, no authored visual POV, no Epic/Apple-Health-grade density masterclass, no usability evidence. Safety > craft. |
| webapp-gui-design | 64 | Yes (10 sections) | Yes (TSX) | Yes (§0) | Deep, implementation-ready | Strongest code skill: real Next.js/Radix/TanStack patterns, four-state rule, a11y sweep. But visually generic (`slate-50`/`indigo-500` = the convergent defaults the doctrine bans); two unintegrated stacks bolted together; no data-density depth. |
| interaction-design-patterns | 60 | Yes (sections) | No | Yes | Medium | Faithful Tidwell digest. But a **secondhand textbook summary** — no Linear/Stripe-era patterns (command palettes, optimistic UI, multiplayer presence, AI-inline), no worked application, no pattern-choice decision tree. |
| enterprise-ux-process | 58 | Yes (many) | Partial | Yes | Deep (process) | Rigorous 9-phase UX-ops methodology, maturity model, blueprinting sub-modules. But **process, not visual craft** — produces evidence packs, says nothing about what makes the UI *look* world-class. Right tool, wrong axis. |
| ux-psychology | 58 | Yes (legacy 547L) | No | Yes | Theory-dense | Rich roster (Gestalt, Nielsen 10, Norman, Miller 7±2, Branson, Deacon). But a **generic skeleton SKILL.md over a legacy dump**: no worked critique, no bias→pattern table, no measurement (SUS/time-on-task). Teaches vocabulary, not the move. |
| form-ux-design | 58 | Yes (6, deep) | Yes (code) | Yes | Deep | Strong cross-platform (Bootstrap/Compose/SwiftUI ~2,700 ref lines), correct opinions. But **generic boilerplate header**, no single fully-worked exemplar form, nothing on 2026 (passkeys, OTP autofill, inline AI assist). Audits correctness not distinctiveness. |
| design-audit | 57 | Yes (2 thin) | No | Yes | Medium | Usable 10-dimension rubric. But **overlaps visual-product-slop-audit + the doctrine** it should delegate to; AI-slop weighted only 4% despite being the engine's reason to exist; **no worked sample audit report** for calibration. |
| motion-design | 57 | **No** | Inline CSS only | Yes (2) | Good checklist, shallow physics | Solid 100/300/500 + GPU-only + reduced-motion. But **forbids the very 2026 technique it should teach** (springs/oscillation — Linear/Vercel/Family are spring-driven); no scroll-driven animation, no View Transitions, no FLIP, **zero refs**, no worked sequence. |
| legal-sector-ui-ux | 55 | Yes (4 real) | No | Yes | Generic stub over decent refs | **SKILL.md is a pure boilerplate stub** saved only by useful refs (bar-association rules, attorney profiles, legal SEO). Sector visual direction thin; no top-firm trust-pattern teardown; ethics not jurisdiction-resolved. Slop-prone entrypoint. |
| sector-strategies | 54 | Yes (vast ~80 files) | Templates | Yes (+ anti-homogeneity) | Broad, shallow per-sector | 13 sectors at template depth = none world-class; same generic stub entrypoint; "choose sector → customize template" is structurally *toward* the convergent mean. **Risks being a slop factory** unless the anti-homogeneity gate is enforced — which the stub doesn't operationalize. |
| ai-agent-ux | 52 | Yes (11) | Partial | Yes | Thin top (router) | A 70-line **pure router** — SKILL.md is generic boilerplate deferring everything to child refs. No opinionated agent-UX POV, no worked agent surface, no 2026 agent-loop/approval-diff/interrupt patterns at the top level. |
| visual-product-slop-audit | 52 | **No** | No | Yes (tight) | Focused checklist | Cleanest small skill, correctly scoped/delegating. But a **thin mirror of `ai-slop-taxonomy.md`** — no 2026 generative tells (diffusion artifacts, AI-video flicker, C2PA/provenance, detector tooling), no severity-scored worked audit, no own refs. |

---

## Group 04 — Color & Visual Identity — **56/100**

Two strong, doctrine-native skills (`color-system-and-palette`, `brand-visual-identity`); three weaker legacy/boilerplate-wrapped or redundant ones. **Biggest structural weakness: 5 overlapping color/brand skills** (`color-selection` vs `color-system-and-palette`; `brand-alignment` vs `brand-style-guide` vs `brand-visual-identity`) a world-class engine would consolidate. Critically, **OKLCH is named but never operationalized** (no formula, no worked ramp) and contrast is **WCAG 2 AA only — no APCA/WCAG 3.** No skill ships an actual generated ramp with hex values as a worked example.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification |
|---|---:|---|---|---|---|---|
| color-system-and-palette | 68 | No own dir | No | Yes (deep) | Deep, principled | Best in group: anchor-first, perceptual ramp, semantic roles, 60-30-10, dark-mode-as-remap, hard contrast gate, cites Albers/Itten. But OKLCH never operationalized; WCAG 2 only; no worked palette with hexes; punts categorical/sequential scales to G05. |
| brand-visual-identity | 65 | No own dir | No | Yes (deep) | Deep | Strategy-first, ownability test, consistency gate, cites Rand/Vignelli/Neumeier. But no logo-construction technique (grids, optical correction), no worked identity, no motion/sonic-system depth a Pentagram/Koto identity needs. |
| brand-style-guide | 52 | Yes (3) | Template only | Cited, shallow | Thin | Real `style-guide-template.md` + CMYK awareness. But body is generic boilerplate; 4-step stub workflow; no worked specimen. |
| color-selection | 50 | Yes (9) | In flux ref | Cited | Mixed | Salvaged by deep `flux-process.md` + `palette_generator.py`. But top half pure boilerplate; **redundant** with color-system-and-palette (routing note admits the overlap); WCAG AA only; HSL not perceptual. |
| brand-alignment | 44 | Yes (2) | No | Cited | Thin | Near-pure boilerplate "quality lens." `trust-architecture-checklist.md` is generic web-trust content, not visual-identity craft. Adds little the other brand skills don't. **Generic/redundant stub.** |

---

## Group 05 — Layout, Grid & Data-Viz — **64/100**

The strongest-balanced group: only two skills, both doctrine-native and substantive, **no boilerplate shells.** `data-visualization` is the single most complete skill in the engine (exhaustive Knaflic distillation + Tufte data-ink + Gestalt + preattentive + chart-selection tree + a real SVG/D3 implementation ref). Falls short of FT/NYT/Pentagram desks: **anchored almost entirely to one 2015 book**, lacking scrollytelling, uncertainty viz, perceptual color scales (ColorBrewer/viridis), and animation craft; WCAG 2 only. `layout-grid-and-spacing` cites the right canon (Müller-Brockmann, Tschichold, Vignelli, Lupton) but has **no own refs and zero worked examples** — no annotated before/after, no real grid spec with numbers.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification |
|---|---:|---|---|---|---|---|
| data-visualization | 69 | Yes (3) | Partial (SVG ref) | Yes (deep) | Deep | Exhaustive Knaflic + Tufte/Gestalt/preattentive, chart-selection tree, zero-baseline rules, colorblind cues, SVG/D3 + responsive refs. But single-book spine (2015); no scrollytelling/uncertainty/small-multiples-as-code; no viridis/ColorBrewer; WCAG 2 only; no worked dashboard exhibit. |
| layout-grid-and-spacing | 61 | No own dir | **No** | Yes (deep) | Deep but abstract | Principled grid-as-discipline, focal point, intentional asymmetry, optical alignment, breakpoint re-composition. But no own refs, **no worked example**, no concrete grid spec with measurements, no CSS Grid/container-query 2026 depth, no print-grid baseline case. |

---

## Group 06 — Mobile UI/UX — **49/100** (weakest group)

Both SKILL.md entries are **thin checklists** (75–76 lines) reading as senior-dev guardrail lists, not world-class craft. They name the right primitives (Material 3, 48dp/44pt, TalkBack/VoiceOver, Dynamic Type, edge-to-edge, WindowSizeClass) but stop at enumeration. The deep references are **legacy code-style-guide imports** with the same generic boilerplate shell — SwiftUI/Compose *coding* standards, not UX-design craft. Major 2026 gaps: **no haptics design, no Dynamic Island / Live Activities, no Material 3 Expressive (2025's flagship), no gesture-system design, no iOS 26 Liquid Glass beyond a one-line mention, no worked screen flow, no motion specs.** Both explicitly defer real work to a separate development skill — so they are gates, not generators.

| Skill | Score | Refs? | Examples? | Doctrine? | Depth | Justification |
|---|---:|---|---|---|---|---|
| ios-ui-ux-design | 51 | Yes (3) | No | Cited (charter) | Thin checklist | Correct HIG primitives + good SF Pro font caveat. But no haptics, no Dynamic Island/Live Activities, no worked flow, Liquid Glass one-liner only; refs are legacy SwiftUI *coding* standards with boilerplate shells. |
| android-ui-ux-design | 48 | Yes (1) | No | Cited (charter) | Thin checklist | Correct M3 primitives + good Roboto caveat. But **no Material 3 Expressive**, no haptics/motion specs, no predictive-back design, no worked screen; single ref is a legacy Compose *coding* guide with the generic template shell. |

---

## Group ranking (weakest → strongest)

| Rank | Group | Score | One-line verdict |
|---|---|---:|---|
| 6 (weakest) | **06 Mobile UI/UX** | 49 | Two thin checklists deferring real work; refs are legacy *coding* guides; missing all 2026 mobile craft (haptics, Dynamic Island, M3 Expressive, gesture design). |
| 5 | **01 Typography & Fonts** | 56 | Sharp doctrine, but the skills are thin wrappers re-routing to it; no own refs, no worked examples, no executable depth. |
| 4 (tie) | **02 Document Formatting (Decks)** | 56 | One deck template ×8; formats nothing (never builds PPTX); good content briefs, not world-class design; redundant + self-contradictory doctrine use. |
| 4 (tie) | **04 Color & Visual Identity** | 56 | Two strong skills dragged down by 3 redundant/boilerplate ones; OKLCH named-not-operationalized; no APCA. |
| 2 | **03 Web & UI Design** | 60 | Bimodal — `distinctive-by-design` (72) and a few strong code/premium skills carry it; the rest are textbook digests or boilerplate stubs; no worked examples anywhere. |
| 1 (strongest) | **05 Layout, Grid & Data-Viz** | 64 | Two substantive, doctrine-native skills, no boilerplate; held back by single-source data-viz spine and zero layout worked examples. |

---

## Aggregate engine score — **58/100** (current skill depth/quality)

**Justification.** Weighting by skill count (01:4, 02:8, 03:15, 04:5, 05:2, 06:2 = 36 scored skills) the mean lands at **~58/100** — squarely in the "competent / amateur-to-solid-pro" band, **visibly short of world-class** and consistent with the brief's strict-default expectation.

The engine **clears the amateur bar** because: (a) the doctrine it sits on is genuinely excellent and well-sourced; (b) a handful of skills are real — `distinctive-by-design`, `data-visualization`, `practical-ui-design`, `premium-ui-ux-design`, `webapp-gui-design`, `color-system-and-palette`, `ai-output-design`; (c) the anti-slop *intent* is correct and unusually disciplined.

It **fails the world-class (75+) bar** for four structural reasons, all recurring across every group:

1. **No worked examples.** Not one full generic→world-class transformation, named-studio teardown, or finished exemplar across 37 skills. The engine *tells* but never *shows*; output quality is delegated entirely to the model's pre-existing taste. This single deficiency is disqualifying at the top-0.1% bar.
2. **Boilerplate-stub entrypoints.** A templated, near-identical SKILL.md shell fronts a large minority of skills — itself a slop signal in an anti-slop engine, and evidence the skills were bulk-migrated rather than individually authored.
3. **Missing 2026 standards.** No APCA/WCAG 3, OKLCH never operationalized, no View Transitions / scroll-driven animation / container queries / fluid type / spring physics (actively forbidden), no C2PA, no Material 3 Expressive / Dynamic Island / haptics.
4. **Redundancy + thinness at the edges.** Group 02 (8× one template) and Group 04 (5 overlapping skills) pad breadth; Groups 01 and 06 are thin wrappers/checklists.

**Net:** a strong doctrine with a competent-but-not-yet-crafted skill layer. The fastest route to a world-class score is not more skills — it is (a) ship worked before/after exemplars and named-studio teardowns in every skill, (b) delete the boilerplate stubs and the duplicated deck/color skills, (c) make the deck group actually build doctrine-compliant `.pptx`, and (d) bring the color/motion/mobile skills to 2026 standards (APCA, operationalized OKLCH, spring physics + View Transitions, Material 3 Expressive / haptics).

### Per-skill scores at a glance (sorted)

72 distinctive-by-design · 69 data-visualization · 68 practical-ui-design · 68 ai-output-design · 68 color-system-and-palette · 66 deck-initial-pitch · 66 premium-ui-ux-design · 65 brand-visual-identity · 64 healthcare-ui-design · 64 webapp-gui-design · 62 font-selection-and-pairing · 62 deck-annual-review · 61 layout-grid-and-spacing · 60 interaction-design-patterns · 60 deck-quarterly-review · 59 deck-strategy-presentation · 58 enterprise-ux-process · 58 ux-psychology · 58 form-ux-design · 57 design-audit · 57 motion-design · 57 deck-monthly-report · 57 deck-campaign-proposal · 55 ai-slop-typography-audit · 55 deck-credentials · 55 legal-sector-ui-ux · 54 sector-strategies · 54 deck-ai-strategy-presentation · 52 premium-font-scan · 52 ai-agent-ux · 52 visual-product-slop-audit · 52 brand-style-guide · 51 ios-ui-ux-design · 50 font-embedding-and-licensing · 50 color-selection · 48 android-ui-ux-design · 44 brand-alignment

**Skills flagged as stubs / generic / slop-prone:** brand-alignment, brand-style-guide, color-selection (boilerplate shell over deep ref), legal-sector-ui-ux, sector-strategies (slop-factory risk), ai-agent-ux (router shell), ux-psychology (skeleton over legacy dump), all 8 deck skills (templated + redundant), the mobile pair (thin checklists), font-embedding-and-licensing & premium-font-scan (thin wrappers).
