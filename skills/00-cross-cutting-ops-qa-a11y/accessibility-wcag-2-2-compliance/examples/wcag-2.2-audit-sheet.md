# Worked Example — WCAG 2.2 AA Audit Sheet (FILLED)

**Component audited:** "Edit profile" **modal dialog** containing a form (Name, Email,
Avatar reorder list, Save / Cancel). Web, React.
**Conformance target:** AA (the Chwezi floor). **Date:** 2026-06-21. **Auditor:** design-qa.
**Tools:** axe-core 4.x + Lighthouse (automated); manual keyboard (mouse unplugged);
NVDA + Firefox (Win) and VoiceOver + Safari (mac); zoom/target-size spot checks.

Legend: **Pass** / **Fail** / **N/A**. Every Fail on an AA criterion blocks ship until fixed.
Criteria sourced from [`doctrine/references/wcag-2.2-criteria.md`](../../../../doctrine/references/wcag-2.2-criteria.md).

---

## The 9 new WCAG 2.2 criteria

| Criterion | Level | Result | Evidence | Fix |
|---|---|---|---|---|
| 2.4.11 Focus Not Obscured (Min) | AA | **Fail** | Tabbing to the Email field scrolled it under the sticky dialog header; ~12px of the field hidden. | Add `scroll-margin-top: 64px` to focusable fields = sticky header height. **Fixed → Pass.** |
| 2.4.12 Focus Not Obscured (Enhanced) | AAA | N/A | AAA, not in AA scope; noted as reach goal after the 2.4.11 fix. | — |
| 2.4.13 Focus Appearance | AAA | N/A | AAA reach; current ring is 2px @ 3.4:1, would need larger area for AAA. | — |
| 2.5.7 Dragging Movements | AA | **Fail** | Avatar list reordered by drag only; no keyboard or button path. | Add ↑/↓ "Move up / Move down" buttons per row (single-pointer + keyboard). **Fixed → Pass.** |
| 2.5.8 Target Size (Min) | AA | **Fail** | Close "×" was 18×18px; the new reorder arrows were 16×16px and adjacent. | Enlarge to 24×24px min (used 44×44 touch targets per HIG). **Fixed → Pass.** |
| 3.2.6 Consistent Help | A | Pass | Dialog has no help mechanism; the app's persistent "Help" link keeps its position site-wide. | — |
| 3.3.7 Redundant Entry | A | **Fail** | Email field was blank though the user's email is already known from the account. | Prefill from profile; allow edit. **Fixed → Pass.** |
| 3.3.8 Accessible Authentication (Min) | AA | N/A | No authentication step in this dialog. | — |
| 3.3.9 Accessible Authentication (Enhanced) | AAA | N/A | No auth step. | — |

---

## Perennial AA checklist (carried from 2.1)

| Area | Criterion | Result | Evidence | Fix |
|---|---|---|---|---|
| Contrast — body | 1.4.3 | Pass | Body 16px on #FFF at 7.1:1 (verified WCAG ratio after designing in APCA). | — |
| Contrast — UI/graphic | 1.4.11 | **Fail** | Input borders #D9D9D9 on #FFF = 1.3:1 (< 3:1); focus ring 3.4:1 OK. | Darken default border to #767676 (4.5:1). Owned by `accessible-color-and-contrast`. **Fixed → Pass.** |
| Keyboard operable | 2.1.1 | Pass (after 2.5.7 fix) | All controls operable by keyboard once reorder buttons added. | — |
| No keyboard trap | 2.1.2 | Pass | Focus trapped inside modal by design; Esc and Cancel release and return focus to trigger. | — |
| Focus order | 2.4.3 | Pass | DOM order = Name → Email → reorder list → Cancel → Save; matches visual order. | — |
| Focus visible | 2.4.7 | Pass | `:focus-visible` 2px ring, offset 2px, ≥3:1 on the dialog's light + the avatar's dark thumbnails. | — |
| Name/Role/Value | 4.1.2 | **Fail** | Close "×" button and avatar drag handles had **no accessible name** (NVDA announced "button"). | `aria-label="Close dialog"`; reorder buttons `aria-label="Move <name> up/down"`. **Fixed → Pass.** |
| Non-text content | 1.1.1 | Pass | Avatar thumbnails have `alt="Profile photo of <name>"`; decorative icons `aria-hidden`. | — |
| Reflow / resize | 1.4.10, 1.4.4 | Pass | Dialog reflows to single column at 320px; usable at 200% zoom, no horizontal scroll. | — |
| Motion | 2.3.1, 2.3.3 | Pass | Open/close transition respects `prefers-reduced-motion`; nothing flashes. | — |
| Forms — labels | 3.3.2 | Pass | Each field has a programmatic `<label for>`; required marked in label + `aria-required`. | — |
| Forms — error ID | 3.3.1 | **Fail** | Invalid email showed a red border only — no text, not announced. | Add error text tied via `aria-describedby` + `aria-invalid="true"`; surface in a polite live region. **Fixed → Pass.** |

---

## Dialog-specific structural checks

| Check | Result | Evidence | Fix |
|---|---|---|---|
| `role="dialog"` + `aria-modal="true"` | Pass | Present on container. | — |
| Named by title (`aria-labelledby`) | Pass | Points at the "Edit profile" `<h2 id>`; NVDA reads the title on open. | — |
| Focus moved in on open | Pass | Focus lands on the Name field on open. | — |
| Background inert | **Fail** | Page behind remained Tab-reachable. | Apply `inert` / `aria-hidden` to the app root while open. **Fixed → Pass.** |
| Focus returned on close | Pass | Esc/Cancel/Save return focus to the "Edit profile" trigger button. | — |

---

## Automated vs manual (why manual mattered)

- **axe + Lighthouse:** flagged the contrast border (1.4.11) and one missing label — ~30–40% of
  the real defects, consistent with `wcag-2.2-criteria.md` §testing.
- **Manual keyboard** caught: focus obscured by sticky header (2.4.11), drag-only reorder
  (2.5.7), undersized targets (2.5.8), background not inert.
- **Screen reader (NVDA/VoiceOver)** caught: unnamed Close/reorder buttons (4.1.2) and the
  silent email error (3.3.1).

## Verdict
**13 AA-relevant criteria applicable; 8 initial Fails, all remediated; AAA items deferred as
reach goals.** After fixes: **all AA criteria Pass → cleared for ship.** Hand this sheet to
`design-qa-and-pre-launch-review` as the accessibility gate evidence.
