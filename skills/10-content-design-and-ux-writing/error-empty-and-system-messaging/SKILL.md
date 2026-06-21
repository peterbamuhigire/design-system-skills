---
name: error-empty-and-system-messaging
description: Use when writing the words that appear when something goes wrong, when there is nothing yet, or when the system needs to talk to the user — error messages, empty/zero states, success/confirmation copy, loading and offline messaging, toasts/banners, permission and destructive-action dialogs, 404/500 pages, validation and form-error text. Covers the helpful-error formula (what happened + why + how to fix, with no blame and no jargon), empty-state copy that teaches the first action instead of apologizing, and system messages that match severity to channel. This is the COPY layer; pair it with the visual skill `04-…/empty-error-and-loading-states`, which designs the states these words live in. Produces ready-to-ship message strings and a reusable message library. Routes here for "error message", "empty state copy", "validation copy", "404 / 500 page", "toast / banner / snackbar wording", "confirmation dialog text", "offline message", "system message", "error copy", "microcopy for errors".
status: active
metadata:
  portable: true
  category: 10-content-design-and-ux-writing
  compatible_with:
    - claude-code
    - codex
---

# Error, Empty And System Messaging
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Writing an **error message** — a field validation, a failed save, a network drop, a 4xx/5xx
  page, a payment decline, a permission denial. You need words that tell the user what happened,
  why (when it helps), and the one thing they can do next — without blaming them or leaking a
  stack trace.
- Writing an **empty / zero state** — the first-run screen, an empty list, no search results, a
  cleared inbox. The copy must orient the user and teach the first action, not just announce
  "Nothing here."
- Writing **system / status messaging** — success confirmations, toasts, banners, snackbars,
  loading and skeleton labels, offline/reconnecting notices, maintenance and rate-limit notices,
  destructive-action and permission dialogs.
- Standardizing the **copy half** of a state design: the visual skill
  `04-…/empty-error-and-loading-states` has laid out the empty/error/loading/success frames and
  you now need the actual strings that go in them — written to one voice, one formula, one
  severity model.
- Building or auditing a product's **message library** — turning ad-hoc, inconsistent error
  strings ("Error 0x4 occurred", "Oops!", "Invalid input") into a consistent, reusable set.

## Do Not Use When

- You are designing the *visual* state — the layout of the empty illustration, the skeleton
  loader, the error banner's placement and colour, the success animation. That is
  `04-…/empty-error-and-loading-states`. This skill writes the words that go *inside* those
  frames; build them together but they are different layers.
- You are writing **general interface microcopy** — button labels, field labels, tooltips,
  onboarding hints, menu and CTA wording in the *happy path*. That is
  `10-…/ux-writing-and-microcopy`. This skill is specifically the not-happy-path and
  system-to-user channels (error, empty, status). Errors do borrow that skill's button-copy
  rules for their action buttons.
- You are establishing the product's **voice and tone system** from scratch (the personality,
  the lexicon, the dos/don'ts). Do that first; this skill *applies* a defined voice to the
  hardest moments — error and emptiness are where a voice is tested, not where it is invented.
- The message is a piece of **marketing or instructional content** (a help article, an email
  campaign, a landing page) rather than an in-product system message. Different length budget,
  different channel, different skill.

## Required Inputs

- The product's **voice & tone** definition (or at least: how formal, how warm, does it use "we",
  does it ever use humour — and the rule that humour is forbidden in genuine error/failure states).
