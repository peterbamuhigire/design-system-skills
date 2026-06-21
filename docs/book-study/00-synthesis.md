# Book Study — Synthesis & Plan Deltas

Consolidates the 6 critical studies (`01`–`06`) of `Downloads\uiux_markdown` (20 books) into the
net changes to the engine and plan. The engine is **53 skills / 14 groups**; Phase 0 + Phase 1 +
examples backfill + `product-design-audit` are DONE. This synthesis drives the rewritten plan
(`docs/plans/hardening-june/PLAN-v2-book-informed.md`).

## The single biggest idea (file 04)
Kocienda's **"creative selection"** (demo → feedback → next demo; concrete decisions over
abstractions; *live on it*; the "41 shades of blue" = a taste decision wrongly outsourced to a
metric) is our **sourcing-authority asymmetry expressed as process**. → New doctrine reference
`creative-selection-and-taste.md` (highest leverage, do first).

## NEW skills the books justify (beyond/refining the gap list)
| Skill | Group | Source | Priority |
|---|---|---|---|
| `ux-remediation-and-redesign` (diagnose→triage→redesign→re-validate→measure) | 00 | Fixing Bad UX (Maioli) | **P1** (new; not in gap list) |
| `xlsx-and-financial-model-presentation` (DESIGN content only; defer formula/pivot mechanics to finance engine) | 13 | Advanced Excel | **P1** (build now) |
| `demo-driven-design-process` | 05 | Kocienda | P2 |
| `design-storytelling-and-case-studies` (fenced — narrative must never decorate slop) | 13/05 | Sandler + anthology | P2 |

## NEW doctrine references
- `creative-selection-and-taste.md` (Kocienda) — sharpens the Mission + `distinctive-by-design`.
- `interaction-anti-patterns.md` (Neil ch.11: Idiot Boxes, Forced Sign-Up, etc.) → cited by group 00 audits.

## CHANGE existing skills (with book-sourced content)
- `design-audit` — add a **triage step** (red-route × effort-impact × MoSCoW) + a bad-UX pattern-catalogue reference + a worked fix (Maioli).
- `figma-and-tooling-workflow` (P1) — rewrite to **current Figma** (variables, dev-mode); the books' Axure/Sketch/XD is stale.
- `ux-writing-and-microcopy` — adopt Podmajersky's `{}`/`[]` pattern notation, the editing curve, "concise ≠ short", title↔CTA continuity.
- `error-empty-and-system-messaging` — add Podmajersky's **Inline/Detour/Blocking** error taxonomy + Ben-David's 3-part empty-state + inclusive-language bans.
- `voice-tone-and-content-style-guide` (P1) — carry the **Voice Chart + Voice Guide + Tone Map**; add a boundary guard deferring textual-AI-slop detection to the digital-research engine.
- `content-modeling-and-information-design` (P2) — **rescope** to `content-structure-and-readability` (plain-language anchored).
- `logo-and-wordmark-design` (P1) — add Janoff's **interactive wit / small surprise** + **mark-encodes-the-USP**.
- `docx-report-and-document-formatting` — small add: mirror-margins/gutter, Even/Odd section breaks, Building Blocks.
- `component-states-and-interaction-fidelity` (P1) — supply Book 3's per-component anatomy numbers + state lists.

## HARDEN (Phase-2 P1 items CONFIRMED + given book content)
`touch-gesture-and-haptics`, `micro-interactions-and-feedback`, `onboarding-and-first-run-design`,
`composition-and-visual-hierarchy`, `journey-mapping-and-service-design`,
`heuristic-evaluation-and-design-critique`, `design-critique-and-review-facilitation`,
`wireframing-and-prototyping` — all confirmed; extract worked content from the relevant studies' tables.

## EXCLUDE / DON'T BUILD
- **Niehaus "Robotics for Writers"** — misfiled (a fiction-writers' ChatGPT guide); irrelevant.
- A generic "rich-interaction" skill — REDUNDANT (covered by interaction-design-patterns + motion + states).
- Anything sourced from Janoff or the anthology *alone* (memoir, not method).
- `conversation-and-agent-content-design` — justified but DEFERRED; never source from the misfiled book.

## INOCULATE (counter-doctrinal claims in the books — add explicit "do NOT adopt" notes where relevant)
- Glassmorphism-as-best-practice (Fundamentals book) — contradicts the anti-slop charter.
- Red/blue fixed semantics + shadow-only dark elevation (Mobile Pattern Gallery) — we use OKLCH roles + lightness elevation.
- `ease-*-back` bounce interpolators (App Design Apprentice) — contradict `motion-design`'s ζ≥0.7 bounce ban.

## Net effect on the plan
Most of the current Phase-2 P1 list is **CONFIRMED** and now has *sourced worked content*; **+2 new
P1 skills** (`ux-remediation-and-redesign`, `xlsx-...`), **+1 doctrine ref to do first**
(`creative-selection-and-taste.md`), several **CHANGE** rewrites, **2 P2 additions**
(`demo-driven-design-process`, `design-storytelling-and-case-studies`), and one **rescope**. No
book makes a *done* skill redundant. See the v2 plan.
