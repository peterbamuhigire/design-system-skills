# Example: Every State of One Real Component — a Paginated Data Table

A worked spec showing **all states designed up front** for a single, realistic component:
the **Transactions table** in a fintech dashboard (`Maduuka`-style). The data is async,
paginated, server-filtered, and occasionally streamed — so it exercises the full state matrix.
This is what "states as first-class design" looks like in practice: not the filled table plus
three afterthoughts, but every reachable state authored as a sibling of the happy path.

**Component contract**
- Columns: Date · Description · Counterparty · Amount · Status.
- Data source: paginated REST (`GET /transactions?page&filters`), p50 ≈ 220 ms, p95 ≈ 1.6 s.
- Filters: date range, status, search. Sort: any column.
- Width: full-width region inside the dashboard shell (shell stays interactive).

Reachable states (enumerated **before** designing any — Step 1 of the skill):
ideal · first-run empty · no-results-from-filter · loading (initial) · loading (page change) ·
partial/streaming · row-level error · page-level (region) error · offline · success
(after an inline edit). Each is specced below.

---

## State 1 — Ideal (the happy path)

Full table, rows rendered, pagination footer showing range + page controls, sort indicators on
the active column. Amount right-aligned and tabular-figures; Status as a coloured chip **with a
text label and a shape/icon** (never colour alone — WCAG 1.4.1). This is the *reference geometry*
every other state must respect so transitions don't shift layout.

---

## State 2 — Empty: first-run (blank slate)

The account is new; there has never been a transaction.

- **Visual:** an authored line-illustration of a ledger/receipt in the brand's stroke style —
  **not** a centered grey magnifying glass. Sized to the table's content area, not floating in a
  vast void.
- **Message (from the content skill):** headline "No transactions yet" + one line of value
  ("They'll appear here the moment money moves").
- **Action:** one primary CTA — "Record your first transaction" (or "Connect a bank") — focus
  lands here. Optional secondary: "Import a CSV".
- **Layout:** occupies the table body region; the header row and filter bar remain so the empty
  state reads as *this table, empty*, not a different screen.
- **A11y:** CTA ≥44px touch / ≥24px min (2.5.8); single logical focus target.

> Why authored: this is the highest-leverage onboarding moment the component has. A generic
> "No data" wastes it (Anti-Slop Charter, `doctrine/design-doctrine.md`).

---

## State 3 — Empty: no results from a filter

Data exists, but the current filter/search matched nothing. **Distinct** from State 2.

- **Visual:** lighter treatment (small inline glyph, not the full onboarding illustration) — this
  is a transient query result, not an empty account.
- **Message:** "No transactions match these filters." Echo the **active filters** so the user
  sees *why*.
- **Action:** primary "Clear filters" (restores results immediately); optionally "Widen date
  range". No dead end.
- **Critical:** if the fetch actually **failed**, do **not** render this state — render State 7/8.
  Error-disguised-as-empty is a bug, not an empty state.

---

## State 4 — Loading: initial load (skeleton)

First paint, no cached rows. Latency tier is ~100 ms–1.6 s, content region → **skeleton screen**.

- **Skeleton geometry mirrors the real table exactly:** same column count, same column widths,
  same row height, ~8 placeholder rows (a typical page). Date/Description/Counterparty as text
  bars; Amount as a right-aligned shorter bar; Status as a chip-shaped block. Header row is real
  (not skeletoned) so sort/filter affordances are immediately visible.
- **Result: zero layout shift** when real rows replace the skeleton — protects the **CLS ≤ 0.1**
  budget (`doctrine/references/web-performance-budgets-2026.md`).
- **Animation:** subtle left-to-right shimmer; under `prefers-reduced-motion` → static dimmed
  blocks, no shimmer (WCAG 2.3.3).
- **Threshold:** if the fetch resolves under ~100 ms (warm cache), skip the skeleton entirely —
  no flash.
- **A11y:** region marked `aria-busy="true"`; a polite live region announces "Loading
  transactions" (4.1.3).

---

## State 5 — Loading: page change / sort (in-place)

