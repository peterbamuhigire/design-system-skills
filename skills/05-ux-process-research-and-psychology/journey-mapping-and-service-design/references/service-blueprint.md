# Service Blueprint

A service blueprint extends a journey map **downward**: past what the customer sees, into the
staff actions, systems, and processes that deliver (or fail to deliver) the experience. Its
entire value is making **backstage failure points** visible — the ones the customer never sees
but always feels. A "blueprint" that only redraws the frontstage screens has skipped its only
real job (`doctrine/design-doctrine.md` §0 — the experience must read as deliberately delivered,
not accidentally assembled).

Provenance: Shostack's original service-blueprinting model, as carried in the Nielsen Norman
Group and Kalbach (*Mapping Experiences*) literature. Human design authority only (doctrine §2).

---

## 1. The swimlanes (top to bottom)

Anchor everything to the **customer actions** across the top, time-ordered to match the journey
map's stages. Then separate the lanes with the three lines:

| Lane | What it holds |
|---|---|
| **Physical evidence / channels** | What the customer encounters at each step (the app screen, the SMS, the receipt, the shop counter). |
| **Customer actions** | What the customer does, step by step — the spine, aligned to the journey map. |
| — **Line of interaction** — | Crossed every time the customer interacts directly with the service. |
| **Frontstage (onstage) actions** | What staff/systems do **visibly** to the customer (the agent who answers, the confirmation screen). |
| — **Line of visibility** — | The critical line. Above it the customer sees; below it they do not. |
| **Backstage actions** | What staff do **out of sight** to fulfil the step (verifying, packing, approving). |
| — **Line of internal interaction** — | Crossed when one internal group calls another or a system. |
| **Support processes & systems** | The infrastructure: databases, payment gateways, third-party APIs, fulfilment partners, policies. |

---

## 2. How to build it

1. **Start from the journey map.** Reuse the same actor, the same stages, the same customer
   actions across the top. The blueprint is the journey map with the floor removed.
2. **For each customer action, trace down the lanes.** What evidence do they see? What does
   frontstage do? What must happen backstage to make that possible? Which systems/partners
   does it depend on?
3. **Draw the lines deliberately.** The **line of visibility** is the most important line in the
   document — moving an action above or below it is itself a design decision (do we make the
   wait visible, or hide it?).
4. **Map dependencies and hand-offs.** Draw the arrows where one lane hands to another. Every
   arrow that crosses the line of internal interaction is a **seam** — a candidate failure point.
5. **Mark fail points and waits.** Flag every step where a hand-off can drop, a system can be
   down, a queue can form, or **no team owns the step**. These are the opportunities a journey
   map alone could never surface.

---

## 3. Finding backstage failure points (the payoff)

The blueprint earns its cost here. Hunt specifically for:

- **Ownership gaps** — a step that sits between two teams so neither owns it; it rots silently.
- **Hidden waits** — a backstage queue (manual review, batch job, partner SLA) the customer
  feels as an unexplained delay frontstage.
- **Single points of failure** — one third-party API, one person, one overnight job the whole
  step depends on.
- **Visibility mismatches** — work happening backstage that the customer *should* see (progress,
  a reason for the wait) but doesn't, so they assume the service is broken.
- **Re-keying / system seams** — data hand-typed between systems that don't talk, each a chance
  for error and delay.

Each one becomes a ranked opportunity in the alignment-diagram backlog
(`journey-map-templates.md` §5), traced to its evidence.

---

## 4. Blueprint vs. journey map — when to spend the extra effort

| Question | If yes → |
|---|---|
| Is the failure in *how the service is delivered* (staff, systems, hand-offs), not just the UI? | Blueprint. |
| Does fixing it require changing what staff or back-office systems do? | Blueprint. |
| Is the problem fully visible to the customer on one screen/flow? | Journey map (or a wireflow) is enough. |
| Are multiple teams/partners involved and blaming each other for a drop? | Blueprint — it surfaces the owning lane. |

Do not reach for a blueprint when a journey map answers the question — the extra lanes are cost,
not virtue. But when the failure lives backstage, only the blueprint can find it.

---

## 5. Accessibility & doctrine hooks

- Model the **alternative channels** (phone, SMS, in-person, offline fallback) as their own
  frontstage/backstage paths, not afterthoughts — channel equity is part of the service, and a
  single-channel blueprint is incomplete against `doctrine/references/wcag-2.2-criteria.md`.
- A backstage that produces a frontstage so generic the customer doesn't trust it is a slop
  signal at service scale (`doctrine/references/ai-slop-taxonomy.md`); the delivered experience,
  like the rendered one, must read as authored (doctrine §0).
