---
name: product-design-audit
description: Point the WHOLE design engine at a real, existing PRODUCT (not a single
  artifact) and produce a scored, multi-platform design audit with a PRIORITIZED
  recommendation table where every finding is routed to the exact engine skill that
  fixes it. Audits across ALL surfaces a product ships on — marketing website, SaaS
  web app, iOS app (iPhone/iPad/Mac), Android app, and desktop app — running the
  doctrine anti-slop gate, each relevant design-group lens, and the cross-cutting
  WCAG-2.2 / Core-Web-Vitals / content gates over the whole experience. Triggers:
  "audit my product", "audit our app", "design review of the whole product", "score
  our SaaS / website / iOS app / Android app / desktop app", "product-level design
  audit", "multi-platform design audit", "where is our design losing us users",
  "what should design fix first", "route the findings to skills", "design health
  check", "cross-platform design parity audit", "is our product design any good".
  For a single screen/artifact critique use design-audit; for a pass/fail ship gate
  use design-qa-and-pre-launch-review. This skill composes both and adds the
  product + platform breadth and the skill-routing.
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
  - claude-code
  - codex
---

# Product Design Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- You have a **real, existing product** (live or staging) and want a single, scored
  design audit of the **whole thing**, not one screen — covering every surface it ships
  on and ending in a prioritized, skill-routed fix list.
- The product spans **multiple platforms** — e.g. a marketing **website** + a **SaaS web
  app** + an **iOS app** (iPhone/iPad/Mac) + an **Android app** + a **desktop app** — and
  you need each platform judged on its own idioms *and* the experience judged for
  cross-platform parity.
- You want findings that **route to the engine skill that remediates them** (e.g. low
  contrast → `accessible-color-and-contrast`, Inter in use → `font-selection-and-pairing`,
  no empty states → `empty-error-and-loading-states`, non-idiomatic iOS →
  `ios-ui-ux-design`) so the audit becomes an executable work plan, not just a critique.
- You need a **defensible number** (0–100, with the hard gates that can cap it) per surface
  and an overall product verdict for a stakeholder, investor, or roadmap conversation.
- You are doing **due diligence** on a product (yours or one you are acquiring/consulting on)
  and need the design-quality picture across all its clients.

## Do Not Use When

- You only need to critique **one screen or one artifact** (a landing page, a single
  dashboard, one PDF) — use `design-audit`. This skill *invokes* it per surface; do not
  duplicate it for a single-artifact job.
- You need a **pass/fail go/no-go ship gate** for a build that is about to launch — use
  `design-qa-and-pre-launch-review`. This skill is an exploratory, scored, product-wide
  diagnostic, not a launch sign-off (though its findings can feed one).
- You only need **one cross-cutting dimension**: slop → `visual-product-slop-audit`; WCAG
  → `accessibility-wcag-2-2-compliance`; CWV/budgets →
  `performance-as-ux-and-core-web-vitals`; type slop → `ai-slop-typography-audit`.
- There is **no built product yet** (early design only) — there is nothing to audit. Use the
  design/research skills to *create* first; return when there is something running.
- The deliverable is a **document** (DOCX/PDF/PPTX) rather than a product — use the group-13
  document skills; CWV / platform idioms do not apply.

## Required Inputs

- **The product and its platform set.** Name the product and confirm *which* surfaces are in
  scope: website, SaaS web app, iOS (iPhone/iPad/Mac), Android, desktop (native vs Electron).
  The audit runs only the platform lenses that apply — but it must run **all** that do.
- **Access to each surface in scope** — a live URL / staging build / TestFlight / APK /
  desktop binary, OR a representative set of **screenshots per key flow per breakpoint/device**.
  Refuse to score a surface from a single hero screenshot; ask for the core flows.
- **Product context** — who the users are, the primary jobs-to-be-done, the brand
  personality, and any design system / tokens already in place. This sets the bar the audit
  scores against (`design-audit` §Step 1).
