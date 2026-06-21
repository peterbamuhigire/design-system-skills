# Reference: Button & CTA Copy

Buttons are where intent becomes action — the most-read and highest-stakes microcopy in any
product. A button's job is to let the user **predict exactly what happens when they press it**.
Generic labels ("Submit", "OK", "Yes") break that prediction and are the verbal signature of an
unconsidered, templated UI (see `doctrine/design-doctrine.md` §0–2). This file is the system for
getting them right.

---

## 1. The formula: verb + object (the outcome, in the user's words)

A button should **complete the sentence "I want to ___"**.

> **`[Action verb]` + `[object]`** — e.g. `Create project`, `Send invite`, `Add payment method`.

- Lead with a **specific verb** that names the outcome: *Create, Send, Add, Save, Publish,
  Delete, Invite, Connect, Download, Pay, Book, Start*.
- Include the **object** when it removes ambiguity and space allows ("Save draft" vs a bare
  "Save" when several things could be saved).
- Drop the object only when the surrounding context makes it obvious (a single primary form).
- **Quantify when it sharpens the stakes:** `Delete 3 files`, `Pay $49`, `Invite 5 people`.

| Vague | Specific (preferred) |
|---|---|
| `Submit` | `Create account` / `Send message` / `Place order` (name the real outcome) |
| `OK` | `Got it` / `Save` / `Delete` (which one is it?) |
| `Yes` | `Delete` / `Discard` / `Leave` (the verb, never the answer) |
| `Continue` | `Continue to payment` (where does it go?) |
| `Done` | `Save changes` / `Finish setup` |
| `Click here` | `Read the pricing guide` (a link is a verb too) |

---

## 2. The action hierarchy (one primary per view)

| Role | Copy rule | Weight |
|---|---|---|
| **Primary** | The verb for the *single* main outcome of the view (`Create project`). One per view. | Filled / strongest |
| **Secondary** | The verb for an alternate, less-common path (`Save as draft`). | Outline / tonal |
| **Tertiary / cancel** | The escape. `Cancel` (in a flow), or the inverse verb (`Keep editing`). | Text / ghost |
| **Destructive** | Its **real verb** (`Delete`, `Remove`, `Discard`) — never softened to `OK`. | Guarded: danger colour, often de-emphasised or requires intent |

Rules:
- **Exactly one primary** action per view — competing primaries paralyse the user.
- **Cancel is a real, easy target**, but never the visual primary.
- A **destructive primary** keeps its true verb and is visually marked as dangerous; pair it with
  a clearly-safe escape (e.g. `Delete account` / `Keep account`).

---

## 3. Catalogue by action type (good / bad)

| Action | Bad | Good |
|---|---|---|
| Create something | `Submit`, `Add` (bare) | `Create project`, `Add card` |
| Send | `Submit`, `Go` | `Send invite`, `Send for review` |
| Save | `OK`, `Apply` | `Save changes`, `Save draft` |
| Publish | `Submit`, `Done` | `Publish`, `Publish post` |
| Delete (destructive) | `OK`, `Yes`, `Remove?` | `Delete`, `Delete 3 files` |
| Discard edits | `Cancel`, `No` | `Discard changes` |
| Leave a flow | `Exit`, `Cancel` | `Leave without saving` |
| Pay | `Submit`, `Confirm` | `Pay $49`, `Subscribe — $9/mo` |
| Start / sign up | `Submit`, `Go` | `Create free account`, `Start free trial` |
| Sign in | `Submit`, `Enter` | `Sign in`, `Sign in with Google` |
| Connect a service | `OK`, `Authorize` | `Connect to Slack` |
| Download | `Get`, `Click` | `Download CSV`, `Download invoice` |
| Confirm a choice | `Yes` / `No` | the two verbs: `Delete` / `Keep` |
| Dismiss info | `OK`, `Close` | `Got it`, `Dismiss` |

---

## 4. Marketing CTAs (landing/hero) — value over command

On marketing surfaces the CTA can lead with the **value or first-person voice** rather than the
bare verb, but it must still be honest and specific (no dark patterns — pairs with
`04-web-and-ui-design/landing-page-and-conversion-design`).

| Weak CTA | Stronger CTA |
|---|---|
| `Submit` | `Get my free quote` |
| `Sign up` | `Start free — no card needed` |
| `Learn more` | `See how pricing works` |
| `Buy now` | `Get the annual plan (save 20%)` |
| `Download` | `Download the 2026 report (PDF)` |

First-person framing ("Start **my** trial") can lift conversion, but never at the cost of clarity
or honesty — the button must do exactly what it says.

---

## 5. Loading / pending / disabled states

The label should reflect the **current state** so the press feels acknowledged.

| State | Copy |
|---|---|
| Idle | `Send invite` |
| Pending | `Sending…` (present participle, same verb) |
| Success (brief) | `Sent ✓` then revert |
| Disabled (why?) | keep `Send invite`; explain the block in adjacent helper text, not in the label |

Don't change a disabled button's label to "Can't send" — say *why* it's disabled nearby, and keep
the action verb stable so the user knows what becomes available.

---

## 6. Style & accessibility defaults

- **Sentence case** ("Create project", not "Create Project" or "CREATE PROJECT").
- **No trailing punctuation** on buttons.
- **Keep it short** — aim ≤ 3 words; if you need more, the action is doing too much.
- **Consistent verbs** — one verb per concept across the whole product (`Delete` everywhere, not
  `Delete` here and `Remove` there); see `microcopy-patterns.md` §7.
- **Accessible name = the visible verb.** Icon-only buttons need an `aria-label` carrying the same
  verb (WCAG 4.1.2). Target size ≥ 24×24 px, 44×44 on touch (WCAG 2.5.8 — see
  `doctrine/references/wcag-2.2-criteria.md`).
- **Honest** — the label must match the outcome. "Continue" that actually charges a card is a
  dark pattern; say `Pay $49`.
