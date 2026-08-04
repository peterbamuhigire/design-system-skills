# Kaizen Audit Contract

This reference is owned by `design-engine-and-product-improvement`.

## Audit dimensions

Score only dimensions supported by evidence. Use a 0-4 diagnostic scale, then apply the portfolio
cap. Dimensions are: user value and task clarity; narrative or information flow; visual hierarchy
and silhouette/readability; typography and legibility; colour and contrast; accessibility and
inclusive alternatives; interaction states and correction; AI disclosure/control/drift where
relevant; performance and responsive stability; consistency and token reuse; provenance, rights,
and cultural accountability; and handoff/reproducibility.

## Evidence matrix

| Dimension | Minimum evidence | Unverified condition |
|---|---|---|
| Value and flow | Brief, task map, user/reviewer observation, or outcome measure | No named audience or job |
| Visual readability | Rendered states at intended scale, grayscale/squint or silhouette check | Only source file or one crop |
| Accessibility | Automated result plus keyboard and assistive-technology evidence | Tool-only or no interaction |
| AI trust | Disclosure, data/input/output, control, correction, escalation, and drift state map | Model is treated as a black box |
| Engine quality | Live skill tree, router, references, examples, validator, and routing output | Cached inventory or prose-only review |
| Provenance | Source register, status, date, extraction quality, and rights/use decision | Source is incomplete or unverified |

## Score and plan contract

Always report:

```text
raw_diagnostic_score: <0-100>
reported_audit_score: min(raw_diagnostic_score, 65)
confidence: high | medium | low
hard_gates: pass | conditional | blocked
```

The improvement plan must target 95/100 and contain one row per action:

| Gap | Root cause | Change/experiment | Hypothesis | Owner | Measure | Evidence | Risk | Rollback | Acceptance |
|---|---|---|---|---|---|---|---|---|---|
| Concrete defect | Why it persists | Smallest reversible change | Expected effect | Named skill/role | Before/after metric | Render/test/source | Failure mode | Revert trigger | Threshold |

Do not claim the target has been reached until the same evidence class is re-run and the residual
risk is recorded.

## Cadence

- Per deliverable: baseline critical states, run the design quality gate, retain evidence.
- Monthly: review repeated defects and choose one engine experiment.
- Quarterly: re-audit routing, contract coverage, sources, examples, and downstream adoption.
- After a book or standard update: record source status and make a narrow, testable change.