- **The stated type/colour choice** (per the Mission) if one exists — or note its absence as
  the first slop finding.
- **Field performance data** (CrUX / RUM p75) for the web surfaces where available; lab
  (Lighthouse) is a labelled proxy only.
- The **page/app archetype** per web surface (marketing, web-app shell, document) — selects
  the budget row in `web-performance-budgets-2026.md`.

## Workflow

1. **Intake the product and lock the platform matrix.** Record the product, its users/JTBD,
   brand, and the exact surfaces in scope. Build a matrix: rows = surfaces (Website / SaaS
   web app / iOS / Android / Desktop), columns = the cross-platform dimensions
   (`references/audit-dimensions.md`). Every in-scope surface gets a row; every applicable
   dimension gets scored. See `references/audit-dimensions.md`.
2. **Run the doctrine / anti-slop gate over the whole product first.** Before any nicety,
   delegate to `visual-product-slop-audit` (visual + product tells) and
   `ai-slop-typography-audit` (banned fonts, pairing) across the surfaces. Confirm the
   type/colour/layout choice was **stated** (Mission), no banned default font
   (`doctrine/references/ai-slop-banned-fonts.md` — Inter, Geist, Roboto, Space Grotesk…),
   and no convergent visual tell survived. **This gate is binary and product-wide:** any FAIL
   caps the affected surface's score (`references/recommendation-format.md` §gates) and is the
   first routed finding (→ `font-selection-and-pairing` / `distinctive-by-design`).
3. **Score every surface on the cross-platform dimensions.** For each in-scope surface, run
   the 11 dimensions in `references/audit-dimensions.md` (the `design-audit` 10 + IA/Navigation
   + Trust), scoring each 0–4 against the extended rubric. Reuse `design-audit`'s
   `references/audit-rubric.md` for the gate logic and 0–100 math; this skill adds the
   per-surface application and the two extra dimensions.
4. **Apply each platform lens.** For every surface, run its specific lens from
   `references/platform-lenses.md`: **Website** (Core Web Vitals, responsive/container
   queries, SEO-visual); **SaaS web app** (app shell, data density, tables, states,
   onboarding); **iOS** (HIG + Liquid Glass, SF Symbols, Dynamic Type, haptics; Mac
   Catalyst/menus/windows, iPad multitasking/pointer, iPhone safe areas/Dynamic Island);
   **Android** (Material 3 Expressive, dynamic colour, predictive back, foldables,
   edge-to-edge); **Desktop** (native vs Electron, window chrome, density, keyboard/shortcuts,
   menus). Non-idiomatic findings route to the platform's owning skill (`ios-ui-ux-design`,
   `android-ui-ux-design`, `webapp-gui-design`).
5. **Run the cross-cutting gates per surface.** Accessibility against
   `doctrine/references/wcag-2.2-criteria.md` via `accessibility-wcag-2-2-compliance` (the AA
   floor **plus** the nine 2.2 deltas; automated **plus** keyboard **plus** screen-reader —
   automation alone catches ~30–40%); performance against
   `doctrine/references/web-performance-budgets-2026.md` via
   `performance-as-ux-and-core-web-vitals` (web surfaces); content/UX-writing against
   `ux-writing-and-microcopy` / `error-empty-and-system-messaging`. Each gate can cap the
   surface score (`references/recommendation-format.md`).
6. **Check cross-platform parity.** Where the same product spans surfaces, run the parity lens
   (`cross-platform-design-parity`): consistent IA, terminology, brand, and state model
   without forcing one platform's idioms onto another (an iOS tab bar ported verbatim to
   Android is a finding, not parity). Record parity gaps as their own findings routed to
   `cross-platform-design-parity`.
