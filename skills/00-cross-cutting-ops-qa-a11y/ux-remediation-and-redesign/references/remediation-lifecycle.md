# Reference: The Remediation Lifecycle

The post-audit fix discipline, expressed as five phases. The defining property — taken from
Maioli's *Fixing Bad UX Designs* (2018) and aligned to the Chwezi doctrine — is that this is a
**loop, not a waterfall**: every re-validation that still fails **re-enters at triage**, not at
redesign, because a failed fix means the *priority/approach* was wrong, not just the pixels.

```
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              ▼
DIAGNOSE ──▶ TRIAGE ──▶ REDESIGN ──▶ RE-VALIDATE ──▶ MEASURE ──▶ (ship gate)
  (intake)   (rank)     (lo→hi-fi)   (prove)          (quantify)
              ▲             │             │
              └─────────────┴─────────────┘
              re-enter on: new finding | still-failing re-test
```

Parent skill: `ux-remediation-and-redesign`. Companion: `references/triage-matrix.md` (the engine
inside phase 2).

---

## Phase 1 — Diagnose (intake, do NOT re-audit)

**Entry:** a severity-rated finding list from `design-audit` or `product-design-audit`.
**This phase never re-runs the slop/WCAG/CWV gates** — it consumes their verdicts.

Do three things:

1. **Cluster by root flow and fix domain.** Group findings so related fixes ship as one change
   (all of "signup" together; all "hierarchy" together). A scattered finding-by-finding plan
   re-touches the same screen repeatedly.
2. **Name each finding against the anti-pattern catalogue.** Map every finding to its entry in
   `doctrine/references/interaction-anti-patterns.md` (D1 Flat Hierarchy, B3 Vague CTAs, C2 Silent
   System, A2 Mystery-Meat Nav…). The catalogue's **"fix" column is the target right-pattern** —
   this is what the redesign aims at, so naming it now removes guesswork later.
3. **Carry the gate tag forward.** Each finding that fed a hard gate (AI Slop / WCAG 2.2 AA / CWV,
   per `design-audit/references/audit-rubric.md`) is tagged. Gate-failing findings are pre-flagged
   because they **cap the score** until cleared — the triage will force them to Must.

**Exit:** a clustered, anti-pattern-named, gate-tagged finding list. No prioritisation yet.

---

## Phase 2 — Triage (rank with the matrix)

**Entry:** the named finding list. **Exit:** a ranked fix queue.

This is the core sequencing step; the full method is in `references/triage-matrix.md`. In summary,
each finding passes three lenses — **Travis red-route severity** (Critical/Serious/Minor),
**effort × impact** (quick win / major project / fill-in / thankless), and **MoSCoW**
(Must/Should/Could/Won't) — with two overrides: a **gate-failing finding is always Must**, and
**frequency-weighted** issues outrank one-off sightings. Output: the order fixes will be built.

---

## Phase 3 — Redesign (fix at rising fidelity, against doctrine)

**Entry:** the ranked queue. **Exit:** target-state designs, each annotated with the finding(s) it
closes and the re-validation method it will face.

For each fix, in this order:

1. **Conceptual** — state the intent and the target right-pattern (from the catalogue's fix column).
2. **Lo-fi** — wireframe/structure the change; validate the *structure* cheaply before investing in
   visuals (a tree test for IA, a paper/click-through for a flow).
3. **Hi-fi** — apply the real type, colour, layout, states, and motion via the owning craft skill
   (routed in the SKILL's table).

**Doctrine gate on every redesign** (`doctrine/design-doctrine.md`): state the type/colour/layout
choice; never reach for a banned default (`ai-slop-banned-fonts.md`); prefer the *authored* option.
**A fix that clears one finding but introduces a slop tell or a new gate failure is not a fix** —
it re-enters Phase 2 (triage), because the approach, not the execution, needs rethinking.

---

## Phase 4 — Re-validate (prove it, don't assert it)

**Entry:** the hi-fi redesign. **Exit:** a pass/fail per fix with evidence. A still-failing fix
**re-enters at triage**, not redesign.

The book's standard for "fixed": *the task is completed without confusion **and** the violated
standard now passes* — never "users said they liked it." Pick the method by change type:

| Fix type | Re-validation method | Pass condition |
|---|---|---|
| Flow / hierarchy / findability | **5-user moderated/unmoderated usability test** (Nielsen 5-user floor) | task-completion % up, time-on-task down, error rate down vs baseline |
| Conversion (forms, CTAs, checkout) | **A/B test** where traffic allows; else moderated test | statistically meaningful conversion / CTR uplift, no new drop-off |
| IA / navigation restructure | **Tree test** (+ card sort if labels changed) | findability success rate up; fewer wrong-first-clicks |
| Accessibility | **Automated + manual keyboard + screen-reader** re-check | the *exact* WCAG 2.2 criterion that failed now passes (re-cite it) |
| Performance | **Field CWV re-measure** (CrUX/RUM p75); lab as proxy | LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; back under budget |
| Slop / distinctiveness | re-run `visual-product-slop-audit` + `ai-slop-typography-audit` | the slop gate now PASSES; choice is stated and authored |

Re-validation **is the gate clearance**: re-assert the specific failing criterion/threshold, don't
just claim "a11y improved."

---

## Phase 5 — Measure (quantify the uplift, close the loop)

**Entry:** passed re-validations. **Exit:** a before→after report + handoff.

Compare against the **baseline captured before the first edit** (Required Inputs). Report:

- **Audit-score delta** — the 0–100 from the rubric, and explicitly **which cap lifted** (e.g.
  "≤59 slop+a11y cap cleared → 88").
- **Task metrics** — completion %, time-on-task, error rate, before→after.
- **Product KPIs** — funnel completion, bounce, session duration, conversion, before→after.
- **Summary instrument** — SUS (usability), NPS (loyalty), or HEART task-success — one number a
  stakeholder can read.

Present as a single **before→after table**. Then **close the loop**: hand the re-built, re-validated
artifact to `design-qa-and-pre-launch-review` for the pass/fail ship sign-off, and route any
*newly surfaced* findings back to `design-audit`. The lifecycle only ends when the gate signs off.

---

## The loop discipline (why this is not a checklist)

- A fix that re-validates **fail** does not get "polished" — it returns to **triage**, where its
  priority and approach are reconsidered (maybe the right-pattern was wrong, maybe effort was
  underestimated). This is the single most-skipped step and the book's central correction.
- A redesign that opens a **new** finding (a slop tell, a broken red route, a fresh gate failure)
  is itself a new finding → back to diagnose/triage. Net quality must go up, never sideways.
- The loop terminates at the **ship gate**, not at "we made the change."

---

*Provenance: Maioli, *Fixing Bad UX Designs* (2018), 5-phase diagnose→fix→measure method, updated
to 2026 — WCAG 2.2 re-check, field-p75 CWV, and the Anti-Slop Charter folded into Phases 3–4.
Composes `design-audit/references/audit-rubric.md` (the score/gates it consumes) and
`doctrine/references/interaction-anti-patterns.md` (the right-patterns it aims at).*
