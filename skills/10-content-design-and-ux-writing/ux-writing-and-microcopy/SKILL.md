---
name: ux-writing-and-microcopy
description: Use when writing or reviewing the words inside an interface — button and CTA labels, form field labels and hints, tooltips, menu items, empty/onboarding nudges, confirmation and destructive-action dialogs, toggle and checkbox text, placeholder text, success/inline-feedback strings, and tab/nav labels. Triggers on "what should this button say", "rename this label", "write microcopy", "the copy is confusing", "make this clearer", clarity-first interface copy, action-verb buttons, consistent terminology, and tying the words to the brand voice. Pairs with error-empty-and-system-messaging for error/empty/system copy and with brand-style-guide for the voice definition.
status: active
metadata:
  portable: true
  category: 10-content-design-and-ux-writing
  compatible_with:
    - claude-code
    - codex
---

# UX Writing & Microcopy (Clarity-First Interface Copy)

Microcopy is the small, functional text the user reads *at the moment of action* — the verb on
a button, the label above a field, the one line in a confirmation dialog. It is where most of
an interface's words live and where most of its friction hides. This skill makes that copy
**clear first, on-brand second, and never decorative** — and ties every string back to the
product's voice rather than letting each screen drift.

Microcopy is also a doctrine concern, not just a writing concern. Generic, hedged interface
copy ("Submit", "Are you sure?", "Oops! Something went wrong") is the verbal form of AI slop:
the convergent, unconsidered default. Per [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md)
§0–2, the moat is output that looks **authored** — and that includes the words. State the voice,
then write copy a templating tool would never have produced.

<!-- dual-compat-start -->
## Use When
- Deciding what a **button or CTA** should say (primary action, secondary, cancel, destructive).
- Writing **form labels, hints, placeholders, helper text**, and inline-success strings.
- Writing **tooltips** and short helper text for ambiguous icons or controls.
- Writing **confirmation / destructive-action dialogs** (delete, discard, overwrite, sign out).
- Writing **toggle, checkbox, radio, and menu-item** labels so state and consequence are clear.
- Auditing existing UI copy that is **vague, jargon-heavy, inconsistent, or off-voice**.
- Establishing a **terminology glossary** so one concept has exactly one word across the product.

## Do Not Use When
- The copy is an **error message, empty state, or system status** (offline, loading, 404,
  permission-denied) → use `10-content-design-and-ux-writing/error-empty-and-system-messaging`
  (it owns the error formula and the empty-state library; this skill owns the *interactive*
  copy — buttons, labels, tooltips, confirmations).
- You are **defining the brand voice / tone-of-voice spectrum itself** (the adjectives, the
  do/don't voice chart) → that lives in `02-color-brand-and-visual-identity/brand-style-guide`.
  This skill *consumes* that voice and applies it to microcopy.
- You are designing the **visual** empty/error/loading states (layout, illustration, hierarchy)
  → `04-web-and-ui-design/empty-error-and-loading-states`. This skill writes the words that go
  in them.
- You are writing **long-form** marketing or documentation prose, not in-interface strings.

## Required Inputs
- The **screen/flow and the moment**: what the user is trying to do, what they just did, what
  happens next when they act. Microcopy without context becomes generic.
- The **brand voice** — the tone adjectives and do/don't from `brand-style-guide`. If none
  exists, state a provisional voice in one line before writing (per doctrine §2 non-negotiable 1).
- The **consequence and reversibility** of each action (especially for buttons/confirmations:
  is it destructive? irreversible? does it cost money or notify someone?).
- The **locale / reading level** and any string-length constraint (button width, mobile).

## Workflow
1. **State the voice before writing a word** (doctrine §2, non-negotiable 1). One line: the tone
   adjectives and the register (e.g. "plain, warm, confident — never cute, never corporate").
   Pull it from `brand-style-guide`; if absent, declare a provisional voice. Clarity outranks
   voice when they conflict — voice is *how* you are clear, never an excuse to be cute.
2. **Name the user's goal and the moment.** Write the copy from the user's intent, not the
   system's. "Save changes" (their goal) beats "Submit form" (the system's plumbing).
3. **Buttons & CTAs — lead with a specific verb that names the outcome.** Use
   `references/button-and-cta-copy.md`: action verb + object where space allows
   ("Create project", "Send invite", "Delete 3 files"), not "OK" / "Submit" / "Yes". The button
   text should complete the sentence "I want to ___". Make destructive verbs explicit
   ("Delete", "Discard", "Remove") — never soften them to "OK". One primary action per view.
4. **Labels & fields — name the data in the user's language.** Label = noun phrase the user
   recognises ("Work email", not "Email address 2"). Helper text states format or *why* you ask,
   not the obvious. Never use placeholder text as the label (it vanishes on input and fails
   contrast — see [`doctrine/references/wcag-2.2-criteria.md`](../../../doctrine/references/wcag-2.2-criteria.md)
   §perennial 4.1.2 / 1.4.3). See `references/microcopy-patterns.md`.
