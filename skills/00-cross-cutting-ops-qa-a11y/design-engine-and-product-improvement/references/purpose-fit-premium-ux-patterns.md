# Purpose-fit premium UX patterns

Parent skill: [Design Engine And Product Improvement](../SKILL.md).

This reference turns three Eleken articles into a small, evidence-bearing design method. The
articles are inspiration and practitioner commentary, not standards or proof of an outcome. Use
their patterns to generate hypotheses; use the client's evidence, human design judgement, and
authoritative accessibility guidance to make the final decision.

## Source and currentness boundary

| Source | Accessed | Tier and use | Disposition |
|---|---|---|---|
| [18 UX Improvements That Move Product Metrics](https://www.eleken.co/blog-posts/ux-improvements) | 2026-09-08 | Tier 5 practitioner article; friction hypotheses | Use patterns, not its reported results or implied universality |
| [16 Best Dashboard Design Examples](https://www.eleken.co/blog-posts/dashboard-design-examples-that-catch-the-eye) | 2026-09-08 | Tier 5 practitioner article; dashboard composition prompts | Use as a prompt library, not as a chart standard |
| [Compelling Design Takes More Than “Making It Like Stripe”](https://www.eleken.co/blog-posts/making-it-like-stripe) | 2026-09-08 | Tier 5 practitioner article; originality and craft method | Use the principle of purpose-fit authorship; do not copy Stripe's surface language |
| [WAI-ARIA Dialog Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/) | 2026-09-08 | Tier 1 authoritative accessibility guidance | Current interaction reference; verify support in the target stack |
| [WCAG 2.2 Error Identification](https://www.w3.org/WAI/WCAG22/Understanding/error-identification) | 2026-09-08 | Tier 1 authoritative accessibility guidance | Current form-error reference; scope to the target conformance claim |
| [MDN `prefers-reduced-motion`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/%40media/prefers-reduced-motion) | 2026-09-08 | Tier 2 technical reference | Current browser capability reference; validate the supported browser matrix |

Model-currentness review: official provider pages reviewed 2026-09-08. The installed policy check
reported `DRIFT: root model policy drift` and actual account entitlement was not exposed to this
audit, so runtime availability is `NOT_ASSESSED`. Retain the explicit Astra-orchestrator and
Luna-execution decision already authorised by Peter; do not silently change it.

## The premium UX brief

Before choosing a pattern, create this short brief. A missing field is an evidence gap, not an
invitation to fill it with a fashionable visual style.

| Field | Required decision |
|---|---|
| Client and audience | Who is using this, with what knowledge, pressure, device, locale, and access needs? |
| Primary job | What must the person understand, decide, create, or recover from? |
| Product truth | What data, content, service promise, or constraint makes this product different? |
| Visual thesis | One sentence describing the intended feeling and hierarchy in service of the job |
| Signature choice | One distinctive, defensible choice that belongs to the client and earns its place |
| Reference translation | Principle borrowed, surface treatment rejected, and why |
| Critical states | Empty, loading, error, recovery, success, permission, long-content, and interruption states |
| Proof | Real-content demo or render, interaction review, accessibility evidence, performance evidence, and owner |

The brief prevents two opposite failures: a usable but generic interface and an expressive
interface that makes the user's work harder. Premium is the intersection of purpose, authorship,
clarity, and finish.

## Pattern families and audit prompts

### 1. Remove avoidable entry friction

Use upload/import, sensible defaults, progressive disclosure, grouped sections, and short guided
steps when the task evidence shows that manual entry or a long undifferentiated form is the main
barrier. Keep a manual path, editable extracted values, saved progress, and recovery where the
task can fail.

Audit prompts:

- Can existing information be imported without removing user control?
- Does each step have one decision and a visible end state?
- Are fields grouped by the user's mental model, not the database schema?
- Does validation identify the field, describe the problem in text, and give the next move?
- Is the first action obvious without forcing an unnecessary click?

### 2. Make navigation and context visible

Expose high-frequency filters, active-filter chips, search, and primary actions where the user's
existing conventions predict them. Use a sidebar when the information architecture has outgrown a
top row, but do not turn a small product into a heavy admin shell. Keep the current entity,
selection, and return path visible when opening details.

Audit prompts:

- Can a returning user reach the primary job from the first viewport?
- Are applied filters, scope, date range, and permissions visible at the point of decision?
- Does a detail view preserve enough context to return without reconstructing the task?
- Is a hover-only explanation duplicated by focus, tap, or inline content where it is essential?

### 3. Design dashboards as decision surfaces

Do not start with a chart catalogue. Start with the decisions the audience must make. Classify
the surface as operational, analytical, strategic, or a deliberate combination, then give each
level a role:

1. **Signal:** the few measures that answer “what needs attention?”
2. **Explanation:** trends, comparisons, or drivers that answer “why?”
3. **Action and detail:** filters, records, definitions, and drill-down that answer “what next?”

Use cards, tables, charts, tabs, or side panels only when the encoding matches the question. A
five-second scan can be a useful hypothesis for the first signal, but it is not a universal
standard; test comprehension with the actual audience. A dashboard may be visually bold or quiet,
but the visual emphasis must preserve data meaning and decision priority.

Audit prompts:

- Can the audience identify the primary signal and its period, unit, and comparison?
- Does every chart have a question, a suitable encoding, an empty state, and a data-quality note?
- Are colour, shape, labels, and ordering redundant enough that meaning is not colour-dependent?
- Are secondary metrics available without making the first view a warehouse of everything?
- Can users customise a view without losing a reliable default or shared interpretation?

### 4. Preserve flow while showing detail

Use a modal, popover, side panel, or inline expansion for a quick inspection or small edit when
the current context matters. Use a full page when the detail is deep, linkable, or requires its
own navigation. A shorter flow is not automatically better: combine steps only when their
decisions are independent and the page remains scannable.

For modal detail, apply the current WAI-ARIA dialog guidance: move focus into the dialog, contain
keyboard navigation, close with Escape, and return focus to the invoking control or a logical
successor. Treat these as implementation acceptance checks, not visual decoration.

### 5. Make waiting, progress, and correction legible

Replace an unexplained wait with stage-aware status when the system can truthfully expose stages.
Use a determinate step count when the flow has known steps. If the system cannot know progress,
say that honestly and provide cancellation, retry, or safe continuation. Never use rotating copy
as theatrical filler.

Audit prompts:

- Does the message describe a real stage or the next available action?
- Can the user distinguish waiting, success, partial completion, failure, and retry?
- Does progress survive interruption where the task is costly?
- Are animated transitions reduced or replaced when the user requests reduced motion?

### 6. Finish the authored system

Premium craft is visible in the details that make the system coherent: type pairing and scale,
spacing rhythm, data density, copy, icon meaning, state transitions, focus treatment, empty-state
composition, responsive reflow, and the last 10% of edge cases. The finish pass follows a purpose
thesis; it does not add decoration to compensate for an unresolved job.

Use the creative-selection loop: build a real slice with real content, review it in context,
make one deliberate variation, live with the slice long enough to notice friction, and record
what survived selection. Metrics inform task outcomes; they do not choose the signature visual
decision for the designer.

## Decision table

| Evidence | Choose | Avoid |
|---|---|---|
| Repeated manual entry with a trustworthy source document | Import/upload plus editable confirmation | Forced transcription or opaque extraction |
| A dashboard has one high-frequency operational decision | Signal-first overview with drill-down | Equal-weight card mosaic |
| A dashboard serves materially different jobs | Tabs or role-specific views with a stable shared vocabulary | One overloaded screen |
| Detail is quick and context-dependent | Modal, popover, or side panel with focus recovery | New page that discards task context |
| Process stages are known and meaningful | Numbered stepper and stage-aware status | Spinner with invented progress |
| The reference look is recognisable as another product | Extract the user principle and create a new visual thesis | Copying gradients, diagonals, layouts, or copy |
| The visual choice is expressive but harms comprehension or access | Narrow or remove the expression | Calling novelty premium by default |

## Minimum evidence slice

For each adopted improvement, retain one record with:

```text
client_and_audience:
primary_job:
observed_friction:
visual_and_experiential_thesis:
signature_choice:
pattern_or_change:
baseline_measure:
hypothesis:
critical_states_reviewed:
accessibility_and_responsive_checks:
after_measure_or_reasoned_review:
rollback_trigger:
owner_and_reaudit_date:
```

Acceptance requires the named source or observation, a real-content demo or render, the relevant
state and accessibility checks, and a recorded human design decision. If a render, user result,
or target-platform check is unavailable, mark that evidence `NOT_ASSESSED` and keep the change
conditional.

## Anti-patterns

- **“Make it like Stripe.”** Extract the underlying job, clarity, or craft principle; create a
  client-specific thesis and reject the recognisable surface treatment.
- **Dashboard as chart wallpaper.** Tie every visual to a decision, unit, period, comparison, and
  action; remove visuals that do not earn a place.
- **Premium as decoration.** Use expressive colour, motion, imagery, or type only when it improves
  comprehension, trust, recognition, or emotional fit.
- **Five-second rule as a score.** Use scan time as a test hypothesis, not as a universal pass
  threshold detached from audience and task complexity.
- **Spinner theatre.** Show truthful stages or honest waiting; never invent progress to disguise a
  slow operation.
- **Hover as the only explanation.** Provide keyboard, touch, inline, or accessible equivalents
  for essential information.
- **Polish before purpose.** Stop the finish pass when the user job, hierarchy, or failure path is
  still unclear; route back to discovery or requirements.

## Worked example

For a clinic operations dashboard, the brief might name a care coordinator who must spot overdue
follow-ups during a busy shift. The thesis could be “calm clinical triage with one unmistakable
next action.” The signature choice might be a restrained amber attention rail paired with plain
language and a compact timeline, rather than a copied gradient or a wall of colourful cards. The
acceptance record would show the overdue signal, its date range and definition, an empty state,
keyboard and reduced-motion checks, a narrow viewport layout, and a before/after task-comprehension
measure. Without those artefacts, the visual direction remains a proposal, not a world-class
result.
