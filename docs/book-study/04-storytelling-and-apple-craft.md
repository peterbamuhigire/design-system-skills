# Book Study 04 — Design Storytelling & Apple Craft/Taste (4 books, critically mapped to the engine)

**Engine:** `C:\wamp64\www\design-system-skills` — 53 skills / 14 groups, anchored on `doctrine/design-doctrine.md`
(Mission: *the moat is looking human-made*; the Anti-Slop Charter; the sourcing-authority asymmetry rule).
**Date:** 2026-06-21 · **Author:** study pass for the hardening-june programme.

## How to read this document

This is a **critical study, not a summary.** For each book it states (a) the load-bearing,
*transferable* ideas worth extracting; (b) a critical take — separating transferable **method** from
mere anecdote/memoir, what genuinely **sharpens the anti-slop "human-made" Mission** vs what is merely
inspiring or dated; and (c) engine impact — how it sharpens the **doctrine itself**, `distinctive-by-design`,
`brand-visual-identity`, the **deck-system narrative**, and the **critique/process** skills — plus a clear
**BUILD / DON'T-BUILD** verdict on any net-new skill or doctrine reference, and **CONFIRM / CHANGE /
REDUNDANT** calls on the Phase-2 P1 plan (`docs/plans/hardening-june/phase-2-p1-wave/01-skill-specs.md`).

**The standing filter differs from Book Study 01–03.** Those were beginner/intermediate craft primers we
mined *downward* for numbers and checklists. **These four are different in kind, and split into two pairs:**

- **The Apple pair (Kocienda, Janoff)** operates *at or above* our doctrine's altitude on the one axis we
  care about most — **taste, refinement, and pushing away from the convergent mean.** These are not books we
  out-rank; they are the closest published articulation of *why* our Mission is correct and *how* a real
  world-class shop actually produced authored work. We mine them for **process spine and vocabulary**, which
  is exactly the thing we told ourselves the primers could never give us.
- **The storytelling pair (Sandler, *UX Storytellers*)** is a **frameworks reference (Sandler)** + a
  **memoir anthology (*UX Storytellers*)**. Sandler is genuinely extractable as a *catalogue of named
  narrative structures* for decks and case studies; the anthology is ~90% inspiration/memoir with one
  load-bearing thesis ("the story is the thing") and almost no transferable mechanics.

So the extraction posture inverts the earlier studies: **mine the Apple pair for METHOD and the doctrine's
own backbone; mine Sandler for named NARRATIVE FRAMEWORKS for the deck/case-study skills; mine the anthology
for a single confirming thesis and otherwise treat it as motivation, not method.**

