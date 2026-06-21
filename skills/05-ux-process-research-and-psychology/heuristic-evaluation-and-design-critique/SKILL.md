---
name: heuristic-evaluation-and-design-critique
description: Use when you need a structured, expert-led heuristic evaluation or design critique of
  an existing interface or flow — walking a UI against Nielsen's 10 usability heuristics and
  Tognazzini's first principles, capturing each violation with a screen reference, the heuristic
  it breaks, evidence, and a 0–4 severity rating. Triggers — "heuristic evaluation", "expert
  review", "usability inspection", "design critique", "Nielsen heuristics", "Tognazzini /
  first principles of interaction design", "rate the severity of this usability problem",
  "walk this screen/flow and find the usability issues", "discount usability method", "review
  this UI without testing users". This is the inspection (no-users) evaluation method; pair it
  with `design-audit` (the scored 0–100 artifact rubric).
status: active
metadata:
  portable: true
  category: 05-ux-process-research-and-psychology
  compatible_with:
    - claude-code
    - codex
---

# Heuristic Evaluation & Design Critique

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- You need an **expert usability inspection** of a built or prototyped UI **without recruiting
  users** — the "discount usability" method: 3–5 evaluators independently walk the interface
  against a shared set of heuristics, then merge findings.
- You want a **structured design critique** that is defensible — every comment tied to a named
  heuristic and a severity rating, not to taste or "I'd have done it differently."
- You have screens, a flow, a Figma file, or a live URL and want a **prioritised list of
  usability violations** with locations, evidence, and 0–4 severities to feed a fix backlog.
- You are reviewing early, before usability testing, to **cheaply remove the obvious violations**
  so user tests spend their budget on the subtle, behaviour-only problems.

## Do Not Use When

- You need a **scored 0–100 quality rubric** across visual hierarchy, slop, performance,
  typography, etc. → use `design-audit` (the scored artifact audit; this skill is the
  heuristic-walkthrough method, not a numeric grade).
- You need a **ship go/no-go gate** with spec/pixel parity → use `design-qa-and-pre-launch-review`.
- You need to **observe real users** completing tasks → use
  `ux-research-and-usability-testing` (inspection finds *suspected* problems; testing finds
  *actual* ones — they are complementary, not substitutes).
- You have an audit's findings and need to **redesign, re-validate, and measure the uplift** →
  use `ux-remediation-and-redesign` (the fix side).

## Required Inputs

- **The artifact** — screens, screenshots, a prototype, a flow, or a URL, ideally covering the
  product's red-route tasks (sign-up, core task, checkout) end to end.
- **Context** — who the users are, their tech literacy, the platform (web / iOS / Android /
  desktop), the design system if any, and the brand personality. Heuristics are interpreted
  *against* the user's mental model, so this is not optional.
- **Evaluator count** — ideally 3–5 independent evaluators (Nielsen: ~5 evaluators surface
  ~75% of usability problems; one finds only ~35%). A single evaluator pass is still valuable
  but state the coverage limitation in the report.

## Workflow

The evaluation is a **structured walkthrough**, not a free-form opinion. Run it in seven steps.

1. **Frame the evaluation.** State the user, task, platform, and brand context. List the
   **red-route tasks** to be walked (the critical paths). Confirm the heuristic set:
   Nielsen's 10 + Tognazzini's first principles (`references/heuristics-catalog.md`).
