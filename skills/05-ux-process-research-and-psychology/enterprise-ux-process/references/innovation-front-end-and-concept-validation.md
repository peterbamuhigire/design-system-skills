# Innovation Front End and Concept Validation

Parent skill: [`../SKILL.md`](../SKILL.md) (`enterprise-ux-process`).

**When to read:** before Phase 1 when the engagement is not "improve an existing product" but "find
and prove a new service, product or business line" inside an established organisation; whenever a
promising concept keeps dying in portfolio review; and when a compressed one-to-two-week client
engagement must still move from a fuzzy brief to a tested concept and a funded next step.

---

## 1. When this procedure applies

| Situation | Use this procedure? | Consequence of the wrong choice |
|---|---|---|
| The work crosses user need, business model, technology and organisational fit at once | Yes, full six-stage run | A UX-only process ships a desirable concept the organisation will not fund or cannot operate |
| An established organisation where good ideas have repeatedly been killed by "not a priority for us" | Yes; the organisational-fit dimension is mandatory | The team repeats the failure because fit was never tested |
| The brief itself is vague (the fuzzy front end is the real problem) | Yes; do not skip the landscape and research stages | Solution lock-in: the team builds the first familiar idea |
| A bounded feature or interface question that can be settled in days | No; use a five-day sprint or `wireframing-and-prototyping` | Weeks of framing overhead for a question a prototype answers |
| Continuous iteration on a live software product | No; use hypothesis cycles in `experience-mapping/` | Front-end ceremony slows a team that already has a validated frame |
| A regulated enterprise product at maturity Level 3 or 4 | Run this first, then hand the reframed vision into Phases 1-9 of the parent skill | Phases 1-9 optimise the wrong problem |

This procedure is an umbrella: sprints, lean experiments and agile delivery run inside it, and it
hands over to agile delivery at the end.

## 2. The four dimensions and the four success tests

Track four **dimensions** in every stage, not only the user:

| Dimension | Question the team keeps answering |
|---|---|
| User | Who needs this, in what situation, and what do they do today? |
| Market | Who else serves this need, where is the profit, who are the non-customers? |
| Technology | What can be built, integrated and operated with available or obtainable capability? |
| Organisation (firm) | Does this fit the organisation's intent, risk appetite, funding band, sponsors and delivery capacity? |

Judge every concept against four **success tests**:

| Test | A concept passes when... |
|---|---|
| Desirability | Evidence shows the focus user wants it and will change behaviour for it |
| Viability | A plausible model shows it can earn more than it costs |
| Feasibility | It can be built and operated with capability the organisation has or can obtain |
| Strategic suitability | It fits the organisation's stated direction, risk appetite, investment band, sponsorship and time-to-deployment |

Strategic suitability is the addition to the familiar desirability-viability-feasibility triple. It
exists because concepts that pass the first three still die when they do not fit the organisation.
Never report a concept as ready while strategic suitability is untested.

## 3. The six stages (overview)

| Stage | Question it settles | Gate evidence (must exist before moving on) |
|---|---|---|
| 1. Landscape audit | What is the present state of market, technology and organisation? | Project outline; organisational innovation profile; environmental action map |
| 2. Deep user research | Who are the users and stakeholders and what do they really need, and why? | Field notes; empathy maps; experience maps; root-cause chains; raw insights |
| 3. Reframe | What new perspective and scope make a breakthrough possible? | Insight notes; persona(s); persona needs matrix; signed reframed vision |
| 4. Ideate | Which concepts could realise the new frame? | One or two concept boards with assumptions listed; first sanity check |
| 5. Validate | Are the critical assumptions in the concept and its business model true? | Lean canvas v1; assumption map; experiment evidence |
| 6. Prove at small scale | Can the concept show revenue-earning capacity at limited scale? | Investment concept board; business case dashboard; test plan and experiment canvases |

Rules that apply across all stages:

- **Order matters; execution is nested.** Keep the stage order, but every method inside a stage has
  its own diverge-then-converge loop.
- **Artefacts travel forward.** Every later artefact cites an earlier one: the concept board cites
  the persona needs matrix; the lean canvas cites the concept board; the business case dashboard
  cites the lean canvas and the assumption map. An artefact with no backward link is a warning sign.
- **Skipping a stage is allowed but raises risk.** Record the skip, the reason and the risk accepted
  in the decision log. The process de-risks; it is not a straitjacket.
- **Stay with the user from start to launch.** User evidence is gathered in stage 2 and re-tested in
  stages 5 and 6, not left behind after research.
- **Launch is a graduation, not a stage.** A concept graduates to delivery once stage 6 evidence is
  accepted.

## 4. Stage procedures

### Stage 1 - Landscape audit