> **Provenance note.** Kocienda is a primary-source memoir by the iPhone keyboard/Safari engineer — its
> *method* (creative selection, demo discipline, the algorithm/heuristic split, taste-over-A/B) is
> first-hand and reusable; its *anecdotes* (Steve's moods, the door-broken-with-a-bat) are colour, not
> method, and are logged as such. Janoff is a short illustrated memoir whose *design-philosophy chapter*
> ("New growth") is the extractable core; the rest is autobiography.

---

## Book 1 — *Creative Selection: Inside Apple's Design Process During the Golden Age of Steve Jobs* (Ken Kocienda, 2018)

This is the most important of the four for the engine. It is the rare insider account of *how authored,
non-convergent product work actually gets made*, written by the person who built the iPhone autocorrect and
co-built Safari. Almost everything in it is method, and almost all of that method is transferable.

### (a) Load-bearing transferable ideas

- **Creative selection itself — the demo → feedback → next-demo loop as a Darwinian variation/selection
  engine.** Not brainstorming, not specs, not A/B: a *continuing progression* of concrete working demos,
  each one a deliberate variation on the last, with feedback as the selection pressure. "We habitually
  converged on demos, then allowed demo feedback to cause a fresh divergence." This is the missing **process
  spine** under our entire Mission — the doctrine says *make an authored choice*; Kocienda says *here is the
  machine that reliably produces authored choices.*
- **The concrete demo beats the abstract discussion — always.** The book's repeated anti-pattern is "talking
  about whose imaginary puppy is cuter" — meetings, specs, and paper mock-ups with nothing real to react to.
  The rule: **never hold a design discussion without a concrete artifact to ground it.** (Directly indicts
  lorem-ipsum design, which our `distinctive-by-design` already bans on the same logic — *placeholder text
  produces placeholder design*.)
- **The "thick imaginary marker" / Hollywood-backlot demo-fidelity rule** (Richard's Konqueror demo). Draw a
  conceptual ring around the *one thing the demo must prove*; build that at the highest fidelity (the
  lamppost that bears the actor's weight); fake or omit everything outside the ring (the empty hat-shop
  facade); take extra care only at the boundary. Define **goals and explicit *non-goals*** before building.
  This is a precise, teachable method for **what to make real and what to fake** in any prototype, mock, or
  pitch artifact.
- **Taste vs. the algorithmic crutch — the "41 shades of blue" critique.** Kocienda's central argument
  against Google's A/B-tested blue: A/B testing has a tiny dynamic range (it picks the best of 41 options it
  was *handed*) and its opportunity cost is the design that would have been 10× better. **"Google factored
  out taste. At Apple we never would have dreamed of it… we picked one and moved on."** This is the single
  most quotable, doctrine-grade passage in all four books — it is the **sourcing-authority asymmetry rule
  expressed as a process choice**: do not outsource a taste decision to a metric (or, by extension, to an AI
  recommend-list) when the real lever is conviction + refinement.
- **Algorithms vs. heuristics — the two-sided coin of craft.** Algorithms have an "arrow of improvement"
  that always points the same way (faster page load = better); heuristics (animation duration, a colour, a
  swipe threshold) have a *value but no objective arrow* and can be resolved **only** by demo + taste + time.
  The error Google made was using an algorithm (A/B) where a heuristic was required. **Knowing which kind of
  decision you are facing is itself a craft skill.** Hugely useful as a critique lens.
- **"Live on the software."** You cannot judge a heuristic from one demo; the team *used* the build daily
  ("I lived on the software") to feel whether choices added up. Refinement is **longitudinal**, not a single
  review.
- **Simplicity as load-shedding, grounded in Miller's 7±2.** The iPad-keyboard story (Steve: "we only need
  one of these, right?"), the removed suggestion bar (fewer places to look = *measurably faster* typing),
  charged buttons, touch-warping, slide-to-unlock-a-child-can-use. The discipline: **answer hard questions by
  eliminating the need to ask them.** "Edit for less."
- **"Working at the intersection" (technology × liberal arts).** You cannot engineer a thing and then bolt on
  "look and feel" — the algorithm and the heuristic are interleaved (the photo-swipe: heuristic → algorithm →
  algorithm → heuristic). *"Design is how it works."*
- **The seven essential elements:** inspiration, collaboration, craft, diligence, decisiveness, taste,
  empathy — explicitly *not* a checklist but a distillation; "everything counts, no detail is too small."
- **Small teams, a single decider, decisiveness on the spot.** Ten people shipped Safari beta; ~25 are on the
  iPhone patent. Every review had *one* "decider"; access to the room was earned by *making the work better*,
  not by org-chart rank.

### (b) Critical take — method vs memoir; what sharpens the Mission

- **This book sharpens the Mission more than any other source we have read.** Our doctrine asserts the moat
  (*looking human-made*) but is comparatively thin on the *production method* that yields it. Kocienda
  supplies that method, first-hand, from the one company whose name is synonymous with authored craft. The
  "41 blues" passage is effectively a **second, process-side statement of our sourcing-authority asymmetry
  rule** — and a far more memorable one than our current phrasing.
- **Separate the method from the hagiography.** The transferable core is: creative selection, the demo
  fidelity ring, the algorithm/heuristic split, taste-over-metric, live-on-it, edit-for-less. The
  *non*-transferable residue is the Steve-Jobs theatre (moods, the RDF, the broken doorknob, the champagne) —
  inspiring, but it is **survivorship-flavoured memoir**, not a repeatable practice. Do **not** import "a
  single all-powerful mercurial decider" as a process recommendation; import "every review has *a* decider
  and decisiveness is required." (Kocienda himself flags the *Seagull Manager* — influence without
  involvement — as the failure mode, so the book guards this for us.)
