# Worked Form Spec — Account Sign-Up (Web)

A complete, build-ready specification for a real **email sign-up form** on web
(Bootstrap 5 / Tabler markup conventions). It applies every rule in `SKILL.md`:
words-first, single column, labels above inputs, validate on blur, inline errors
that say *what* and *how to fix*, and WCAG 2.2 conformance including the three new
criteria that bite forms hardest — **3.3.7 Redundant Entry**, **3.3.8 Accessible
Authentication**, and **2.5.8 Target Size (Minimum)**.

Use it as a template: swap the fields, keep the structure and the rules.

---

## 0. Scope and intent

| Item | Decision |
|------|----------|
| Form | Create a new account |
| Fields | Full name, Email, Password, optional Referral code |
| Submit action | `POST /signup` → email verification screen |
| Single column? | Yes (no naturally paired fields here) |
| Field count | 4 → under 7, so **no wizard**; one page |
| Tone | Plain, second person, no jargon ("Create your account", not "Registration") |

We collect only what is needed to create and verify an account. We do **not** ask
for a username (email is the identifier), a "confirm password" field (see §4), date
of birth, phone, or marketing opt-ins on this screen — each extra question lowers
completion.

---

## 1. Field anatomy

Every field uses the same vertical stack, top to bottom:

```
[ Label ]                 ← always visible, above the input
[ Helper text ]           ← optional, only when it removes a question
[ Input control ]         ← 44px min height
[ Inline message slot ]   ← reserved; holds success OR error, never both
```

The inline message slot is **always present in the DOM** (empty by default) so the
layout never shifts when an error appears — a reflow on error is disorienting and
pushes the submit button under the user's thumb mid-tap.

### Field table

| # | Label | Type | Autocomplete | Required | Helper text |
|---|-------|------|--------------|----------|-------------|
| 1 | Full name | `text` | `name` | Yes | — |
| 2 | Email | `email` | `email` | Yes | "We'll send a verification link here." |
| 3 | Password | `password` | `new-password` | Yes | "At least 8 characters." |
| 4 | Referral code (optional) | `text` | `off` | No | "From an invite email or a friend." |

Notes:
- `inputmode="email"` + `type="email"` on field 2 → email keyboard on mobile, native format hint.
- Field 4 is marked **"(optional)"** in the label text. Required fields get **no**
  asterisk and no "required" decoration — required is the default and the three
  required fields read as such because only the optional one is annotated.

---

## 2. Label placement

- Labels sit **above** every input, on all breakpoints. No placeholder-as-label,
  no float labels.
- Placeholders are used only as *format examples*, never as the label, and never
  as the only hint:
  - Email placeholder: `you@company.com`
  - Referral placeholder: `e.g. FRIEND-2026`
- Label is programmatically tied to the input with `for`/`id`, so a click on the
  label focuses the field and screen readers announce the pairing.

```html
<div class="mb-3">
  <label class="form-label" for="email">Email</label>
  <input type="email" class="form-control" id="email" name="email"
         autocomplete="email" inputmode="email"
         aria-describedby="email-help email-msg"
         placeholder="you@company.com">
  <div id="email-help" class="form-text">We'll send a verification link here.</div>
  <div id="email-msg" class="field-msg" aria-live="polite"></div>
</div>
```

---

## 3. Input types and mobile behaviour

| Field | `type` | `inputmode` | `autocomplete` | Mobile keyboard / behaviour |
|-------|--------|-------------|----------------|------------------------------|
| Full name | text | text | name | Standard, autocapitalize words |
| Email | email | email | email | `@` and `.` keys surfaced; no autocapitalize, no autocorrect |
| Password | password | text | new-password | Reveal toggle (see §6); password-manager save offered |
| Referral | text | text | off | `autocapitalize="characters"` (codes are upper-case) |

Mobile specifics:
- Inputs are **full-width**, minimum **44px** tall (16px+ vertical padding) so the
  on-screen keyboard never covers the field being edited after the page scrolls it
  into view on focus.
- Font size on inputs is **16px minimum** — below 16px iOS Safari auto-zooms on
  focus, which is jarring.
- Submit button is full-width on viewports < 576px and pinned within the form flow
  (not floating), with 12px clearance above it.
