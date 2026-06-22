---
name: form-ux-design
description: Cross-platform form UX/UI patterns for web (Bootstrap 5/Tabler), Android
  (Jetpack Compose), and iOS (SwiftUI). Covers field anatomy, validation, error states,
  multi-step wizards, accessibility, touch-friendly inputs, and submission workflows.
  Use when designing, building, reviewing, or refactoring any form on any platform.
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
    - claude-code
    - codex
---

## Platform Notes

- Optional helper plugins may help in some environments, but they must not be treated as required for this skill.

# Form UX/UI Design
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- Building, reviewing, or refactoring any form: sign-up, login, checkout, settings, contact, search filters, or multi-step wizards on web (Bootstrap 5/Tabler), Android (Jetpack Compose), or iOS (SwiftUI).
- Deciding label placement, single vs. two-column layout, required/optional marking, or whether to split a long form (>7 fields) into steps or a gateway screen.
- Writing or fixing inline validation: when to validate (on blur, not keystroke), the five field states, error-summary-with-anchors for long forms, and Enders-style error copy that says what's wrong and how to fix it.
- Making fields accessible: WCAG 2.2 redundant entry (3.3.7), accessible authentication (3.3.8), target size (2.5.8), autocomplete attributes, and screen-reader/keyboard behaviour.
- Choosing touch-friendly input types, smart defaults, and auto-formatting (phone, currency) to cut keystrokes and friction.

## Do Not Use When

- The screen has no data-entry fields — for blank/no-data, failure, and loading screens use sibling `empty-error-and-loading-states` (this skill covers the field-level loading/error states only).
- You need general button/input hover, press, and focus motion fidelity across a component library — use `component-states-and-interaction-fidelity` or `interaction-design-patterns`.
- The work is page-level layout, spacing rhythm, or visual hierarchy rather than form mechanics — use `practical-ui-design`; for menus/wayfinding use `navigation-and-information-architecture`.
- Picking error/success/validation colour roles — defer to `02-color-brand-and-visual-identity/color-system-and-palette` and gate every pair on WCAG contrast.

## Required Inputs

- Platform(s) in scope: web (Bootstrap 5/Tabler + PHP), Android (Compose + Material 3), iOS (SwiftUI) — components and code differ per platform.
- The actual fields being collected and which are genuinely required, so unnecessary questions can be cut.
- Deliverable type: a build-ready form spec (see `examples/form-spec-worked.md`), new component code, a UX audit, or a refactor of an existing form.
- Any validation/business rules (formats, async uniqueness checks, dependencies) and the WCAG conformance target.

## Workflow

- Read this `SKILL.md` first, then load only the referenced deep-dive files that are necessary for the task.
- Apply the ordered guidance, checklists, and decision rules in this skill instead of cherry-picking isolated snippets.
- Produce the deliverable with assumptions, risks, and follow-up work made explicit when they matter.

## Quality Standards

- Keep outputs execution-oriented, concise, and aligned with the repository's baseline engineering standards.
- Preserve compatibility with existing project conventions unless the skill explicitly requires a stronger standard.
- Prefer deterministic, reviewable steps over vague advice or tool-specific magic.

## Anti-Patterns

- Treating examples as copy-paste truth without checking fit, constraints, or failure modes.
- Loading every reference file by default instead of using progressive disclosure.

## Outputs

- A **form UX audit** covering field grouping, validation, error states, submission affordances,
  accessibility, and platform-specific behaviour.
- A build-ready form spec or implementation guidance when the task is creation or refactoring rather than audit.
- Clear assumptions, tradeoffs, or unresolved gaps when the task cannot be completed from available context alone.
- References used, companion skills, or follow-up actions when they materially improve execution.

## References

- `doctrine/design-doctrine.md` — the Mission and the Anti-Slop Charter; forms must look authored, not defaulted.
- `doctrine/references/ai-slop-taxonomy.md` — the convergent-default tells to avoid in form layout and styling.
- `doctrine/references/type-scale-and-spacing.md` — label/field type sizing and spacing rhythm.
- This skill's own `references/` directory for platform-specific deep detail (web/Android/iOS components, validation, accessibility) after reading the core workflow below.
- Sibling: `02-color-brand-and-visual-identity/color-system-and-palette` for error/success/validation colour roles (gate every pair on WCAG contrast).

## Examples

