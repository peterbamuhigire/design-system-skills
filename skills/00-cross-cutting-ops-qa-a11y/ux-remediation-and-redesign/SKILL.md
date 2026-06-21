---
name: ux-remediation-and-redesign
description: Use when you already HAVE audit findings (from design-audit or product-design-audit)
  and now need to FIX them — owns the post-audit remediation discipline the audits deliberately
  stop short of: diagnose → triage → redesign → re-validate → measure. Triggers - "fix these
  findings", "remediation plan", "now redesign it", "sequence the fixes", "what do we fix first",
  "turn the audit into a work plan", "prioritise the UX fixes", "re-test the redesign", "prove the
  fix worked", "measure the UX improvement", "before/after redesign", "remediate the checkout /
  onboarding / form". Composes a real triage matrix (red-route × effort-impact × MoSCoW) to
  sequence fixes, redesigns at lo-fi→hi-fi against doctrine, re-validates with a usability / A/B /
  tree-test protocol, and measures the uplift (SUS/NPS/HEART, KPI delta). For finding the problems
  use design-audit (one artifact) or product-design-audit (whole product); for the final pass/fail
  ship gate use design-qa-and-pre-launch-review. This is the FIX side; those are the DIAGNOSE side.
status: active
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
  - claude-code
  - codex
---

# UX Remediation & Redesign
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- You have a **set of audit findings** (severity-rated, ideally scored) for an existing,
  already-built flow or product, and you now need to turn them into a **sequenced, defensible fix
  plan** rather than a flat backlog.
- You need to **prioritise** competing fixes when you cannot do everything at once — to decide what
  ships this sprint vs next quarter vs never, using a real method, not vibes.
- You are **redesigning a broken flow** and need the discipline that carries it from finding →
  lo-fi → hi-fi → re-test → measured improvement, closing the loop back to the audit and forward
  to the ship gate.
- You need to **prove a fix actually worked** — task-completion uplift, contrast now passing, a
  cleared gate, a before/after KPI delta — not just assert "we fixed it."

## Do Not Use When

- You **don't yet have findings** — there is nothing to remediate. Run `design-audit` (a single
  screen/artifact) or `product-design-audit` (a whole multi-platform product) first; this skill
  consumes their output, it does not re-discover problems.
- You only need the **diagnosis** (the scored critique, the slop/WCAG/CWV gates) — that is
  `design-audit` / `product-design-audit`. Do not re-run those gates here; cite their results.
- You need the **final pass/fail go/no-go** before launch — that is
  `design-qa-and-pre-launch-review`. This skill hands a re-built, re-validated artifact *to* that
  gate; it is not the gate itself.
- You are creating a **new** design from scratch (no existing flow to fix) — use the relevant
  group 03–13 craft skills to build, then audit, then return here only if findings surface.

## Required Inputs

- **The audit findings** — the severity-rated list from `design-audit` / `product-design-audit`
  (each finding: dimension, location, issue, impact, the standard it violates, a fix direction).
  Without this, stop and run the audit first.
- **The red routes** — the product's critical paths (the few flows that, if broken, break the
  business: sign-up, checkout, the core job-to-be-done). The triage cannot run without them; if
  unstated, ask, then derive from the product's primary jobs-to-be-done.
- **Effort signal** — a rough design+dev cost per fix (a token swap is trivial; an IA
  restructure is not). Get it from whoever will build it; estimate and label the estimate if not.
- **The baseline** — the pre-fix numbers you will measure against (task-completion %, time-on-task,
  error rate, the audit score, the failing CWV/contrast values, funnel conversion). No baseline →
  no provable improvement; capture it before touching anything.
- **Constraints** — release window, team capacity, any frozen surfaces, brand/legal limits.

## Workflow

The remediation lifecycle is **diagnose → triage → redesign → re-validate → measure**, and it is a
**loop, not a waterfall** — each re-validation that still fails re-enters at triage. Full detail in
`references/remediation-lifecycle.md`; the prioritisation engine in `references/triage-matrix.md`.

1. **Diagnose (intake the findings — do not re-audit).** Ingest the audit's severity-rated
   findings. Cluster them by *root flow* and by *fix domain* (hierarchy, conversion, a11y, IA,
   content…) so related fixes ship together. Name each finding against the
   `doctrine/references/interaction-anti-patterns.md` vocabulary (e.g. "Flat Hierarchy D1",
   "Vague CTAs B3", "Silent System C2") — that gives every finding a known target right-pattern.
   Carry forward which **gate** (slop / WCAG 2.2 AA / CWV) each finding feeds; gate-failing items
   are pre-flagged because they cap the score until cleared (`design-audit/references/audit-rubric.md`).

