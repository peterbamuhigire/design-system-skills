# B11-A04 — Intentional omission review

Status: IMPLEMENTED DESIGN GOVERNANCE PACK. This record evaluates what a
design deliberately leaves out; it does not certify usability without the
required render, interaction, accessibility, and reviewer evidence.

## Review record

| Field | Required entry |
|---|---|
| Product/surface | Named product, screen, component, or document |
| Audience and task | Who is acting, what they need to accomplish, and consequence of error |
| Omission | Exact element, state, control, copy, decoration, or motion omitted |
| Reason | Task focus, cognitive load, performance, privacy, safety, or system constraint |
| Alternative | How the same need remains available, if it remains in scope |
| Evidence | Brief, user/reviewer observation, render, interaction trace, or source |
| Accessibility impact | Keyboard, screen-reader, zoom/reflow, target-size, contrast, motion, and language effects |
| Risk/owner | Severity, affected users, accountable owner, due/review date |
| Decision | Keep omission / restore / narrow / `NOT_ASSESSED` |

An omission is intentional only when the job, affected state, and recovery path
are explicit. “Cleaner” or “more premium” is a taste statement and is not
sufficient evidence by itself.

## Review questions

1. Does the omission remove a duplicate, decoration, or competing signal while
   keeping the primary task legible?
2. Does it remove a required action, status, error, disclosure, text alternative,
   focus target, or recovery route? If yes, restore it or block the decision.
3. Can a keyboard user, screen-reader user, low-vision user, touch user, and
   reduced-motion user still complete the named task?
4. Does the omission affect privacy, consent, AI uncertainty, provenance, or
   correction? If yes, record the replacement control and reviewer.
5. Is the omitted element absent in every state, or only in a specified normal
   state? Check loading, empty, error, success, offline, and recovery states.

## Decision examples

| Candidate omission | Safe disposition | Evidence required |
|---|---|---|
| Decorative gradient behind a data table | Keep omitted | Grayscale/readability inspection; no semantic loss |
| Visible label replaced by an icon-only control | Reject unless accessible name and equivalent text are proven | Render plus keyboard and assistive-technology evidence |
| Advanced filters hidden behind a labelled disclosure | Keep with review | Task test, focus order, empty/error state, and discoverability evidence |
| Error detail removed to shorten copy | Reject or narrow | Error recovery, cause/action text, and content review |

## Acceptance and failure path

Accept only when the record names the user job, replacement/recovery path,
affected accessibility criteria, owner, and evidence. If the surface is not
rendered or interaction-tested, mark the visual and behavioural decision
`NOT_ASSESSED`; do not convert the omission into a standard. A reviewer may
restore the element or define a bounded experiment with a stop/rollback trigger.

