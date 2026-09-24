# Human-AI Collaboration and Trust Calibration

Parent skill: [ai-agent-ux](../SKILL.md). Load this reference when designing how people decide
together with an AI: how much the AI explains, how confidence is shown, how the person overrides
or hands off, how persona and warmth are dialled, and how the design is evaluated for appropriate
reliance rather than for acceptance. Output formatting and citations stay with `ai-output-design`;
the verifiable requirement wording lives in the SRS engine
(`02-requirements-engineering/14-ai-feature-prd-spec/references/human-ai-collaboration-requirements.md`).

## 1. Design goal: calibrated trust, not maximum trust

The interface succeeds when people rely on the AI where it is right and override it where it is
wrong. Two failures to design against:

- **Over-reliance (automation bias):** users accept output without checking; worsens under time
  pressure, with fluent prose, with human-like personas, and when the AI speaks first.
- **Under-reliance (algorithm aversion):** users dismiss good output, often because of the "AI"
  label, one visible early mistake, or loss of control.

Every pattern below should move reliance toward accuracy, and the evaluation in section 6 proves it.

## 2. Choose the collaboration posture per surface

| Posture | Interface shape | Wrong choice causes |
|---|---|---|
| Assist (optional help) | Suggestions inline, dismissible with one action, never modal | Nagging overlays that users learn to ignore |
| Augment (human decides with AI input) | Human's workspace first; AI panel secondary; judge-first option for consequential calls | AI recommendation anchors the decision |
| Cooperate (AI does bounded sub-tasks, human reviews) | Review queue with diff of AI changes, bulk accept only for low-risk items | Rubber-stamping large batches |
| Delegate (AI acts under policy) | Activity feed, preview before irreversible actions, global pause, undo window | Invisible actions and lost accountability |

## 3. Pattern decisions

**Explanation depth**

| Situation | Pattern |
|---|---|
| Fast, repeated, low-stakes decisions | One-line reason or none; details on demand |
| User must justify the decision to someone else | Top 2-3 factors in domain language, plus a "why not the alternative" comparison |
| Expert user checking the model | Expandable detail: data sources, date, factors, counter-evidence |
| Explanation would expose other people's data or protected logic | Explain the data category and purpose, not the values |

Default to partial, progressive explanation. Long rationales raise perceived complexity and can
lower appropriate trust; walls of reasoning are also a slop tell.

**Confidence display**

| Evidence available | Show |
|---|---|
| Calibrated model with measured accuracy per band | Categorical bands (High / Medium / Low) with a stated action per band |
| Ranking or generation without calibration | N-best alternatives or evidence and sources; no percentages |
| Expert audience with calibrated intervals | Range or interval visual, labelled in plain language |
| Model below abstention threshold | "Not enough to go on" state with the manual path, not a guess |

**Anchoring control.** For consequential Augment decisions offer judge-first: the person records a
view, then the AI's view appears with where they differ. Alternatively delay the AI panel until the
person has opened the underlying record. Do not use judge-first on trivial suggestions; it adds
friction without benefit.