- **One honest limitation to log:** Kocienda's "we never A/B tested anything" is partly era + product luck
  (a secret project with no population to test on). The defensible doctrine reading is **not** "telemetry is
  bad" — it is "do not let a metric *make a taste decision for you*, and do not let measurement displace
  conviction and refinement." Keep that nuance when we cite it, or we'll mis-teach it.
- **Nothing here is dated.** The method is substrate-independent; it reads as directly applicable in 2026 as
  in 2007. This is the only book in any study so far of which that is true.

### (c) Engine impact

- **Sharpen the DOCTRINE.** Add a short doctrine reference — `doctrine/references/creative-selection-and-taste.md`
  — capturing (i) the demo → feedback → next-demo loop as the *named production method behind the Mission*;
  (ii) the **algorithm-vs-heuristic** decision lens; (iii) the **"41 shades of blue"** passage as the
  canonical illustration of the sourcing-authority asymmetry rule on the *process* side (a taste decision
  outsourced to a metric is the same error as a taste decision outsourced to an AI recommend-list). This is
  the highest-leverage single change the four books justify. The Mission gains a *how*, not just a *what*.
- **Harden `04…/distinctive-by-design`.** Its workflow currently jumps from "state the ONE decision" to
  "build." Insert a **demo/iteration loop** between them: build the smallest real artifact that proves the
  one distinctive idea (the fidelity ring), live on it, get feedback, vary, re-decide. Add the
  **algorithm-vs-heuristic** distinction to step 3 (composition/heuristic calls are *demo-and-taste*
  decisions, not metric decisions). Add "edit for less / answer hard questions by removing them" as an
  explicit move.
- **Harden the critique/process group (00 `design-critique-and-review-facilitation`, P1; 05
  `heuristic-evaluation-and-design-critique`, P1).** The **single-decider + decision-capture** model and the
  **demo-grounded critique** rule ("no critique without a concrete artifact to react to") are exactly the
  protocol spine those two P1 skills need. The taste/heuristic-vs-algorithm lens is a reusable critique axis.
- **`brand-visual-identity` + `color-system-and-palette`:** add the "41 blues" reasoning as the named
  argument for **picking a signature colour by conviction, not by test** — it strengthens the existing
  anti-gradient stance with a process rationale.
- **NEW-SKILL verdict — `05…/demo-driven-design-process` (a.k.a. "creative-selection"): BUILD (P2, high
  value).** Justified, and *not* redundant with anything in groups 00/05. It would carry: the demo loop, the
  fidelity-ring/non-goals method, prototype-fidelity tiers, "live on it," the decider model, and the
  algorithm/heuristic lens. **Caveat:** keep it a *process* skill in group 05; do **not** let it duplicate
  the doctrine reference (the doctrine ref states the principle; the skill operationalises it). Build the
  doctrine ref first (cheap, high-leverage), then this skill.

---

## Book 2 — *Taking a Bite Out of the Apple: A Graphic Designer's Tale* (Rob Janoff, 2018)

Memoir of the designer of the 1977 Apple logo. Most of it is autobiography; the value is concentrated in
the logo-design narrative (chapters "Taking a bite" / "Ripening it") and the explicit design-philosophy
chapter ("New growth"). It is a **brand-identity-craft** source, narrow but sharp.

### (a) Load-bearing transferable ideas

- **Simplicity for *memorability* — "When in doubt, leave it out."** Janoff opens his guidelines with it and
  ties it to a hard outcome: a logo's job is to *be remembered*, and complexity is the enemy of memory.
  Clients arrive with "laundry lists of must-haves" — "a recipe for failure." **A clear message is singular.**
  ("Simple is deceptively difficult.")
- **Idea before execution; tech can be an idea-killer.** "Going straight to the computer… is often devoid of
  an idea… you're fussing over a corner and forgetting the bigger idea. The idea should come first, the
  execution follows." A near-verbatim restatement of our **anti-slop process rule** (don't reach for the
  tool/default to "get something on screen").