7. **Score and band each surface, then the product.** Produce a 0–100 per surface (gates
   applied) using the rubric, then an **overall product verdict** = the gate-respecting roll-up
   across surfaces (the product is only as shippable as its weakest blocking gate). Band per
   `references/recommendation-format.md`.
8. **Build the prioritized, skill-routed recommendation table.** This is the payload. Every
   finding gets: surface, dimension, severity, evidence, **P0/P1/P2 priority** (user-impact ×
   effort, per `references/recommendation-format.md`), the standard it violates, and the **exact
   engine skill that remediates it**. Group by priority so the team can execute top-down. Never
   leave a finding un-routed — if no skill fits, say so and name the doctrine reference instead.
9. **Write the verdict.** Lead with the product verdict and the single highest-leverage fix,
   then the per-surface scores, then the routed table. Make assumptions, evidence gaps, and any
   surface you could not fully access explicit.

## Quality Standards

- **Product-level, not artifact-level.** Score whole surfaces and their flows, not one hero
  screen. A surface scored from a single screenshot is flagged as low-confidence.
- **Every applicable platform is actually audited** on its own idioms — an iOS app is judged
  against HIG/Liquid Glass, an Android app against Material 3 Expressive, never one rubric
  flattened across both.
- **Every finding is routed** to a real, existing engine skill (glob-verified name) — the audit
  is an executable work plan. Un-routable findings name the doctrine reference instead.
- The three hard gates (slop, WCAG-2.2-AA, CWV) are **run, not assumed**, and they **cap** the
  score per `references/recommendation-format.md`. Never report ≥ 60 for a surface while slop or
  a11y is failing.
- Accessibility uses automation **plus** manual keyboard **plus** screen-reader. A green
  Lighthouse number is not an a11y pass.
- Scores trace to `design-audit`'s `references/audit-rubric.md`; thresholds trace to the
  canonical `wcag-2.2-criteria.md` and `web-performance-budgets-2026.md` — never re-invented.

## Anti-Patterns

- **Auditing one screen and calling it the product.** The whole point is breadth across
  surfaces and flows; a single-artifact critique is `design-audit`'s job.
- **One rubric flattened across platforms.** Scoring an iOS app with web heuristics (or vice
  versa) and missing the platform idioms — that is what `platform-lenses.md` exists to prevent.
- **Findings with no skill route.** A critique that says "fix contrast" without pointing at
  `accessible-color-and-contrast` is not actionable; route every finding.
- **Letting a weighted total hide a failing gate.** A surface with a slop or AA failure cannot
  score ≥ 60 no matter how pretty — apply the caps.
- **Forcing cross-platform sameness.** Calling a faithful Material 3 app "inconsistent" because
  it does not look like the iOS app — parity is shared IA/brand/terminology, not pixel-identical
  chrome.
- **Re-deriving thresholds or duplicating the audits.** Inventing contrast/CWV numbers, or
  re-writing the slop/a11y/perf logic here instead of invoking the owning skills — this skill
  *composes* them across the product, it does not fork them.
- **Treating Lighthouse green as the whole a11y or perf story.** Field p75 and manual passes
  are required.

## Outputs

- A **product design audit report** (`examples/product-audit-worked.md` shape): header (product,
  platforms, context), the product-wide anti-slop verdict, a **per-surface scorecard** (0–100
  with gates and band each), and the **overall product verdict**.
- A **prioritized, skill-routed recommendation table**: every finding with surface, dimension,
  severity, P0/P1/P2, evidence, violated standard, and the **engine skill that fixes it**.
