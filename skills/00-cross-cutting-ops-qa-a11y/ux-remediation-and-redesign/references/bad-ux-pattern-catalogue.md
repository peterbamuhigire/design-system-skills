# Bad-UX Pattern Catalogue and a Worked Hierarchy Fix

Parent skill: [`../SKILL.md`](../SKILL.md) (`ux-remediation-and-redesign`).

**When to read:** when diagnosing an existing product and grouping findings so each can be routed
to the right fix. Findings are organised by *where in the product they appear*, so an auditor can
walk the product from arrival to transaction. Triage the resulting list with
[`triage-matrix.md`](triage-matrix.md).

Thresholds below are working heuristics. Before quoting one to a client, check it against the
engine's doctrine and the current standards (WCAG 2.2; current Core Web Vitals thresholds).

---

## 1. Inputs

| Input | Use |
|---|---|
| The product (live, staging or recordings) | Walk it zone by zone (section 2) |
| Analytics: funnel, abandonment, load times from the field | Locates where findings cost the most |
| Existing audit, if any (`design-audit`) | Avoids duplicate findings |
| For physical or service touchpoints: permission to observe on site | Required for zone F |

## 2. Catalogue by product zone

Walk the zones in order. Log each finding with its zone, type, evidence and the fix route.

### Zone A — Finding your way (navigation and structure)

| Finding type | Check | Fix route |
|---|---|---|
| Labels people do not understand | Tree test: can users pick the right label for a task? | Rename in users' words |
| Categories that do not match how users group things | Open or closed card sort | Regroup to the users' model |
| Deep nesting | Count levels to the key tasks | Flatten; surface frequent tasks |
| Missing breadcrumbs or location cues | Can a user say where they are after a deep link? | Add breadcrumbs and active states |
| Unclear global navigation | First-click test on the home screen | Consistent, labelled global navigation |
| Needless steps | Count steps against the minimum the task requires | Remove or merge steps |

### Zone B — Reading a screen (hierarchy, type, colour, icons)

| Finding type | Check | Fix route |
|---|---|---|
| Size and weight do not match importance | Rank elements by importance; compare with their visual rank | Re-order hierarchy (see section 4) |
| Poor reading sequence | Trace the eye path; does it reach the key item first? | Re-sequence layout |
| Misalignment | Overlay the grid | Align to the grid |
| Line length outside roughly 45-75 characters | Measure a typical line | `fine-typesetting-and-typesetting-qa` |
| Cramped line spacing; body text too small | Inspect computed styles at real sizes | `fine-typesetting-and-typesetting-qa` |
| More than about three typefaces; inconsistent emphasis | Inventory faces and emphasis styles | Reduce to a defined type system |
| Poor contrast | WCAG 2.2 contrast minimums | `accessibility-wcag-2-2-compliance` |
| Meaning carried by colour alone | WCAG 2.2 success criterion 1.4.1 | Add text, shape or pattern |
| Colour used without a strategy; inconsistent colour-coding | Map every colour to one meaning | Define semantic colour roles |
| Unlabelled non-standard icons | Can users name the icon's action unaided? | Icon plus text label |
| Mixed icon styles | Inventory stroke, fill and corner treatment | One icon style |
| Too many icons in one group (more than about seven); decorative overload | Count icons per group; remove any that carry no action or meaning | Group, label or remove |

### Zone C — Understanding the words (content and microcopy)

| Finding type | Check | Fix route |
|---|---|---|
| Vague microcopy; vague calls to action | Does each label name the outcome? | `ux-writing-and-microcopy` |
| Unclear or inconsistent voice | Compare tone across screens | Voice guide |
| Over-long text | Can the key point be found in one scan? | Cut and front-load |
| Features stated instead of benefits | Does the copy say what the user gains? | Rewrite to outcomes |
| Missing instructions | Can a first-time user complete the step without help? | Add inline guidance |
| Jargon | Would the target user use this word? | Plain language |

### Zone D — Completing a transaction (forms, checkout, sign-up)

