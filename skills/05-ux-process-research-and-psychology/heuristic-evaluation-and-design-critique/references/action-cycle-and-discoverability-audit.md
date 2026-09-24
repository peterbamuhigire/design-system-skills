# Action-Cycle and Discoverability Audit

Parent skill: [`../SKILL.md`](../SKILL.md) (`heuristic-evaluation-and-design-critique`).

**When to read:** when a heuristic walkthrough needs to explain *why* a step fails, not only which
Nielsen heuristic it breaks; when a screen "looks clean" but people hesitate, tap the wrong thing
or cannot tell whether an action worked; when a control, gesture or hardware-adjacent interaction
(scanner, POS keypad, card reader, printer) is involved; and when a critique must say whether the
fix is a signifier, a mapping, a constraint or a feedback change.

This is an **inspection rubric**. It predicts suspected problems from expert judgement. It does
not measure task success, time or error rates; those come from
`ux-research-and-usability-testing`. Accessibility conformance comes from
`accessibility-wcag-2-2-compliance`. Keep all three verdicts separate in the report.

---

## 1. Inputs

| Input | Why it matters | If missing |
|---|---|---|
| The task, stated as the user's goal ("pay this term's school fees") | The action cycle starts from a goal, not a screen | Ask; do not audit screens without a task |
| Every step of the flow, including states after each action | Evaluation failures only show after an action | Mark post-action steps `NOT_ASSESSED` |
| Who the user is and what they already know | Discoverability is relative to prior knowledge and convention | State the assumed user explicitly |
| Device, input method and environment | Mappings and signifiers differ for touch, keypad, mouse, glare, noise | Default to the lowest-capability realistic device |

## 2. Two gulfs, seven questions

Every step a person takes crosses two gaps. The **execution gap** is the distance between what
they want and knowing what to do. The **evaluation gap** is the distance between what happened
and knowing whether it worked. A design closes the first with *feedforward* (signifiers,
constraints, mappings, a legible conceptual model) and the second with *feedback*.

Walk every step of the red-route task and answer the seven questions **as the user would**:

| # | User's question | Side | What must be present for "yes" | Typical defect signature |
|---|---|---|---|---|
| Q1 | What am I trying to achieve here? | Goal | The screen names the job in the user's words | Screen titled by system object ("Transaction entity") |
| Q2 | What are my options? | Execution | Alternatives are visible or one obvious step away | Key path hidden in overflow menu or long-press only |
| Q3 | What can I do right now? | Execution | Available and unavailable actions are distinguishable; disabled states explain why | Everything looks tappable, or nothing does |
| Q4 | How do I do it? | Execution | The control's form and label say how to operate it | Swipe-only action with no visible cue |
| Q5 | What happened? | Evaluation | Immediate, perceivable response at the point of action | Spinner with no text; silent save; toast off-screen |
| Q6 | What does it mean? | Evaluation | The new state is described in the user's terms | "Status: 2" or a colour change with no label |
| Q7 | Am I done? Is this okay? | Evaluation | Explicit completion and a durable record (receipt, reference) | Flow ends on a blank dashboard |

Record a **No** or **Partly** for any question as a finding. Name the side (execution or
evaluation); the fix family follows from it.

## 3. Seven-principle audit rubric

For each step, score each principle **Pass / Weak / Fail** with evidence. A Weak or Fail becomes a
finding card in the parent report's format.

| Principle | Pass looks like | Fail looks like | Fix family |
|---|---|---|---|
| **Discoverability** | A first-time user can find the possible actions and the current state without instruction | Features found only by accident, a tour, or support calls | Surface the action; reorder by frequency; label |
| **Feedback** | Every action is acknowledged within about 0.1 s and completion or failure is stated; feedback is prioritised, not a flood | No response, delayed response, or so many beeps and toasts that none is noticed | Inline acknowledgement, progress with text, outcome message, one channel per event |
| **Conceptual model** | The user can predict what an action will do and explain where their data "lives" | Surprise outcomes; people invent wrong theories ("it saves only when I go back") | Show the model: previews, summaries, visible states, consistent object names |
| **Affordance** | The action is physically possible for this user on this device (reach, target size, input method) | Control too small, beyond thumb reach, or needs a gesture the device lacks | Resize, relocate, add an alternative input path |
| **Signifier** | A perceivable cue says *where* and *how* to act (label, shape, underline, handle, button form) | Flat text that is secretly a button; a button-styled label that does nothing (false signifier) | Real control styling for real controls only; remove false signifiers |
| **Mapping** | Controls sit next to, and move in the same direction as, what they affect; order matches the world's order | A list of toggles unrelated to the layout they control; "next" arrow that goes back in time | Co-locate control and effect; spatial or sequential correspondence |
| **Constraints** | Invalid actions are impossible or clearly blocked; physical, logical, semantic and cultural cues limit choices | Free text where a picker belongs; impossible dates accepted; order of steps unenforced when order matters | Pickers, masks, disabled-with-reason, step gating, forcing functions (see error reference) |

Add one cross-cutting check: **knowledge in the world versus in the head.** List every fact the
user must remember to complete the task (a code from a previous screen, a till number, which of
two similar icons means what). Each remembered item is a risk; move it onto the screen unless the
user is a trained expert operating at speed, and then still keep it retrievable.

