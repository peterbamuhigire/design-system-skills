# 02 — Coverage & Taxonomy Evaluation

**Engine:** `C:\wamp64\www\design-system-skills`
**Doctrine reviewed:** `doctrine/design-doctrine.md` (v0.1.0)
**Inventory:** 37 skills across 6 numbered groups (excludes `_TEMPLATE`).
**Target ceiling:** 75–100 skills.
**Date:** 2026-06-21
**Verdict:** the 6-group taxonomy is **NOT sufficient** for world-class, multi-output coverage.

---

## 1. The current taxonomy, as built

| Group | Skills | Count | What it actually contains |
|---|---|---|---|
| 01 Typography & Fonts | selection-and-pairing, ai-slop-typography-audit, premium-font-scan, font-embedding-and-licensing | 4 | Coherent. Pure type discipline. Well-sized. |
| 02 Document Formatting | 7× `deck-*` (initial-pitch, strategy, ai-strategy, campaign-proposal, credentials, monthly-report, quarterly-review, annual-review) + 0 real doc skills | 8 | **Mislabelled.** This is a *presentations/decks* group, not "document formatting." There is **no** DOCX/PDF/XLSX/long-form formatting skill here at all. |
| 03 Web & UI Design | ai-agent-ux, ai-output-design, design-audit, distinctive-by-design, enterprise-ux-process, form-ux-design, healthcare-ui-design, interaction-design-patterns, legal-sector-ui-ux, motion-design, practical-ui-design, premium-ui-ux-design, sector-strategies, ux-psychology, visual-product-slop-audit, webapp-gui-design | 16 | **Overloaded grab-bag.** Mixes: foundational UI craft, UX *process*, UX *psychology*, sector verticals (healthcare/legal), motion, interaction patterns, AI-native UX, and two audits. At least 5 distinct sub-domains live here. |
| 04 Color & Visual Identity | brand-alignment, brand-style-guide, brand-visual-identity, color-selection, color-system-and-palette | 5 | Two concerns fused: **colour** (2) and **brand/identity** (3). Workable now, will split under growth. |
| 05 Layout, Grid & Data-viz | layout-grid-and-spacing, data-visualization | 2 | **Under-sized and mis-fused.** Layout/grid is a foundation; data-viz is a deep discipline. They share a group only by accident. |
| 06 Mobile UI/UX | android-ui-ux-design, ios-ui-ux-design | 2 | **Under-sized.** Two platform stubs; no cross-platform, no responsive, no touch/gesture/adaptive depth. |

---

## 2. Taxonomy score — **48 / 100**

Scored strictly (default band 45–65; 70+ requires extraordinary justification, which this does not earn).