2. **Triage (sequence with the matrix — this is the core).** Run every finding through the
   three-lens stack in `references/triage-matrix.md`:
   (a) **Red-route severity** (Travis): is it on a critical path? hard for users to overcome?
   persistent/recurring? → **Critical / Serious / Minor**.
   (b) **Effort × Impact** quadrant → fix the **high-impact / low-effort** quadrant first
   ("quick wins"), schedule high-impact/high-effort ("major projects"), defer the rest.
   (c) **MoSCoW** → **Must / Should / Could / Won't** for this release.
   Apply the two **override rules**: a **gate-failing finding is always Must** (a legal/charter
   floor outranks the quadrant), and **frequency-weighted** issues (seen repeatedly in research,
   not a one-off test artifact) outrank single sightings. Output a **ranked fix queue**.

3. **Redesign (fix at rising fidelity, against doctrine).** For each queued fix, design the target
   state — **conceptual → lo-fi → hi-fi** — applying the *right-pattern* from
   `interaction-anti-patterns.md` and the relevant craft skill (route via the table below). Every
   redesign must satisfy the **Anti-Slop Charter** (`doctrine/design-doctrine.md`): state the
   type/colour/layout choice, never reach for a banned default, prefer the *authored* option. A
   fix that clears one finding but introduces a slop tell or a new gate failure is **not** a fix —
   re-enter triage. Annotate each redesign with *which finding(s) it closes*.