## 4. Severity anchors for this rubric

Use the parent skill's 0-4 scale (`severity-scoring.md`). These anchors keep ratings consistent:

| Pattern | Default severity | Raise when | Lower when |
|---|---|---|---|
| Evaluation gap on a money, health, legal or data-loss step (user cannot tell whether it worked) | 4 | - | A durable receipt arrives by another channel within seconds |
| False signifier on a primary path | 3 | It triggers an irreversible action | It is on a rarely used screen |
| Missing signifier for a primary action (hidden gesture, unlabeled icon) | 3 | No alternative path exists | A visible alternative exists one step away |
| Poor mapping between control and effect | 2 | Mis-selection causes a wrong transaction or record | Selection is previewed before commit |
| Weak conceptual model (users can operate but mispredict) | 2 | Misprediction causes data loss or duplicate payment | Undo is available and visible |
| Missing constraint allowing invalid input caught later | 2 | Invalid input reaches a commit step | Inline validation catches it at the field |
| Feedback flood (competing toasts, badges, sounds) | 2 | A critical alert is lost among routine ones | - |
| Memory burden on a novice path | 2 | Item must be recalled across an interruption (a call, an agent queue) | Item is always visible |

Severity is still frequency x impact x persistence. The anchors are starting points, not overrides.

## 5. Procedure

1. Write the goal in the user's words and list every step, including system responses.
2. For each step, answer Q1-Q7 (section 2). Capture a screenshot or state description per answer.
3. For each step, score the seven principles (section 3) and run the memory check.
4. Convert every No/Weak/Fail into a finding card: location, question failed, principle failed,
   evidence, consequence for this user, severity with rationale, fix family.
5. Cross-reference to the Nielsen and Tognazzini codes in `heuristics-catalog.md` so the finding
   merges cleanly with the rest of the evaluation (Q5-Q7 usually map to N1; signifier and
   constraint failures to N5 and N6; conceptual model to N2 and N4).
6. Before proposing a fix, ask how the defect arose (a component reused out of context, an API
   status leaking into UI copy, a platform default). Fixes that address the cause stop the defect
   returning elsewhere.
7. Name the strongest step too. The report must say what already closes the gulfs well.

## 6. Output line format

```
F7 | Step 4 "Confirm payment" | Q6 What does it mean? (evaluation) | Feedback: Weak; Conceptual model: Fail |
Evidence: after tapping Pay, badge reads "PENDING-2"; no explanation; no reference number |
Consequence: parent pays again at the bank, double payment | Severity 4 (frequent, money, persistent) |
Fix family: outcome message in plain words + reference number + SMS receipt + "what happens next"
```

## 7. Worked example (original)

**Context.** A Kampala secondary school's parent portal on a mid-range Android phone. Task: "Pay
Term II fees for my daughter using mobile money."

| Step | Finding | Question / principle | Severity |
|---|---|---|---|
| Home | Fee balance shown as "UGX -1,450,000" in red with no label | Q6 / conceptual model: negative sign reads as a refund to some parents | 3 |
| Student picker | Two children listed by admission number only | Q3 / signifier and memory: parent must remember which number is which child | 2 |
| Amount | Free-text amount field accepts "1450000" and "1,450,00" alike | Constraints: no format mask or sensibility check against balance | 3 |
| Pay | Button reads "Proceed"; next screen is the operator's PIN prompt | Q4 / signifier and mapping: the parent does not know money is about to leave | 3 |
| After PIN | Screen returns to Home with no message; balance updates two minutes later | Q5-Q7 / feedback: evaluation gap on a money step | 4 |

**Fix set.** Label the balance "Still to pay: UGX 1,450,000"; show children by name and class with
a photo initial; amount picker defaults to the outstanding balance with "Pay part" as a secondary
choice and a check against overpayment; button reads "Pay UGX 1,450,000 with mobile money";
after the PIN step, a pending state that says "Waiting for confirmation from your mobile money
provider" followed by a success screen with school reference and an SMS receipt.

**What already works.** The school's crest and name appear on every screen, a strong trust cue
for parents paying money into a portal they did not choose. Preserve it.

## 8. Premium versus generic output

| Generic AI critique | Senior critique |
|---|---|
| "Improve affordances and feedback." | Names the step, the question the user cannot answer, the principle that failed, and the exact change |
| Treats every issue as a visual polish issue | Separates execution fixes (signifiers, mapping, constraints) from evaluation fixes (feedback, state description) |
| Rates severity by how ugly it looks | Rates by consequence on the task, especially money, health and data |
| Blames the user ("users should read the label") | Treats repeated user error as a design signal and traces its cause |
| Claims "usability validated" | States: expert inspection only; confirm Severity 3-4 with task testing |

## Evidence and currentness

Concept inputs (durable): Norman (2013) *The Design of Everyday Things*, revised and expanded
edition, Basic Books (action cycle, gulfs, discoverability principles, knowledge in the world);
Nielsen (1994, refined) usability heuristics as carried in `heuristics-catalog.md`. No platform
version, threshold or standard is asserted here beyond the 0.1 s acknowledgement convention,
which is a long-standing human-factors rule of thumb, not a standard. Access date 2026-09-24.
Measured task data, assistive-technology behaviour and render proof remain `NOT_ASSESSED` unless
the audit record attaches them.
