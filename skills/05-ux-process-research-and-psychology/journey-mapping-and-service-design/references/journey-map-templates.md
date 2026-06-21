# Journey-Mapping Templates & Models

Canonical templates for personas, JTBD, journey/experience maps, and the alignment-diagram /
opportunity backlog. Every template here enforces the same rule: **nothing on a map exists
without evidence behind it.** A persona trait, an emotion trough, or an opportunity with no
traceable source is fiction, and fiction at experience scale is `doctrine/design-doctrine.md`
slop (§0 — the moat is the experience reading as *authored*, not invented to fit a roadmap).

Provenance: synthesises Kalbach (*Mapping Experiences*), the Nielsen Norman Group journey-map
and alignment-diagram models, and Christensen's Jobs-To-Be-Done. Human design literature only —
no AI-vendor recommendation is treated as authority (doctrine §2, the asymmetry rule).

---

## 1. Evidence-based persona

A persona is a **research-grounded archetype**, not a demographic invented to justify a plan.
Every field carries its evidence or is flagged as an assumption to validate.

| Field | What it holds | Evidence rule |
|---|---|---|
| **Name + one-line role** | A memorable handle and the role in *their* world ("Amina, runs a 2-staff hardware shop"). | Role must come from real segments seen in research. |
| **Context / environment** | Where, on what device, under what constraints they act (bandwidth, interruptions, literacy, time). | From observation/interviews — not assumed. |
| **Goals** | What they are trying to achieve in this domain. | Quote or behaviour per goal. |
| **Jobs (link to JTBD)** | The jobs they hire the product to do (see §2). | Derived from goals + observed behaviour. |
| **Pain points today** | What's broken in their current workaround. | Quote / ticket / observed failure. |
| **Real quote** | One verbatim line that captures their stance. | Actual participant words, with ID. |
| **Behavioural attributes** | Frequency, tenure, sophistication — only the axes that change the design. | From data; drop demographic decoration that doesn't move a decision. |
| **Confidence / gaps** | Which fields are evidenced vs. assumed-to-validate. | Be honest; route gaps to `ux-research-and-usability-testing`. |

**Anti-pattern:** the stock-photo persona — invented age/income/hobbies, a smiling avatar, no
research. It launders a pre-made decision as "user-centred". Mark every unevidenced field as an
assumption, not a fact.

---

## 2. Jobs-To-Be-Done (JTBD)

Frame the *why* before the *how*. The job is stable across solutions; the feature is not.

```
When [situation],
I want to [motivation / capability],
so I can [expected outcome].
```

- **Functional job** — the practical task ("track which stock is running low").
- **Emotional job** — how they want to feel ("feel in control, not anxious about running out").
- **Social job** — how they want to be seen ("look professional / trustworthy to my customers").

Worked: *"When I close my shop at night, I want to know which products are nearly out, so I can
restock before I lose a sale tomorrow."* Judge every opportunity against the job: does it advance
"know what's low and restock in time", or is it just a feature someone liked?

---

## 3. Choosing the map: journey vs. experience vs. blueprint

| Use… | When | Scope |
|---|---|---|
| **Journey map** | One persona, one scenario, your service already exists; you want to see *their* experience through your touchpoints and find pain. | One actor, time-ordered, your touchpoints. |
| **Experience map** | Before a specific solution — understanding the human behaviour/problem space, organisation-agnostic. | Broader, not tied to your product. |
| **Service blueprint** | You must change *how the service is delivered* (staff, systems, hand-offs), not just the UI. Extends a journey map downward past the line of visibility. | Frontstage + backstage + support — see `service-blueprint.md`. |

Picking the wrong artifact is the most common waste: a blueprint when you needed a quick journey
map, or a journey map when the failure is a backstage hand-off only a blueprint reveals.

---

## 4. The journey-map grid (stage × layer)

Columns are **stages** in the actor's own mental phases and words (not your funnel labels).
Rows are the experience **layers**:

| Layer | What it captures | Evidence rule |
|---|---|---|
| **Stage** | The actor's phase, named in their words. | From how participants describe it. |
| **Doing** | Concrete actions/touchpoints in this stage. | Observed behaviour. |
| **Thinking** | Questions, expectations, mental model. | Quotes. |
| **Feeling (emotion curve)** | A plotted high/low per stage. | **Every peak/trough cites a quote, ticket, or metric.** No bare squiggle. |
| **Touchpoint / channel** | App, web, phone, SMS, in-person, third party. | Real names. |
| **Pain points & moments of truth** | Where it breaks; the make-or-break moments; cross-channel seams; ownership gaps. | Evidence per pain. |

**The emotion-curve evidence rule:** a curve is a *finding*, not decoration. If a low point has
no source beneath it, delete it or go get the evidence (`ux-research-and-usability-testing`).
Mark **moments of truth** (the few interactions that disproportionately set the whole
perception) and **seams** (channel hand-offs and waits) — services fail at seams.

---

## 5. Alignment diagram & opportunity backlog

An **alignment diagram** lines up the *outside* (the customer's journey, top) with the *inside*
(the org's touchpoints/processes, bottom) so the gaps are visible — research feeds the top,
opportunities fall out of the gaps. The spine is **research → map → opportunity**: every
opportunity traces back to evidence, and every pain point traces forward to an opportunity.

Score and rank each opportunity:

| Field | Meaning |
|---|---|
| **Opportunity** | "How might we…" reframing of a pain point / unmet job. |
| **Evidence** | The research/datapoint(s) it traces to (participant IDs, ticket counts, funnel %). |
| **Impact on the job** | How much it advances the JTBD (H/M/L). |
| **Frequency** | How many of the actors hit this, how often. |
| **Feasibility** | Effort/risk to deliver (H/M/L). |
| **Priority** | impact × frequency × feasibility → a ranked order. |

**Completeness gate:** an opportunity with no evidence is invented; a pain point with no
opportunity is unfinished. The map is the means — the **ranked backlog** is the deliverable.

---

## 6. Doctrine & accessibility hooks

- Troughs where the actor says "felt generic / didn't trust it / looked like everyone else's"
  are **slop signals** (`doctrine/references/ai-slop-taxonomy.md`); escalate as opportunities,
  not nuisance notes — the moat is the experience reading as deliberately authored (doctrine §0).
- A map that models one channel and one ability is incomplete. Add the keyboard-only,
  screen-reader, low-bandwidth, low-literacy, and offline-fallback paths, or state the gap
  explicitly against `doctrine/references/wcag-2.2-criteria.md`.
