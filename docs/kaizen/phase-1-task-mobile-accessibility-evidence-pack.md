# B21-A03 — Task, mobile, and accessibility evidence pack

Status: IMPLEMENTED EVIDENCE PACK. It is a reusable handoff schema; this
repository does not claim a passing product audit without a real build, render,
device, keyboard, and assistive-technology run.

## Task and surface contract

| Field | Required entry |
|---|---|
| Task ID and audience | One observable task, audience, stakes, and success measure |
| Surface/platform | Web, iOS, Android, responsive document, or other target |
| Content slice | Real or explicitly fictional content, language, and data state |
| State matrix | Normal, loading, empty, error, recovery, offline, permission, reduced motion |
| Viewports/devices | Width, height, density, orientation, Dynamic Type/zoom setting |
| Implementation owner | Component/token/source owner and handoff version |
| Reviewer route | Design reviewer, accessibility reviewer, product owner, decision date |

## Mobile evidence checklist

- Capture narrow and wide layouts with the same content and state.
- Confirm the primary action remains reachable, labelled, and visible at the
  intended touch size; record any sticky or obscuring chrome.
- Verify content reflows at 320 CSS px and 200% zoom; identify intrinsic 2D
  content such as a data table and provide an accessible alternative.
- Exercise keyboard/focus where a hardware keyboard is supported, and touch
  alternatives for drag, swipe, or gesture-only actions.
- Check orientation, safe-area/inset behaviour, text scaling, dark/high-contrast
  variants, and reduced-motion behaviour for the target platform.

## Accessibility evidence matrix

| Check | Evidence | Result |
|---|---|---|
| Accessible name, role, state | DOM/semantic tree or native inspector | PASS / FAIL / N/A / NOT_ASSESSED |
| Keyboard order and no trap | Recorded traversal; focus remains visible |  |
| Screen-reader output | NVDA/VoiceOver/TalkBack smoke path |  |
| Contrast and non-colour cue | Measured text/UI contrast and state labels |  |
| Target size | Measurement; minimum 24×24 CSS px, touch aim 44px/48dp |  |
| Error association and recovery | Field/state, message, correction route |  |
| Reflow and zoom | 320px and 200% captures/inspection |  |
| Motion | Reduced-motion setting and stop/pause behaviour |  |
| Authentication/help | Paste/password-manager path and consistent help order |  |

## Normal and failure paths

The normal path completes the named task with all controls announced, visible
focus, and a recorded render at each target width. Failure evidence must retain
the failing state and correction owner. Examples include an icon-only control
with no accessible name, a focus target hidden under sticky chrome, a 320px
layout that loses the submit action, a drag-only operation with no alternative,
or an error message not associated with its field. Any such failure blocks a
`PASS` decision until corrected and re-run.

## Evidence decision

Use `PASS` only when the same task, content, state, and evidence class has been
re-run after fixes. Use `CONDITIONAL` when structural records exist but a real
render, device, or assistive-technology check is pending. Use `BLOCKED` for an
applicable AA failure or missing recovery path. Use `NOT_ASSESSED` where the
target build or evidence tool is unavailable. A manifest with self-asserted
labels is not independent proof.