- `examples/form-spec-worked.md` — a complete, build-ready spec for a real account sign-up form: field anatomy, label placement, input types, inline validation with timing, the five field states plus form-level states, and WCAG 2.2 accessibility (3.3.7 redundant entry, 3.3.8 accessible authentication, 2.5.8 target size) with mobile behaviour. Use as a fill-in template.
<!-- dual-compat-end -->
Cross-cutting form design patterns for **web** (Bootstrap 5 / Tabler + PHP), **Android** (Jetpack Compose + Material 3), and **iOS** (SwiftUI). Apply this skill whenever you build, review, or refactor any form.

## Quick Reference

| Topic | Reference File | Scope |
|-------|---------------|-------|
| Web form components | `references/web-form-components.md` | Bootstrap/Tabler inputs, selects, checkboxes, radios, switches, textareas, file uploads |
| Android form components | `references/android-form-components.md` | Compose TextField, ExposedDropdownMenu, Checkbox, RadioButton, Switch, Slider |
| iOS form components | `references/ios-form-components.md` | SwiftUI TextField, Picker, Toggle, DatePicker, Stepper |
| Validation patterns | `references/form-validation.md` | Validation logic, error states, async validation, submission workflows (all platforms) |
| Accessibility | `references/form-accessibility.md` | WCAG form requirements, ARIA, screen readers, keyboard nav, touch targets (all platforms) |

---

## 1. Form Design Philosophy

Five rules that govern every form decision:

**Three dimensions of every form** (most to least influential):
1. **Words** — what you say and how you say it. Users can work around bad layout; they cannot work around bad wording.
2. **Layout** — how things are visually presented
3. **Flow** — how the user moves through the form

**A form is a conversation.** Order, tone, appropriateness, and effort all matter to humans. Design accordingly.

**"Start with nothing. Then only add what's needed to communicate with the user."** — Every pixel must serve a purpose. Be ruthless.

**Collect only what you need.** Every additional question reduces completion rate and data quality. Never add questions "just in case."

### Rule 1 — Labels Above Inputs (ALWAYS)

Labels above inputs on ALL screen sizes. NEVER use placeholder text as the label — it disappears on focus, makes fields look pre-filled, is not reliably announced by screen readers, and corrupts data when left in the field. NEVER use float labels — they have all the same problems as placeholder-as-label plus broken animation on long labels.

Mark **optional** fields with "(optional)" appended to the label. Do NOT mark required fields with red asterisks — they are abstract, visually noisy, inaccessible, and often labelled with jargon like "mandatory."

### Rule 2 -- Single Column by Default

One column for forms. Two-column layout only for naturally paired fields (first name / last name, city / state). Mobile is always single column regardless.

### Rule 3 -- Progressive Disclosure

Show only what is needed now. Reveal advanced fields conditionally (toggles, dependency rules). Break long forms (more than 7 fields) into logical steps.

### Rule 4 -- Instant Feedback

Validate on blur (not on keystroke). Show errors inline below the field. Display success indicators (green border or checkmark) for completed fields that passed validation.

**Error message must do three things** (Enders):
1. Convey that an error has occurred
2. State exactly what the error is and where
3. Tell the user how to fix it — in plain, non-accusatory language

Never use vague messages ("Invalid input"). Never use the word "error" alone — be specific. For long forms: provide an error summary at the top of the page with anchor links to each error. Pair all error colours with an icon — never rely on colour alone.

### Rule 5 -- Minimal Friction

Use smart defaults, autocomplete attributes, and auto-formatting (phone, currency). Reduce keystrokes. Never ask for information you already have or can derive.

---

## Additional Guidance

Extended guidance for `form-ux-design` was moved to [references/skill-deep-dive.md](references/skill-deep-dive.md) to keep this entrypoint compact and fast to load.

Use that deep dive for:
- `2. Field Anatomy`
- `3. Field States`
- `4. Essential Code Examples`
- `5. Multi-Step Form Pattern (Wizard)`
- `5b. Gateway Screen (Before Long Forms)`
- `5c. Confirmation Screen (After Submission)`
- `5d. Specific Field Rules (from Enders)`
- `6. Form Submission Workflow`
- `7. Touch Target and Spacing Rules`
- `8. Form DOs and DON'Ts`
- `9. Common Form Types -- Quick Patterns`
- `10. Integration with Existing Skills`