- **The bite = scale-relater + interactivity + wit.** The bite makes the silhouette *unmistakably an apple,
  not a cherry* (scale), and it **invites the viewer in** ("you too can take a bite of this new world") —
  it makes the mark *interactive*. The "byte" pun was a happy accident, but the lesson is deliberate: **a
  mark that carries wit or a small surprise gets remembered.** (His exemplars: the FedEx hidden arrow; Glaser's
  I♥NY.) This is *meaning earned through a single device*, not literal depiction.
- **Distinctiveness is relative and contextual — "do your homework."** Know the client, the competition, and
  *where the mark will be seen* (store aisle? favicon? sign?). FedEx deliberately did "everything the
  opposite of UPS" to stand out. This is precisely our `brand-visual-identity` "not-to-be-confused-with"
  list — stated from the practitioner's mouth.
- **Metaphor/subliminal, never literal.** "If there's a message, visualise it metaphorically, perhaps
  subliminally — certainly not literally."
- **Empathy as a design input.** "You need empathy — for the client and the consumer — to reach the right,
  unique solution… as an observer you may end up with greater insight into their business than they have."
- **A mark must survive reduction and stand alone.** The Apple mark works at the corner of every screen, in
  one colour, from memory; a strong icon eventually sheds the wordmark and crosses languages with "no
  translation required." (Reinforces our responsive-logo / favicon / mono-variant requirements.)
- **The rainbow stripes were *tied to the product's USP*** — the Apple II's defining capability was colour
  on a home TV; the six-colour logo *was* that story. Identity choices should encode what makes the product
  different, not decorate.

### (b) Critical take — method vs memoir; what sharpens the Mission

- **Janoff's craft principles are world-class and *exactly our doctrine*, but mostly already covered.**
  Simplicity, the memory test, distinctiveness-against-competitors, metaphor-not-literal, mono/favicon
  survival, no-literalness — `brand-visual-identity` already carries every one of these (it cites Rand,
  Vignelli, Neumeier for the same points). So Janoff is **largely CONFIRMATORY, not net-new.** His value is
  *primary-source quotability* and two sharper-than-ours formulations.
- **The two genuinely sharpening additions:** (1) the **scale-relater + "interactive wit"** idea — a mark
  that *invites the viewer in* and carries a small surprise/pun is more memorable; this is a *generative*
  identity move our skill doesn't currently name (we say "ownable," he says "interactive + a surprise"). (2)
  **Identity encodes the product's USP** (stripes = colour-on-TV) — a concrete rule for *what* the
  distinctive element should mean, which our strategy step gestures at but doesn't make explicit.