User clicks page 2 or re-sorts. Rows already on screen.

- **Pattern:** keep the **current rows visible**, dim them slightly, and show an in-region
  progress indicator (thin top bar or footer spinner) — do **not** collapse back to a full
  skeleton (that would be state thrash and a jarring flash). Disable pagination controls while
  in flight.
- **Optimistic sort:** if sorting client-side cached data, reorder instantly (optimistic) and
  only show a loader if a server round-trip is actually needed.

---

## State 6 — Partial / streaming

Large page streams in (or arrives row-batch by row-batch).

- **Pattern:** render the shell + header immediately, then fill rows as they arrive; remaining
  rows stay as skeleton placeholders so total height is stable (still zero CLS). A footer reads
  "Loading more…". Best perceived performance available for this data shape.

---

## State 7 — Error: row-level (scoped to a cell/row)

One row's Status couldn't resolve (e.g. enrichment service failed) but the rest of the page is
fine. **Match UI to blast radius** — do not fail the whole table.

- **Treatment:** that row's Status cell shows an inline warning icon + "Couldn't load" + a small
  "Retry" affordance scoped to the row. Every other row is fully usable.
- **A11y:** icon + text (not colour alone); retry control ≥24px; focusable.

---

## State 8 — Error: page-level / region (the fetch failed)

The whole `GET /transactions` call failed (500 / timeout). The **dashboard shell stays
interactive** — only the table region shows the error.

- **Visual:** authored error illustration in the table body (brand style, not a red triangle
  clip-art), contained to the region.
- **Message (content skill):** what happened + reassurance the data is safe + how to recover —
  never a bare "Something went wrong".
- **Actions:** primary "Retry" (re-issues the request, preserves current filters/sort); secondary
  "Contact support" / status-page link for a persistent 500.
- **Work preserved:** filters, sort, and page position are kept so retry returns to the same view.
- **A11y:** error announced via `role="alert"` live region; "Retry" focusable and ≥24px.

---

## State 9 — Offline

The browser lost connectivity (distinct from a server error).

- **Treatment:** an **offline** banner/state — "You're offline. Showing the last loaded
  transactions." — over the last-good rows if cached; auto-retry on reconnect and quietly
  refresh; show a brief "Back online" confirmation when it returns.
- **Distinct** from State 8: different cause, different copy, different (automatic) recovery.

---

## State 10 — Success: after an inline edit

User edits a transaction's category inline.

- **Pattern:** **optimistic** — the cell updates immediately; a subtle inline checkmark micro-
  state confirms; on failure, **roll back visibly** and surface a row-level error with retry.
- **No celebration:** routine save → silent/inline confirmation, auto-dismissing. A confetti
  moment here would be slop. Reserve a full confirmation screen only for high-stakes,
  irreversible actions (e.g. "Submit month-end close"), which this inline edit is not.
- **A11y:** success announced via polite live region; reduced-motion path for the checkmark.

---

## Acceptance criteria (handoff-ready)

A developer/QA can check each:

- [ ] All ten states implemented and reachable; **error never renders as empty**.
- [ ] Skeleton (State 4) column widths/row height/row count match the loaded table → **CLS ≤ 0.1**,
      verified in Lighthouse.
- [ ] Loads under ~100 ms show **no** skeleton (no flash); page-change (State 5) does **not** drop
      to full skeleton.
- [ ] Every error state (7, 8, 9) has a recovery affordance and preserves filters/sort/input.
- [ ] Row error (7) does not take down the table; page error (8) does not take down the shell.
- [ ] All chips/statuses use icon + text, not colour alone (WCAG 1.4.1).
- [ ] Every interactive control across every state ≥24px (2.5.8); focus never stranded on a
      removed node when a state swaps (2.4.3).
- [ ] Loading/error/success announced via appropriate live regions (4.1.3).
- [ ] All animation (shimmer, checkmark) honours `prefers-reduced-motion` (2.3.3).
- [ ] Copy for each state sourced from the paired skill
      `10-content-design-and-ux-writing/error-empty-and-system-messaging`.
