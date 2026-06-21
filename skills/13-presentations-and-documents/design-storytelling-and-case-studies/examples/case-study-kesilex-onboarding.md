# Worked Example — Case-study/deck narrative: KesiLex onboarding redesign

A fully worked narrative spec for a **real** project (KesiLex, a legal-tech product named in the
doctrine's Anti-Slop Charter). It shows the four decisions this skill demands: (1) the chosen
framework and *why*; (2) the protagonist casting; (3) the before→after contrast; (4) the beats with
**concrete evidence anchored at each one**. This spec is the artifact you hand to `deck-system` (for
a pitch/credentials deck) or `docx-report-and-document-formatting` (for a written case study).

> **Fence check first (Workflow step 1).** Is there a real thing to tell? **Yes** — the redesigned
> onboarding flow shipped to production; we have the old flow, the new flow, instrumented metrics
> before and after, and recorded user sessions. If any of those were missing, there would be no
> case study and this file would not exist. The numbers below stand in for the project's real
> instrumented data; in a live use you replace them with the actual measured figures — **never
> invent them to make the arc stronger.**

---

## 1. Chosen framework — Pixar Story Spine (+ Contrast spine, + Peak-End shaping)

**Why Pixar.** The story is a **relatable human change**: a new KesiLex user (a paralegal) had a
painful first-run experience every day, until one specific design decision eased it. Pixar's
"Every day… / Until one day…" makes the user's *daily pain* felt, and it bakes in user-as-protagonist
— exactly the framing this story needs. (Three-Act would have worked too, but it foregrounds the
*work* over the *user's day*; the daily-pain quality of this story is what makes Pixar the better
fit — see the decision table in `references/narrative-frameworks.md`.)

**Why not the others.** Freytag is heavier than this single-decision story needs. Kishōtenketsu is
wrong because there *is* a real conflict (the abandoned onboarding) — we would have to suppress true
stakes to use a no-villain structure. **Contrast** is layered in as the spine (we open on the pain,
not the fix). **Peak-End** decides where the strongest number goes and how we close.

---

## 2. Protagonist (Workflow step 2)

**Protagonist: Amara, a paralegal at a 12-person law firm** — not KesiLex, not the design team.
KesiLex is the **bit-player** that had to fit *her* Monday-morning drama (clear a backlog of case
intake before partners arrive), not star in its own feature tour. Every beat is told from her point
of view.

---

## 3. Contrast, beginning-to-end (Workflow step 3)

- **Before:** Amara abandons KesiLex onboarding halfway and goes back to her spreadsheet.
- **After:** Amara completes her first real case intake inside KesiLex before her coffee is cold.

We open hard on the **abandonment**, not on the polished new flow. The size of that delta is the
narrative. (If we opened on the slick new screen, the audience would assume it was always that easy.)

---

## 4. The beats, mapped onto Pixar, each anchored to evidence (Workflow steps 4–8)

| Pixar beat | Case-study beat | The telling (Amara's POV) | Evidence anchored here |
|---|---|---|---|
| **Once upon a time…** | Problem (before) | Amara's firm bought KesiLex to replace a fragile intake spreadsheet. | The old spreadsheet flow (screenshot); the purchase context. |
| **Every day…** | Stakes | Every morning she opened onboarding, hit a 9-field "firm setup" wall before she could enter a single case, and gave up — back to the spreadsheet. | **Baseline metric:** onboarding completion **31%**; median time-to-first-case **never reached** for 69% of trials. Session recording of the drop-off. Her quote: *"I just need to log a case, not configure a firm."* |
| **Until one day…** | **Authored decision (the climax / turning point)** | We made *one* defensible, taste-driven choice: **defer firm setup entirely** — let her log her first real case in two fields, and ask for firm details *later, in context, only when first needed.* | The decision itself: the new two-field first screen **beside the rejected 9-field original**; the *reasoning* (a heuristic — "answer the hard question by removing it," not an A/B test); the **working demo** we lived on for a week before shipping. **This is the Mission-visible beat** — a templating tool would have kept the tidy upfront form. |
| **Because of that…** | Before/after (transformation) | Amara now reaches "first case logged" in under a minute; firm setup happens painlessly two days later when she invites a colleague. | **Paired before/after flows** (9 steps → 2 steps to first value); the live demo. |
| **Because of that…** | Proof | The change held across all new firms, not just Amara. | **Post-change metrics vs. the §stakes baseline:** completion **31% → 78%**; median time-to-first-case **8m40s → 47s**; 30-day retention **+22pts**. Three user quotes. *(Attributed to the change, same cohort definition, 6-week window.)* |
| **Until finally…** | CTA | (Credentials deck:) *This is how we design onboarding — by removing the question, not styling the form.* (Pitch:) *Approve the same treatment for the matter-management flow.* | The single, audience-matched ask. |

---

## 5. Peak and End (Workflow step 7)

- **Peak:** the **31% → 78%** completion jump, shown large beside the two-field-vs-nine-field
  screens — placed at the structural high point (the "Because of that… / proof" beat), not buried.
- **End:** close on Amara's transformed Monday + the **one** CTA. We do **not** end on a feature
  list of the new onboarding or a thank-you slide (that would waste the Peak-End close).

---

## 6. Top-tasks cut (Workflow step 8)

Cut from the telling (real, but off the through-line — Kill Your Darlings): the colour/type refresh
that shipped in the same release, the analytics pipeline rebuild, and the settings reorganisation.
They are true and even good — but the one thing this audience came for is *"how a single authored
decision turned abandonment into completion."* Everything else is the long neck; it goes.

---

## 7. What gets handed off (Workflow step 9)

- **To `deck-system`:** this arc becomes the slide spine — action titles per beat (e.g. *"Defer the
  firm; log the case"* for the turning point), the 31%→78% exhibit as the S.T.A.R. moment, the
  Sparkline toggling Amara's old pain vs. new ease. deck-system owns the slide craft, type/colour,
  and presenter notes; this spec owns the **narrative structure** it renders.
- **To `docx-report-and-document-formatting`:** the same six beats become the written case study's
  sections, with the before/after screens as figures.

---

## Fence check (closing)

Walk the beats: problem and stakes are the *real* abandoned flow and the *real* 31% baseline; the
turning point is an *actual* shipped decision with its rejected alternative; before/after and proof
are *measured*, same cohort, stated window. Nothing here is manufactured to thicken the arc. The
structure (Pixar + Contrast + Peak-End) made **true, authored** work legible and memorable — it did
not invent the work, and it could not have rescued an unbuilt or convergent flow. That is the skill
working as fenced (`doctrine/references/creative-selection-and-taste.md`; `doctrine/design-doctrine.md`).
