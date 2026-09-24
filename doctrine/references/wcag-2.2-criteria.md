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
- **Motion:** no content flashes more than 3 times per second (2.3.1, A); moving, blinking or
  auto-updating content that starts automatically and lasts over 5 s can be paused, stopped or
  hidden (2.2.2, A). Honouring `prefers-reduced-motion` / Reduce Motion for interaction-triggered
  animation is SC 2.3.3 (AAA) — a **Chwezi house floor**, not an AA conformance item; report it
  as such.
- **Text spacing and hover/focus content:** no loss when users override line, paragraph, letter
  and word spacing (1.4.12); tooltips and popovers are dismissible, hoverable and persistent (1.4.13).
- **Forms:** labels, error identification, suggestions, and prevention on important data (3.3.x).

## Contrast method note (design with a perceptual check, certify with WCAG 2.2)
The WCAG 2.x ratio is the **conformance** test (use it to certify). **APCA** is a useful
*perceptual* design-time check (it accounts for size, weight and polarity), but it is **not** part
of any W3C Recommendation, and the current WCAG 3.0 Working Draft (10 September 2026) does not name
APCA: its text-contrast requirement still reads "contrast measure to be determined". Use APCA only
as a design aid, never as a conformance claim, and never describe it as "the WCAG 3 method".

## Heuristic review versus measured conformance
Every accessibility statement in a Chwezi deliverable carries one of three evidence classes:

| Class | What it is | May claim |
|---|---|---|
| `HEURISTIC` | Expert judgement from designs, specs or screenshots (for example a design critique) | "Likely issue", "risk", "recommendation" — never "conforms" |
| `MEASURED` | A recorded test on the rendered or implemented artefact: tool output (axe, contrast analyser), manual keyboard traversal, screen-reader pass (VoiceOver, TalkBack, NVDA), zoom/reflow at 320 CSS px and 200% | Pass/fail for the named success criteria, surfaces and states that were tested |
| `NOT_ASSESSED` | No render, device, assistive-technology run or reviewer | Nothing; list it as an open gap that blocks a `PASS` verdict |

A WCAG conformance claim requires `MEASURED` evidence for every applicable success criterion on
the full page or process, including all states. Automated scanners find only a subset of
failures, so an automated pass alone is never a conformance claim.

## Testing
Automated tools (axe, Lighthouse) find only part of the failures (commonly quoted at roughly a
third; treat the figure as indicative, not measured); always add **manual keyboard** traversal and
a **screen-reader smoke test** (VoiceOver / TalkBack / NVDA). WebAIM Million 2026 (February 2026
crawl) found detectable WCAG 2 failures on 95.9% of home pages, averaging 56.1 errors per page —
passing this checklist is a real differentiator.

## Evidence/currentness (accessed 2026-09-24)
- W3C WAI, *WCAG 2 Overview* (w3.org/WAI/standards-guidelines/wcag/): WCAG 2.2 published
  5 October 2023, updated 12 December 2024; approved as ISO/IEC 40500:2025. SC 4.1.1 Parsing is
  obsolete in 2.2. Status: verified.
- W3C, *WCAG 3.0* Working Draft 10 September 2026 (w3.org/TR/wcag-3.0/): draft, not for
  conformance; text contrast measure "to be determined". Status: verified. Re-check at each
  Kaizen cycle.
- WebAIM, *The WebAIM Million* 2026 (webaim.org/projects/million/). Status: verified.
- Automated-coverage fraction ("about a third"): `NOT_ASSESSED` against a primary study.
