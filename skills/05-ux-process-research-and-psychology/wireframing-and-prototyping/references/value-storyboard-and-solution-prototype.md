# Value Storyboards and Minimum Solution Prototypes

Parent skill: [`../SKILL.md`](../SKILL.md) (`wireframing-and-prototyping`).

**When to read:** before any wireframe exists, when a new product or major feature must be tested
for *value* (do people want this, and does the key moment make sense?) rather than usability of
finished screens. Sits below the lowest rung of `fidelity-ladder.md`: a storyboard frames the
experience, and a minimum solution prototype makes the few moments that carry the value
testable.

---

## 1. Value storyboard

A storyboard shows the moments that make the product worth having, across the whole experience,
including offline moments the interface never shows.

**Procedure**

1. List six to eight panels covering the full span, from the trigger to the outcome, however long
   it takes in real life (an hour, a week, a harvest season).
2. Keep only the moments that carry value or risk; drop routine steps (log-in, settings).
3. Include at least one offline or human moment (an agent visit, a delivery, a phone call) where
   the service can fail outside the screen.
4. Choose the fastest visual form: sketches, photos of the real setting, or rough composites.
   Keep every panel the same aspect ratio. Do not wireframe at this stage.
5. Write a caption of two short lines or fewer under each panel; say what happens and what the
   person feels or decides.
6. Review for flow (does each panel lead to the next?), brevity, and whether a stranger can retell
   the value in one sentence after viewing it.

| Decision | Rule | Failure caused by the wrong choice |
|---|---|---|
| Panels show features | Show moments of value and decision | A feature tour that tests nothing |
| Offline steps omitted | Include the handover and fulfilment moments | Screen-perfect product that fails at delivery |
| High-fidelity panels | Keep rough | Reviewers judge polish instead of the idea |
| Only happy path | Add one complication panel | Hidden failure point surfaces after build |

## 2. Minimum solution prototype

The smallest set of screens that lets a participant experience the value proposition and react to
the business model. Typically five parts, each one to three screens:

| Part | Shows | Question it answers |
|---|---|---|
| Entry | Landing or home state as the user would first meet it | Does the person understand what this is for? |
| Key moment 1 | The interaction that delivers the distinctive value | Does the core idea make sense and appeal? |
| Key moment 2 | The next most important interaction | Does the flow hold together? |
| Outcome | The result of a successful task (confirmation, delivered value) | Is the result worth the effort? |
| Price or terms (if relevant) | Fees, plan, commission or package | Would they pay this, this way? |

**Build rules**

1. Write the screen list as an outline before drawing anything.
2. Assemble quickly from sketches, existing components and placeholder imagery. Pattern
   references from other products are acceptable *inside a disposable test artefact* to reach
   realism quickly; they must never pass into production design, which follows the doctrine's
   authorship and anti-imitation rules (`doctrine/design-doctrine.md` §0).
3. Use representative content in the user's language and currency; lorem and fake-looking data
   distort reactions.
4. Deliver it on the device participants will use (usually a mid-range Android phone), as a
   clickable file or a swipeable PDF so participants move at their own pace.
5. Stop building when the five parts are testable. A prototype nobody learns from is waste.

## 3. Testing it

- Run with five participants from the target segment per round (see
  `../../ux-research-and-usability-testing/references/guerrilla-intercept-sessions.md` for
  low-cost recruitment and session logistics).
- Ask participants to talk through what they think each screen is for before tapping.
- Record: comprehension of the entry screen, reaction at each key moment, stated and behavioural
  willingness at the price screen (a request to be notified or to book is stronger than praise).
- Decide persevere, change or stop against a threshold set before the round.

## 4. Worked example (original): input credit for smallholder farmers, Mbale

A cooperative wants farmers to order seed and fertiliser on credit through an agent's phone,
repaid after harvest via mobile money.

Storyboard panels: farmer hears at a cooperative meeting that inputs can be ordered on credit;
agent visits and checks eligibility on the phone; farmer chooses a seed and fertiliser package;
confirmation SMS in Lumasaaba and English; inputs collected at the depot; harvest sold and
repayment deducted, with a receipt; complication panel: depot runs out of the chosen seed.

Minimum solution prototype (agent's phone): entry (farmer look-up by name and group); key moment 1
(package choice with total cost and repayment date in shillings); key moment 2 (credit terms read
aloud by the agent, farmer confirms); outcome (SMS confirmation mock-up); terms (interest and
penalty shown plainly). Test: five agents and ten farmers in two sessions. Threshold: eight of
ten farmers can restate the repayment date and total without prompting. Result: `NOT_ASSESSED`.

## 5. Checks

- [ ] Storyboard spans trigger to outcome and includes an offline moment and a complication.
- [ ] Prototype covers entry, one or two key moments, outcome and, where relevant, price.
- [ ] Borrowed patterns are confined to the disposable test artefact.
- [ ] Content, currency and language are representative of the participants.
- [ ] A decision threshold was set before testing.

---

**Evidence/currentness (accessed 2026-09-24):** method guidance only; no tools, versions or
statistics are claimed. Prototyping-tool capabilities: `NOT_ASSESSED`; choose tools per current
vendor documentation.

Sources: Levy (2015) *UX Strategy*, O'Reilly Media; Buxton (2007) *Sketching User Experiences*;
Deacon (2020) *UX and UI Design Strategy*.