- **What's dated/memoir, not method:** the "present only one concept to the client" story (he himself says
  he'd never do it today — show three), the late-'60s pop-art influences (Peter Max, *Yellow Submarine*),
  and the autobiography. The internet-criticism aside ("just because everyone has an opinion doesn't make
  opinions equal value") is a nice line for critique facilitation but not load-bearing.
- **Mission fit:** strongly aligned. Janoff is a living argument that *one simple, authored, witty mark beats
  a literal, busy, committee-driven one* — i.e. our "restraint plus one strong choice." But it does not
  *extend* the Mission the way Kocienda does; it confirms it from the identity corner.

### (c) Engine impact

- **Harden `02…/brand-visual-identity`** with: (i) **"interactive wit / a small surprise"** as a named,
  generative move in the logo step (with FedEx-arrow and I♥NY as the canonical examples, alongside the
  existing Rand/Vignelli grounding); (ii) **"the mark should encode the product's USP/differentiator"** as
  an explicit strategy rule (stripes = the Apple II's colour-on-TV); (iii) Janoff's **"When in doubt, leave
  it out"** and the **memory test** as quotable reinforcements (the memory test already exists in our
  Consistency Gate — add Janoff as a named authority beside Rand).
- **Feed the Phase-2 P1 `02…/logo-and-wordmark-design`** (already planned) the Janoff material directly: the
  silhouette-iteration story (draw it every which way until the essence appears), scale-relater, mono/favicon
  survival, stand-alone-icon threshold. This is the **most natural home** for Janoff and the plan item is
  **CONFIRMED and strengthened** by it.
- **Harden `distinctive-by-design`** with Janoff's "idea before execution / tech is an idea-killer" as a
  one-line reinforcement of the existing "don't reach for the default to get something on screen" rule.
- **NEW-SKILL verdict: DON'T-BUILD.** Janoff justifies **no** net-new skill — every transferable idea lands
  inside the existing `brand-visual-identity` and the already-planned `logo-and-wordmark-design`. Adding the
  two sharpening moves to those is the entire correct action.

---

## Book 3 — *Universal Principles of Storytelling for Designers: 100 Key Concepts* (Lyle H. Sandler, 2023)

An A–Z reference of 100 narrative/literary/psychology concepts, each a two-page entry with cross-references,
drawn from theatre, literature, anthropology, film, and psychology. Format mirrors the *Universal Principles
of Design* series. It is a **catalogue, not a method** — which makes it ideal raw material for a
narrative-frameworks reference, and poor material for a process spine.

### (a) Load-bearing transferable ideas

- **A genuine *named-frameworks catalogue* for narrative** — the part of "design storytelling" our engine has
  no vocabulary for. The reusable structures: **Freytag's Pyramid** (exposition → rising action → climax →
  falling action → denouement/catharsis); **Three-Act**; **The Hero's Journey**; **Pixar's story structure
  ("Once upon a time… every day… until one day…")**; **Vonnegut's shapes of stories**; **Kishōtenketsu** (a
  conflict-*less* four-act structure — useful for explanatory/product narratives that don't want a villain);
  **In Medias Res**; the **Seven Basic Plots**.
- **Contrast, Beginning-to-End** — "a distinct *otherness* must exist between the start and end of your
  story." The before/after delta *is* the narrative; if you open on the solution (the filtration system)
  instead of the problem (the drought), the audience never feels the transformation's size. **This is the
  single most useful entry for case studies and decks** — it is the before/after spine of every credible
  design case study, stated as a principle.
- **Conflict / The Trigger or Wicked Problem** — the *why behind the what*. Story (and design) needs a
  named problem with stakes; the six conflict types and Rittel's wicked-problem attributes give a vocabulary
  for *framing the stakes* of a design challenge in a pitch.
