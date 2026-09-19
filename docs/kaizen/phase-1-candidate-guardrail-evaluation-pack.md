# B15-A02 — Candidate, guardrail, and evaluation pack

Status: IMPLEMENTED EVALUATION CONTRACT. It supports a reversible design
experiment and cannot turn a candidate into a standard without retained evidence
and an accountable reviewer decision.

## Candidate register

| ID | Candidate and user job | Hypothesis | Surface/state | Owner/status |
|---|---|---|---|---|
| C-001 | Make the primary task action visually dominant | Clear hierarchy reduces hesitation and wrong-path activation | Normal, focus, error, mobile | Design owner / proposed |
| C-002 | Replace decorative status colour with label plus icon/pattern | Redundant cues improve comprehension and colour-independent use | Success, warning, error, dark mode | Design + accessibility / proposed |
| C-003 | Keep advanced controls collapsed by default | Progressive disclosure reduces scan cost without hiding recovery | Normal, keyboard, empty, error | Product owner / proposed |

The examples are candidate hypotheses, not measured outcomes. Real content,
target devices, and a named audience must be attached before evaluation.

## Guardrail register

| Guardrail | Minimum evidence | Failure action |
|---|---|---|
| Task clarity | Brief and observable success criterion | Narrow candidate or stop |
| Perceptual hierarchy | Render at intended scale plus grayscale/squint inspection | Rework; do not standardise taste |
| Accessibility | Automated sweep plus keyboard and assistive-technology evidence | Block release on applicable AA failure |
| State completeness | Loading, empty, error, success, recovery, offline where applicable | Add missing state or mark unassessed |
| Responsive stability | Mobile and target-width renders, 320px/200% spot checks | Stop if content or action is lost |
| Privacy and AI trust | Input/output, disclosure, correction, escalation, and data-use map where relevant | Quarantine unsafe candidate |
| Provenance and rights | Source identity, licence/use status, and authored rationale | Remove asset or block handoff |
| Reversibility | Prior version, token/source identity, rollback owner and trigger | Do not run experiment |

## Evaluation protocol

1. Record the baseline and candidate with the same real or explicitly fictional
   content, viewport, state, and type/palette choices.
2. Capture the source identity, rendered output, interaction trace, and reviewer
   notes. A source file alone is not render evidence.
3. Evaluate task success, wrong-path events, comprehension, keyboard completion,
   focus visibility, screen-reader names/states, target size, reflow, contrast,
   reduced motion, and implementation variance.
4. Separate observation, inference, preference, and unassessed evidence.
5. Apply the decision rule: `ACCEPT`, `ACCEPT_WITH_CAVEATS`, `REVISE`, `REJECT`,
   or `NOT_ASSESSED`. Record the rollback and next review date.

## Minimal score sheet

| Dimension | Baseline | Candidate | Evidence | Confidence |
|---|---:|---:|---|---|
| Task completion |  |  | Trace or observed review |  |
| Comprehension |  |  | Prompted explanation or review |  |
| Visual hierarchy |  |  | Render and grayscale inspection |  |
| Accessibility |  |  | Automated + manual evidence |  |
| Responsive stability |  |  | Device/viewport captures |  |
| Handoff/reuse |  |  | Token/source/variance record |  |

Do not average away a hard gate. A failed applicable accessibility, privacy,
rights, or recovery guardrail blocks standardisation even when the candidate
looks better.

