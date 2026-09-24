# Payment Fields, Forgiveness and Control Choice

Parent skill: [`../SKILL.md`](../SKILL.md) (`form-ux-design`).

**When to read:** when designing sign-up, checkout, payment or any data-entry form. Paraphrased
from Grant, W. (2018) *101 UX Principles*, Packt, and Pixsel Academy, *101 Dos and Don'ts of UI
Design*; current platform and accessibility rules (WCAG 2.2, including redundant entry 3.3.7 and
accessible authentication 3.3.8) come from `accessibility-wcag-2-2-compliance`.

---

## 1. Keep forms short

- Ask only what the task needs now (sign-up: email or phone plus password; name optional).
- Pre-fill anything already known (the username on a password-reset screen).
- Do not ask for the same information twice in one process.

## 2. Forgiveness rules

- Strip leading, trailing and internal spaces from codes, card numbers and phone numbers.
- Accept flexible phone formats (+256 772 000000, 0772000000) and normalise them yourself.
- Treat email and usernames case-insensitively; passwords stay case-sensitive.
- Validate on blur, not on every keystroke; never clear the field on error; show the error beside
  the field with the fix.

## 3. Payment fields

- One card-number field with automatic grouping into blocks of four as the person types.
- Expiry and security code only; do not ask for card type (derive it from the number).
- Support browser and device autofill.
- For East African checkouts, mobile money usually comes first: phone number field with network
  detection, then a clear "approve on your phone" waiting state with timeout and retry.

## 4. Control choice

| Data | Control |
|---|---|
| Two or three options | Radio buttons (round) or segmented control |
| Many options | Select or searchable list |
| Independent yes/no choices | Checkboxes (square, never round) |
| Numbers | Numeric keypad input |
| Dates | Native date picker where suitable |
| On/off setting with immediate effect | Switch |

Prefer device-native controls; they help users and cost less to build.

## 5. Field presentation

- Labels above fields, never placeholder-as-label.
- Boxed fields are usually parsed faster than underline-only fields.
- Show password rules inline and before submission, not only in a tooltip; allow showing the
  password.
- Specific button labels ("Create account", "Pay UGX 45,000"), not "OK" or "Next".