Market, technology and organisation are audited here with established strategy tools; deep user
work waits for stage 2.

1. Write the **project outline** (one page): project name and date; primary motivation or problem
   statement; possible areas of interest; initial scope (in and out); known constraints; key
   questions to answer; success indicators (placeholder until stage 3).
2. Write the **organisational innovation profile**: strategic intent and direction; risk appetite
   (low, medium, high); investment band available; internal capabilities (technology, channels,
   brand); named senior champion(s); adjacent strategic projects; cultural and process readiness;
   time-to-deployment capability. Every later stage checks concepts against this profile.
3. Scan the wider environment (**PESTEL**): one issue per note, sorted into political, economic,
   social, technological, environmental and legal. Rate each issue low, moderate, high or very high
   on *importance* and on *uncertainty*.
4. Place the issues on an **environmental action map** (importance against uncertainty):

   | | Low uncertainty | High uncertainty |
   |---|---|---|
   | **High importance** | Act now | Watch closely; plan scenarios |
   | **Low importance** | Schedule routine handling | Ignore for now |

5. Map the industry: competitive forces (rivals, new entrants, substitutes, buyer power, supplier
   power) with the organisation at the centre, and a **profit-pool table** (segment against share of
   industry profit).
6. Identify sub-markets and use cases: a **non-customer tier list** (tier 1: customers about to
   leave; tier 2: people who consciously refuse the offer; tier 3: people nobody in the industry has
   considered), and a **process-chain map** (the value chain left to right, with sub-steps, pain
   points and current actors marked).