5. **Tooltips & helper text — only for genuine ambiguity, and keep them short.** A tooltip is a
   patch for an unclear control; first try to make the control self-evident. When a tooltip is
   warranted, one phrase, no period needed, no restating the label. Tooltips must be keyboard-
   and screen-reader-reachable (WCAG 1.4.13 / 4.1.2) — they are not a place to hide essential
   info. See `references/microcopy-patterns.md` §tooltips.
6. **Confirmations & destructive dialogs — title states the consequence, buttons name the
   choices.** Title = the specific outcome as a question or statement ("Delete this invoice?"),
   body = what is lost and whether it is reversible, buttons = the two *verbs*
   ("Delete" / "Keep"), never "Yes / No" or "OK / Cancel". The destructive button is labelled
   with its real verb and visually de-emphasised or guarded. Don't pop a confirmation for
   trivial, reversible actions — reserve the interrupt for the costly and irreversible. See
   `references/microcopy-patterns.md` §confirmations.
7. **Enforce one term per concept.** Build a tiny glossary: pick *one* word for each concept
   ("project" vs "workspace" vs "board" — choose one) and use it everywhere, including buttons,
   labels, menus, and confirmations. Inconsistent terminology is a top clarity killer.
8. **Cut, then cut again.** Remove "please", "simply", "just", "click here", and any word that
   survives deletion without loss. Front-load the meaningful word. Sentence case for almost
   everything (more legible and less shouty than Title Case); reserve all-caps for nothing.
9. **Voice-check, then clarity-check.** Read each string aloud: does it sound like the stated
   voice? Then strip it to its meaning: would a first-time, stressed, or non-native user
   understand it in one read? If voice and clarity fight, clarity wins.
10. **Accessibility & i18n pass.** Every control still has a programmatic accessible name even
    when the visible label is an icon (WCAG 4.1.2). Avoid idioms and puns that don't translate;
    leave room for ~30% string expansion in other languages; never bake meaning into word order
    that breaks when translated.

## Anti-Patterns
- **"Submit" / "OK" / "Yes-No" buttons** — they name the mechanism, not the outcome. Use the verb.
- **"Are you sure?" with Yes/No** — the user can't tell which button does what without re-reading.
- **Cute over clear** — "Oopsie!", "Let's gooo!", forced jokes that delay comprehension. Voice
  serves clarity; it never replaces it.
- **Placeholder-as-label** — disappears on focus, fails contrast, breaks screen readers (4.1.2).
- **Mystery-meat tooltips** — essential info hidden in hover-only text unreachable by keyboard.
- **Terminology drift** — "project" on one screen, "workspace" on the next, for the same thing.
- **Filler words** — "Please simply click the button below to get started now." Cut to the verb.
- **Title Case Everything / ALL CAPS** — harder to read, reads as shouting or generic-template.
- **Softened destructive actions** — "OK" on a delete dialog hides the consequence. Say "Delete".
- **Confirmation fatigue** — interrupting reversible, trivial actions trains users to click past.
- **Untranslatable idioms / word-order tricks** — break the moment the product ships a locale.
- **Copy written from the system's view** — "Form submitted successfully" vs "Invite sent".

## Outputs
- Final interface strings for the screen/flow: button & CTA labels, field labels + helper text,
  tooltips, toggle/menu labels, confirmation dialog title/body/buttons, inline success strings.
- A short **terminology glossary** (one word per concept) for consistency across the product.
- A one-line **voice statement** the copy was written against (for handoff and review).

## Examples
- `examples/before-after-microcopy.md` — real slop-tier interface copy rewritten to clear,
  on-voice strings, **with the reasoning** for each change (buttons, labels, tooltips, a
  destructive confirmation), so the *why* transfers, not just the wording.

## References
- [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md) — §0–2: copy is part of
  the "looks authored" moat; state the voice before producing; no convergent default strings.
- [`doctrine/references/wcag-2.2-criteria.md`](../../../doctrine/references/wcag-2.2-criteria.md)
  — accessible names (4.1.2), contrast for labels/placeholders (1.4.3), focus appearance for
  tooltips (1.4.13). Microcopy must satisfy the AA floor.
- `references/microcopy-patterns.md` — patterns + good/bad for labels, tooltips, confirmations,
  toggles/menus, success strings, and the terminology-glossary discipline.
- `references/button-and-cta-copy.md` — the button/CTA copy system: verb+object formula, the
  primary/secondary/cancel/destructive hierarchy, and a good/bad catalogue by action type.
- Pairs with `10-content-design-and-ux-writing/error-empty-and-system-messaging` (error/empty/
  system copy), `02-color-brand-and-visual-identity/brand-style-guide` (the voice this consumes),
  and `04-web-and-ui-design/empty-error-and-loading-states` (the visual states copy fills).
<!-- dual-compat-end -->