**Override and correction.** Accept, edit, reject and dismiss sit where the output sits, one action
away. After an override, show that it stuck ("Your value will be used; the assistant will not change
it") and never let a later AI pass silently revert it.

**Handoff.** Escalation to a person carries the conversation, the AI outputs shown and the user's
inputs; the receiving agent's screen shows them. Tell the user who they are now talking to, and
the expected wait.

**Persona and warmth.** Keep the assistant voice competent and neutral for work and finance
tasks. No claims of feelings, no human names or faces implying a person, no affection or urgency to
steer choices. Warmth may rise for supportive contexts (health information, onboarding), but
capability disclosure must stay visible. Over-humanisation erodes perceived professionalism and
raises privacy discomfort.

**Sensitive disclosure.** Chat invites oversharing. When a user types health, money, identity or
family details the task does not need, show a quiet notice of what is kept and for how long, and an
option to remove it.

**Change over time.** When the model, policy or behaviour changes, notify users in context and
explain what differs; adapt cautiously rather than silently re-ranking familiar results.

## 4. Mapping to current industry guidance

| Pattern above | Microsoft HAX guideline | Google PAIR chapter |
|---|---|---|
| Capability and limit disclosure | G1, G2 | Mental Models |
| Explanation depth | G11 | Explainability + Trust |
| Confidence bands, N-best, abstention | G2, G10 | Explainability + Trust; Errors + Graceful Failure |
| One-action dismiss, correct, override | G8, G9 | Feedback + Control |
| Global pause and settings | G17 | Feedback + Control |
| Change notification, cautious adaptation | G14, G18 | Mental Models |
| Social norms, bias, persona | G5, G6 | User Needs + Defining Success |
| Consequences of feedback | G15, G16 | Feedback + Control |

Apple's HIG publishes a Generative AI page; when shipping on Apple platforms, read it directly and
record its guidance in the design evidence (its detailed wording was `NOT_ASSESSED` in this pass).

## 5. Inclusion and localisation

- AI output must be navigable by screen readers: clear start and end of each response, labelled
  copy, edit, regenerate and rate controls, and streaming announced politely rather than word by
  word.
- Evaluate each supported language separately; East African products often need English plus
  Luganda, Swahili, Kinyarwanda or Runyankore. Truncated or awkward output in one language is a
  design defect, not a model footnote.
- Low-bandwidth: stream text before images; allow a text-only explanation view.

## 6. Evaluating the design

Measure reliance, not delight.

| Measure | How | Target direction |
|---|---|---|
| Over-reliance rate | Share of wrong AI outputs accepted (seed known-wrong cases in tests) | Down |
| Under-reliance rate | Share of correct AI outputs rejected | Down |
| Override success | Time and errors to correct a wrong output | Down |
| Explanation usefulness | Task: "Which factor would change this result?" answered correctly | Up |
| Mental-model accuracy | Users predict when the AI will fail | Up |

A rising acceptance rate on its own is not success. Run these in moderated sessions with seeded
errors before launch; in production, rely on the SRS reliance logging.

## 7. Anti-patterns and corrections

- "94% confident" badge on a language-model answer. Correction: evidence or bands backed by
  calibration.
- AI suggestion pre-filled into the decision field. Correction: separate panel; explicit accept.
- Friendly named avatar for a loan-screening aid. Correction: neutral tool identity, visible limits.
- Handoff that restarts the conversation. Correction: transfer context and show it to both sides.
- Success dashboard showing only acceptance rate. Correction: add over- and under-reliance.

## 8. Worked example (original)

A Kampala clinic triage assistant for nurses. Posture: Augment. The nurse records vitals and an
initial priority before the assistant shows its suggested priority (judge-first). The suggestion
shows a band and two reasons ("temperature 39.4 C; child under five"). When the nurse disagrees, a
single tap records her choice; the case never reverts. Seeded-error sessions with eight nurses show
over-reliance at 1 of 16 wrong suggestions, down from 6 of 16 in the prototype that showed the
suggestion first. The assistant has no name or face and says "Suggested priority", never "I think".

## Evidence/currentness

Access date 2026-09-24. Verified: Microsoft HAX Toolkit 18 Guidelines for Human-AI Interaction
(G1-G18 titles from the HAX design library); Google PAIR People + AI Guidebook chapters and its
confidence-display options (categorical, N-best, numeric, visualisation) and partial-explanation
advice. NOT_ASSESSED: Apple HIG Generative AI detailed wording; any product's calibration data.

Sources: Wu & Liang (eds.) (2026) *Human-AI Interaction and Collaboration*, Cambridge University
Press; Amershi et al. (2019) Guidelines for Human-AI Interaction (CHI); Google PAIR (2021)
*People + AI Guidebook*.
