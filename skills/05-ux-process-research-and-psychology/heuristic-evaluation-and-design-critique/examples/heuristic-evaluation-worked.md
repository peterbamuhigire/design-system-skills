# Worked Example — Heuristic Evaluation of a Mobile Money-Transfer Flow

A full, filled heuristic evaluation of a real screen-and-flow, run by the method in `SKILL.md`
against the heuristics in `references/heuristics-catalog.md`, rated with
`references/severity-scoring.md`. It shows what a finding card, the severity table, and the
positive findings look like in practice — and how a single finding can cite both a Nielsen
heuristic and a Tognazzini principle.

**Artifact evaluated:** the "send money" flow of **Kasozi Pay**, a fictional East-African mobile
wallet — used here as a representative AI-assisted first build. Flow: *Home → Send → enter
recipient + amount → confirm → result.* Five screens, four taps on the happy path.

---

# Heuristic Evaluation / Design Critique
**Date:** 2026-06-21   **Evaluator(s):** 3 (lead designer, a11y reviewer, mobile engineer)
**Target:** Kasozi Pay — "send money" flow (Home → Send → Recipient/Amount → Confirm → Result)
**Platform:** Android (primary), iOS (secondary); one-handed thumb use is the dominant context
**Context:** Users range from low to moderate tech literacy; many on mid-range devices and
intermittent networks. Brand personality: trustworthy, calm, locally grounded — *not* a generic
fintech gradient deck.
**Heuristic set:** Nielsen 10 + Tognazzini first principles (+ interaction-anti-patterns A1–E3)
**Red routes walked:** send money to a saved contact; send to a new number; recover from a
failed/timed-out transfer.

> Method note: each screen was walked twice (feel-pass, then inspection-pass) per Workflow Step 2.
> The three evaluators found 11 raw issues; after merge/dedup, 8 findings remain. Each evaluator
> then rated the merged list independently; ratings below are the rounded mean.

---

## Findings

### F1 — Transfer submits with no acknowledgement, then freezes
- **Location:** Confirm screen → "Send UGX 50,000" button.
- **Heuristic violated:** N1 Visibility of system status + T10 Latency reduction + T2 Autonomy
  (also anti-pattern **C2 Silent System**).
- **Issue:** tapping "Send" produces **no immediate visual change**; the UI then freezes for 2–6 s
  on a slow network while the request runs on the main thread. Users re-tap, firing a **second
  transfer** on retry-tolerant endpoints.
- **Evidence:** screen-capture `f1-send-freeze.mp4` (00:02–00:08 no state change); reproduced 3/3
  on throttled 3G; double-submit confirmed in two of five test sends.
- **Severity:** **4** — every user, every send, on common slow networks; blocks the red-route task
  and risks **duplicate money movement** (frequency High × impact Blocking × persistent; market-
  impact modifier: financial loss).
- **Caught by:** 3 of 3 evaluators.
- **Fix / right pattern:** acknowledge the tap within ~50 ms (disable + inline spinner-in-button +
  "Sending…"), run the call off the main thread, make the endpoint **idempotent**, and show an
  explicit success/failure result. (N1 + T10.)

### F2 — No "you are here" in a four-step flow
- **Location:** all four flow screens.
- **Heuristic violated:** N1 Visibility of status + T11 Visible navigation (anti-pattern **A3**).
- **Issue:** the flow has no step indicator; users cannot tell how many steps remain or where they
  are, raising abandonment on the amount screen.
- **Evidence:** screenshots `f2-step1..4.png` — no progress affordance on any screen.
- **Severity:** **2** — common path, mild confusion, recoverable (freq High × impact Mild ×
  persistent).
- **Caught by:** 2 of 3.
- **Fix:** a 3-dot / "Step 2 of 3" progress indicator persistent across the flow.

### F3 — Recipient field is an unlabelled icon-only chooser
- **Location:** Recipient/Amount screen → contact picker.
- **Heuristic violated:** N6 Recognition rather than recall + N2 Match real world (anti-pattern
  **A2 Mystery Meat**).
- **Issue:** the only way to pick a saved contact is a bare person-silhouette icon with no text
  label; new users do not recognise it as "choose a saved recipient" and instead retype the number.
- **Evidence:** screenshot `f3-recipient.png`; icon-only comprehension ~60% vs ~88% with a label.
- **Severity:** **3** — common path, hard to discover, recurs until learned (freq High × impact
  Hard × persistent).
- **Caught by:** 3 of 3.
- **Fix:** label it "Choose contact" (icon **plus** text); pre-fill the last recipient (T5 Defaults).

### F4 — Failed transfer is a dead end with a coded error
- **Location:** Result screen (failure state).
- **Heuristic violated:** N9 Help users recover + N3 User control & freedom + T7 Protect the user's
  work (anti-pattern **C3 Dead End**).
- **Issue:** on failure the screen shows **"Txn error E_402"** with an OK button that returns to
  Home — wiping the entered recipient and amount, with no retry.
- **Evidence:** screenshot `f4-fail.png`; re-entry required on every failure; WCAG 2.2 3.3.7
  (redundant entry) concern.
- **Severity:** **4** — failures are frequent on this network profile, fully blocks completion, and
  **loses the user's input** (gate floor: T7 data-loss → 4).
- **Caught by:** 3 of 3.
- **Fix:** plain-language cause + "Try again" that **preserves the entered values**; never drop to
  Home on failure.

