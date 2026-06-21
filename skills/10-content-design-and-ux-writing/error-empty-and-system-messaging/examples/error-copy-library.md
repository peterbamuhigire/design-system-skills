# Worked Example — Error / Empty / System Message Library

A real, populated message library for a fictional but realistic SaaS product, **Maduuka**
(an invoicing + payments app). This is the artifact this skill produces: every in-product
not-happy-path string, written to one voice and the what + why + how-to-fix formula, with the
weak "before" it replaced, the channel, the severity, the action label, and the a11y role.

**Voice for this product:** calm, plain, warm-but-professional, uses "we"/"you", **no humour in
genuine failures** (wit allowed only in playful empty states). Strings written for ~35% expansion
headroom. Codes shown go in a copyable support detail line, never as the headline.

Channel key: `inline` = field text · `toast` = auto-dismiss snackbar · `banner` = persistent,
dismissible · `dialog` = modal · `page` = full screen.
A11y role key: `alert` = `role="alert"`/`aria-live="assertive"` · `status` =
`role="status"`/`aria-live="polite"` · `inline-err` = associated with field via
`aria-describedby` + `aria-invalid` (3.3.1).

---

## A. Form validation (inline)

| # | Trigger | Before (weak) | After (formula) | Action | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|
| A1 | Email field blank on submit | `Required` | **Email is required.** | — | inline | inline | inline-err |
| A2 | Email malformed | `Invalid email` | **That email doesn't look right — check for a typo? (e.g. name@company.com)** | — | inline | inline | inline-err |
| A3 | Password too short | `Password invalid` | **Use at least 8 characters. You have 5.** | — | inline | inline | inline-err |
| A4 | Phone wrong length | `Illegal value` | **Phone numbers need 10 digits — you entered 9.** | — | inline | inline | inline-err |
| A5 | Amount over limit | `Error` | **Single invoices are capped at $50,000. Split this into two to continue.** | — | inline | inline | inline-err |
| A6 | Date in the past | `Bad date` | **The due date is in the past. Pick today or later.** | — | inline | inline | inline-err |

Note A2/A4/A5 carry a **suggestion** (3.3.3), not just a diagnosis. None says "invalid" or
"illegal" (no blame). Each names its subject so it stands alone when read aloud (3.3.1).

---

## B. Authentication

| # | Trigger | Before | After | Action | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|
| B1 | Wrong email/password | `Auth failed` | **That email and password don't match. Try again, or reset your password.** | Reset password | inline/banner | persistent | alert |
| B2 | Account not found | `User does not exist` | **We couldn't find an account for that email. Did you sign up with a different one? Or create an account.** | Create account | banner | persistent | alert |
| B3 | Too many attempts | `429 Too Many Requests` | **Too many tries. For your security, wait 5 minutes and try again.** (detail: `Ref: AUTH-429`) | — | banner | persistent | alert |
| B4 | Session expired | `Token expired` | **You've been signed out after a while away. Sign in again to pick up where you left off.** | Sign in | page | blocking | — |

B1 avoids confirming *which* field is wrong (security) while still giving a path forward. B3 gives
the *why* ("for your security") because it helps the user accept the wait, and tucks the code in a
support line.

---

## C. Payments

| # | Trigger | Before | After | Action | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|
| C1 | Card declined | `Payment error` | **Your card was declined by the bank. Try another card, or contact your bank — nothing was charged.** | Use another card | dialog | blocking | alert |
| C2 | Card expired | `Invalid card` | **This card expired in 04/25. Update the expiry date or add a new card.** | Update card | inline | inline | inline-err |
| C3 | Network drop mid-payment | `Something went wrong` | **We couldn't confirm your payment — the connection dropped. We haven't charged you. Check your connection and try again.** | Retry | dialog | blocking | alert |
| C4 | Payment success | (none / silent) | **Payment of $40.00 sent to Aria Studio.** | View receipt | toast→banner | transient | status |

C3 is the textbook "Something went wrong" rewrite: it names the cause (connection), removes the
money fear ("we haven't charged you"), and gives the fix. C4 is a **costly/invisible** action, so it
gets an explicit, specific confirmation — not silence.

---

## D. Network / offline / system