- **Show, Don't Tell; Transformation (prompt change + provoke action); Calls to Action; the Peak-End Rule**
  (memory is shaped by the most intense moment + the end — design the climax and the closing of a deck
  deliberately); **Rule of Three; Kill Your Darlings** (cut features/elements that don't serve the story —
  the same discipline as Kocienda's "edit for less," from the writing side); **Data Storytelling** (the
  intro's Chas anecdote: a pie chart is not a story; turn numbers into people-with-stakes).
- **Empathy / Character Relatability / Personas / Jobs-to-Be-Done** — the audience-centring entries (largely
  things our UX group already covers, but useful as the *narrative* framing of them).

### (b) Critical take — method vs anecdote; what sharpens the Mission

- **This is a vocabulary/structure reference, and that is its honest value.** It will not teach taste,
  refinement, or craft, and it makes **no contact with the anti-slop Mission** — it is medium-agnostic and
  would happily wrap a templated product in a Hero's-Journey deck. Its danger, used naively, is **narrative
  as decoration over slop.** So the framing for the engine must be: *story structure organises a deck or
  case study; it never substitutes for the authored artifact the story is about.* (Kocienda's demo discipline
  is the guard: the story must be *about a real working thing*, not the imaginary-puppy pitch.)
- **Breadth-over-depth is the format's weakness.** 100 two-page entries means each framework gets a
  definition and a thin example, not an applied method. We extract the *named structures and the one or two
  decision-rules per structure* (Freytag's five beats; Contrast's before/after; Kishōtenketsu's
  no-villain option) and supply our own applied worked examples.
- **A few entries are filler for our purposes** (Star Trek, Mary's Room, Infrathin, Super Normal) — skip.
  Roughly 25–30 of the 100 are directly useful to a deck/case-study skill; the rest are literary colour.
- **Mission fit: neutral-to-positive *if* fenced.** It does not sharpen the Mission, but it **fills a real
  capability gap** — group 13 (deck-system) currently has *narrative* in scope but no named toolkit for it,
  and we have no case-study skill at all. Properly fenced ("structure serves the authored artifact"), it is
  a clean add. Unfenced, it risks becoming a slop-enabler. Fence it.

### (c) Engine impact

- **Harden `13…/presentations-and-documents` (deck-system) narrative scope** with a **narrative-frameworks
  reference**: Freytag, Three-Act, Pixar, Kishōtenketsu (no-villain explanatory option), Contrast
  beginning-to-end, Peak-End (design the close), Rule of Three, Data Storytelling (numbers → stakes). This is
  the most natural home for Sandler.
- **NEW-SKILL verdict — `13…/design-storytelling-and-case-studies` (narrative for decks & case studies):
  BUILD (P2), but RESCOPE and FENCE.** Justified: we genuinely lack a skill for *narrative structure of a
  deck/case study/portfolio piece*, and Sandler is the right source for its frameworks reference. **Rescope**
  so it is explicitly about **structuring the telling of real, authored work** (problem→stakes→authored
  decision→before/after transformation→proof→CTA), with the **standing guard that the story never replaces
  the artifact** (cite the doctrine + Kocienda's anti-"imaginary-puppy" rule in its Do-Not-Use/Anti-Pattern
  section). Pair it with the demo-discipline ref so a case study is built on a *real demo/outcome*, not a
  narrated mock. **Don't** build a generic "storytelling" skill divorced from the deck/case-study use — that
  invites narrative-as-decoration.
- **Harden the critique skills** with **Kill Your Darlings** as the writing-side twin of "edit for less."

---

## Book 4 — *UX Storytellers: Connecting the Dots* (ed. Jursa, Köver, Grünewald, 2010)

A ~50-essay community anthology of UX/IA practitioners' personal career stories. Per the brief this was
skimmed for **recurring themes**, not deep-read. It is overwhelmingly **memoir and inspiration**, with one
load-bearing thesis and very little transferable mechanics.

### (a) Load-bearing transferable ideas (the recurring themes)

- **"The story is the thing" (Andrew Hinton — the anthology's clearest essay and its de facto thesis).**
  *Stories are the foundation; data/information is the artificial abstraction we lay over them.* Design is
  "weaving a new story into an existing fabric so it makes it stronger." A product is **a bit player in the
  user's own drama** — they are the protagonist; what we make must fit the contours of *their* story. Method
  residue: **listen, watch, absorb the whole story before designing** ("if I just watch, listen and absorb,
  my design heads generally in the right direction"); a survey gives decontextualised pie-charts, a *story*
  carries the context that makes the data mean anything.
- **Recurring theme — empathy via real observation over abstraction.** Across essays (Hinton's medical-office
  newbies, the breast-cancer forum, Chris Khalil's "probing your audience"): the unit of insight is the
  *person's narrative*, not the metric. Reinforces our research/UX group's contextual-inquiry stance.
- **Recurring theme — top-tasks over the long tail (Rønjum, "Cutting Through the Opinions").** Gerry
  McGovern's "long neck": a handful of top tasks are 90% of demand; "content is expensive… like fresh food";
  websites drown real tasks in "a cacophony of countless voices." A **prioritisation/decisiveness** argument
  — strip to what users actually came for. (Echoes Kocienda's "edit for less" from the content/IA side.)
- **Recurring theme — the practitioner's career *is* a story** (Jursa's biology-to-IA arc, Beatson's "long
  way round," Kalbach): the book performs its own thesis — most chapters are personal narrative arcs. This is
  *charming and motivational* but is the memoir, not the method.

### (b) Critical take — almost all anecdote, one transferable thesis

- **This is the least extractable of the four — and that's fine, it was meant to be skimmed.** ~90% is
  inspiration/memoir with no reusable mechanic. Its one durable contribution is **Hinton's thesis**, which is
  a *philosophical grounding* for why narrative belongs in UX/IA at all — and which dovetails exactly with
  Sandler's Data-Storytelling and Contrast entries and with our existing UX-research empathy posture.
- **Dated surface, durable core.** The 2010 detail (Flash, "the long tail" debates, FTP'ing into a server)
  is period colour. The empathy-via-story core is timeless and already largely lives in our group-05 UX
  process/research skills.
- **No Mission contact, and a mild risk.** Like Sandler, it could be misread as "tell a nice story" rather
  than "make an authored thing." Same fence applies. It adds **no** net-new capability beyond confirming the
  storytelling-belongs-in-design premise that justifies the (fenced) Sandler-based skill.
- **Mission fit: neutral.** Confirmatory of the empathy/research posture; irrelevant to anti-slop craft.

### (c) Engine impact

- **Harden, lightly, `05…/journey-mapping-and-service-design` (P1) and the UX-research skills** with Hinton's
  thesis as a *grounding quote*: the user is the protagonist; our product is a bit-player that must fit their
  existing story; listen to the whole narrative, not just the metric. Useful as a one-line framing in
  persona/JTBD/journey work — **not** a structural change.
- **Feed the (fenced) `design-storytelling-and-case-studies` skill** Hinton's thesis as its *why-this-matters*
  framing and the **top-tasks/long-neck** prioritisation as a content-cutting rule.
- **NEW-SKILL verdict: DON'T-BUILD anything from this book alone.** It justifies no skill on its own; it
  supplies grounding quotes to skills justified by Kocienda and Sandler.

---

## Phase-2 P1 plan — CONFIRM / CHANGE / REDUNDANT calls

Against `docs/plans/hardening-june/phase-2-p1-wave/01-skill-specs.md`:

| Plan item (group) | Call | Rationale from these four books |
|---|---|---|
| **`logo-and-wordmark-design`** (02) | **CONFIRM — strengthened** | Janoff is the ideal primary source: scale-relater, "interactive wit," silhouette iteration, USP-encoding, mono/favicon survival, stand-alone-icon threshold. The plan item is correct; feed it the Janoff material. |
| **`design-critique-and-review-facilitation`** (00) | **CONFIRM — strengthened** | Kocienda supplies the missing protocol spine: **single decider + decision capture + no critique without a concrete artifact**, plus the algorithm-vs-heuristic critique axis and "edit for less." Sandler's "Kill Your Darlings" is a complementary cut-rule. |
| **`heuristic-evaluation-and-design-critique`** (05) | **CONFIRM** | The **algorithm vs. heuristic** lens (objective arrow vs. taste-and-time) is a clean addition to the critique rubric; "live on it" is a longitudinal-review caveat worth stating. |
| **`composition-and-visual-hierarchy`** (03) | **CONFIRM** | "Edit for less" / Miller 7±2 load-shedding and the "answer hard questions by removing them" move reinforce the focal-point + whitespace-as-structure spec. |
| **`journey-mapping-and-service-design`** (05) | **CONFIRM — lightly** | Hinton's "user is the protagonist; product is a bit-player" + Sandler's Contrast (before/after) and JTBD/persona framing give the narrative grounding for journey/experience maps. |
| All other P1 items (typography, layout-editorial, onboarding, trust, component-states, fintech, ecommerce, mobile, motion, figma, voice-tone, illustration, ai-image, chart, xlsx, inclusive, ethics, email) | **REDUNDANT to these books** | None of the four touch these domains; they neither confirm nor change them. No action. |
| **Net-new not in the plan: doctrine ref `creative-selection-and-taste.md`** | **ADD (do first — highest leverage)** | Kocienda's demo-loop + algorithm/heuristic + "41 blues" gives the Mission a *production method*, not just an assertion. Cheapest, highest-value change the four books justify. |
| **Net-new not in the plan: `demo-driven-design-process` / "creative-selection"** (05) | **BUILD (P2)** | The process skill operationalising the doctrine ref. Not redundant with critique skills. Build after the ref. |
| **Net-new not in the plan: `design-storytelling-and-case-studies`** (13) | **BUILD (P2) — fenced** | Fills the real deck/case-study narrative gap (Sandler frameworks + Hinton thesis). Must be fenced: *structure serves the authored artifact; story never replaces the demo.* |

---

## Extract-into table (source → extract → engine target → form)

| Extract | Source | Engine target | Form |
|---|---|---|---|
| **Creative selection** (demo → feedback → next-demo loop) as the named production method behind the Mission | Kocienda | **NEW** `doctrine/references/creative-selection-and-taste.md` → then `05…/demo-driven-design-process` | doctrine ref + new skill |
| **"41 shades of blue"** — a taste decision outsourced to a metric is the asymmetry-rule error on the *process* side | Kocienda | `doctrine/references/creative-selection-and-taste.md`; cited in `distinctive-by-design`, `brand-visual-identity`, `color-system-and-palette` | doctrine ref + harden |
| **Algorithm vs. heuristic** decision lens (objective arrow vs. taste-and-time) | Kocienda | doctrine ref; `00…/design-critique-and-review-facilitation`, `05…/heuristic-evaluation-and-design-critique` | ref + critique axis |
| **Demo fidelity ring / Hollywood-backlot / goals + non-goals** (what to make real, what to fake) | Kocienda | NEW `05…/demo-driven-design-process` → `references/demo-fidelity-and-nongoals.md` | new skill ref |
| **"Live on it"** (longitudinal refinement) + **single decider + decision capture** + **demo-grounded critique** | Kocienda | `00…/design-critique-and-review-facilitation`, `05…/heuristic-evaluation-and-design-critique` | harden (P1) |
| **Edit for less / answer hard questions by removing them** (Miller 7±2) | Kocienda | `distinctive-by-design`; `03…/composition-and-visual-hierarchy` (P1) | harden |
| Insert a **demo/iteration loop** between "state the ONE decision" and "build" | Kocienda | `04…/distinctive-by-design` (workflow) | harden |
| **"Interactive wit / a small surprise"** as a generative identity move (FedEx arrow, I♥NY) | Janoff | `02…/brand-visual-identity`; `02…/logo-and-wordmark-design` (P1) | harden + new-skill input |
| **Mark encodes the product's USP/differentiator** (stripes = colour-on-TV) | Janoff | `02…/brand-visual-identity` (strategy step) | harden |
| Silhouette iteration; scale-relater; mono/favicon survival; stand-alone-icon threshold; "When in doubt, leave it out"; memory test (Janoff as named authority beside Rand) | Janoff | `02…/logo-and-wordmark-design` (P1); `brand-visual-identity` Consistency Gate | new-skill input + harden |
| "Idea before execution; tech is an idea-killer" | Janoff | `distinctive-by-design` (reinforce don't-reach-for-default rule) | harden (one line) |
| **Narrative-frameworks reference** — Freytag, Three-Act, Pixar, Kishōtenketsu (no-villain), Hero's Journey, Vonnegut shapes | Sandler | `13…/presentations-and-documents` (deck-system) → `references/narrative-frameworks.md` | harden ref |
| **Contrast, Beginning-to-End** (before/after delta = the case-study spine); **Peak-End** (design the close); **Rule of Three**; **Data Storytelling** (numbers → stakes) | Sandler | NEW `13…/design-storytelling-and-case-studies` (fenced) | new skill |
| **Conflict / Wicked Problem** vocabulary for framing design stakes in a pitch | Sandler | `13…/design-storytelling-and-case-studies` | new skill |
| **Kill Your Darlings** (writing-side "edit for less") | Sandler | `00…/design-critique-and-review-facilitation`; `13…` storytelling skill | harden |
| **"The story is the thing"** (user is protagonist; product is bit-player; listen to the whole story over the metric) | *UX Storytellers* (Hinton) | `05…/journey-mapping-and-service-design` (P1) grounding; `13…/design-storytelling-and-case-studies` why-it-matters | grounding quote |
| **Top-tasks / long-neck** prioritisation (strip to what users came for) | *UX Storytellers* (Rønjum) | `13…/design-storytelling-and-case-studies` (content-cutting rule); `05…` IA work | grounding/rule |
| **Standing fence:** narrative structure serves the authored artifact; a story never replaces a real demo/outcome | Kocienda (guard) + doctrine | `13…/design-storytelling-and-case-studies` (Do-Not-Use / Anti-Patterns) | fence clause |
