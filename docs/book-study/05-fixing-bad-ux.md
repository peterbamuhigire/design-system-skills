# Book Study 05 — *Fixing Bad UX Designs* (Lisandra Maioli, Packt, 2018)

**Studied against:** `doctrine/design-doctrine.md`,
`skills/00-cross-cutting-ops-qa-a11y/design-audit/SKILL.md`,
`skills/00-cross-cutting-ops-qa-a11y/design-qa-and-pre-launch-review/SKILL.md`,
and the group-00 visual-product-slop-audit + gap-list critique skills.
**Date:** 2026-06-21 · **Verdict headline:** CHANGE (harden `design-audit` with an explicit
remediation loop + a triage matrix; add a worked-fix reference example) + **CONFIRM a new,
narrowly-scoped `ux-remediation-and-redesign` skill** (P2) to own the *fix-side* lifecycle the
current audit/QA skills deliberately stop short of.

---

## (a) What the book actually is — method + bad-UX taxonomy

The book's premise is the one thing our engine does **not** yet own end-to-end: it is not about
*auditing* a UI, it is about the **full diagnose → fix → re-validate lifecycle** of an *existing,
already-broken* product. That is its distinctive contribution, and the reason it is worth a study
rather than a footnote.

### The diagnosis → remediation method (5 phases, iterative not linear)

The book is explicit that this is a **cycle**, re-entered after each test — not a one-pass waterfall:

| Phase | Name (book) | What it does |
|---|---|---|
| 1 | **Identifying UX issues** | Stakeholder mapping (RACI / stakeholder matrix), user research (20+ methods: usability labs, ethnography, interviews, surveys, card sorting, heatmaps, A/B), competitive comparative analysis, journey/touchpoint mapping, problem statement via a POV ("Point of View") tool. |
| 2 | **Exploring potential solutions** | Organise/visualise findings, **categorise by severity** (Critical/High/Medium/Low), theme-cluster the problems, **effort-vs-impact** map, write the findings report (background, method, results, findings & recommendations). |
| 3 | **Prototyping & validation** | Conceptual → lo-fi → mid-fi → hi-fi prototype progression; usability testing (moderated + unmoderated, Nielsen 5-user floor), tree testing for IA, A/B / multivariate, refine on results. |
| 4 | **Implementation** | Hand-off via UX/Lean-UX Canvas; annotated wireframes, functional specs, sitemaps, user flows, storyboards, user stories; QA coordination with UX context. |
| 5 | **Measuring solutions** | Define metrics (SUS, NPS, HEART), track KPIs (usability/engagement/conversion), before/after analytics comparison, ROI back to stakeholders. |

### The bad-UX taxonomy (catalogued by fix-domain, chapters 4–8)

This is the most directly reusable asset. The book organises problems by **domain of the fix**,
not as one flat list:

- **A. Conversion problems (Ch 4):** form friction (too many/badly-ordered fields, no autocomplete,
  no progress), slow load (3 s → ~40% abandonment), vague CTAs ("See Details" vs "Go"), no
  responsive/mobile, a11y barriers to checkout, weak hierarchy forcing user thinking, missing
  social proof.
- **B. UI & content communication (Ch 5):** *visual hierarchy* (size/weight not matching
  importance, bad sequencing, misalignment, mis-applied F/Z/Gutenberg reading patterns);
  *typography* (serif body on web, line length outside 44–75 chars, bad line-spacing, body
  < 12 pt, > 3 typefaces, inconsistent emphasis); *colour* (poor contrast, non-strategic colour,
  inconsistent colour-coding, colour-blindness ignored); *iconography* (unlabelled non-standard
  icons — 60% vs 88% comprehension with labels, inconsistent set style, > 7±2 per group, decorative
  load); *content/copy* (vague microcopy, unclear voice/tone, over-long text, feature- not
  benefit-led, missing instruction text).
- **C. Accessibility (Ch 6):** WCAG POUR failures, colour-only signalling, screen-reader
  incompatibility, missing alt text, keyboard-nav failure, low contrast, cognitive load (jargon).
- **D. IA & navigation (Ch 8):** poor labels/nomenclature, categories not matching mental models,
  deep nesting / bad findability, no breadcrumbs, unclear global nav, needless task-flow steps.
- **E. Physical/environmental UX (Ch 7):** Norman doors, missing feedback, confusing control
  panels (ATM/elevator/toilet), unclear sequencing.

### Triage / prioritisation (the part our skills are thinnest on)

