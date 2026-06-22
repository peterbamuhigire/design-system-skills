# Reference: The State Matrix — every state a component needs

> A component is not "done" when its filled state looks good. It is done when **every state a
> real user can reach** has been deliberately designed. The default-filled mock is the *least*
> common thing a user sees. This file is the enumeration you run **before** designing any single
> state — owned by `empty-error-and-loading-states`. Cites
> `doctrine/references/web-performance-budgets-2026.md` and `wcag-2.2-criteria.md`.

---

## 1. The six top-level states (every component has these)

| State | What it is | Reachable when |
|---|---|---|
| **Ideal** | The designed-for, full, correct content. | Data present, action succeeded. |
| **Empty / Zero** | No content to show. | First run, user cleared all, filtered to nothing, or never any data. |
| **Partial** | Some content, some still missing/loading. | Pagination, streaming, lazy regions, mixed-success batch. |
| **Loading** | Fetching or processing; nothing actionable yet (or in-place). | Async fetch, submit, recompute. |
| **Error** | Something failed. | Network, server, validation, permission, not-found, offline, timeout. |
| **Success / Confirmation** | An action completed. | After create/save/delete/submit. |

If a state in this table can be reached for your component, you owe it a design. Enumerate first;
design second. **A state you didn't enumerate is a state you'll ship broken.**

---

## 2. Empty / Zero — the four distinct empties (different copy, different action)

Treat empty as an **opportunity**, never a void. Each sub-type needs a different design:

| Sub-type | Cause | Primary job of the state | Anti-slop note |
|---|---|---|---|
| **First-use (blank slate)** | New account, never had data. | **Onboard.** Explain the value in one line, show **one** primary CTA, optionally a real preview/sample. Your best activation moment. | Authored illustration or sample content — never a grey magnifying glass. |
| **User-cleared** | They deleted/archived everything. | Acknowledge intentionality; offer "Add new" + undo if recent. | Don't congratulate ("Inbox zero!") unless brand voice earns it. |
| **No-results (filter/search)** | Query/filter matched nothing. | **Help them recover the query.** Show the active filters, offer "Clear filters", suggest broader terms. Distinct from "no data exists". | Don't imply the feature is broken or empty forever. |
| **Error-as-empty** | A failed load rendered as "empty". | **This is a bug, not an empty state.** Detect failure and render the *error* state instead. | Silently showing "No data" on a 500 is the most insidious slop. |

**Design anatomy of a good empty state:** authored visual → one-line value/explanation → single
primary action (secondary optional) → never a dead end. Keep the keyboard focus landing on the
primary action.

---

## 3. Loading — choose by latency tier and region size

Loading design is a **perceived-performance** decision, not an honesty decision
(`web-performance-budgets-2026.md` §Perceived performance: *skeletons over spinners*).