- The **actual failure taxonomy**: for each error, *what* technically went wrong, *whose* action
  (or no one's) caused it, whether it is recoverable, and *what the user can do next*. Copy that
  isn't grounded in the real cause becomes a vague "Something went wrong" — the least useful
  message there is. You cannot write a good error without knowing its cause and its fix.
- The **state inventory** from `04-…/empty-error-and-loading-states` (which empty/error/loading/
  success/offline states exist and where), so every designed state gets copy and none is left as
  raw default text.
- The **channel and severity** for each message: is it a blocking dialog, an inline field error, a
  toast that auto-dismisses, a persistent banner, a full page? Severity must match channel
  (§Workflow step 5) — a dismissible toast must never carry data-loss-critical information.
- Localization constraints if multi-locale: target languages and the string-expansion budget
  (`07/00-…/internationalization-and-rtl-design`), because terse English error strings can grow
  30–40% in translation and overflow the component.

## Workflow

1. **Name the real cause and the real fix before writing a word.** For the message in hand,
   answer four questions: *What happened? Why (in user terms)? Whose fault — and is it actually
   the user's? What is the single next action?* If you can't answer "what's the fix", the message
   will collapse into "Something went wrong" — the signature of an unconsidered error. This
   grounding is the whole skill; the wording is downstream of it. See
   `references/error-message-formula.md`.

2. **Write the error to the formula: what + why + how-to-fix, no blame, no jargon.** State what
   happened plainly, give the reason only when it helps the user act, and give the concrete next
   step — ideally as an action they can take right there. Strip three things: **blame** ("You
   entered an invalid…" → "That email doesn't look right — check for a typo?"), **jargon / error
   codes as the headline** (codes go in a copyable detail line for support, never as the message),
   and **alarm** ("FATAL", "❌", "Oops!"). Enforce the **inclusive-language bans**: never "invalid"
   (blaming *and* ableist) or "illegal" — say what's expected instead; default to singular **"they"**
   and assume no gender/ability/device; keep internal nouns (`null`, `token`, `exception`, raw
   codes) out of the prose. Match the doctrine: this is an *authored* message, not a reflexive
   default. (`references/error-message-formula.md` §1; `doctrine/design-doctrine.md` §0.)

3. **Write empty states as teaching moments, not apologies.** Run the **3-part empty-state
   framework** (Ben-David) as the content checklist: **(1) confirm the void is on purpose** (what
   this is + why it's empty), **(2) motivate filling it** (the *value*, not just "do this"), and
   **(3) facilitate the action** (the real button, not prose). Then set the *tone* by **type**:
   **first-use** (onboarding, "Create your first invoice"), **user-cleared** (affirming, "Inbox
   zero — nicely done"; may drop the CTA), and **no-results** (diagnostic, "No matches for 'xyz' —
   try fewer filters"). Never a bare "No data." An empty state is the highest-leverage onboarding
   surface in the product; treat it as such. (`references/error-message-formula.md` §2.)

4. **Write success and confirmation copy proportional to the action.** Routine success often
   needs *no* message (the result is visible) or a quiet toast — don't celebrate a saved draft.
   Reserve explicit confirmation for actions that are irreversible, costly, or invisible ("Payment
   of $40 sent to Aria", "Account deleted — this can't be undone"). For destructive-action
   *dialogs*, the formula flips: name the consequence specifically and make the button say the
   verb ("Delete 3 files" / "Cancel"), never "OK / Cancel". Confirmations that fire for everything
   train users to ignore them — the boy who cried toast.

4b. **Classify each error by interruption — Inline / Detour / Blocking (Podmajersky).** Before
   choosing a channel, decide *how much the error interrupts the person* and push it to the least
   disruptive level that still works (the downgrade rule: Blocking → Detour → Inline). **Inline** =
   fixable in place → terse, located words (a bad field). **Detour** = the original path is blocked
   but a real alternative reaches the goal → write the **alternate-path instruction first**, reason
   second ("Use another card to finish — your bank declined this one"). **Blocking** = the flow
   halts for a decision → calm, complete, one choice (session expired, 403/404/500, destructive
   confirm). This decides message *style*; the severity map (step 5) then picks the channel — they
   almost always agree. See `references/error-placement-taxonomy.md`.

5. **Match severity to channel — and never mismatch.** Map each message to its channel by
   stakes and recoverability: **inline** (field-level, fixable in place) → field error text;
   **transient** (informational, auto-recovers) → toast/snackbar, auto-dismiss; **persistent**
   (affects the session until resolved) → banner, user-dismissible; **blocking** (needs a decision
   or stops the flow) → dialog/full page. The hard rule: information the user must not miss
   (data loss, security, money) must **never** live in an auto-dismissing toast. Over-severity is
   as bad as under: a full-page red error for a recoverable hiccup is alarmist. See
   `references/error-message-formula.md` §Severity.

6. **Make every message accessible by construction.** Error and status copy is announced to
   screen-reader users, so the *string itself* must stand alone — "Required" floating with no
   field name is useless when read out of context; write "Email is required." The message must be
   programmatically associated with its field and announced via the right live region: validation
   errors via `role="alert"` / `aria-live="assertive"`, passive status (saving, saved, offline)
   via `aria-live="polite"` / `role="status"`. Never convey error by colour alone — the words and
   an icon/text marker must carry it (`doctrine/references/wcag-2.2-criteria.md`, 3.3.1 Error
   Identification, 3.3.3 Error Suggestion, 1.4.1 Use of Colour, 4.1.3 Status Messages).

7. **Offer the suggestion, not just the diagnosis (3.3.3).** Whenever the system can guess the
   fix, write it in: "We couldn't find that account — did you sign up with a different email?",
   "Card declined — try another card or contact your bank." A diagnosis with no suggestion leaves
   the user stuck; the suggestion is what turns an error from a dead end into a detour. Don't
   re-ask for data the user already gave in this flow (3.3.7 Redundant Entry).

8. **Localize within the expansion budget and avoid idiom.** Keep strings short and
   literal — idioms, puns, and culture-bound humour don't translate and read as flippant in a
   failure. Leave layout headroom for ~35% expansion (`…/internationalization-and-rtl-design`).
   Interpolate variables with named placeholders and pluralization rules, never by gluing
   fragments ("You have " + n + " errors") — that breaks in most languages.

9. **Assemble the message library and keep it the source of truth.** Collect the written strings
   into a structured library keyed by state and severity (the `examples/error-copy-library.md`
   shape): the trigger, the channel, the string(s), the action label, the a11y role. Engineering
   pulls from this, not from inline literals. Audit existing products *into* this library — every
   "Oops!" and raw code you find is a row to rewrite. This is what keeps a hundred error strings
   speaking in one voice. Hand off alongside the visual states from
   `04-…/empty-error-and-loading-states`.

## Anti-Patterns

- **"Something went wrong."** / "Oops!" / "An error occurred." — the null message. Says nothing,
  helps nothing, hides the fix. Almost always a sign step 1 (find the real cause) was skipped.
- **Blaming the user** — "You entered invalid data", "Illegal value", "You failed to…". The
  system asked for the input in a confusing way; own it or stay neutral. Never "invalid" (it's also
  ableist), never "illegal", never "you failed". Never gender or assume the user — singular "they".
- **Over-interrupting** — a Blocking dialog or full page for something fixable Inline, or stating a
  diagnosis when a Detour (alternate path) exists. Push every error down the interruption ladder
  (Blocking → Detour → Inline). A Detour that buries the alternate action behind the reason is the
  same failure — lead with the action.
- **Raw error codes / stack traces as the headline** — "Error 0x80004005", "NullPointerException".
  Codes belong in a copyable detail line *for support*, beneath a human sentence — never as the
  message the user reads first.
- **Empty state that just says "No data" / "Nothing here"** — wastes the single best onboarding
  surface in the app. No reason, no next action, no teaching.
- **Humour or cute mascots in a genuine failure** — a grinning robot over "We lost your payment"
  is tone-deaf. Wit is fine in a playful empty state; it is never fine when the user has lost
  work, money, or access.
- **Severity / channel mismatch** — critical, must-not-miss info in an auto-dismissing toast; or
  a full-page red catastrophe screen for a recoverable, retryable blip. Both erode trust.
- **"OK / Cancel" on a destructive dialog** — ambiguous and dangerous. Buttons say the verb
  ("Delete 3 files", "Discard draft"); the consequence is named specifically.
- **Colour-only error signalling** — a red border with no words and no icon. Invisible to
  colour-blind users and to screen readers (1.4.1, 4.1.3).
- **Context-stripped strings** — "Required", "Invalid", "Try again" with no subject. Read aloud by
  a screen reader, detached from the field, they mean nothing. Name the subject in the string.
- **Confirmation fatigue** — a toast/dialog for every trivial success until users tune them all
  out, including the one that mattered.

## Outputs

- **Ready-to-ship message strings** for each state: the error text (what + why + fix), empty-state
  copy (with its first-action label), success/confirmation copy, and system/status messages —
  written to one voice and the helpful-error formula, blame- and jargon-free.
- A **reusable message library** (the `examples/error-copy-library.md` structure) keyed by state,
  trigger, channel, and severity, with the action label and the a11y role for each — the source
  of truth engineering pulls strings from.
- **A11y-annotated** messages: each carries its live-region role (`alert`/`status`), its
  field association, and the non-colour marker, ready to drop into the visual states.
- An **audit log** when applied to an existing product: every weak string (null messages, blame,
  raw codes, bare empties) rewritten into the library.

## Examples

- `examples/error-copy-library.md` — a real, populated message library for a SaaS app: form
  validation, auth/login, payment, network/offline, permissions, 404/500, empty states
  (first-use, cleared, no-results), success/confirmation, and destructive dialogs — each row
  showing the trigger, **placement (Inline / Detour / Blocking)**, channel, severity, the before
  (weak) and after (rewritten) string, the action label, and the a11y role. Detour rows lead with
  the alternate action; empty-state rows are worked through Ben-David's 3-part framework. The worked
  artifact this skill produces.

## References

- `doctrine/design-doctrine.md` — Mission §0 (authored, human-made output over the convergent AI
  mean: "Something went wrong" is the slop default; a specific, helpful message is the authored
  one) and Anti-Slop Charter §2 (state the intent before producing — here, the real cause and fix
  before the wording).
- `references/error-message-formula.md` — the what + why + how-to-fix formula, the no-blame /
  no-jargon / no-alarm rules **with the specific inclusive-language bans** ("invalid"=ableist,
  singular "they", no internal jargon), the empty-state three-types model **plus Ben-David's
  3-part framework** (confirm-on-purpose / motivate / facilitate), the success-proportionality
  rule, and the severity-to-channel map. The core method of this skill.
- `references/error-placement-taxonomy.md` — Podmajersky's **Inline / Detour / Blocking** taxonomy:
  classifying an error by *how much it interrupts* the person and mapping message style to each
  (terse-located / instruction-led / decision-framing), with the downgrade rule. Read alongside the
  severity map — interruption sets the style, severity sets the channel.
- `doctrine/references/wcag-2.2-criteria.md` — Error Identification (3.3.1), Error Suggestion
  (3.3.3), Redundant Entry (3.3.7), Use of Colour (1.4.1), and Status Messages (4.1.3): the
  accessibility rules that make these strings stand alone and get announced correctly.
- Pairs with: `04-…/empty-error-and-loading-states` (the **visual** layer — designs the frames
  these words live in; build the two together). Upstream/sibling: `10-…/ux-writing-and-microcopy`
  (the happy-path microcopy and the button-copy rules the action labels follow);
  `00-…/internationalization-and-rtl-design` (string-expansion budget and idiom avoidance).
- Standards (named for provenance, not in-repo): WCAG 2.2; Nielsen Norman Group error-message and
  empty-state guidance; the widely-used "what happened / why / how to fix" error pattern.
<!-- dual-compat-end -->