- A **per-surface dimension worksheet** (the rubric's 0–4 grid, extended with IA/Nav + Trust).
- A **cross-platform parity note** listing parity gaps routed to `cross-platform-design-parity`.
- An **evidence-gap list** — surfaces/flows not fully accessible, marked low-confidence.

## Evidence Produced

| Category | Artifact | Format | Example |
|----------|----------|--------|---------|
| Product UX | Product design audit | Markdown report: per-surface scorecards + overall verdict | `docs/ux/product-audit-acme.md` |
| Product UX | Skill-routed recommendation table | Prioritized P0/P1/P2 table, each finding → remediating skill | `docs/ux/audit-recommendations.md` |
| Product UX | Per-surface dimension worksheet | 0–4 grid (11 dimensions) per surface with gate flags | `docs/ux/audit-scorecards.md` |
| Product UX | Cross-platform parity note | Parity gaps routed to `cross-platform-design-parity` | `docs/ux/audit-parity.md` |

## Examples

- `examples/product-audit-worked.md` — a fully worked product audit of a real-ish SaaS product
  (a small-business invoicing tool, "Tenda Books") that ships a marketing website, a SaaS web
  app, and an iOS app. Real findings with evidence, per-surface 0–4 dimension worksheets, the
  three gates applied (with a contrast + a banned-font failure capping two surfaces), the
  prioritized P0/P1/P2 **skill-routed** recommendation table, and an overall product verdict.
  Not lorem — concrete thresholds, real skill names, no banned fonts.

## References

- `references/audit-dimensions.md` — the 11 cross-platform dimensions this audit scores (the
  `design-audit` 10 + IA/Navigation + Trust), each with what it checks and the skill it routes to.
- `references/platform-lenses.md` — the per-platform check lists (Website, SaaS web app, iOS
  [iPhone/iPad/Mac], Android, Desktop) and which skill remediates each platform finding.
- `references/recommendation-format.md` — how to score (severity), apply the hard-gate caps,
  prioritize (P0/P1/P2 = user-impact × effort), and route each finding to the exact engine skill.
- `design-audit` → `references/audit-rubric.md` — the 0–100 rubric and three-gate cap logic this
  skill reuses per surface (do not duplicate; compose).
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter; the rule that a slop / a11y
  / perf blocker caps a surface and that convenience never overrides.
- `doctrine/references/wcag-2.2-criteria.md` and `doctrine/references/web-performance-budgets-2026.md`
  — the canonical accessibility floor (AA + nine 2.2 deltas) and performance floor (CWV "good").
- `doctrine/references/ai-slop-taxonomy.md`, `doctrine/references/ai-slop-banned-fonts.md`,
  `doctrine/references/font-groups-and-usage.md` — the slop tells, the banned faces, and the
  8 intent-based font categories the typography findings route against.
<!-- dual-compat-end -->
## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `design-audit` | Per-surface scored 0–100 diagnostic — this skill runs it per surface and aggregates |
| `design-qa-and-pre-launch-review` | When a surface is about to ship and needs the pass/fail gate, not a diagnostic |
| `visual-product-slop-audit` | The product-wide visual + product slop gate — blocking |
| `ai-slop-typography-audit` | The banned-font / pairing half of the slop gate — blocking |
| `accessibility-wcag-2-2-compliance` | The per-surface WCAG 2.2 AA gate — blocking |
| `performance-as-ux-and-core-web-vitals` | The per-web-surface Core Web Vitals / budget gate — blocking |
| `cross-platform-design-parity` | The parity lens across surfaces of one product |
| `ios-ui-ux-design` / `android-ui-ux-design` / `webapp-gui-design` | The platform lenses' remediation owners |

---

*Sources: composes `design-audit`, `design-qa-and-pre-launch-review`, `visual-product-slop-audit`,
`ai-slop-typography-audit`, `accessibility-wcag-2-2-compliance`,
`performance-as-ux-and-core-web-vitals`, and `cross-platform-design-parity`. Standards: WCAG 2.2
AA (`doctrine/references/wcag-2.2-criteria.md`); web.dev Core Web Vitals
(`doctrine/references/web-performance-budgets-2026.md`); Apple HIG; Material 3 Expressive; the
Chwezi Anti-Slop Charter (`doctrine/design-doctrine.md`). NNG heuristic evaluation for structure.*
