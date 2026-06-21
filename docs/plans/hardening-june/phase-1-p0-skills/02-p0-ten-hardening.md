# Phase 1 — P0-Ten Hardening (existing skills)

The ten existing skills whose hardening gives the biggest jump (per
`docs/initial-analysis/07-hardening-existing-skills.md`). Each gets named `references/*` +
`examples/*` and a 2026-standards injection. This is what moves the engine ~70 → ~85.

| Skill (new group) | Add `references/*` | Add `examples/*` | 2026 standards to inject |
|---|---|---|---|
| **color-system-and-palette** (02) | `oklch-ramp-construction.md`, `semantic-color-roles.md` | `oklch-palette-worked.md` (a full applied ramp, light+dark) | Operationalize **OKLCH**; APCA design / WCAG certify; dark-mode roles |
| **font-selection-and-pairing** (01) | `type-scale-recipes.md`, `pairing-catalog.md` | `applied-type-scale.md` (px/rem scale for a real brief) | Variable-font axes; fluid `clamp()` scale |
| **layout-grid-and-spacing** (03) | `grid-systems-catalog.md`, `spacing-rhythm.md` | `grid-template-worked.md` (a real 12-col + 8pt applied) | Container queries; intrinsic layout |
| **design-audit** (00) | `audit-rubric.md` (composes slop+a11y+perf gates) | `design-audit-filled.md` (a real scored audit) | WCAG 2.2 + Core Web Vitals checks |
| **ios-ui-ux-design** (07) | `hig-liquid-glass.md`, `ios-sensory-and-haptics.md` | `ios-screen-spec.md` (a worked screen) | **Liquid Glass**, SF Symbols, Dynamic Type, haptics |
| **android-ui-ux-design** (07) | `material-3-expressive.md`, `android-motion.md` | `android-screen-spec.md` | **Material 3 Expressive**, dynamic color, predictive back |
| **data-visualization** (12) | `chart-encoding.md`, `dashboard-patterns.md` | `chart-worked-examples.md` (good/bad encodings) | Perceptual encoding; accessible charts |
| **visual-product-slop-audit** (00) | (cites `ai-slop-taxonomy.md`) `visual-tells-checklist.md` | `slop-audit-filled.md` (a real before/after) | Current AI-image tells |
| **brand-visual-identity** (02) | `identity-system-spec.md`, (folds `brand-consistency-gate.md` from brand-alignment) | `identity-mini-guide.md` (a worked mini brand) | — |
| **motion-design** (08) | `spring-physics-and-easing.md`, `view-transitions.md`, `reduced-motion.md` | `micro-interaction-spec.md` | Spring physics, **View Transitions API**, `prefers-reduced-motion` |

## Process per skill
1. Read the skill; identify what's thin (usually: no examples, no `references/`, stale standards).
2. Author the named `references/*.md` (real frameworks/specs, not prose).
3. Author ≥1 `examples/*` (applied artifact — the convention from Phase 0.3).
4. Inject the 2026 standard with the specific criterion/threshold + cite the cross-cutting ref.
5. Tick the skill in `examples-backfill-tracker.md`.

## Acceptance
Each of the ten ships its listed references + ≥1 worked example; each names the injected
standard with a concrete value; the backfill tracker shows 10/10 for this set. **Effort: L (the bulk of Phase 1's value).**