2. **Two-pass walkthrough (Nielsen's recommendation).** Walk each screen/flow **twice**: pass
   one to get a feel for the flow and scope; pass two to inspect each element slowly against
   every heuristic. Walk the red routes as tasks, not just static screens — a violation often
   only appears mid-flow (a missing "you are here", a silent save, a dead end).
3. **Detect against the heuristic catalogue.** For each screen/element, check it against all of
   Nielsen's 10 and the relevant Tognazzini principles. Cross-walk the behavioural
   anti-patterns in `doctrine/references/interaction-anti-patterns.md` (A1–E3) — any match is a
   heuristic violation (e.g. an interrupting "Done" modal = C1 Idiot Box = breaks Nielsen #8
   *Aesthetic & minimalist design* and Tognazzini *Efficiency of the user*).
4. **Capture evidence for every finding.** A finding is not a finding without: **(a) location**
   (screen + element), **(b) the heuristic violated** (by name/number), **(c) what is wrong**
   (observed, specific), **(d) evidence** (the screenshot, the measured value, the
   reproduction step — never "feels off"). See "Evidence capture" below.
5. **Rate severity 0–4** independently per finding using the three factors — **frequency ×
   impact × persistence** — per `references/severity-scoring.md`. In a multi-evaluator
   evaluation, evaluators rate **independently first**, then the facilitator merges and the
   panel re-rates the merged list (independent-then-aggregate removes single-rater bias).
6. **Merge & deduplicate.** Combine evaluators' lists; collapse duplicates (keep the clearest
   wording); note how many evaluators independently caught each issue (multi-catch issues are
   higher-confidence). Order by **severity descending**, then by red-route position.
7. **Write the critique report.** Use the report structure (Section 2): per-finding cards +
   a severity-ordered table + positive findings (what works — always name strengths, a critique
   that only lists faults is not credible). Tie each finding to its fix / right-pattern.

## Anti-Patterns

- **Opinion dressed as evaluation.** "I'd use a different colour" with no heuristic and no
  severity is a preference, not a finding. Every comment cites a heuristic.
- **No severity, or severity by gut.** Skipping the 0–4 scale, or rating on annoyance rather than
  frequency × impact × persistence, makes the list un-prioritisable. Use the rubric.
- **Single static screen.** Inspecting only the hero screen and not walking the red-route *flow*
  misses the feedback, recovery, and "where am I" violations that only appear in motion.
- **Critique with no strengths.** A report that only attacks reads as adversarial and loses the
  room; name what works and why (it also tells the team what *not* to break).
- **Confusing inspection with testing.** Heuristic evaluation predicts *suspected* problems from
  expert judgement; it does **not** replace observing real users. Say so in the report.
- **Cosmetic = trivial reflex.** Frequency and persistence can push a "cosmetic" issue up the
  scale; do not auto-floor visual issues to severity 1.

## Outputs

- A **heuristic evaluation / design critique report**: framing, the heuristic set used, per-finding
  cards (location · heuristic · issue · evidence · severity · fix), a **severity-ordered findings
  table**, positive findings, and an evaluator-coverage note.
- A **prioritised violation list** (severity 4 → 0) ready to hand to `ux-remediation-and-redesign`
  as a fix backlog, or to feed `design-audit`'s triage queue.

## Examples

- `examples/heuristic-evaluation-worked.md` — a full worked heuristic evaluation of a real
  screen-and-flow (a mobile bank transfer flow), with findings tied to specific Nielsen/Tognazzini
  heuristics, evidence, and 0–4 severities, ordered into a fix backlog.

## References