- `autocomplete` attributes let the platform offer the user's saved name/email in
  one tap — directly satisfies Rule 5 (minimal friction) and supports §9.

---

## 4. Password field — and why there is no "confirm password"

A second "confirm password" box is a friction tax that **3.3.8 Accessible
Authentication** and modern guidance push us to drop. Instead:

- One password field with a **show/hide reveal toggle** (eye icon). The user
  verifies their own entry by looking at it — more reliable than retyping, and it
  removes a whole field and its mismatch error.
- The reveal toggle is a real `<button type="button">`, 44×44px, with
  `aria-pressed` and an `aria-label` that flips between "Show password" and
  "Hide password".
- No composition rules beyond a minimum length. We do **not** block paste, and we
  do **not** forbid password managers — both are 3.3.8 failures because they force
  the user to transcribe or memorise a secret (a "cognitive function test").

```html
<div class="mb-3">
  <label class="form-label" for="password">Password</label>
  <div class="input-group">
    <input type="password" class="form-control" id="password" name="password"
           autocomplete="new-password" minlength="8"
           aria-describedby="password-help password-msg">
    <button type="button" class="btn btn-outline-secondary" id="pw-toggle"
            aria-label="Show password" aria-pressed="false"
            style="min-width:44px;min-height:44px;">
      <i class="ti ti-eye" aria-hidden="true"></i>
    </button>
  </div>
  <div id="password-help" class="form-text">At least 8 characters.</div>
  <div id="password-msg" class="field-msg" aria-live="polite"></div>
</div>
```

---

## 5. Inline validation and timing

Validation is conversational, not nagging. Rules:

| Trigger | What runs | Why |
|---------|-----------|-----|
| **On keystroke** | Nothing that shows an error | Erroring while the user is mid-typing an email is hostile |
| **On blur** (field loses focus) | Validate that single field; show error OR success | The user has signalled "I'm done with this field" |
| **On re-edit after error** | Re-validate on `input`, clear the error the moment it passes | Reward the fix instantly; don't make them blur again |
| **On submit** | Validate all fields; focus + scroll to first error; render error summary | Catch untouched fields |

Per-field rules:

| Field | Rule | Error message (says what + how to fix) |
|-------|------|-----------------------------------------|
| Full name | Non-empty after trim | "Enter your name so we know what to call you." |
| Email | Valid email shape; server checks uniqueness on submit | Format: "Enter a valid email, like you@company.com." Taken: "An account already uses this email. Try signing in instead." |
| Password | ≥ 8 characters | "Use at least 8 characters." |
| Referral | If present: matches `^[A-Z0-9-]{4,16}$` | "Referral codes are 4–16 letters, numbers, or dashes. Leave it blank if you don't have one." |

Notes:
- **Async email-uniqueness** check runs on blur with a 400ms debounce *and* again on
  submit (authoritative). While in flight, show a subtle spinner in the message
  slot with `aria-busy="true"` — never block typing in other fields.
- Errors are **inline, below the field**, paired with an icon and text (never colour
  alone — WCAG 1.4.1). The word "error" is never used bare.

---

## 6. Field states (the full set)

Each field is specced for five states. The message slot height is reserved so none
of these cause layout shift.

| State | Visual | Border | Icon | Message slot | a11y |
|-------|--------|--------|------|--------------|------|
| **Empty / default** | Resting | neutral, ≥3:1 vs bg | none | empty | — |
| **Focused** | Ring | brand, 2px | none | empty | visible focus ring ≥3:1 |
| **Filled-valid** (after blur) | Subtle | success green | check `ti-check` | "Looks good." (optional) | `aria-invalid` removed |
| **Error** | Highlight | danger red | alert `ti-alert-circle` | message from §5 table | `aria-invalid="true"` + `aria-describedby` points to msg |
| **Disabled** (e.g. submit while submitting) | Dimmed | neutral @ .65 opacity | none | empty | `disabled`, text still readable |

Form-level states:

- **Empty form (initial):** all fields default, submit enabled (we validate on
  submit rather than disabling submit — a disabled submit gives no feedback about
  *why*).