### Latency tiers (when to show what)
| Perceived delay | What to show |
|---|---|
| **< ~100 ms** | **Nothing.** It feels instant. Showing a loader here causes a flash and feels *slower*. |
| **~100 ms – 1 s** | A skeleton or inline indicator, shown only *after* the perception threshold (so fast loads don't flash). For a content region: skeleton. For a button action: in-button spinner + disabled. |
| **1 s – 10 s** | Skeleton for content; **determinate progress** if you can estimate it (progress bar with %). Keep the layout stable. |
| **> 10 s** | Determinate progress + reassurance + the ability to background/cancel. Tell the user it's working and roughly how long. |

### Loading pattern by region
| Pattern | Use for | Rule |
|---|---|---|
| **Skeleton screen** | Content regions (cards, lists, tables, profile headers). | Skeleton geometry **must match** the real layout's boxes and sizes so there is **zero layout shift** when content arrives — this directly protects the **CLS ≤ 0.1** budget. Subtle shimmer/pulse; respect `prefers-reduced-motion` (WCAG 2.3.3) → fall back to a static dimmed block. |
| **Spinner** | Short, in-place, indeterminate actions (button submit, small inline refresh). | Never for full content regions or long loads. No layout preview, no CLS protection, feels slower. |
| **Progress bar** | Determinate operations (upload, multi-step processing). | Show real % when known; never fake a finishing jump that then stalls. |
| **Progressive / streaming** | Data that can arrive in parts (server-rendered streaming, paginated, AI token stream). | Reveal as it arrives; show the shell first, then fill. Best perceived performance when available. |
| **Optimistic UI** | High-confidence, low-risk writes (like, toggle, reorder). | Apply the change immediately, reconcile on response, **roll back visibly** on failure. Only when failure is rare and reversible. |

---

## 4. Error — match the UI to the blast radius

Every error state must: (a) be **scoped** to what actually failed, (b) carry a **recovery
affordance**, (c) **preserve the user's work**, (d) pair colour with **icon + text** (WCAG 1.4.1).

| Error scope | UI treatment | Recovery affordance |
|---|---|---|
| **Field-level** | Inline, below the field. (Owned by `form-ux-design`.) | Fix-it guidance; keep entered value. |
| **Form / section** | Error **summary** at top with anchor links to each failing field + inline markers. | Jump-to-error links; nothing cleared. |
| **Component / widget** | Error contained to the widget; **rest of page still works**. | "Retry" on the widget. |
| **Page-level** | Full-region error (the route failed). | Retry, Go back, navigate elsewhere. |
| **Not found (404)** | Authored 404; explain + route home/search. | Search, home, recent. |
| **Server (500)** | Honest failure; reassure data is safe; offer retry + support path. | Retry, contact, status link. |
| **Offline / network** | Distinct offline state (not a generic error). Queue actions if possible; auto-retry on reconnect. | Auto-retry; show when back online. |
| **Permission-denied (403)** | Explain *why* and *who to ask* — not "Error". | Request access / sign in / switch account. |
| **Timeout** | Treat as transient; offer immediate retry. | Retry; don't lose the request. |

**Never:** a vague "Something went wrong" with no scope and no retry; an error that blows up the
whole screen because one widget died; an error that clears the user's input.

---

## 5. Success / Confirmation — choose the right weight

| Pattern | Use for | Notes |
|---|---|---|
| **Silent / optimistic** | Reversible, low-stakes changes (toggle, autosave). | The changed UI *is* the confirmation. A persistent "Saved" microstate beats a toast. |
| **Inline toast / checkmark** | Routine successful actions (item added, message sent). | Auto-dismiss (~3–5 s); don't block; reduced-motion-safe. Announce via live region (4.1.3). |
| **Confirmation screen / modal** | Irreversible or high-stakes (payment, delete account, submission with a reference number). | Show what happened, the reference/next step, and a clear exit. |

Success motion is a small reward — brief, purposeful, and reduced-motion-safe. Reserve
celebration (confetti, big animation) for moments that genuinely earn it; the reflex to celebrate
every save is slop.

---

## 6. The per-component checklist (run this every time)

For the component in front of you, confirm each:

- [ ] **Enumerated** all reachable states from §1 before designing any.
- [ ] **Empty**: identified which of the four sub-types apply; each has an authored visual, a
      one-line message, and exactly one primary action; no dead ends.
- [ ] **Error-as-empty** is impossible — failures render the error state, not "No data".
- [ ] **Loading**: chosen tier (nothing / skeleton / progress / progressive) per latency; content
      regions use skeletons whose **geometry matches** the loaded layout (zero CLS).
- [ ] **Skeleton/animation** respects `prefers-reduced-motion`.
- [ ] **Error**: scoped to blast radius; every error has a recovery affordance; user work
      preserved; colour paired with icon + text.
- [ ] **Offline** and **permission-denied** handled as their own states.
- [ ] **Success**: chosen the right weight (silent / inline / confirmation screen).
- [ ] **A11y across all states**: target size ≥24px (2.5.8); focus moves sensibly when a state
      swaps and never strands the keyboard (2.4.3); loading/error/success announced via live
      region (4.1.3); contrast holds in every state.
- [ ] **No state thrash** (skeleton → spinner → content) and no loader flash under ~100 ms.

---

## 7. Division of labour with the content skill

This matrix and all visual/interaction decisions live here. The **words** of each state — the
error formula (what happened / why / how to fix), the empty-state copy, the tone (no blame, no
"error" alone) — live in `10-content-design-and-ux-writing/error-empty-and-system-messaging`.
Design the state here; write its message there; ship them together.
