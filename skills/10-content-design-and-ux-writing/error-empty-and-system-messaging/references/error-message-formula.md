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

### Inclusive-language bans (no blame · no jargon · no alarm — made specific)

The three subtractions above are easy to nod at and hard to enforce. These are the concrete word
bans that operationalize them; treat them as lint rules.

- **"Invalid" / "illegal" are banned — they are blaming and "invalid" is ableist.** "Invalid"
  doubles as a slur for disabled people and frames the *person* as the defect; "illegal" implies
  wrongdoing. Say what's *expected* instead: not "Invalid email" → **"That email needs an @ sign."**;
  not "Illegal character" → **"Passwords can't include spaces."** Also banned: "you failed",
  "you forgot", "you didn't", "wrong" *(of the person)* — the UI asked unclearly; own it or stay
  neutral.
- **Default to singular "they"; never gender or assume the user.** Write "Ask whoever owns this
  workspace to share it with **them**", not "him/her". No assumed name, gender, ability, or device.
- **No jargon, no internal nouns, no codes as words.** Ban `null`, `token`, `exception`, `payload`,
  `400/500` *as the sentence*, `0x…`, `ECONNREFUSED`, "the server", "the database" — the person
  doesn't have those concepts. Codes live in a copyable support line, never in the prose.
- **No alarm vocabulary.** Ban "FATAL", "CRITICAL", "ERROR" *(as a shout)*, "WARNING", all-caps,
  "❌", "Oops!", "Uh-oh!", and exclamation pile-ups. The steady voice carries more authority than
  the panicked one. (Humour is also banned in *genuine* failures — wit is allowed only in playful
  empty states; see §2 and `breaking-best-practices` for the rare, reasoned override.)

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

### The 3-part empty-state framework (Ben-David)

The *type* above tells you the **tone**; this framework tells you the **three things every empty
state must contain**, in order. It maps cleanly onto the what/why/fix spine. From Ben-David,
*The Fundamentals of UX Writing*:

| Part | Job | The question it answers | Maps to |
|---|---|---|---|
| **1. Confirm the void is on purpose** | Reassure that the emptiness is expected, not a bug or a loading hang. Name *what this is* and *why it's empty* (first run / cleared / no results). | "Is this broken, or just empty?" | *what it is + why it's empty* |
| **2. Motivate filling it** | Give the *value* — not just "do this", but *why it's worth doing*. The pitch, not just the instruction. | "Why would I bother?" | *why act* |
| **3. Facilitate the action** | Provide the **actual button** to act, not prose telling them to act. One primary action. | "How do I start?" | *what to do next* |

Worked (first-use):
> **Your invoices will live here.** *(part 1 — confirms it's empty on purpose)*
> Create your first one and we'll track who's paid, chase late payers, and total it all up.
> *(part 2 — the value, not just "create an invoice")*
> `[ Create invoice ]` *(part 3 — the real button)*

The two views combine: pick the **type** (first-use / user-cleared / no-results) for tone, then run
the **3 parts** as the content checklist. A user-cleared state often softens or drops part 2/3 (no
nagging CTA when the person *chose* the empty) — that's a reasoned `breaking-best-practices`
override, not an exception to forget about.

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

> **First decide the *interruption* level.** Before picking a channel by stakes, classify the error
> by *how much it interrupts the person* — **Inline / Detour / Blocking** — per
> `references/error-placement-taxonomy.md`. That decides the message *style* (terse-located /
> instruction-led / decision-framing) and pushes you to the least disruptive placement that still
> works. The severity map below then picks the channel; the two almost always agree.

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
- [ ] **Placement classified** as Inline / Detour / Blocking, pushed to the least disruptive level
      that works; Detours lead with the alternate-path instruction (`error-placement-taxonomy.md`).
- [ ] **No blame** ("invalid"/"illegal"/"you failed"/"wrong" all removed; "invalid" is also ableist).
- [ ] **Inclusive language**: singular "they", no assumed gender/ability/device, no internal jargon
      (`null`/`token`/`exception`) in the prose.
- [ ] **No raw code/jargon as headline** (codes → copyable support detail line).
- [ ] **No alarm** (no FATAL/❌/Oops!/all-caps).
- [ ] Empty states **teach** (type-appropriate tone + one action), never "No data".
- [ ] Success is **proportional**; destructive dialogs name the consequence + verb buttons.
- [ ] **Severity matches channel**; nothing critical in an auto-dismiss toast.
- [ ] String is **self-contained** (names its subject) and announced via the right live region.
- [ ] **Not colour-only**; carries a suggestion (3.3.3) where one exists.
- [ ] Localizable: short, literal, named placeholders, expansion headroom.