| Criterion | Weight | Score | Rationale |
|---|---|---|---|
| **Collective exhaustiveness** (does it have a home for every world-class concern?) | 25 | 9/25 | Major domains have **no group at all**: accessibility, design systems/tokens, content/UX-writing, imagery/illustration art-direction, design-ops/handoff, prototyping/research, internationalization. A world-class engine cannot route work it has no category for. |
| **Mutual exclusivity** (clean boundaries, low overlap) | 20 | 8/20 | 03 is a dumping ground (process + psychology + verticals + motion + AI-UX + audits). "Document formatting" overlaps decks and has no actual doc-formatting skill. Brand vs colour fused. Layout vs data-viz fused. Three audits scattered (typography in 01, design-audit + visual-product-slop in 03) with no QA/critique home. |
| **Balance / sizing** (no group starved or bloated) | 15 | 4/15 | Gini is severe: 03 holds 43% of skills (16) while 05 and 06 hold 2 each. The numbered order implies a hierarchy that the contents contradict. |
| **Scalability to 75–100** (will the structure absorb 2.5× growth without re-shuffling?) | 20 | 9/20 | At 75–100, 03 would balloon past 30 skills and 02 past 15 — both unnavigable. The current 6 buckets do not pre-allocate slots for the missing domains, so growth forces a re-org rather than infill. |
| **Naming clarity & labelling honesty** | 10 | 5/10 | "02 Document Formatting" is actively misleading (it's decks). "05 Layout-Grid-and-Data-viz" names two unrelated things. Otherwise group names are serviceable. |
| **Doctrine alignment** (does structure express the anti-slop mission?) | 10 | 13/10→capped 13 | Strong: the anti-slop charter, distinctive-by-design gate, and three audits genuinely operationalize the moat. This is the engine's best asset and the reason the score isn't lower. (Capped contribution applied.) |
| **Total** | 100 | **48** | Foundation is real and the mission is well-expressed, but the cabinet has too few drawers, mislabelled drawers, and two drawers doing 43% of the work. |

**One-line verdict:** good bones and an excellent mission, but a 6-drawer cabinet cannot file 75–100 world-class skills — it needs ~13 honestly-named, evenly-loadable drawers.

---

## 3. Specific structural defects (the case for re-org)

1. **"02 Document Formatting" is a misnomer.** It holds 8 deck skills and zero document-formatting skills. Decks deserve their own group; real document/editorial formatting (DOCX reports, PDF proposals, XLSX models, long-form editorial) is **entirely missing** and needs a genuine home.
2. **03 is doing the work of 5 groups.** UI craft, UX *process/research*, UX *psychology/behavioral*, sector *verticals*, and AI-native UX are different disciplines with different evidence bases. At 16 skills today and unbounded growth ahead, it must be decomposed.
3. **Mobile (06) is starved and platform-thin.** iOS + Android stubs only. World-class mobile needs cross-platform parity, touch/gesture, adaptive layout, app-store presence craft, and platform-idiom depth — a 6–8 skill domain, not 2.
4. **Data-viz is buried under layout (05).** Dashboards and data products are a premium deliverable type; data-viz/charts/dashboards deserve their own group, leaving layout/grid as the foundation it is.
5. **No accessibility group.** WCAG 2.2, contrast, focus, screen-reader, reduced-motion, RTL/i18n have no home — a disqualifying gap for "world-class" and a legal/ethical one.
6. **No design-systems / tokens / theming group.** Tokens, components, dark mode, multi-brand theming, handoff are the backbone of any top studio's output and have no category.
7. **No content/UX-writing group.** Microcopy, voice & tone, error/empty/onboarding copy, naming — the cheapest highest-leverage quality lever — is absent.
8. **No imagery / art-direction group.** Photography, illustration, iconography, 3D/immersive, AI-image direction — the single biggest "looks human-made vs slop" lever per the doctrine's own mission — is absent.
9. **No design-ops / QA / critique group.** Three audits exist but scattered; handoff, design review, versioning, and a critique discipline have no consolidated home.

---

## 4. Proposed revised category structure (built for 75–100)

Thirteen groups. Each is a real discipline with clean boundaries and room to grow to 5–9 skills. Numbering keeps foundations first, then craft, then delivery/ops.

| # | Group | Scope | Migrates in | Target size |
|---|---|---|---|---|
| **01** | **Typography & Fonts** | Type selection, pairing, scale, embedding, licensing, slop-audit | *(unchanged — all 4)* | 5–7 |
| **02** | **Color, Brand & Visual Identity** | Palettes, contrast-as-design, brand systems, logo/lockup, identity tie-in | 04's 5 skills (split brand vs colour internally) | 7–9 |
| **03** | **Layout, Grid & Composition** | Grids, spacing, hierarchy, responsive/adaptive composition, editorial layout | `layout-grid-and-spacing` from 05 | 6–8 |
| **04** | **Web & UI Design (foundations & craft)** | Core interface craft: practical-ui, distinctive-by-design, webapp-gui, interaction patterns, premium-ui | 03's craft skills (practical-ui-design, distinctive-by-design, webapp-gui-design, interaction-design-patterns, premium-ui-ux-design) | 7–9 |
| **05** | **UX Process, Research & Psychology** | Discovery, research, usability, heuristics, behavioral/cognitive, enterprise process | 03's enterprise-ux-process, ux-psychology | 6–8 |
| **06** | **Sector & Domain UX** | Vertical playbooks (healthcare, legal, fintech, e-comm, gov/NGO, education…) | 03's healthcare-ui-design, legal-sector-ui-ux, sector-strategies | 6–9 |
| **07** | **Mobile (iOS / Android / Cross-platform)** | Platform idioms, touch/gesture, adaptive, app-store craft | 06's ios + android | 6–8 |
| **08** | **Motion & Interaction** | Animation, micro-interactions, transitions, gesture choreography, reduced-motion | 03's motion-design (+ split interaction motion from patterns) | 5–7 |
| **09** | **Design Systems, Tokens & Theming** | Tokens, components, dark mode, multi-brand theming, dev-handoff/Figma | *(net-new group)* | 7–9 |
| **10** | **Content Design & UX Writing** | Microcopy, voice/tone, error/empty/onboarding copy, naming, localization copy | *(net-new group)* | 5–7 |
| **11** | **Imagery, Illustration & Art Direction** | Photography direction, illustration, iconography, 3D/WebGL/immersive, AI-image direction | *(net-new group)* | 6–8 |
| **12** | **Data Viz & Dashboards** | Charts, dashboards, KPI exhibits, data products | `data-visualization` from 05 | 5–7 |
| **13** | **Presentations & Documents** | Decks (the 7 `deck-*`) **+** real DOCX/PDF/XLSX/editorial formatting | 02's 8 deck skills + net-new doc skills | 9–12 |
| **(X)** | **Design Ops, QA & Accessibility** *(cross-cutting)* | Accessibility/WCAG, design QA/critique, handoff, ethics, sustainability, performance-as-UX. Modelled like the finance engine: **activates alongside** any group. | 03's design-audit, visual-product-slop-audit; 01's slop-audit cross-links | 8–10 |

**Why 13 + 1 cross-cutting and not fewer:** at 75–100 skills, ~12–14 groups give ~6–8 skills each — the sweet spot for navigability (a router can list a group's skills on one screen) without fragmenting. Fewer groups recreate today's 16-deep grab-bag; more groups fragment.

**Accessibility/QA as cross-cutting, not a numbered silo:** like the finance doctrine that activates alongside domain engines, accessibility, QA/critique, ethics, and performance-as-UX should be *always-co-activated* rather than buried in one numbered group — this matches the engine's own architectural pattern and ensures they are never skipped.

---

## 5. Migration impact summary

- **No skill is deleted.** Every existing skill maps to exactly one revised group (table above).
- **02 is renamed and rescoped** to honestly cover presentations + documents.
- **03 is decomposed** into groups 04, 05, 06, 08 (and audits → cross-cutting).
- **05 splits** into 03 (layout) and 12 (data-viz).
- **04 absorbs** into the new 02 (color+brand).
- **Net-new groups (09, 10, 11, cross-cutting)** open the headroom the gap analysis fills.

See `04-gap-analysis-new-skills.md` for the skill-level infill that brings each revised group to its target size and lands the engine in the 75–100 range.