The book gives a **concrete, reusable triage stack**:

1. **Travis severity matrix** — three yes/no questions per issue: (a) on a *red route* (critical
   path)? (b) hard for users to overcome? (c) persistent/recurring? → Critical / Serious / Minor.
2. **Effort-vs-impact matrix** — impact (problem-for-customers) × effort (design/dev cost); fix the
   high-impact/low-effort quadrant first.
3. **MoSCoW** — Must/Should/Could/Won't.
4. **Frequency weighting** — issues seen repeatedly in research outrank one-off test findings.
5. **Business alignment** — conversion-blocking and KPI-affecting issues outrank aesthetics.

### Validation (how to prove a fix worked)

5-user moderated/unmoderated usability tests (task-completion %, time-on-task, error rate);
A/B testing (conversion/CTR uplift = fix validated); **tree testing** for IA restructures;
before/after quantitative analytics (bounce, session duration, funnel completion); qualitative
post-test interviews. Emphasis: success = *task completed without confusion*, not satisfaction.

### The worked fix (template-grade)

**2017 Oscars "La La Land" card error.** Diagnosis: three hierarchy failures — Oscar logo (least
important) was the largest element; winner name was the *same* weight as the producer credits below
it; the category ("Best Picture") was smallest and last in reading order — so a stressed presenter
could not parse the card. Fix (Brandon Jameson): re-order by criticality — **category largest at
top → winner bold/centred → credits smaller → logo de-emphasised at bottom**. This is a clean
*content-audit → hierarchy-analysis → re-order-by-criticality → re-validate* template (captured as a
reference deliverable in the Engine-Impact section).

---

## (b) CRITICAL — current vs dated, and vs our existing audit/QA skills

### Currency (2018, ~8 years old at time of study)

- **Timeless:** the methodology spine (research → severity → effort/impact → prototype → validate →
  measure), WCAG POUR, hierarchy/typography/colour fundamentals, Nielsen heuristics, tree testing.
- **Dated:** the *tooling and trend* layer. Prototyping list (Sketch-era, Figma still nascent),
  analytics vendor names (AppSee/Woopra/Lucky Orange), "flat design" framed as a live trend,
  AirPlay screen-recording workarounds. **Predates** design tokens / component libraries, WCAG 2.2,
  dark mode, motion/micro-interaction depth, mobile-first framing, AI-native UX.
- **Net:** read the **method**, ignore the **tool/trend examples**. Our doctrine already supplies the
  current floors (WCAG 2.2, Core Web Vitals, the anti-slop taxonomy) that the book lacks.

### Versus our existing skills — what overlaps, what is genuinely new

| Dimension | Our engine today | The book | Verdict |
|---|---|---|---|
| **Diagnostic critique of a built UI** | `design-audit` — 10 scored dimensions, gates (slop/WCAG-2.2/CWV), 0–100 rubric. **Stronger & more current** than the book. | Looser, no scored rubric, no slop dimension, pre-WCAG-2.2. | We win — keep ours. |
| **Ship gate** | `design-qa-and-pre-launch-review` — composed go/no-go, spec/pixel parity, signed verdict. No equivalent in book. | — | We win — keep ours. |
| **Severity model** | `design-audit` has Critical/High/Medium/Low *definitions* but **no triage algorithm**. | **Travis red-route/difficulty/persistence test + effort-impact + MoSCoW + frequency weighting.** | **Book adds** — a real prioritisation engine. |
| **The fix lifecycle** | Both our skills *stop at the finding*. `design-qa` even says "use design-audit for diagnosis"; neither owns redesign → re-prototype → re-test → measure-the-improvement. | **This is the book's whole spine (phases 3–5).** | **Book adds** — the missing fix-side half. |
| **Validating that a fix worked** | Implicit ("re-run the audit"); no usability-test / A/B / tree-test / before-after-metrics protocol. | Explicit and concrete. | **Book adds.** |
| **Problem taxonomy as a reference** | Tells are scattered across the 10 dimensions + `ai-slop-taxonomy.md`. | A clean by-domain catalogue with thresholds (line length 44–75, < 3 typefaces, 7±2 icons, 3 s load). | **Book adds** a consolidated bad-UX pattern catalogue. |
| **Root-cause analysis** | Neither. | Book also lacks structured RCA (no 5-Whys/fishbone) — a *shared* gap. | Neither — note as a future add. |

