# Worked Example: Three Tidwell Patterns Applied to One Real Screen

This walks one concrete screen — the **invoice line-items editor** inside an SMB accounting SaaS —
and shows how three named interaction patterns combine on it: **Inline Edit**, **Optimistic Action**,
and **Progressive Disclosure**. For each, the trigger→response wiring, the states it moves through,
and why that pattern fits this screen specifically.

The point is not "use these three patterns." It is to show *how a pattern is selected from the user's
behaviour*, *how its states are enumerated before any markup is written*, and *how the patterns share
one undo/escape backbone* so the screen stays coherent.

---

## The screen

A user is editing **Invoice #INV-2041** for a customer. The body is a table of line items:

| Description | Qty | Unit price | Tax | Line total |
|---|---:|---:|---:|---:|
| Monthly retainer — May | 1 | 1,200.00 | 18% | 1,416.00 |
| On-site visit (travel) | 2 | 85.00 | 18% | 200.60 |
| + Add line | | | | |

Below the table: a running subtotal, tax, and grand total that must stay correct after every edit.
The invoice is a **draft** — not yet sent — so edits are frequent, small, and iterative.

**User behaviours observed on this screen (the basis for pattern choice):**

- They correct one cell at a time — a typo'd quantity, a renegotiated price — not the whole row
  (*Incremental Construction*).
- They expect the total to update the instant they change a cell, with no Save round-trip
  (*Instant Gratification*, *Incremental Construction*).
- 90% of lines need only Description, Qty, Unit price. The other fields (discount, account code,
  cost centre) are needed by a minority and clutter the row for everyone else (*Deferred Choices*,
  *Satisficing*).

These three behaviours map cleanly onto three patterns.

---

## Pattern 1 — Inline Edit

**Why it fits:** the user changes one cell, sees the whole invoice while doing it, and works in tight
build-evaluate-adjust cycles. Opening a modal "Edit line" dialog for a single quantity correction
would break *Incremental Construction* (loses sight of the whole) and add three clicks to a one-keystroke
task. Inline Edit keeps the edit *in place* in the table the user is already reading.

**Trigger → response wiring:**

| Trigger | Response |
|---|---|
| Click (or Tab into) a cell | Cell turns into an input, text selected, caret ready; cell border highlights |
| Type a new value | Value updates in the input only (not yet committed) |
| `Enter` / `Tab` / click outside | Commit: validate, write value, recompute line total + invoice totals |
| `Esc` | Abandon edit, restore the previous value, exit edit mode |
| `Tab` from last cell of a row | Move to first editable cell of the next row (keyboard-only path through the table) |

**States of one cell:**

1. **Read** — plain text, but visibly editable on hover (cursor changes, faint affordance).
2. **Editing** — input active, original value still recoverable via `Esc`.
3. **Validating** — on commit, check the value (Qty must be a positive number; Unit price ≥ 0).
4. **Invalid** — value rejected: cell stays in edit mode, red border, inline message
   ("Qty must be a whole number ≥ 1"), focus retained so the user fixes it in place — never a
   blocking dialog.
5. **Committed** — new value shown in Read state; line total and invoice totals recomputed.

**Pattern-fit note:** Inline Edit relies on *Safe Exploration* — `Esc` is the per-cell Escape Hatch.
Without a reliable abandon, users hesitate to try edits, which defeats the purpose.

---

## Pattern 2 — Optimistic Action

**Why it fits:** the recompute and the persistence of a committed cell should feel instant
(*Instant Gratification*). The realistic failure rate of saving a single draft cell is low, and the
action is fully reversible (it is just a draft). So we apply the new value to the UI and totals
*immediately*, fire the save in the background, and only surface a problem if the save actually fails —
rather than freezing the row behind a spinner on every keystroke-commit.

**Trigger → response wiring:**

| Trigger | Response |
|---|---|
| Cell commit (from Pattern 1) | Apply value to model **immediately**; recompute totals **immediately**; render new state at once |
| (background) | `PATCH /invoices/INV-2041/lines/{id}` fires; a quiet "Saving…" pill appears top-right |
| Save succeeds | Pill becomes "All changes saved" then fades; no other change |
| Save fails | Roll the cell + totals back to the last-saved value; show a non-blocking banner: "Couldn't save that change. [Retry] [Discard]"; keep the user's attempted value available on Retry |

