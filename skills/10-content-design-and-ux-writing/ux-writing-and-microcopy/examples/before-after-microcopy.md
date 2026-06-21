# Worked Example: Slop → Clear Microcopy Rewrites

Real interface copy taken to its "AI-default" worst, then rewritten clear and on-voice — **with
the reasoning**, so the principle transfers, not just the wording.

**Product context:** a small B2B invoicing SaaS used by freelancers and finance staff.
**Stated voice (declared first, per `doctrine/design-doctrine.md` §2 non-negotiable 1):**
*plain, calm, and competent — talks to a busy professional like a sharp colleague; never cute,
never corporate, never alarmist.* Clarity outranks voice wherever they conflict.

References applied throughout: `references/button-and-cta-copy.md`,
`references/microcopy-patterns.md`, `doctrine/references/wcag-2.2-criteria.md`.

---

## 1. Primary button — new invoice form

**Before**
> `Submit`

**After**
> `Create invoice`

**Reasoning.** "Submit" names the system's mechanism (posting a form), not the user's goal. The
verb+object formula (`button-and-cta-copy.md` §1) completes "I want to ___ → create invoice".
It also disambiguates from "Save draft" sitting beside it. Sentence case, no punctuation.

---

## 2. Field label + placeholder — client email

**Before**
> Label: *(none)* — placeholder only: `Email`
> Helper: `Please enter the email address.`

**After**
> Label: `Client email`
> Placeholder: `name@company.com`
> Helper: `We'll send the invoice here.`

**Reasoning.** Placeholder-as-label vanishes on input, fails contrast, and isn't a reliable
accessible name (WCAG 1.4.3 / 4.1.2 — `microcopy-patterns.md` §1–2). A persistent label fixes
that. "Client email" names the data in the user's terms (whose email, and why). The old helper
restated the obvious; the new one tells the user the *consequence* — where the email goes.

---

## 3. Tooltip — the recurring-invoice icon

**Before**
> Icon-only ↻ button, `aria-label="button"`, tooltip: `Click here to set up recurring`

**After**
> Icon-only ↻ button, `aria-label="Make recurring"`, tooltip: `Make recurring`

**Reasoning.** The control had no real accessible name (4.1.2) — a screen reader announced
"button". The tooltip restated nothing useful and led with "Click here". A tooltip is a patch for
an unclear icon, so it should carry the action in one phrase (`microcopy-patterns.md` §3), and the
`aria-label` must match it so keyboard and screen-reader users get the same meaning.

---

## 4. Toggle label

**Before**
> `Reminders` *(on/off — unclear what it does)*

**After**
> `Email the client before the due date`

**Reasoning.** A toggle should name its **stable consequence**, not a vague noun
(`microcopy-patterns.md` §5). Now "on" has an unambiguous meaning: the client gets a reminder
email. No guessing who is reminded or how.

---

## 5. Destructive confirmation dialog

**Before**
> Title: `Are you sure?`
> Body: `This action cannot be undone.`
> Buttons: `OK` · `Cancel`

**After**
> Title: `Delete this invoice?`
> Body: `This permanently removes invoice #1043 and its 3 line items. You can't undo this.`
> Buttons: `Delete invoice` · `Keep it`

**Reasoning.** "Are you sure?" carries zero information; the user must re-read the screen behind
it to know what they're confirming. The new title states the **consequence**; the body says
*exactly* what is lost and that it's irreversible; the buttons are the two **verbs**, so the user
never has to map "OK → which thing?" (`microcopy-patterns.md` §4). The destructive button keeps
its true verb (`Delete`) and would be styled as the guarded/danger action, with the safe escape
("Keep it") as the easy default. Calm, not alarmist — on voice.

---

## 6. Success / inline feedback

**Before**
> `Operation completed successfully! 🎉🎉`

**After**
> `Invoice sent to maya@studio.co`

**Reasoning.** "Operation completed" is system-speak and the confetti is cute-over-clear, which
the voice forbids. The rewrite confirms the **user's** outcome from their point of view and even
names the recipient, so they know it went to the right place (`microcopy-patterns.md` §6). Quiet
and useful beats loud and empty.

---

## 7. Terminology consistency (cross-screen)

**Before** (three screens, same concept)
> Dashboard: `New bill` · Sidebar: `Create invoice` · Email: `Your statement is ready`

**After**
> Everywhere: `Invoice`

**Reasoning.** "Bill", "invoice", and "statement" referred to the same object, forcing the user to
re-learn the vocabulary on each screen. One concept, one word (`microcopy-patterns.md` §7),
applied to buttons, nav, and notifications alike — the cheapest, highest-leverage clarity win.

---

## 8. Marketing CTA (landing hero)

**Before**
> `Sign up`

**After**
> `Start invoicing free — no card needed`

**Reasoning.** On a marketing surface the CTA can lead with **value** while staying honest
(`button-and-cta-copy.md` §4). It names the outcome ("start invoicing"), the price ("free"), and
removes the top objection ("no card needed") — without any dark-pattern bait. Still does exactly
what it says when pressed.

---

### What carried across every rewrite
1. **Wrote from the user's goal**, not the system's plumbing.
2. **Verb + object** on every actionable control; the two **choices as verbs** in the dialog.
3. **One word per concept**, product-wide.
4. **Cut filler** ("please", "click here", confetti) and front-loaded the meaningful word.
5. **Met the AA floor** — real labels, accessible names, adequate contrast (WCAG 4.1.2 / 1.4.3).
6. **Clarity first; voice as the texture**, never as a substitute for being understood.
