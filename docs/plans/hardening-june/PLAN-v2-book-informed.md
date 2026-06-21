# Hardening Plan v2 — Book-Informed (supersedes the Phase 2/3 specs)

This rewrites the remaining plan after the critical study of `Downloads\uiux_markdown` (20 books;
see `docs/book-study/00-synthesis.md`). It **removes everything now covered** and reframes the rest.
The original `phase-0/` and `phase-1/` folders are retained as a historical record; this doc is the
live plan for what remains.

## DONE — strike from all P0/P1 lists (do not re-plan)
- **Phase 0** (14-group taxonomy, standards refs, examples convention, decks/brand de-dup).
- **Phase 1** (all 23 P0 skills + the P0-ten hardening).
- **Examples backfill** — all 52 skills ship a worked example.
- **`product-design-audit`** skill (multi-platform product audit, skill-routed recs).
- **8-category intent-based font taxonomy** (folders + MANIFESTs + doctrine reconciled).
- Engine is **53 skills / 14 groups**; post-Phase-1 re-audit ~67/100 (will rise with examples now done).

---

## TRACK A — Doctrine first (highest leverage, do before the skills)
1. **`doctrine/references/creative-selection-and-taste.md`** (Kocienda). The Mission's missing
   *production method*: demo → feedback → next-demo loop; concrete decisions over abstractions;
   "live on it"; the "41 shades of blue" = sourcing-authority asymmetry on the process side.
   Cite from `distinctive-by-design`, the critique/process skills, and `product-design-audit`.
2. **`doctrine/references/interaction-anti-patterns.md`** (Neil ch.11 + Maioli). The bad-UX/
   anti-pattern catalogue (Idiot Boxes, Forced Sign-Up, dead-ends, etc.). Cited by group-00 audits.
3. **Inoculation notes** — add explicit "do NOT adopt" lines to the relevant skills:
   glassmorphism-as-best-practice, fixed red/blue semantics + shadow-only dark elevation, and
   `ease-*-back` bounce (contradicts `motion-design` ζ≥0.7). Source: studies 01/02.

## TRACK B — New skills the books justify
| Skill | Group | Pri | Source / content |
|---|---|---|---|
| `ux-remediation-and-redesign` | 00 | **P1** | Maioli: diagnose→triage→redesign→re-validate→measure; triage matrix (red-route×effort-impact×MoSCoW). Composes `design-audit`→fix→re-validate→`design-qa`. |
| `xlsx-and-financial-model-presentation` | 13 | **P1** | Advanced Excel: number-formatting, conditional-formatting-as-encoding, table/cell styles, chart styling, print exhibits, blue-input/black-formula convention. **DESIGN content only — defer formula/pivot/model calc to the finance engine.** |
| `demo-driven-design-process` | 05 | P2 | Kocienda: the working-demo discipline; non-goals/fidelity ring; algorithm-vs-heuristic lens. |
| `design-storytelling-and-case-studies` | 13 (or 05) | P2 | Sandler frameworks (Freytag, Three-Act, Pixar, Kishōtenketsu, Peak-End), **fenced**: narrative serves the authored artifact, never replaces the demo or decorates slop. |

## TRACK C — CHANGE / harden existing skills (with book-sourced content)
- **`design-audit`** — add a **triage step** + cite the new anti-patterns ref + a worked fix (Maioli).
- **`figma-and-tooling-workflow`** (P1, group 09) — author it to **current Figma** (variables, dev-mode), not the books' Axure/Sketch/XD.
- **`ux-writing-and-microcopy`** — Podmajersky `{}`/`[]` notation, the editing curve, "concise ≠ short", title↔CTA continuity.
- **`error-empty-and-system-messaging`** — Podmajersky **Inline/Detour/Blocking** error taxonomy + Ben-David 3-part empty-state + inclusive-language bans.
- **`voice-tone-and-content-style-guide`** (P1, group 10) — carry the **Voice Chart + Voice Guide + Tone Map**; boundary-guard textual-AI-slop to the research engine. *(Re-point `ux-writing-and-microcopy`'s voice routing here once it ships.)*
- **`logo-and-wordmark-design`** (P1, group 02) — add Janoff's **interactive wit / small surprise** + **mark-encodes-the-USP**.
- **`docx-report-and-document-formatting`** — small add: mirror-margins/gutter, Even/Odd section breaks, Building Blocks.
- **`component-states-and-interaction-fidelity`** (P1, group 04) — Book 3 per-component anatomy numbers + state lists.
- **`content-modeling-and-information-design`** (P2) — **rescope** to `content-structure-and-readability` (plain-language anchored).

## TRACK D — Remaining Phase-2 P1 (CONFIRMED by the books; now have sourced worked content)
From `phase-2-p1-wave/01-skill-specs.md`, these stand and gain book content (see each study's
extract-into table): `touch-gesture-and-haptics`, `micro-interactions-and-feedback`,
`onboarding-and-first-run-design`, `trust-credibility-and-social-proof`,
`composition-and-visual-hierarchy`, `editorial-and-long-form-layout`,
`journey-mapping-and-service-design`, `heuristic-evaluation-and-design-critique`,
`design-critique-and-review-facilitation`, `fintech-and-financial-product-ui`,
`ecommerce-and-checkout-ux`, `app-store-presence-and-aso`, `variable-fonts-and-opentype-features`,
`fluid-responsive-typography`, `illustration-style-and-systems`, `ai-image-generation-art-direction`,
`chart-selection-and-encoding`, `email-and-newsletter-design`, `inclusive-and-assistive-design`,
`design-ethics-and-anti-dark-patterns`, `figma-and-tooling-workflow`.

## TRACK E — EXCLUDE / DON'T BUILD
- **Niehaus "Robotics for Writers"** — misfiled, irrelevant.
- A generic "rich-interaction" skill — redundant.
- Skills sourced from Janoff/anthology alone — memoir, not method.
- `conversation-and-agent-content-design` — DEFER; never source from the misfiled book.

---

## Recommended execution order
1. **Track A** (2 doctrine refs + inoculation notes) — cheap, high-leverage, cited by everything.
2. **Track B P1** (`ux-remediation-and-redesign`, `xlsx-...`) + **Track C** changes.
3. **Track D** P1 wave (parallel-agent authoring, each briefed with its study's extract-into rows).
4. **Track B P2** (`demo-driven-design-process`, `design-storytelling-and-case-studies`) + remaining P2.
5. Fresh **re-audit** (`skill-engine-audit`) — target ~80.

Count check: 53 now + ~4 new (Track B) + the Track-D P1 wave (~20) ≈ **75–80 skills**, inside target.