4. **Re-validate (prove it, don't assert it).** Pick the validation method that matches the change
   (`references/remediation-lifecycle.md` §Re-validate): **5-user usability test** (task-completion %,
   time-on-task, error rate — Nielsen's 5-user floor) for flow/hierarchy fixes; **A/B test**
   (conversion / CTR uplift) for conversion fixes where traffic allows; **tree test** for IA
   restructures; **automated + keyboard + screen-reader** re-check for a11y fixes (re-assert the
   exact WCAG criterion now passes); **field CWV re-measure** for performance fixes. Success =
   *the task is completed without confusion and the failing standard now passes* — not "users said
   they liked it." A still-failing re-validation re-enters at **triage**, not redesign.

5. **Measure (quantify the uplift, close the loop).** Compare against the baseline from Required
   Inputs: the **audit-score delta** (and any cap now lifted), **task metrics** (completion/time/
   error before→after), **product KPIs** (funnel, bounce, session), and a summary instrument
   (**SUS / NPS / HEART task-success**). Report the before→after as a table. Then **close the loop**:
   hand the re-built, re-validated artifact to `design-qa-and-pre-launch-review` for the pass/fail
   ship gate, and feed any *newly surfaced* findings back to `design-audit`.

### Route each fix to its owning craft skill

| Finding domain (anti-pattern group) | Redesign with |
|---|---|
| Flat hierarchy, reading order (D1) | `composition-and-visual-hierarchy` |
| Typographic noise, banned fonts (D2) | `font-selection-and-pairing`, `type-scale-and-spacing` |
| Colour-only signalling, contrast (D3) | `accessible-color-and-contrast` |
| Icon soup (D4) | `iconography-and-icon-systems` |
| Form friction, forced sign-up, vague CTAs (B1–B3) | `forms-and-input-design`, `ux-writing-and-microcopy` |
| Idiot boxes, silent system, dead ends (C1–C3) | `error-empty-and-system-messaging`, `micro-interactions-and-feedback` |
| Deep nesting, mystery-meat nav (A2–A3) | `information-architecture`, `navigation-design` |
| Any a11y gate finding | `accessibility-wcag-2-2-compliance` |
| Any CWV / budget finding | `performance-as-ux-and-core-web-vitals` |

(Glob the engine for the exact skill name before citing; if none fits, name the doctrine
reference instead — never leave a fix un-routed.)

## Anti-Patterns

- **Re-auditing instead of remediating.** This skill consumes findings; it does not re-run the
  slop/WCAG/CWV gates. Re-deriving the diagnosis here duplicates `design-audit` and wastes the
  triage budget.
- **Vibes-based prioritisation.** "Let's fix the homepage first because it's visible" — without the
  red-route × effort-impact × MoSCoW matrix the order is indefensible. Run the matrix.
- **Skipping the gate override.** Sequencing a contrast or banned-font fix as "Could" because it's
  low-effort-low-impact-looking — a gate-failing finding is **always Must**; it caps the score
  until cleared.
- **Declaring victory without re-validation.** "We redesigned it" is not "it works." No
  task-completion re-test / cleared-criterion / KPI delta = not done.
- **Fixing one finding and opening another.** A redesign that clears the contrast finding but
  introduces a slop gradient, or flattens IA but breaks a red route — re-enter triage, don't ship.
- **No baseline.** Measuring improvement you never benchmarked is unprovable. Capture the
  before-numbers *before* the first edit.
- **Treating the loop as a waterfall.** Real remediation re-enters triage after each failed
  re-validation; a one-pass plan that never re-tests is the book's exact anti-pattern.

## Outputs

- A **triaged fix queue** — every finding ranked by the matrix (Critical/Serious/Minor ×
  effort-impact quadrant × MoSCoW), gate-failing items forced to Must, with the sequence justified.
- A **remediation plan** — per fix: the finding(s) it closes, the target right-pattern, the owning
  craft skill, the fidelity reached (lo-fi/hi-fi), and the chosen re-validation method.
- A **re-validation record** — the method run and its result (task-completion %, cleared WCAG
  criterion, A/B uplift, re-measured CWV), with a pass/fail per fix.
- A **before→after measurement table** — audit-score delta (caps lifted), task metrics, product
  KPI delta, and a summary instrument (SUS/NPS/HEART). This is the "fix worked" evidence.
- A **handoff note** to `design-qa-and-pre-launch-review` (ship gate) plus any new findings routed
  back to `design-audit`.

## Examples

- `examples/checkout-remediation-worked.md` — a full worked remediation of the **Aurora Analytics
  signup/landing** flow whose flaws were diagnosed in `design-audit/examples/design-audit-filled.md`
  (the 41/100, two-gates-failed audit). It takes those exact findings → triages them with the real
  matrix (gate-failers forced to Must; one quick-win, one major project) → redesigns each against
  the anti-pattern right-patterns and the Anti-Slop Charter → re-validates (5-user test + a11y
  re-check + CWV re-measure) → measures the before→after (score 41 → 88, both caps lifted, task
  completion 58% → 91%). Real numbers, no lorem, no banned fonts.

## References

- `references/remediation-lifecycle.md` — the five phases (diagnose → triage → redesign →
  re-validate → measure) as a loop, with the per-phase entry/exit criteria and the re-validation
  method-selection table.
- `references/triage-matrix.md` — the concrete prioritisation engine: the Travis red-route
  severity test, the effort × impact quadrant, MoSCoW, and the two override rules (gate-failers =
  Must; frequency weighting), with a worked scoring table.
- `doctrine/references/interaction-anti-patterns.md` — the diagnosis vocabulary and the *target
  right-pattern* for each finding; every redesign aims at the "fix" column here.
- `doctrine/design-doctrine.md` — the Mission and Anti-Slop Charter every redesign must satisfy; a
  fix that introduces a slop tell is not a fix.
- `design-audit` → `references/audit-rubric.md` — the upstream scored diagnosis this skill
  consumes, and the gate/cap logic that makes gate-failing findings always-Must.
- `doctrine/references/wcag-2.2-criteria.md` and `doctrine/references/web-performance-budgets-2026.md`
  — the accessibility and performance floors a remediation must clear (and re-assert in re-validation).
<!-- dual-compat-end -->
## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `design-audit` | Upstream — produces the findings this skill remediates (one artifact) |
| `product-design-audit` | Upstream — produces product-wide, skill-routed findings to remediate |
| `design-qa-and-pre-launch-review` | Downstream — the pass/fail ship gate the re-built artifact hands to |
| `composition-and-visual-hierarchy` | When redesigning hierarchy / reading-order findings |
| `accessibility-wcag-2-2-compliance` | When remediating any a11y gate finding (and re-validating it) |
| `performance-as-ux-and-core-web-vitals` | When remediating any CWV / budget finding |

---

*Sources: Lisandra Maioli, *Fixing Bad UX Designs* (Packt, 2018) — the diagnose→fix→measure
lifecycle, the Travis red-route severity test, the effort-impact matrix, and the re-validation +
measurement protocol — updated to 2026 and aligned to WCAG 2.2, Core Web Vitals, and the Chwezi
Anti-Slop Charter. Composes `design-audit` / `product-design-audit` (diagnose) upstream and
`design-qa-and-pre-launch-review` (ship gate) downstream. Right-patterns from
`doctrine/references/interaction-anti-patterns.md`.*
