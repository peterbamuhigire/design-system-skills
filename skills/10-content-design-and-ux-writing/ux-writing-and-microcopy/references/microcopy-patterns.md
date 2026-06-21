# Reference: Microcopy Patterns (labels, tooltips, confirmations, state copy)

The working patterns for the words inside an interface, with good/bad pairs. Buttons and CTAs
have their own file (`button-and-cta-copy.md`); this file covers everything else the user reads
at the moment of action. Every pattern serves one rule: **clear first, on-voice second, never
decorative** (see `doctrine/design-doctrine.md` §0–2; accessibility per
`doctrine/references/wcag-2.2-criteria.md`).

The four laws under all of it:
1. **Write from the user's goal, not the system's plumbing.**
2. **One word per concept** — pick a term and never drift.
3. **Cut every word that survives deletion without loss.**
4. **Clarity outranks voice;** voice is *how* you are clear, never a licence to be cute.

---

## 1. Field labels

A label names the data in the **user's** language. It is a short noun phrase, sentence case,
above the field (not floating placeholder), and it stays visible while the user types.

| Bad | Good | Why |
|---|---|---|
| `Email address 2` | `Work email` | Names the data the user recognises, not a DB column. |
| `Input your full legal name as it appears on your ID` | `Full name` (+ helper: "As on your passport") | Label is the noun; the constraint goes in helper text. |
| Placeholder `Name` as the only label | Visible label `Name`, placeholder `e.g. Amina Okello` | Placeholders vanish on input and fail contrast (WCAG 1.4.3 / 4.1.2). |
| `DOB` | `Date of birth` | No unexplained abbreviations. |
| `Tel.` | `Phone number` | Plain word over jargon shorthand. |

**Helper text** states a *format* or a *reason*, never the obvious. Good: "We'll only use this to
send your receipt." Bad: "Enter your email address" under a field labelled Email.

---

## 2. Placeholder text

Placeholder is an **example or format hint**, never the label and never essential information
(it disappears, fails contrast, and is skipped by some screen readers — WCAG 1.4.3 / 4.1.2).

| Bad | Good |
|---|---|
| Placeholder `Email` (used as the label) | Label `Email`, placeholder `name@company.com` |
| Placeholder `Search` (only cue) | Label/aria-label `Search`, placeholder `Search invoices` |
| `Enter date` | `DD/MM/YYYY` (shows the format) |

---

## 3. Tooltips & helper text

A tooltip is a **patch for an unclear control**. First, make the control self-evident; reach for
a tooltip only for genuine ambiguity (an icon-only button, a term of art, a non-obvious limit).

Rules:
- **One phrase.** No restating the label, no "Click here to…", no period needed for a fragment.
- **Never hide essential info in hover-only text** — it is unreachable by keyboard and touch.
  Essential info goes in visible helper text. Tooltips must be focusable and dismissible (WCAG
  1.4.13) and the control must still have an accessible name (4.1.2).
- **Explain the consequence or the term, not the icon.**

| Bad | Good |
|---|---|
| Tooltip on a gear icon: `Settings icon` | `Settings` |
| Tooltip: `Click this button to export your data as a CSV file to your computer` | `Export as CSV` |
| (no accessible name) bare `🗑` button | `aria-label="Delete"` + tooltip `Delete` |
| Tooltip carrying the only copy of a rule: `Max 5 MB` | Visible helper `Max 5 MB` under the upload |

---

## 4. Confirmation & destructive-action dialogs

The single highest-stakes microcopy. Structure: **title = consequence**, **body = what's lost +
reversibility**, **buttons = the two verbs**.

- **Title** states the specific outcome, as a question or statement: "Delete this invoice?" —
  not "Are you sure?" (which carries no information).
- **Body** says what is lost and whether it can be undone: "This permanently removes the invoice
  and its 3 line items. This can't be undone."
- **Buttons** are the two *choices as verbs*: `Delete` / `Keep` — never `Yes` / `No` or
  `OK` / `Cancel` (the user shouldn't have to re-read the title to know which is which). The
  destructive button carries its real verb and is visually de-emphasised or guarded; the safe
  choice is the easy default.
- **Don't interrupt trivial, reversible actions** — confirmation fatigue trains users to click
  through. Reserve the modal for the costly and irreversible; for the reversible, prefer an
  **undo** toast instead.

| Bad dialog | Good dialog |
|---|---|
| Title `Are you sure?` · Buttons `Yes` / `No` | Title `Delete this project?` · Body `This removes all 12 tasks and can't be undone.` · Buttons `Delete` / `Keep` |
| Title `Warning` · Body `This action cannot be reversed.` · Buttons `OK` / `Cancel` | Title `Discard your changes?` · Body `Your edits since 2:14pm will be lost.` · Buttons `Discard` / `Keep editing` |
| Confirm dialog on archiving one email | No dialog; archive immediately + `Archived · Undo` toast |

---

## 5. Toggles, checkboxes, radios, menu items

State the **stable consequence**, not the action, and make the on/off meaning unambiguous.

| Bad | Good | Why |
|---|---|---|
| Toggle `Notifications` (on? off? what happens?) | `Email me about replies` | Names what being on *does*. |
| Checkbox `Don't not unsubscribe me` | `Email me product updates` | No double negatives. |
| Radio `Option 1` / `Option 2` | `Pay monthly` / `Pay yearly (save 20%)` | Each option names its real meaning and trade-off. |
| Menu item `Manage` | `Manage members` | Names the object; menus are scanned fast. |

---

## 6. Inline success & feedback strings

Confirm the **user's outcome**, briefly, from their point of view — and let it be quiet.

| Bad | Good |
|---|---|
| `Form submitted successfully.` | `Invite sent to amina@…` |
| `Operation completed.` | `Saved.` (or `Changes saved`) |
| `Success! Your request has been processed. 🎉🎉` | `Payment received — receipt emailed.` |

(For *error*, *empty*, and *system-status* copy, use
`error-empty-and-system-messaging` — that skill owns those.)

---

## 7. The terminology glossary (one word per concept)

Inconsistent terms are a top clarity killer. Maintain a tiny table and use the chosen word on
**every** surface — buttons, labels, menus, tooltips, confirmations.

| Concept | Chosen term | Never also call it |
|---|---|---|
| The container of work | `Project` | workspace, board, space |
| A person with access | `Member` | user, collaborator, seat |
| Remove permanently | `Delete` | remove, trash, erase, kill |
| Remove from view, keep data | `Archive` | hide, close, stash |
| Save a copy | `Duplicate` | copy, clone, fork |

---

## 8. Style defaults (the quiet rules)

- **Sentence case** for buttons, labels, menus, titles — more legible, less shouty than Title
  Case; no ALL CAPS for meaning.
- **Numerals as digits** in UI ("3 files", not "three files") — faster to scan.
- **Active voice, present tense, second person** ("You'll get a receipt", not "A receipt will
  be sent").
- **Front-load the meaningful word**; cut "please", "simply", "just", "in order to", "click here".
- **Contractions are fine** ("you'll", "we'll", "can't") — they read warm and human.
- **No idioms or puns** that don't survive translation; leave ~30% room for string expansion.