7. Capture mission, vision and values alongside the profile.
8. Decide the entry route to stage 2: field research with users now, or, where the organisation
   holds deep internal expertise, start from a structured critique of that expertise (experts
   challenge each other's interpretations of what the product could mean) and test the result with
   users afterwards. Record which route was chosen and why.

### Stage 2 - Deep user research

Qualitative, in context, aiming at *why* as well as *what*. Methods and their templates:

| Method | Template fields | Detailed guidance |
|---|---|---|
| Design ethnography (field study) | Research question; site; participants; observation notes; photos and artefacts; surprises; emerging patterns; follow-up questions | `../../ux-research-and-usability-testing/references/research-method-selector.md` |
| Experience mapping | Lanes: journey stages; user actions; touchpoints and channels; thoughts (verbatim where possible); emotion curve; pain points and opportunities | `experience-mapping/references/journey-map-to-requirements.md` (layered structure) |
| Empathy mapping | Six areas: says; thinks; does; feels; pains; gains. Fill "says" and "does" from observation before inferring "thinks" and "feels" | This file |
| Root-cause chain (five whys) | Observed issue at the top; ask "why?" up to five times, each answer grounded in evidence; the root cause at the bottom | This file |
| Think-aloud sessions | Participant narrates while working | `../../ux-research-and-usability-testing/references/usability-test-protocol.md` |

End each field day with a short (about 30 minutes) insight-capture session that writes insight notes
while memory is fresh.

### Stage 3 - Reframe

Pure synthesis. The new frame is informed by research and sets the scope for ideation. Without this
stage research becomes a report nobody acts on and ideation becomes random.

1. **Affinity-map** observations into themes (see `ux-research-and-usability-testing`).
2. Write **insight notes**, one card each: observation; underlying need; design implication;
   supporting quotes or evidence. Aim for eight or fewer strong notes.
3. Build one or two **personas** traced to research: name; demographic snapshot; behaviours;
   motivations; frustrations; context of use; one representative quote. (The parent skill's persona
   discipline applies.)
4. Fill the **persona needs matrix**: rows are user needs; columns are priority, current solution,
   gap, and design implication.
5. Test the **status-quo (paradigmatic) assumptions** here: beliefs about how the market or service
   "must" work. Concept (causal) assumptions of the form "if we build X, users will do Y" wait for
   stage 5.
6. Write the **reframed vision** (one page): original framing (one sentence); new framing (one
   sentence stating the shift in meaning); why this frame (insight evidence); focus user; in and out
   of scope under the new frame; working title.
7. Tell the frame as a short story of the focus user's situation before and after, for sponsors.
8. Obtain **sign-off of the reframed vision** from the accountable client owner. This is the largest
   decision gate in the procedure.

Rule: a concept cannot serve everyone. Choose the frame most likely to give a compelling answer for
the main user with the highest impact potential, and state who is deliberately not served.

### Stage 4 - Ideate

1. **Diverge.** Brainstorm; force connections between unrelated stimuli; look through the eyes of a
   different role (a regulator, a rival, a child, a field agent); generate deliberately bad ideas and
   invert them; borrow metaphors and analogies from other sectors. Aim for quantity (50 or more raw
   ideas in a day-long session).
2. **Converge by concept synthesis.** Choose a base idea, graft in supporting ideas, name the
   concept, and write a one-line value proposition.
3. Produce a **concept board** (one A3 page per concept): evocative name; one deliberately rough
   hero sketch; one-line value proposition; two to four user benefits; insights addressed (linked to
   rows of the persona needs matrix); headline use scenario.
4. Keep boards low fidelity. Near-realistic visuals make people judge finish ("is it done?") instead
   of the idea ("is this right?"). See `../../wireframing-and-prototyping/references/fidelity-ladder.md`.
5. Run the **feasibility-viability-suitability sanity check** (section 5) on each surviving concept.
   Desirability leads in this stage; the sanity check only catches showstoppers.
6. Output: one or two concepts, each with its assumptions written down.

### Stage 5 - Validate

The concept becomes a business proposal covering all four dimensions.

1. Write **success assertions** per test: for desirability, viability, feasibility and strategic
   suitability, list "for this concept to succeed, ___ must be true."
2. Move every assertion onto the **assumption map** (importance to success against strength of
   existing evidence). High importance with weak evidence is tested first. The scoring and threshold
   discipline in `experience-mapping/references/hypothesis-and-validation-thresholds.md` applies.
3. Draft **lean canvas v1** (nine cells): problem; customer segments; unique value proposition;
   solution; channels; revenue streams; cost structure; key metrics; unfair advantage.
4. Run a **pre-mortem**: imagine the launched concept has failed; each person lists why; convert the
   reasons into assumptions on the map.
5. Test the riskiest assumptions with the cheapest adequate prototype: Wizard of Oz (a person fakes
   the system behind the interface), paper prototype, or role play of the service encounter.
   Prototypes are learning vehicles, not deliverables.
6. Update the lean canvas and assumption map after each round.

### Stage 6 - Prove at small scale

Validation removes assumption risk; this stage proves the *capacity* to earn revenue at limited
scale, with real paying customers where possible. Earning revenue is not the objective.

1. Produce the **investment concept board**: the stage 4 board plus business proposition, market
   size, strategic-fit narrative, key risks and a deployment summary.
2. Produce the **business case dashboard** (one large poster or page): concept hero; target user and
   market; value proposition; lean canvas summary; validated assumptions and remaining risks;
   investment requested and expected return; roll-out roadmap with learning gates.
3. Write the **small-scale test plan**: which experiments, in what order, against which remaining
   assumptions, with what budget, by when.
4. Fill one **experiment canvas** per experiment: hypothesis; method; metric; success threshold (set
   before running); cost; owner; learnings.
5. Keep iterating the lean canvas. Hand the test plan to the client's delivery team in their agile
   cadence.

## 5. Feasibility-viability-suitability sanity check

Nine questions, three per test. Any "no" is a showstopper to resolve or record. Run it at first
convergence (stage 4) and at least monthly for every live concept.

| Test | Question |
|---|---|
| Feasibility | Can the core function be built with technology that exists today? |
| Feasibility | Do we, or a partner we can realistically contract, have the skills to build and run it? |
| Feasibility | Can it integrate with the systems, data and channels it depends on? |
| Viability | Is there a credible payer, and a price they would accept? |
| Viability | Can unit costs fall below unit revenue at a reachable scale? |
| Viability | Is there a regulatory or compliance route that does not erase the margin? |
| Strategic suitability | Does it fit the stated intent and risk appetite in the organisational profile? |
| Strategic suitability | Is the likely investment inside the available band, and is a named champion willing to own it? |
| Strategic suitability | Can the organisation deploy it within the time the opportunity stays open? |

(These nine questions are this engine's own wording of the three-by-three check.)

## 6. Choosing among front-end processes

| Concern | Five-day design sprint | Lean experiment loops | Double diamond | This six-stage procedure |
|---|---|---|---|---|
| Time scale | One week | Continuous | Project length | Weeks to months end to end |
| Problem-space depth | About one day | Often starts at a hypothesis | Discover phase | Two full stages (audit and research) before synthesis |
| Business viability | Light | Central (lean canvas) | Implicit | Tested throughout via the four success tests |
| Organisational fit | Not addressed | Not addressed | Not addressed | Organisational innovation profile is mandatory |
| Reframing | Implicit | Implicit in pivots | Define phase | Dedicated stage with its own evidence and sign-off |
| Validation | One test day | Continuous tests and interviews | Deliver phase | Assumption-mapped prototypes; validation kept separate from small-scale proof |
| Best fit | Quick feature or interface questions | Iterating a software product | General mental model | Established organisations attempting multi-dimensional change |

## 7. Compressed engagement (one to two weeks with a client)

**Before week 1 (two to three days, mostly asynchronous).** Send the project outline and
organisational innovation profile templates as client homework; hold a 60-minute kick-off to walk
through both; draft the PESTEL list, competitive forces and non-customer tiers from desk research.

**Week 1 - audit, research, reframe**

| Day | Stage | Work and outputs |
|---|---|---|
| Mon morning | Audit | Working session: agree the action map and competitive forces; finalise project outline and innovation profile |
| Mon afternoon | Research set-up | Recruit five to six users for Tuesday and Wednesday |
| Tue-Wed | Research | Five to six in-context interviews; build empathy and experience maps live; 30-minute insight capture each evening |
| Thu morning | Reframe | Affinity session (two to three hours); reduce to eight or fewer insight notes; one or two personas; persona needs matrix |
| Thu afternoon | Reframe | Write the reframed vision |
| Fri | Reframe gate | 90-minute review; client signs off the frame (largest decision gate) |

**Week 2 - ideate, validate, small-scale proof (light)**

| Day | Stage | Work and outputs |
|---|---|---|
| Mon morning | Ideate (diverge) | Warm-ups and idea generation; 50 or more raw ideas |
| Mon afternoon | Ideate (converge) | Concept synthesis; two candidate concepts; first sanity check |
| Tue | Ideate | Two A3 concept boards |
| Wed | Validate (set-up) | Lean canvas v1; pre-mortem; assumption map |
| Thu | Validate (tests) | Wizard of Oz, paper or role-play tests with four to five users; update lean canvas |
| Fri morning | Small-scale proof (light) | Investment concept board; business case dashboard; two-page test plan with one to three experiments for the next 30, 60 and 90 days |
| Fri afternoon | Hand-over | Artefact pack handed to the client |

**Never cut, even when compressed:** the organisational innovation profile; the reframed-vision
sign-off; the assumption map; the feasibility-viability-suitability sanity check.

## 8. Worked example (original)

A Kampala savings and credit co-operative (SACCO) asks for "a loan app for our boda-boda rider
members".

- **Audit.** The innovation profile records low risk appetite, a modest investment band, a board
  chair willing to champion, and mobile-money integration as an existing capability. The action map
  puts mobile-money transaction levies (high importance, high uncertainty) in "watch" and new
  digital-lending regulation (high importance, lower uncertainty) in "act now". The non-customer
  tiers show tier 2 includes riders who refuse SACCO loans because repayment schedules are monthly
  while their income is daily.
- **Research.** Rides with six riders and two stage chairmen produce empathy maps; the five-whys chain
  on "missed repayments" ends at "a single breakdown wipes out the week's income", not at "riders
  are careless".
- **Reframe.** Original frame: "a loan app". New frame: "daily-income protection for riders, with
  credit as one part". The status-quo assumption "loans must be repaid monthly" is challenged here.
  The focus user is the owner-rider repaying a motorcycle; riders who rent by the day are out of
  scope for now. The SACCO chair signs the vision on Friday.
- **Ideate.** Two concept boards: "Daily Stage Pot" (small daily repayments via mobile money, with a
  breakdown buffer) and "Spare-Part Credit" (credit paid directly to approved mechanics).
- **Validate.** Top assumption on the map: "riders will save a small amount daily without a
  reminder from their stage chairman". A Wizard of Oz test (a staff member sends and records the
  prompts manually) runs for two weeks with eight riders; the success threshold was set beforehand.
- **Small-scale proof.** The test plan pilots Daily Stage Pot at two boda-boda stages, with a
  threshold for repayment rate and member fee income before the board commits the investment band.

## 9. Checks

- [ ] The four dimensions and four success tests appear in the stage 1 and stage 5 evidence.
- [ ] The organisational innovation profile exists and every concept is checked against it.
- [ ] The reframed vision is signed by an accountable owner before ideation starts.
- [ ] Status-quo assumptions were tested in reframe; concept assumptions in validate.
- [ ] Concept boards are low fidelity and link to persona needs matrix rows.
- [ ] The sanity check has been run within the last month for every live concept.
- [ ] Every experiment has a threshold written before it ran.
- [ ] Validation evidence and small-scale revenue evidence are reported separately.
- [ ] Any skipped stage is logged with its reason and the risk accepted.
- [ ] Design thinking is paired with critical thinking: every creative claim is challenged with
      evidence before it moves a gate.

---

Sources: Devitt, Ryan et al., *Arrive: A Design Innovation Framework to Deliver Breakthrough
Services, Products and Experiences*, Routledge (six-stage meta-process, strategic suitability as a
fourth success test); Maurya (lean canvas); Gray (empathy map); Porter (competitive forces); Kim and
Mauborgne (non-customer tiers); Verganti (design-driven critique of internal expertise).