### F5 — Amount validity shown by red border only
- **Location:** Recipient/Amount screen → amount field (over-balance state).
- **Heuristic violated:** N9 + T3 Colour (anti-pattern **D3 Colour-Only Signalling**).
- **Issue:** entering more than the wallet balance turns the field border red — **no icon, no
  text** — invisible to colour-blind users and unexplained to everyone.
- **Evidence:** screenshot `f5-overbalance.png`; measured against WCAG 2.2 1.4.1 (use of colour).
- **Severity:** **3** — WCAG 2.2 AA gate floor (colour-only) → minimum 3; common on a top-up path.
- **Caught by:** 2 of 3 (the a11y reviewer + lead).
- **Fix:** pair the red with an inline message "Amount exceeds your balance (UGX 42,300)" and a
  warning icon.

### F6 — Confirm dialog uses a double negative
- **Location:** Confirm screen → cancel path → "Don't cancel?" dialog.
- **Heuristic violated:** N2 Match real world + N8 Aesthetic/minimalist.
- **Issue:** backing out raises a dialog "Are you sure you don't want to not send?" — a double
  negative users must parse under decision pressure.
- **Evidence:** screenshot `f6-dialog.png`.
- **Severity:** **2** — off the happy path, recoverable, but recurs and risks the wrong choice.
- **Caught by:** 2 of 3.
- **Fix:** plain phrasing — "Cancel this transfer?" with "Keep editing" / "Cancel transfer".

### F7 — Send CTA in the top-right corner, out of the thumb zone
- **Location:** Confirm screen → primary "Send" button placement.
- **Heuristic violated:** T8 Fitts's Law + N7 Efficiency.
- **Issue:** the primary action sits top-right; on a tall phone in one-handed use it is the hardest
  point to reach, slowing the most important tap.
- **Evidence:** screenshot `f7-cta.png`; button 96 px from the natural thumb arc.
- **Severity:** **2** — common, mild friction, recoverable (Fitts cost, not a block).
- **Caught by:** 1 of 3 (mobile engineer).
- **Fix:** move the primary action to a full-width bottom bar within the thumb zone; ≥ 44×44 target.

### F8 — Hero/Home reads as generic fintech slop
- **Location:** Home screen header.
- **Heuristic violated:** N8 Aesthetic/minimalist + **doctrine Anti-Slop Charter**.
- **Issue:** a purple→blue gradient header with **Inter** and a row of four identical balance cards
  — the convergent AI mean; nothing locally grounded or authored, contradicting the trustworthy,
  locally-rooted brand intent.
- **Evidence:** screenshot `f8-home.png`; matches `doctrine/references/interaction-anti-patterns.md`
  D2 + the slop taxonomy (banned default font + gradient + uniform cards).
- **Severity:** **2** — slop floor (doctrine) on a first-impression surface; not a task blocker but
  erodes trust positioning.
- **Caught by:** 2 of 3.
- **Fix:** re-author per `doctrine/design-doctrine.md` — a deliberate typeface pairing (not Inter),
  a grounded palette, and a hierarchy that is not four identical cards.

---

## Severity-ordered findings table

| # | Title | Heuristic(s) | Location | Severity | Caught by |
|---|---|---|---|---|---|
| F1 | Silent freeze + double-submit on Send | N1, T10, T2 (C2) | Confirm → Send | **4** | 3/3 |
| F4 | Failed transfer is a dead end, loses input | N9, N3, T7 (C3) | Result (fail) | **4** | 3/3 |
| F3 | Unlabelled icon-only recipient chooser | N6, N2 (A2) | Recipient | **3** | 3/3 |
| F5 | Over-balance shown by red border only | N9, T3 (D3) | Amount | **3** | 2/3 |
| F2 | No "you are here" in the flow | N1, T11 (A3) | All steps | **2** | 2/3 |
| F6 | Double-negative confirm dialog | N2, N8 | Confirm | **2** | 2/3 |
| F7 | Send CTA out of thumb zone | T8, N7 | Confirm | **2** | 1/3 |
| F8 | Generic fintech-slop home header | N8, doctrine | Home | **2** | 2/3 |

**Catastrophes (4):** F1, F4 — imperative before release. **Major (3):** F3, F5. **Minor (2):**
F2, F6, F7, F8.

## What works (positive findings — preserve these)

- **N5 Error prevention** is partly well done: the amount field already blocks non-numeric input
  and the confirm screen restates recipient + amount before commit — keep this guard.
- **N4 Consistency:** currency is formatted identically (UGX, thousands-separated) on every screen
  — terminology and number format are locked. Do not regress this.
- **T8 Fitts (positive):** the bottom-nav tab bar uses full-width, thumb-reachable targets — the
  pattern F7 should adopt for the Send CTA already exists in the same app.

## Coverage note

These are **expert-predicted suspected problems** from a 3-evaluator inspection — strong on the
obvious violations, but inspection is not testing. Confirm the borderline ratings (F2, F7) and the
real-world double-submit frequency (F1) with `ux-research-and-usability-testing` on 5 users before
final sequencing. Hand F1 → F8 (severity-ordered) to `ux-remediation-and-redesign` as the fix
backlog; the two catastrophes (F1, F4) are release-blocking.

---

*Run per `SKILL.md`; heuristics from `references/heuristics-catalog.md`; ratings from
`references/severity-scoring.md`. Aligned to WCAG 2.2 AA and `doctrine/design-doctrine.md`.
Kasozi Pay is fictional; no real product or data is depicted.*