- **Submitting:** submit button shows inline spinner + label "Creating account…",
  `aria-busy="true"`, button disabled to prevent double-submit.
- **Error (submit failed):** error summary banner at top of form,
  `role="alert"`, listing each error as an anchor link to its field; focus moves to
  the banner.
- **Success:** redirect to "Check your email" screen with `role="status"`
  confirmation; do **not** silently clear the form and stay in place.

```html
<!-- Error summary, hidden until submit fails -->
<div id="signup-errors" role="alert" class="alert alert-danger d-none" tabindex="-1">
  <strong>Please fix these to continue:</strong>
  <ul id="signup-error-list"></ul>
</div>
```

---

## 7. Accessibility — WCAG 2.2

### 2.5.8 Target Size (Minimum) — AA

- All interactive targets ≥ **24×24 CSS px**; this form uses **44×44px** for inputs,
  the password reveal button, the submit button, and the checkbox/links row.
- Adjacent targets (reveal toggle next to input; "Sign in instead" link) keep ≥ 8px
  spacing so a 24px exclusion circle around each does not overlap.

### 3.3.7 Redundant Entry — A

- We never ask the user to re-enter information already provided in the same process:
  - No "confirm email" or "confirm password" field (§4).
  - On the email-verification step that follows, the email is **pre-filled and shown**
    (not re-requested).
  - If the user navigates back to fix one field, all other entered values are
    **retained**, never cleared.
- Where re-entry is genuinely unavoidable, the prior value would be made available
  to auto-populate or select — but here it is simply avoided.

### 3.3.8 Accessible Authentication (Minimum) — AA

- The only auth step is "know your email + password." We impose **no cognitive
  function test**:
  - **Paste is allowed** into the password field.
  - **Password managers and browser autofill work** (`autocomplete="new-password"`,
    no input interference).
  - The **reveal toggle** lets users verify what they typed instead of memorising or
    retyping it.
  - No "type the 3rd, 5th, and 7th character of your password" puzzle, no
    transcription of one field into another.
- The follow-up email verification uses a clickable magic link (recognition, not
  recall) — also 3.3.8-conformant.

### Carried-forward form a11y (still required)

- Every input has a visible, programmatically associated `<label>`.
- Errors: `aria-live="polite"` per field; error summary `role="alert"`; colour
  never the sole signal (icon + text always).
- Visible focus indicator ≥ 3:1 contrast (2.4.7 / 2.4.11 focus-not-obscured).
- Tab order follows visual order; reveal toggle and submit reachable by keyboard;
  Enter submits.
- Input borders ≥ 3:1 against background (1.4.11); body text ≥ 4.5:1 (1.4.3).

---

## 8. Mobile behaviour summary

- Single column, full-width inputs, 16px+ input font (no iOS zoom-on-focus).
- 44px+ touch targets, 8–12px spacing between them.
- Correct mobile keyboards via `type` + `inputmode` (email keyboard for email,
  upper-case for referral code).
- On focus, the field scrolls clear of the on-screen keyboard; the message slot is
  pre-reserved so the error never appears *under* the keyboard.
- Submit button full-width and within the natural form flow, not a floating bar that
  can sit over a field.
- Browser/OS autofill offers saved name and email in one tap (Rule 5 + 3.3.7).

---

## 9. Build checklist

- [ ] Labels above every input; only the referral field annotated "(optional)".
- [ ] No placeholder-as-label; placeholders are format examples only.
- [ ] Message slot reserved in DOM for every field (no layout shift on error).
- [ ] Validate on blur; clear error on the keystroke that fixes it; full pass on submit.
- [ ] Error messages state what is wrong and how to fix it; icon + text, never colour alone.
- [ ] Single password field with 44×44px reveal toggle; paste + password managers allowed.
- [ ] No "confirm password" / "confirm email" (3.3.7).
- [ ] No cognitive-function auth puzzle (3.3.8).
- [ ] All targets ≥ 44px, ≥ 8px apart (2.5.8).
- [ ] `autocomplete` set correctly on every field.
- [ ] Error summary `role="alert"` with anchor links; focus moves to first error.
- [ ] Success → dedicated "Check your email" screen with `role="status"`.
- [ ] Retained values when navigating back; nothing silently cleared.
```