# The Error Message Formula (and the empty / system rules)

The single canonical method for this skill. An error message is not a place to apologize, blame,
or dump a code — it is a tiny, high-stakes piece of interface that has one job: get the user
un-stuck. Everything below is in service of that.

Provenance: applies `doctrine/design-doctrine.md` §0 (authored over default — "Something went
wrong" is the slop default; a specific, helpful message is the authored one) and
`doctrine/references/wcag-2.2-criteria.md` (3.3.1, 3.3.3, 3.3.7, 1.4.1, 4.1.3). Standards named for
provenance: WCAG 2.2; Nielsen Norman Group error/empty-state guidance.

---

## 1. The formula: **what happened + why + how to fix** — minus blame, jargon, and alarm

Every error message answers, in this order, only what the user needs:

| Part | Question it answers | Rule |
|---|---|---|
| **What** | What just happened? | Plain, specific, first. "Your card was declined." not "Transaction error." |
| **Why** | Why did it happen? | **Only when it helps the user act.** Skip it if the reason is internal/irrelevant. "…because the card has expired." Don't explain the database. |
| **How to fix** | What can I do now? | The most important part. A concrete next step, ideally a button. "Update your card, or try another." |

Then subtract three things — this is where most messages fail:

- **No blame.** The user is never "invalid", "illegal", or at fault for a confusing UI. Reframe:
  - "You entered an invalid email" → **"That email doesn't look right — check for a typo?"**
  - "Illegal characters in password" → **"Passwords can't include spaces."**
  - "You failed to complete the form" → **"A few fields still need filling in (highlighted below)."**
- **No jargon / no raw codes as the headline.** Users don't read `0x80004005` or
  `ECONNREFUSED`. The human sentence comes first; the code goes in a small, **copyable** detail
  line *for support* underneath ("Reference: NET-503 — copy this if you contact us"). Never the
  reverse.
- **No alarm.** Drop "FATAL", "CRITICAL", "❌", "Oops!", all-caps, and exclamation pile-ups. The
  tone is calm and competent. The user already knows something is wrong; your job is to be the
  steady voice, not to amplify the panic.

**The "fix" is the test.** If you cannot state the next action, you have not understood the error
yet — go back to the cause. A message with no fix degrades into "Something went wrong", which is
the absence of a message.

### Worked transforms

| Weak | Rewritten (formula) |
|---|---|
| `Error: Something went wrong.` | `We couldn't save your changes — the connection dropped. Your work is still here; tap Retry.` |
| `Invalid input.` | `Phone numbers need 10 digits. You entered 9.` |
| `Auth failed.` | `That email and password don't match. Reset your password, or check the email is right.` |
| `0 results` | `No invoices match "March 2026". Try a wider date range or clear the filters.` |
| `Upload error 413` | `That file is too large (max 10 MB; yours is 14 MB). Try compressing it or pick a smaller one.` |

---

## 2. Empty states: teach, don't apologize

A zero state is the **highest-leverage onboarding surface** in the product. Never "No data."
Three jobs: say what *would* be here, say *why it's empty*, give the **one action** that fills it
(a real button, not just prose). And it has three distinct flavours — get the tone right for each:

| Type | Trigger | Tone | Pattern |
|---|---|---|---|
| **First-use** | Brand-new, nothing created yet | Inviting, onboarding | "Your invoices live here. **Create your first invoice** to get started." + primary button |
| **User-cleared** | They emptied it themselves | Affirming, rewarding | "Inbox zero — nicely done. New messages will appear here." (no guilt, no nagging CTA) |
| **No-results** | A search/filter returned nothing | Diagnostic, helpful | "No matches for 'xyz'. Check spelling, try fewer filters, or **clear all filters**." |

Anti-patterns: a bare "Nothing here"; a sad mascot with no next step; a first-use empty that reads
like an error ("No items found" on a screen the user has never had items on).

---

## 3. Success & confirmation: proportional to the stakes

Do **not** celebrate everything — confirmation fatigue trains users to ignore the one that matters.

| Action stakes | What to show |
|---|---|
| Routine, result is visible (draft saved, item added) | Nothing, or a quiet auto-dismiss toast. No fanfare. |
| Routine but invisible (settings synced, email queued) | A brief status toast: "Saved." / "Settings updated." |
| Costly / irreversible / money / security | **Explicit, specific** confirmation: "Payment of $40 sent to Aria." / "Account deleted — this can't be undone." |

**Destructive-action dialogs flip the formula** — lead with the consequence, and the button says
the verb:

- Title: name the consequence specifically — "Delete 3 files?" not "Are you sure?"
- Body: what is lost and whether it's recoverable — "These files will be permanently removed. This
  can't be undone."
- Buttons: **the verb**, not OK/Cancel — `[ Delete 3 files ]  [ Keep them ]`. The destructive
  button is visually distinct and never the default-focused one.

---

## 4. Severity → channel map (and the rule you must not break)

Pick the channel by **stakes × recoverability**:

| Severity | Meaning | Channel | Dismissal |
|---|---|---|---|
| **Inline** | Field-level, fixable right here | Field error text under/beside the input | Clears on fix |
| **Transient** | Informational, auto-recovers | Toast / snackbar | Auto-dismiss (~4–6s) |
| **Persistent** | Affects the session until resolved | Banner (top of page/region) | User-dismissible |
| **Blocking** | Needs a decision or halts the flow | Dialog (modal) or full page | Explicit action |

**The hard rule:** information the user **must not miss** — data loss, security, money, anything
irreversible — must **never** live in an auto-dismissing toast. If they look away for five seconds,
it's gone. Over-severity is also a failure: a full-page red catastrophe screen for a recoverable,
retryable blip is alarmist and erodes trust. Match the weight to the reality.

---

## 5. Accessibility: the string must stand alone, and be announced

Error and status copy is read aloud, out of visual context. Two rules:

- **Self-contained strings.** "Required" / "Invalid" / "Try again" mean nothing detached from a
  field. Always name the subject: **"Email is required."**, **"That date is in the past."** (3.3.1
  Error Identification — programmatically associate the message with its field.)
- **Right live region.** Active errors that need immediate attention → `role="alert"` /
  `aria-live="assertive"`. Passive status (saving, saved, offline, reconnecting) → `role="status"`
  / `aria-live="polite"` (4.1.3 Status Messages). Never convey error by colour alone — words + an
  icon/text marker carry it (1.4.1 Use of Colour).

Two more from WCAG that change the *words*:

- **3.3.3 Error Suggestion** — when the system can guess the fix, write it in. A diagnosis with no
  suggestion is a dead end; the suggestion is the detour. "We couldn't find that account — signed
  up with a different email?"
- **3.3.7 Redundant Entry** — don't ask the user to re-enter, in an error, data they already gave
  earlier in the same flow.

---

## 6. Localization

- Keep strings short and **literal** — idioms, puns, and culture-bound humour don't translate and
  read as flippant in a failure.
- Leave layout headroom for **~35% string expansion** (see
  `00-…/internationalization-and-rtl-design`); a terse English error can overflow its component in
  German or Finnish.
- Interpolate with **named placeholders + pluralization rules** (`{count, plural, one {# error}
  other {# errors}}`), never by concatenating fragments ("You have " + n + " errors") — fragment
  gluing breaks grammar in most languages.

---

## 7. The pre-ship checklist for any message

- [ ] States **what** happened, plainly, first.
- [ ] Gives the **why** only where it helps the user act.
- [ ] Gives a **concrete next action** (ideally a button) — the fix exists.
- [ ] **No blame** ("invalid"/"illegal"/"you failed" all removed).
- [ ] **No raw code/jargon as headline** (codes → copyable support detail line).
- [ ] **No alarm** (no FATAL/❌/Oops!/all-caps).
- [ ] Empty states **teach** (type-appropriate tone + one action), never "No data".
- [ ] Success is **proportional**; destructive dialogs name the consequence + verb buttons.
- [ ] **Severity matches channel**; nothing critical in an auto-dismiss toast.
- [ ] String is **self-contained** (names its subject) and announced via the right live region.
- [ ] **Not colour-only**; carries a suggestion (3.3.3) where one exists.
- [ ] Localizable: short, literal, named placeholders, expansion headroom.