| # | Trigger | Before | After | Action | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|
| D1 | Went offline | `No internet` | **You're offline. We'll keep your changes and sync them when you're back.** | — | banner | persistent | status |
| D2 | Reconnected | (none) | **Back online — your changes are synced.** | — | toast | transient | status |
| D3 | Save failed, retryable | `Save error` | **We couldn't save just now. Your work is safe on this device — Retry to sync it.** | Retry | banner | persistent | alert |
| D4 | Scheduled maintenance | `Service unavailable` | **We're doing quick maintenance and will be back by 02:00 UTC. Your data is safe.** | — | page | blocking | — |
| D5 | Rate limited (API) | `429` | **You're going a bit fast for us. Give it a few seconds and try again.** | — | toast | transient | status |

D1/D3 protect against the worst fear (lost work) explicitly. Note severity discipline: D2
("synced") is *transient* (toast) because missing it is harmless; D3 ("couldn't save") is
*persistent* (banner) because the user must act — it is **never** an auto-dismiss toast.

---

## E. Permissions & errors pages

| # | Trigger | Before | After | Action | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|
| E1 | No access to resource | `403 Forbidden` | **You don't have access to this invoice. Ask the workspace owner to share it with you.** | Request access | page | blocking | — |
| E2 | Page not found | `404` | **We can't find that page — it may have moved or been deleted. Head back to your dashboard.** | Go to dashboard | page | blocking | — |
| E3 | Server error | `500 Internal Server Error` | **Something broke on our end, not yours. We've been notified — try again in a minute.** (detail: `Ref: ERR-500-8f3a`) | Retry | page | blocking | — |

E3 explicitly says "on our end, not yours" — **no blame**, and the code is a copyable support
reference, not the headline. No "❌", no "FATAL".

---

## F. Empty / zero states (the three types)

| # | Type | Context | Before | After (headline + body + action) | Action | A11y |
|---|---|---|---|---|---|---|
| F1 | First-use | Invoices list, brand-new account | `No data` | **Your invoices will live here.** Create your first one and we'll track who's paid. | Create invoice | status |
| F2 | First-use | Team members, none added | `Empty` | **Build your team.** Invite teammates to share invoices and get paid together. | Invite teammate | status |
| F3 | User-cleared | Notifications, all read | `Nothing here` | **You're all caught up.** New notifications will show up here. *(no nagging CTA)* | — | status |
| F4 | No-results | Search returns nothing | `0 results` | **No invoices match "March 2026".** Try a wider date range, or clear the filters. | Clear filters | status |
| F5 | No-results | Filtered list empty | `No items` | **No unpaid invoices right now** — nice. Adjust the filter to see all invoices. | Show all | status |

F1/F2 are the highest-leverage onboarding surfaces in the app — they teach the first action with a
real button, never "No data". F3 affirms without nagging. F4 is diagnostic and echoes the query.

---

## G. Success & destructive confirmation (proportionality)

| # | Action stakes | Trigger | Copy | Buttons / Action | Channel | A11y |
|---|---|---|---|---|---|---|
| G1 | Routine, visible | Draft saved | *(silent — the draft is visibly there)* | — | — | — |
| G2 | Routine, invisible | Settings synced | **Settings saved.** | — | toast | status |
| G3 | Irreversible | Delete invoice (dialog) | **Delete this invoice?** This permanently removes it and its payment history. This can't be undone. | `[ Delete invoice ]  [ Keep it ]` | dialog | alert |
| G4 | Irreversible, bulk | Delete 3 files | **Delete 3 files?** They'll be permanently removed — this can't be undone. | `[ Delete 3 files ]  [ Cancel ]` | dialog | alert |
| G5 | Discard work | Leave with unsaved edits | **Discard your changes?** Your edits to this invoice haven't been saved. | `[ Discard changes ]  [ Keep editing ]` | dialog | alert |

G1 shows **no** message (confirmation fatigue avoidance). G3–G5 flip the formula: consequence
named **specifically** in the title, and the buttons **say the verb** — never "OK / Cancel". The
destructive button is visually distinct and is *not* the default-focused button.

---

## How this library is used

- **Engineering pulls strings from this table**, keyed by id, not from inline literals — that is
  what keeps a hundred messages in one voice.
- Each row already carries its **channel, severity, action label, and a11y role**, so it drops
  straight into the matching visual frame from `04-…/empty-error-and-loading-states` (which designs
  *where* these words sit).
- **Auditing an existing product** = filling the "Before" column with whatever weak strings you
  find ("Oops!", "Error 0x4", "Invalid input", "No data") and rewriting each into the "After"
  column to the formula. Every "Before" is a defect; every "After" is the fix.
- Re-run the §7 pre-ship checklist in `references/error-message-formula.md` over each new row
  before it ships.