- `references/heuristics-catalog.md` — the heuristic set: **Nielsen's 10 usability heuristics**
  (full definitions + what each looks like when violated) and **Tognazzini's first principles of
  interaction design** (Anticipation, Autonomy, Consistency, Defaults, Efficiency, Fitts's Law,
  Latency reduction, Learnability, Protect the user's work, Visible navigation, and the rest).
- `references/severity-scoring.md` — the **0–4 severity scale** (0 = not a problem … 4 =
  usability catastrophe) and the **frequency × impact × persistence** rating method, with the
  independent-then-aggregate multi-evaluator protocol and gate floors.
- `doctrine/design-doctrine.md` — the Anti-Slop Charter and the Mission ("the moat is looking
  human-made"); a heuristic critique also flags convergent/slop choices as findings.
- `doctrine/references/interaction-anti-patterns.md` — the behavioural detection checklist
  (A1–E3: navigation, forms, feedback/control, hierarchy/legibility, novelty/platform-fit). Walk
  the UI against it; each match maps to a violated heuristic and is severity-rated here.
- `doctrine/references/wcag-2.2-criteria.md` — accessibility violations are heuristic violations
  (#5 *Error prevention*, #7 *Flexibility*) and are rated on the same scale; certify with WCAG.
<!-- dual-compat-end -->

## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `design-audit` | The **paired** scored artifact audit (0–100 rubric, slop/WCAG/CWV gates). Run heuristic evaluation as the inspection method; run design-audit when a defensible *number* is needed. They share the same anti-pattern checklist. |
| `ux-research-and-usability-testing` | When the suspected problems this inspection surfaces need confirming with **real users** (inspection predicts; testing proves). |
| `ux-remediation-and-redesign` | **Downstream** — hand the severity-ordered violation list over to redesign, re-validate, and measure the uplift. |
| `ux-psychology` | When a finding's *why* is cognitive (Hick's/Miller's/Fitts's load, recognition-over-recall) and the critique should explain the mechanism, not just the symptom. |

---

## 1. The method in one paragraph

Heuristic evaluation is a **discount usability inspection**: a small set of evaluators judge an
interface against recognised usability principles (Nielsen's 10 + Tognazzini's first principles),
independently, then merge. It is fast and cheap, finds the *obvious* violations a user test would
waste money rediscovering, and is **not** a substitute for testing real users — it predicts
*suspected* problems. Its discipline is what makes it more than opinion: **named heuristic +
located evidence + a 0–4 severity per finding.** This skill is the inspection/critique half of the
evaluation pair; `design-audit` is the scored-rubric half. (Provenance: Jakob Nielsen & Rolf
Molich's heuristic-evaluation method and Nielsen's 10 heuristics, 1994/refined; Bruce Tognazzini's
*First Principles of Interaction Design*, revised — both updated here to WCAG 2.2 and the Chwezi
doctrine.)

## 2. Report structure

```
# Heuristic Evaluation / Design Critique
**Date:** [date]   **Evaluator(s):** [n evaluators — names/roles]
**Target:** [screen / flow / product]   **Platform:** [web / iOS / Android / desktop]
**Context:** [users, tech literacy, brand personality]
**Heuristic set:** Nielsen 10 + Tognazzini first principles (+ interaction-anti-patterns A1–E3)
**Red routes walked:** [the critical-path tasks inspected]
```

### Findings (per-finding card)

```
### F[n] — [short title]
- **Location:** [screen + element]
- **Heuristic violated:** [Nielsen #N name] / [Tognazzini principle] (+ anti-pattern code if any)
- **Issue:** [specific, observed — what is wrong]
- **Evidence:** [screenshot ref / measured value / reproduction step]
- **Severity:** [0–4] — [frequency × impact × persistence, one line]
- **Caught by:** [k of n evaluators]   (multi-catch ⇒ higher confidence)
- **Fix / right pattern:** [the target heuristic-satisfying state]
```

### Severity-ordered table

| # | Title | Heuristic | Location | Severity | Caught by |
|---|---|---|---|---|---|
| F1 | … | #1 Visibility of status | … | 4 | 4/5 |

### What works (positive findings)

Name the decisions that *satisfy* the heuristics and should be preserved — strengths to protect,
not just faults to fix.

### Coverage note

State evaluator count and the inspection-not-testing caveat: "These are expert-predicted suspected
problems; confirm the borderline ones with `ux-research-and-usability-testing`."

---

## 3. How this differs from `design-audit` (the pair)

| | **Heuristic evaluation (this skill)** | **`design-audit`** |
|---|---|---|
| **Method** | Expert walkthrough against principles | Scored scan across 10 dimensions |
| **Output** | Findings, each tied to a heuristic + 0–4 severity | A defensible **0–100 number** + gates |
| **Question** | *Which usability principles does it violate?* | *How good is it, on a scale, and does it pass the gates?* |
| **Evaluators** | 3–5 independent, then merged | One scored pass against the rubric |
| **Best for** | Cheap pre-test removal of obvious violations; structured critique | A comparable score, slop/WCAG/CWV gating, exec reporting |

They are **complementary**: run the heuristic evaluation to find and name violations; run
`design-audit` when the work needs a graded score and the three hard gates. Both walk the same
`interaction-anti-patterns.md` checklist, so a finding from one feeds the other.

---

*Sources: Nielsen & Molich heuristic evaluation; Nielsen's 10 Usability Heuristics; Tognazzini,
First Principles of Interaction Design — all aligned to WCAG 2.2 AA and `doctrine/design-doctrine.md`
(the Anti-Slop Charter). Companion to the scored `design-audit`.*
