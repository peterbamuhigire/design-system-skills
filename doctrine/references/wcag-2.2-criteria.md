# Reference: WCAG 2.2 Criteria (the accessibility floor)

The engine's accessibility baseline. **AA is the floor for all Chwezi work**; AAA where feasible.
Cited by every UI/colour/forms/states/mobile/QA skill. Source: W3C WCAG 2.2 Recommendation
(w3.org/TR/WCAG22/); contrast/method notes verified via the 2026 standards benchmark
(`docs/initial-analysis/06-2026-standards-benchmark.md`).

## The 9 new success criteria in 2.2 (deltas vs 2.1) — each a checkable rule
- **2.4.11 Focus Not Obscured (Minimum, AA)** — the focused element is not entirely hidden by
  author content (sticky headers/footers).
- **2.4.12 Focus Not Obscured (Enhanced, AAA)** — no part of the focused element is hidden.
- **2.4.13 Focus Appearance (AAA)** — focus indicator is large enough and high-contrast.
- **2.5.7 Dragging Movements (AA)** — any drag operation has a single-pointer (tap/click) alternative.
- **2.5.8 Target Size (Minimum, AA)** — pointer targets are at least **24×24 CSS px** (or have
  adequate spacing). *(Aim for 44×44 on touch per Apple HIG / 48dp per Material.)*
- **3.2.6 Consistent Help (A)** — help mechanisms appear in a consistent order across pages.
- **3.3.7 Redundant Entry (A)** — don't make users re-enter info already provided in the same process.
- **3.3.8 Accessible Authentication (Minimum, AA)** — no cognitive function test (e.g. solving a
  puzzle, remembering a password) without an alternative.
- **3.3.9 Accessible Authentication (Enhanced, AAA)** — stricter; no object-recognition either.

## Perennial AA checklist (carried from 2.1, must still pass)
- **Contrast:** body text **≥ 4.5:1**; large text (≥24px, or ≥18.66px bold) and UI components/
  graphical objects **≥ 3:1** (1.4.3, 1.4.11).
- **Keyboard:** everything operable by keyboard; visible focus order is logical (2.1.1, 2.4.3, 2.4.7).
- **Name/Role/Value:** all controls expose accessible name + role + state (4.1.2).
- **Non-text content:** meaningful images have alt text; decorative are hidden (1.1.1).
- **Reflow / resize:** usable at 320px width and 200% zoom without loss (1.4.10, 1.4.4).
- **Motion:** honour `prefers-reduced-motion`; no content flashes >3×/s (2.3.1, 2.3.3).
- **Forms:** labels, error identification, suggestions, and prevention on important data (3.3.x).

## Contrast method note (design with APCA, certify with WCAG)
The WCAG 2.x ratio is the **conformance** test (use it to certify). **APCA** (the algorithm in the
**WCAG 3.0 draft** — still draft, not normative) is the better *perceptual* tool — use it while
designing to judge real legibility, then verify against the 4.5:1 / 3:1 ratios for compliance.

## Testing
Automated (axe / Lighthouse) catches ~30–40%; always add **manual keyboard** traversal and a
**screen-reader smoke test** (VoiceOver / NVDA). Per WebAIM Million 2026, ~95.9% of home pages
still have detectable WCAG failures — passing this checklist is a real differentiator.