**Bottom line:** the book is **weaker than us on the audit side** (no rubric, no slop, dated WCAG)
but **owns a half we do not have at all** — the post-finding **remediation lifecycle** (redesign →
re-validate → measure improvement) plus a **real triage matrix**. That asymmetry is the whole
engine-impact case.

---

## (c) ENGINE IMPACT

### 1. Harden `design-audit` (CHANGE — small, high-value)

- Add a **"Triage" step** between "Produce Report" and the severity table: adopt the **Travis
  red-route / difficulty / persistence** test plus the **effort-vs-impact** quadrant to *order* the
  prioritised recommendations (it already lists them by severity but gives no method for the order).
  This is a 1-paragraph addition + a small reference table; it makes the existing
  "Prioritised Recommendations" section defensible rather than vibes-based.
- Cross-reference the **bad-UX pattern catalogue** (below) from Dimensions 2, 4, 5, 9 as the
  worked-example library behind the terse check tables.

### 2. Add a reference + a worked fix (CHANGE)

- New reference `doctrine/references/bad-ux-pattern-catalogue.md` (or under `design-audit/references/`):
  the by-domain taxonomy from §(a)B with the book's concrete thresholds, **mapped onto our 10
  dimensions** so it is a lookup behind the audit, not a parallel system.
- New example `examples/ux-remediation-oscars-card.md`: the Oscars-card before→after as the canonical
  *diagnose → re-order-by-criticality → re-validate* worked fix.

### 3. Build a dedicated skill — `ux-remediation-and-redesign` (CONFIRM, P2)

**Justified — yes, but tightly scoped.** It must NOT duplicate `design-audit` (diagnosis) or
`design-qa` (ship gate). It owns the **fix lifecycle those two deliberately exclude**:

> *Input:* an audit's findings (from `design-audit`). *Process:* triage (Travis + effort/impact) →
> remediation plan → redesign at lo-fi→hi-fi → **validation protocol** (5-user usability / A/B /
> tree test / before-after metrics) → **measure the improvement** (SUS/NPS/HEART, KPI delta).
> *Output:* a remediation plan + a validated before/after with a measured uplift.

It composes `design-audit` upstream and hands a re-built artifact to `design-qa-and-pre-launch-review`
downstream — closing the loop *audit → fix → re-validate → ship*. Place in group-00. **Note the gap
list (`docs/initial-analysis/04-gap-analysis-new-skills.md`) does not currently propose this** — it
should be added there as a new row. Keep current (WCAG 2.2 / CWV / anti-slop) by referencing our
doctrine, not the book's 2018 tool list.

### CONFIRM / CHANGE / REDUNDANT summary

- **CONFIRM:** new `ux-remediation-and-redesign` skill (P2, group-00) — fills a real lifecycle gap.
- **CHANGE:** `design-audit` gains a triage step + a pattern-catalogue reference + a worked-fix example.
- **REDUNDANT (do NOT import):** the book's audit method itself (ours is stronger/current), its
  research-methods survey (covered by group-05), its 2018 tool/trend lists, its prototyping how-to.

---

## "extract-into" table

| From the book | Extract into | As what | Priority |
|---|---|---|---|
| 5-phase diagnose→fix→measure lifecycle | **NEW** `skills/00-…/ux-remediation-and-redesign/SKILL.md` | Skill workflow spine (the fix-side loop) | P2 |
| Travis severity (red-route/difficulty/persistence) + effort-impact + MoSCoW | `design-audit/SKILL.md` §"Triage" (new step) | Prioritisation algorithm for the recommendations list | P1 |
| By-domain bad-UX taxonomy + thresholds (line 44–75, <3 typefaces, 7±2 icons, 3 s) | `doctrine/references/bad-ux-pattern-catalogue.md` (new) | Reference catalogue, mapped to the 10 audit dimensions | P1 |
| Oscars-card before→after | `examples/ux-remediation-oscars-card.md` (new) | Canonical worked-fix template | P2 |
| Validation protocol (5-user / A/B / tree test / before-after metrics) | `ux-remediation-and-redesign` (Validation section) | "Prove the fix worked" step | P2 |
| Measurement (SUS/NPS/HEART, KPI delta, ROI) | `ux-remediation-and-redesign` (Measure section) | Improvement-quantification step | P2 |
| RCA gap (book lacks 5-Whys/fishbone — so do we) | backlog note in the new skill | Future add (not in book) | P3 |
| 2018 tool/trend lists, research-methods survey, audit method | — | **EXCLUDE** (dated or already owned) | — |
