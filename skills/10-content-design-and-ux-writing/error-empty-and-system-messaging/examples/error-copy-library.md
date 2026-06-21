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
**Placement key** (Podmajersky's interruption taxonomy — see `references/error-placement-taxonomy.md`):
`INLINE` = fixable in place, terse + located · `DETOUR` = original path blocked, alternate path
exists, **instruction leads** · `BLOCKING` = flow halts, one decision. Every error row below is
tagged with its placement; note how Detours lead with the alternate action, not the diagnosis.
A11y role key: `alert` = `role="alert"`/`aria-live="assertive"` · `status` =
`role="status"`/`aria-live="polite"` · `inline-err` = associated with field via
`aria-describedby` + `aria-invalid` (3.3.1).

---

## A. Form validation (inline)

| # | Trigger | Before (weak) | After (formula) | Action | Placement | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|---|
| A1 | Email field blank on submit | `Required` | **Email is required.** | — | INLINE | inline | inline | inline-err |
| A2 | Email malformed | `Invalid email` | **That email doesn't look right — check for a typo? (e.g. name@company.com)** | — | INLINE | inline | inline | inline-err |
| A3 | Password too short | `Password invalid` | **Use at least 8 characters. You have 5.** | — | INLINE | inline | inline | inline-err |
| A4 | Phone wrong length | `Illegal value` | **Phone numbers need 10 digits — you entered 9.** | — | INLINE | inline | inline | inline-err |
| A5 | Amount over limit | `Error` | **Single invoices are capped at $50,000. Split this into two to continue.** | — | INLINE | inline | inline | inline-err |
| A6 | Date in the past | `Bad date` | **The due date is in the past. Pick today or later.** | — | INLINE | inline | inline | inline-err |

All of section A is **INLINE** — fixable right where the person stands, so the words are terse and
located, the least disruptive placement. Note A2/A4/A5 carry a **suggestion** (3.3.3), not just a
diagnosis. None says "invalid" or "illegal" (no blame — and "invalid" is also ableist). Each names
its subject so it stands alone when read aloud (3.3.1).

---

## B. Authentication

| # | Trigger | Before | After | Action | Placement | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|---|
| B1 | Wrong email/password | `Auth failed` | **That email and password don't match. Try again, or reset your password.** | Reset password | DETOUR | inline/banner | persistent | alert |
| B2 | Account not found | `User does not exist` | **No account yet for that email — create one to get started. (Or did you sign up with a different email?)** | Create account | DETOUR | banner | persistent | alert |
| B3 | Too many attempts | `429 Too Many Requests` | **Too many tries. For your security, wait 5 minutes and try again.** (detail: `Ref: AUTH-429`) | — | BLOCKING | banner | persistent | alert |
| B4 | Session expired | `Token expired` | **You've been signed out after a while away. Sign in again to pick up where you left off.** | Sign in | BLOCKING | page | blocking | — |

B1/B2 are **DETOUR**s: the original path (sign in to this account) is blocked, but a real alternate
path exists — so the **instruction leads**. B2 was rewritten to put the alternate action ("create
one") *first*, with the diagnosis demoted to a parenthetical — that is the defining Detour move.
B1 avoids confirming *which* field is wrong (security) while still giving the path forward. B3/B4
are **BLOCKING**: the flow halts (security lockout / signed-out), one decision, calm and complete.
B3 gives the *why* ("for your security") because it helps the user accept the wait, and tucks the
code in a support line.

---

## C. Payments

| # | Trigger | Before | After | Action | Placement | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|---|
| C1 | Card declined | `Payment error` | **Use another card to finish — your bank declined this one. Nothing was charged.** | Use another card | DETOUR | dialog | blocking | alert |
| C2 | Card expired | `Invalid card` | **This card expired in 04/25. Update the expiry date or add a new card.** | Update card | INLINE | inline | inline | inline-err |
| C3 | Network drop mid-payment | `Something went wrong` | **We couldn't confirm your payment — the connection dropped. We haven't charged you. Check your connection and try again.** | Retry | BLOCKING | dialog | blocking | alert |
| C4 | Payment success | (none / silent) | **Payment of $40.00 sent to Aria Studio.** | View receipt | — | toast→banner | transient | status |

C1 is a **DETOUR** hosted in a dialog: a card declined still has a clear alternate path (another
card), so the rewrite leads with that action — "Use another card to finish" — and demotes the
reason. C2 is **INLINE** (fix the expiry in place). C3 is **BLOCKING**: the textbook "Something
went wrong" rewrite — names the cause (connection), removes the money fear ("we haven't charged
you"), gives the fix, and stops the flow because the payment state is genuinely unresolved. C4 is a
**costly/invisible** success, so it gets an explicit, specific confirmation — not silence.

---

## D. Network / offline / system

| # | Trigger | Before | After | Action | Placement | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|---|
| D1 | Went offline | `No internet` | **You're offline. We'll keep your changes and sync them when you're back.** | — | DETOUR | banner | persistent | status |
| D2 | Reconnected | (none) | **Back online — your changes are synced.** | — | — | toast | transient | status |
| D3 | Save failed, retryable | `Save error` | **Retry to sync — we couldn't save just now. Your work is safe on this device.** | Retry | DETOUR | banner | persistent | alert |
| D4 | Scheduled maintenance | `Service unavailable` | **We're doing quick maintenance and will be back by 02:00 UTC. Your data is safe.** | — | BLOCKING | page | blocking | — |
| D5 | Rate limited (API) | `429` | **You're going a bit fast for us. Give it a few seconds and try again.** | — | DETOUR | toast | transient | status |

D1/D3/D5 are **DETOUR**s — the normal path (live sync) is blocked but an alternate keeps the person
moving (work offline / retry / wait-and-retry), so the action leads (D3 rewritten to lead with
"Retry to sync"). D4 is **BLOCKING** (whole service down). D1/D3 protect against the worst fear
(lost work) explicitly. Note severity discipline: D2 ("synced") is *transient* (toast) because
missing it is harmless; D3 ("couldn't save") is *persistent* (banner) because the user must act — it
is **never** an auto-dismiss toast.

---

## E. Permissions & errors pages

| # | Trigger | Before | After | Action | Placement | Channel | Severity | A11y |
|---|---|---|---|---|---|---|---|---|
| E1 | No access to resource | `403 Forbidden` | **Ask the workspace owner to share this invoice with you — you don't have access yet.** | Request access | DETOUR | page | blocking | — |
| E2 | Page not found | `404` | **We can't find that page — it may have moved or been deleted. Head back to your dashboard.** | Go to dashboard | BLOCKING | page | blocking | — |
| E3 | Server error | `500 Internal Server Error` | **Something broke on our end, not yours. We've been notified — try again in a minute.** (detail: `Ref: ERR-500-8f3a`) | Retry | BLOCKING | page | blocking | — |

E1 is a **DETOUR** even though it's a full page: a 403 has a real alternate path (request access),
so the rewrite leads with that action and uses singular-neutral phrasing ("the workspace owner…
share it with you"). E2/E3 are **BLOCKING** — nothing the person can route around in the moment, so
one calm decision (go back / retry). E3 explicitly says "on our end, not yours" — **no blame** — and
the code is a copyable support reference, not the headline. No "❌", no "FATAL".

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

**Each row above also satisfies Ben-David's 3-part framework** (confirm-on-purpose / motivate /
facilitate). Reading F1 through it:

| Part | F1 content |
|---|---|
| **1. Confirm the void is on purpose** | "Your invoices will live here." — this is empty *by design*, not broken. |
| **2. Motivate filling it** | "…and we'll track who's paid." — the *value*, not just the instruction. |
| **3. Facilitate the action** | `[ Create invoice ]` — the real button. |

F3 (user-cleared) deliberately drops parts 2–3 — no value pitch, no CTA — because the person *chose*
the empty and a nagging button would be patronizing. That is a reasoned `breaking-best-practices`
override of "every empty state needs a CTA", not a slip.

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
