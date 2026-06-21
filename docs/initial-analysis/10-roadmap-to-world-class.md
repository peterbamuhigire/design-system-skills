# Roadmap to World-Class (51 → 90+)

Sequenced so each phase is shippable and the score moves visibly. Sources: `02` (taxonomy),
`04` (68 new skills), `07` (hardening), `08` (reading list), `06` (2026 standards).

---

## Phase 0 — Foundations that unblock everything (→ ~62)

1. **Adopt the 13-group taxonomy** (`02-coverage-and-taxonomy.md`). Every existing skill migrates;
   none deleted. Fixes the `02`-has-no-docs and `03`-grab-bag problems and creates homes for
   accessibility, design-systems/tokens, motion, content/UX-writing, imagery, design-ops.
2. **Two engine-wide cross-cutting references**, cited by every relevant skill:
   `doctrine/references/wcag-2.2-criteria.md` (the numbered criteria as a checklist) and
   `doctrine/references/web-performance-budgets-2026.md` (Core Web Vitals thresholds + budgets).
3. **Enforce the `examples/` convention** — add it to `CONTRIBUTING.md` and the `_TEMPLATE`:
   every craft skill ships ≥1 worked example. This alone lifts the lowest dimension (22).
4. **De-dupe**: merge the 8 deck skills into one `_deck-system/` with per-deck-type variants;
   consolidate the 5 overlapping colour/brand skills.

## Phase 1 — The ~24 P0 skills (→ ~70, then ~85 as they harden)

Add the must-haves from `04-gap-analysis-new-skills.md` (priority order):
- **Documents**: a real `docx-pdf-document-design` skill (render, embed, subset) — fixes the
  30/100 document gap.
- **Production**: `design-tokens-and-theming`, `design-handoff-and-figma-to-dev` — fixes the 34.
- **Accessibility**: `wcag-2.2-compliance`, `accessible-components` — fixes the 28.
- **Motion**: `motion-and-micro-interactions` (spring physics, View Transitions, reduced-motion).
- **Mobile**: harden `ios-ui-ux-design` (Liquid Glass, sensory/haptics) & `android-ui-ux-design`
  (Material 3 Expressive); add `react-native-flutter-design` — fixes the 22.
- **Web**: `responsive-and-adaptive-design` (container queries, fluid type), `core-web-vitals-ux`.
- **Content**: `ux-writing-and-content-design`; **Forms**: keep + harden; **States**:
  `onboarding-empty-error-states`.

## Phase 2 — The P1 wave (→ ~85)

Iconography, imagery/art-direction (incl. AI-image direction), prototyping, UX research/usability,
dashboards/data-products, editorial/long-form, i18n/RTL, dark-mode, email design, trust/conversion,
design-QA/critique, pitch-deck/proposal craft (the real document side of `02`).

## Phase 3 — Ceiling & ongoing (→ 90+)

P2 items (3D/WebGL, conversational/voice UI, design ethics, green/sustainable UX), then continuous
hardening: extract the **Tier-1 reading list** (`08`) into the deepest skills' `references/` and
`examples/`, and keep the 2026-standards refs current.

---

## Worked-examples mandate (the cheapest big win)
Per `07-hardening-existing-skills.md`, the P0 ten to harden first:
`color-system-and-palette`, `font-selection-and-pairing`, `layout-grid-and-spacing`,
`design-audit`, `ios-ui-ux-design`, `android-ui-ux-design`, `data-visualization`,
`visual-product-slop-audit`, `brand-visual-identity`, `motion-design` — each gets named
`references/*.md` + `examples/*`.

## Counting to the ceiling
37 now → +~24 P0 ≈ **61** → full P1 ≈ **85 skills** → P2 ceiling ≈ **105**. Deferring P2 lands us
at ~85 skills, inside the 75–100 target, with all P0 must-haves shipped first.
