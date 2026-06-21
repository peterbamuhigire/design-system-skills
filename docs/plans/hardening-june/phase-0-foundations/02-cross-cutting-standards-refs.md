# Phase 0.2 — Two Cross-Cutting 2026-Standards References

Source content: `docs/initial-analysis/06-2026-standards-benchmark.md`. These two files become the
single source the whole engine cites for accessibility and performance, so no skill re-states
(or drifts on) the numbers.

## A. `doctrine/references/wcag-2.2-criteria.md`
**Outline:**
1. **Conformance model** — A / AA / AAA; what "AA is the floor for Chwezi work" means.
2. **The 9 new 2.2 success criteria** (the deltas vs 2.1), each as a one-line checkable rule:
   2.4.11 Focus Not Obscured (Min), 2.4.12 Focus Not Obscured (Enhanced), 2.4.13 Focus Appearance,
   2.5.7 Dragging Movements, 2.5.8 Target Size (Minimum, **24×24 CSS px**), 3.2.6 Consistent Help,
   3.3.7 Redundant Entry, 3.3.8 Accessible Authentication (Min), 3.3.9 Accessible Auth (Enhanced).
3. **Perennial AA checklist** grouped Perceivable/Operable/Understandable/Robust — contrast
   (**4.5:1** text, **3:1** large/UI), focus order, keyboard, name/role/value, etc.
4. **Contrast method note** — WCAG 2.x ratio is the conformance test; **APCA** (WCAG 3 draft) is
   the better perceptual tool — use APCA to design, WCAG ratio to certify. (Mark WCAG 3 as draft.)
5. **Testing** — axe/Lighthouse + manual keyboard + screen-reader smoke test.
> Every number carries the primary source already cited in `06-2026-standards-benchmark.md` (W3C, WebAIM).

## B. `doctrine/references/web-performance-budgets-2026.md`
**Outline:**
1. **Core Web Vitals "good" thresholds** — LCP **≤ 2.5 s**, INP **≤ 200 ms**, CLS **≤ 0.1**
   (field/p75). Cite web.dev.
2. **Asset budgets** — JS, CSS, image, font weight budgets per page archetype; total-byte target.
3. **Font perf** — `font-display: swap`, subsetting, variable-font single-file, preload critical.
4. **Image perf** — modern formats (AVIF/WebP), responsive `srcset`, lazy-load below fold, dimensions to avoid CLS.
5. **Perceived performance** — skeletons, optimistic UI, transition masking (links to state-design + motion).
6. **Budget enforcement** — Lighthouse CI thresholds as the gate.

## Citation wiring (which skills must cite these)
- **wcag-2.2-criteria.md** ← cited by: `accessible-color-and-contrast`, `accessibility-wcag-2-2-compliance`, every `*-ui-design`/`webapp-gui-design`/forms/states skill, `design-qa-and-pre-launch-review`, both mobile skills, `design-audit`.
- **web-performance-budgets-2026.md** ← cited by: `performance-as-ux-and-core-web-vitals`, `responsive-and-adaptive-layout`, `font-embedding-and-licensing`, `photography-art-direction`, `motion-and-micro-interactions`, `webapp-gui-design`, `visual-qa`-style audits.

## Acceptance
Both files exist, every number is sourced, and the listed skills add a one-line `## References`
pointer. **Effort: M.**