**States of a committed change:**

1. **Applied (pending)** — value live in UI and totals; request in flight; "Saving…" shown.
2. **Confirmed** — server acknowledged; "All changes saved"; pending state cleared.
3. **Failed** — request errored or timed out; UI **rolled back** to last-known-good; recovery banner shown.
4. **Reconciling** — on Retry, return to *Applied (pending)*; on Discard, accept the rollback.

**Pattern-fit note:** Optimistic Action is only honest if rollback is real. The two non-negotiables:
(a) the UI must visibly **revert** on failure, never silently keep a value the server rejected;
(b) the totals are derived from the model, so rolling back the cell automatically corrects the totals —
there is no second place to fix. This is the *Safe Exploration* guarantee at the network layer.

---

## Pattern 3 — Progressive Disclosure

**Why it fits:** most lines need three fields; a minority need six. Showing all six columns to everyone
punishes the majority with a cramped, scannable-only-with-effort table (*Satisficing* fails: the user
can't pick the right cell at a glance). Progressive Disclosure keeps the common case clean and reveals
the advanced fields **on demand, per row**, so the rare need doesn't tax the common one
(*Deferred Choices*).

**Trigger → response wiring:**

| Trigger | Response |
|---|---|
| Default render | Show only Description, Qty, Unit price, Tax, Line total. A chevron sits at the row's end. |
| Click the row chevron (or "More" affordance) | Expand a detail panel under the row revealing Discount, Account code, Cost centre — each an Inline Edit field |
| Edit a hidden field, then collapse | If any advanced field is non-default, show a small dot on the chevron so the row signals "has extra detail set" |
| Click chevron again / `Esc` | Collapse the panel; values are retained, not discarded |

**States of a row's disclosure:**

1. **Collapsed, clean** — advanced fields at defaults; chevron plain.
2. **Expanded** — detail panel open; advanced fields editable inline (Patterns 1 + 2 apply inside it).
3. **Collapsed, has-detail** — panel closed but a marker dot shows advanced values are set, so the
   detail isn't invisible-and-forgotten (*Prospective Memory*: the row keeps the user's own marker).

**Pattern-fit note:** the disclosure is **per row**, not a global "show advanced columns" toggle,
because the need is per-line. A global toggle would re-clutter every row to serve one. And the marker
dot is essential — disclosure that fully hides *set* values violates *Spatial Memory* and surprises the
user at send time.

---

## How the three patterns share one backbone

The patterns are not independent features bolted together; they share a single interaction spine so the
screen feels like one thing:

- **One undo/escape model.** `Esc` means "abandon the smallest open thing": abandon a cell edit
  (Pattern 1), or collapse a disclosure panel (Pattern 3). A separate **page-level Multi-Level Undo**
  (`Ctrl+Z`) reverses *committed* changes including failed-then-retried ones — so *Safe Exploration*
  holds whether the user is mid-cell or three edits deep.
- **One source of truth for totals.** Inline Edit commits, Optimistic rollbacks, and disclosed-field
  edits all mutate the same line model; totals are derived, never edited directly. Any of the three
  patterns changing a value recomputes totals the same way.
- **One save lifecycle.** Every committed value — visible column or disclosed field — flows through the
  same Optimistic save + rollback path. The user never has to learn "this field saves differently."

---

## What this example is *not*

- Not a component spec or CSS. Visual system (type scale, colour, spacing, the cursor/affordance
  treatment) comes from `practical-ui-design`; React/Bootstrap implementation from `webapp-gui-design`.
- Not the full state catalogue for the table shell (empty invoice, loading, page-level error). That is
  the job of the `empty-error-and-loading-states` skill; this example assumes the table has rows and
  focuses only on the *interaction* patterns inside a populated, editable draft.

## Pattern-selection summary

| User behaviour observed | Pattern chosen | The deciding reason |
|---|---|---|
| Edits one cell, needs whole invoice in view, iterates fast | **Inline Edit** | A modal would lose the whole and add clicks to a one-keystroke task |
| Expects instant total + save with no Save button, on a reversible draft | **Optimistic Action** | Low failure rate + full reversibility make optimistic safe; rollback keeps it honest |
| 90% of lines need 3 fields, 10% need 6 | **Progressive Disclosure** | Per-row reveal keeps the common case scannable without hiding set values |