| Finding type | Check | Fix route |
|---|---|---|
| Too many fields, or fields in a poor order | Field count against what the task needs | Remove, defer or re-order fields |
| No autocomplete; no progress indication | Inspect inputs and multi-step flows | Autocomplete attributes; step indicator |
| Slow load | Load measured in the field, not only in the lab | Performance work |
| Vague calls to action | Action labels name the outcome | Rewrite labels |
| No workable mobile layout | Test at phone width on a real device | Responsive redesign |
| Accessibility barriers in checkout | Keyboard and screen-reader pass of the whole flow | `accessibility-wcag-2-2-compliance` |
| Missing proof (reviews, guarantees, security cues) | Is the trust evidence visible at the decision point? | Place proof beside the action |

### Zone E — Every surface (accessibility)

| Finding type | Check | Fix route |
|---|---|---|
| Not perceivable (missing text alternatives, captions) | Audit against WCAG 2.2 | `accessibility-wcag-2-2-compliance` |
| Not operable (keyboard traps, no focus visibility) | Keyboard-only pass | Same |
| Not understandable (jargon, unpredictable behaviour) | Plain-language and consistency review | Same |
| Not robust (breaks with assistive technology) | Screen-reader pass | Same |

### Zone F — Physical and service touchpoints

| Finding type | Check | Fix route |
|---|---|---|
| Doors, panels, kiosks and counters with no feedback | Observe people using them in place | Add feedback |
| Unclear sequence at a service point | Observe queues and hand-offs in place | Signage, re-ordered steps |

## 3. Validating a fix

| Method | Use when | Measures |
|---|---|---|
| Moderated or unmoderated test, about five users | Any usability fix | Task completion, time on task, errors |
| A/B test | Traffic is enough for significance | Conversion difference |
| Tree test | Navigation or labelling changed | Correct-path rate |
| Before and after analytics | Funnel fixes | Completion and abandonment |
| Short follow-up interviews | Explaining the numbers | Reasons |

A fix succeeds when people complete the task without confusion, not when they say they like it.

## 4. Worked fix: a mobile-money payment confirmation screen

A Kampala school-fees payment app shows a confirmation screen that a parent must read in a few
seconds, often in bright sun at a bank-agent kiosk, while the agent waits.

**Before (diagnosis by ranking):**

| Element | Importance rank | Visual rank before |
|---|---|---|
| Status: payment successful or failed | 1 | 4 (small grey text under the logo) |
| Amount paid (UGX 850,000) | 2 | 3 |
| Pupil name and school | 3 | 5 |
| Transaction ID for the bursar | 4 | 6 (truncated) |
| App logo and promotional banner | 6 | 1 and 2 |
| "Share receipt" action | 5 | hidden in a menu |

The status used green or red colour alone (fails 1.4.1), the logo was the largest item, and the
transaction ID was cut off, so parents photographed the screen and the bursar still could not
match the payment.

**After:** a large status line with icon and word ("Paid" / "Failed — not charged"); the amount
next, bold; pupil, class and school beneath; the full transaction ID in a monospaced face with a
copy action; a visible "Share receipt" button; logo reduced to the footer; banner removed.

**Re-validation:** five parents at an agent kiosk in daylight, each shown a success and a failure
screen for three seconds. Before: two of five correctly reported status and amount. After: five of
five. Bursar match queries fell over the following fortnight.

**Method template (reuse for receipts, tickets, certificates, dashboards and any artefact read
in seconds):**
1. Content audit: list every element.
2. Rank each by criticality to the reader's decision.
3. Compare with the current visual rank; every mismatch is a finding.
4. Re-order hierarchy: size, weight, position and contrast follow criticality.
5. Re-validate with real users under realistic conditions — time pressure, lighting, distance.

## 5. Checks

- [ ] Every zone (A-F) walked, or marked not applicable with a reason.
- [ ] Each finding logged with zone, type, evidence and fix route.
- [ ] Thresholds quoted to a client verified against current standards.
- [ ] Findings triaged with `triage-matrix.md`.
- [ ] Each fix has a named validation method and a success measure.

---

Sources: finding types synthesised from Maioli, L. (2018) *Fixing Bad UX Designs*, Packt, and
the engine's own audit doctrine; the worked example is original.
