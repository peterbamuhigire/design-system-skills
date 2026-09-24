# Reference: Perceived Performance for Streaming AI and Navigations

Parent skill: `../SKILL.md`. Load when a surface streams AI output (chat, drafting, generated tables or components) or when the design must decide how moving between pages feels (instant next page, back button, route transitions). Canonical Core Web Vitals thresholds stay in `doctrine/references/web-performance-budgets-2026.md`; this file adds design decisions for experiences that do not end at page load. Engineering implementation (workers, speculation rules, bfcache fixes) is handed to the engineering catalogue's `frontend-performance` skill.

## Inputs

| Input | Supplied by | If missing |
|---|---|---|
| Surface type: streaming answer, streaming UI, feed, multi-page flow | Product brief | Ask; the patterns differ |
| Typical response length and structure (prose, code, table, cards) | Product and AI lead | Design for the long case and the short case |
| Latency evidence (first token, stalls) | Performance owner | Mark timing assumptions `NOT_ASSESSED` on the spec |

## Streaming AI surfaces: design decisions

| Moment | Design decision | Wrong choice and its failure |
|---|---|---|
| Prompt submitted | Acknowledge within one frame: the prompt moves into the transcript, the input clears or locks, a response container appears in its final position | Nothing changes until the first token; users resubmit |
| Waiting for first content | Show a quiet, shaped placeholder (the outline of the answer area) and, for retrieval features, the sources as they are found | A bouncing-dots spinner with no information; preamble text that pretends to be content |
| Content streaming | Grow the container downward only; keep the reader's position stable; pause auto-scroll the moment the user scrolls up and offer a "jump to latest" control | Auto-scroll fights the reader; content above the viewport grows and shifts what they are reading (CLS) |
| Structured output (tables, code, cards) | Reveal in whole semantic units (row, line, card) with the frame sized before it fills | Half-rendered markdown and tables that reflow on every token |
| Long answer | Emit the outline or first heading early, then fill sections | A wall of text that is only useful at the end |
| During the stream | Keep a visible, always-responsive Stop control; allow copying and reading partial output | Controls disabled until completion; stop that takes seconds to respond |
| Stall or failure | After a short visible stall, state what is happening; on failure keep partial output, label it incomplete, offer retry | Frozen caret; error replaces everything the user already read |
| Screen readers | Announce start and completion politely, not every token; keep focus on the input unless the user moves it | Live region that reads the stream token by token |

Design targets to put on the spec (starting points; engineering confirms feasibility and measures them): first visible acknowledgement within one frame of submit, first content within about 1 second on a cold request, no visible pause longer than about 200 ms in a healthy stream, and page INP within the canonical budget while streaming.

## Navigation feel

| Situation | Design decision | Wrong choice |
|---|---|---|
| Likely next page is predictable (listing to detail) | Design the destination so it can be prepared ahead: no side effects on view, no one-time animations that break when the page was pre-rendered | Destination pages that count views or start timers on load, which makes prerendering unsafe and forces engineering to disable it |
| Back navigation | Design pages to restore exactly: scroll position, filters, expanded items, and entered form data survive back and forward | Pages that reset on return, making users redo work |
| Route transition in a single-page app | Use a short, purposeful transition (shared element or cross-fade) that occupies the fetch time; honour reduced motion | Long decorative transitions that delay the user's next input |
| Slow route | Skeleton of the destination's real layout at the destination position | Full-screen blocking loader that hides where the user is going |

## Review checklist

- The streaming container has a defined initial size and a growth direction on the spec.
- Every streaming state (acknowledged, waiting, streaming, stalled, stopped, failed, complete) exists as a designed frame with copy.
- The Stop control is present and reachable by keyboard and screen reader during the entire stream.
- Auto-scroll behaviour and the "jump to latest" affordance are specified.
- Destination pages have no view-time side effects in the design, and back-navigation restore behaviour is specified.

## Premium versus generic

Generic AI chat design: three animated dots, text that pours in and drags the page, a disabled input, and a single "Something went wrong" state. Premium: the answer area appears in place immediately, sources arrive first, prose grows without moving what the reader is on, stop works instantly, partial answers survive failure, and returning to the conversation finds it exactly as it was left.

## Worked example (original)

A Kampala insurer's claims assistant answers policy questions in English and Luganda. The design reserves an answer card under the question on submit, shows the matched policy clauses as chips within the first second, then streams the explanation. The claims table inside the answer reveals row by row inside a pre-sized frame. If the network drops on a busy mobile connection, the card keeps the partial answer, marks it "Incomplete — tap to continue", and the Stop control never leaves the viewport.

## Evidence and currentness

Accessed 2026-09-24: Core Web Vitals thresholds unchanged (web.dev *Web Vitals*, LCP 2.5 s, INP 200 ms, CLS 0.1 at p75); Speculation Rules prerendering is Chromium-only with Safari behind a flag (developer.chrome.com, updated 2026-01-23); bfcache restoration guidance per web.dev *bfcache* (updated 2026-07-02). Streaming timing targets are practitioner starting points, not standards; device render and screen-reader proof are `NOT_ASSESSED` until performed.

Sources: Osmani (2026) *Web Performance Engineering in the Age of AI*; web.dev and developer.chrome.com documentation above; this engine's `ai-agent-ux` references.
