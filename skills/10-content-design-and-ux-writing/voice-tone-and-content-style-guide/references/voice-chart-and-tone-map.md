# Voice Chart & Tone Map — the method

The canonical method for this skill: how to build a ratified **Voice Chart**, a three-traps-clean
**Voice Guide**, and a magnitude-and-lifecycle **Tone Map**, plus terminology governance and the
casual≠conversational ruling. Sources: Podmajersky, *Strategic Writing for UX* 2nd ed. (Voice
Chart, voice-vs-tone); Ben-David, *The Fundamentals of UX Writing* (Voice Guide three traps, Tone
Maps, casual≠conversational). See `docs/book-study/03-ux-writing.md`.

> **Boundary (read first).** This skill defines **what the product's words should be and whether
> they are on-voice.** It does **not** detect whether a passage reads as generic machine-written
> prose (the em-dash tell, "delve"-class diction, hedged transitions, list-of-three padding) —
> that **textual AI-slop detection is the digital-research engine's writing-slop skills**, not
> here. Cross-reference; never duplicate. We own *defining* the voice; the research engine owns
> *detecting generic machine prose*.

---

## 1. Voice vs. Tone — the durable distinction

- **Voice** = the *consistent, recognizable* set of word-choice characteristics across the **whole**
  experience. It is what makes the product sound legitimate, trustworthy, and unmistakably itself.
  Voice does **not** change screen to screen.
- **Tone** = the *variability* of that voice from one moment to the next — the same voice flexes
  between a celebration, an error, and a routine notification.

The metaphor: overhearing someone on the phone. The **tone** tells you the relationship (talking to
a boss vs. a child vs. a friend), but you are never confused about **whose voice** it is. Voice is
the person; tone is their mood in the moment. **Define the voice once; map the tone many times.**

---

## 2. The Voice Chart (Podmajersky) — the signature artifact

A matrix that converts an intangible brand into per-principle, per-aspect, **ratified** rules.

### Structure

- **Columns = the product's principles.** Use the experience's 2–4 product principles (three is
  common — *not* magical). These are the columns. Voice is *how the product expresses its
  principles in words*, so the principles must come first.
- **Rows = the six aspects of voice:**

  | Aspect | The decision it records |
  |---|---|
  | **Concepts** | Which ideas, metaphors, and framings we reach for (and which we refuse). |
  | **Vocabulary** | The words we use and the words we avoid; the lexicon's flavour. |
  | **Verbosity** | How much we say — terse, or expansive and explaining. |
  | **Grammar** | Sentence shape, person (we/you/I), mood (imperative vs. descriptive), tense. |
  | **Punctuation** | What we use and ban — exclamation marks, em-dashes, ellipses, semicolons. |
  | **Capitalization** | Sentence case vs. Title Case vs. lowercase, and where each applies. |

- **Cells** hold *specific, applicable rules*, never adjectives. "Vocabulary: warm but never cute;
  prefer plain Anglo-Saxon verbs; ban 'leverage', 'utilize', 'seamless'" is a rule. "Friendly" is
  not.

### The four roles of the chart

1. **Train** new content designers — onboard them to the voice fast.
2. **Inform/check LLM** drafting and prompting — the chart is the spec an LLM is held to.
3. **Design new text** — a drafting aid when writing fresh copy.
4. **Break ties** — settle "which wording is more on-voice" by pointing to a cell.

### Tensions are a feature

Deliberate **tension between cells** (e.g. a "concise" principle pulling against a "reassuring" one)
is *intended* — under pressure it generates **divergent drafting options** rather than one flat
answer. Don't sand the tensions out; they are where authored voice lives.

### Ratification & the tiebreaker (the non-negotiable)

A chart can only **break ties** if it carries **stated authority**. In the chart header, record:

- **Who ratified it** (the named owner/committee), and
- **The decision mode**: **consensus** (the team agreed), **autonomous** ("we flipped a coin and
  committed" — a legitimate, fast tie-break), or **hierarchical/autocratic** (a named authority
  decided). The chart **inherits the authority of whoever ratified it.**

Without a ratified tiebreaker the chart is a poster, not a standard. With one, a voice dispute ends
at a cell.

### Worked cell shape

```
Principle: "Calm under money pressure"
  Concepts        → frame money events as facts the user controls, never alarms
  Vocabulary      → "due", "sent", "declined" (plain); never "URGENT", "failed!", "oops"
  Verbosity       → one sentence + one next step; no reassurance padding
  Grammar         → second person, active, imperative for the next step ("Add a card")
  Punctuation     → periods only; no exclamation marks; em-dash allowed for the aside
  Capitalization  → sentence case everywhere
```

---

## 3. The Voice Guide (Ben-David) — "We are / We are not / Examples"

A leaner, classroom-ready complement to the chart. For each voice dimension, three columns:

| We are | We are not | Examples |
|---|---|---|
| The trait we aim for | The adjacent trait we must avoid | Real strings showing it |

### The "We are not" three traps (the hard part)

A "We are not" line is only useful if it names a **legitimate adjacent trait a writer might land on
by accident while aiming at ours.** Avoid all three traps:

1. **Opposites / antonyms** — "We are clear / we are not confusing." Says nothing; nobody aims at
   confusing.
2. **Things no product wants** — "we are not rude / sloppy / boring." Strawmen; no one targets these.
3. **Irrelevancies** — traits no one would ever mistake the product for ("we are not a circus").

**Valid pattern:** aim "Approachable" → the accidental miss is "Best buds" (too familiar). Aim
"Confident" → the accidental miss is "Arrogant". Aim "Efficient" → the miss is "Curt". The "We are
not" marks the **cliff edge next to the trait**, the place a well-meaning writer actually falls.

---

## 4. The Tone Map (Ben-David) — one voice, variable tone

Tone is plotted as a **spectrum with direction AND magnitude** — not a binary, not a flat matrix.
The same voice dials **up or down**; the map tells a writer *how far* at each touchpoint.

### Two axes of mapping

**(a) Across a single flow** — tone moves within one journey:

```
Checkout flow (voice constant: plain, calm, in-control)
  Browse cart      →  neutral, low magnitude
  Enter payment    →  reassuring, +1 (security, trust)
  Payment declined →  calm-precise, steady (NOT alarmed) — the voice tested hardest
  Success          →  warm, +1, then get out of the way
```

**(b) Across the user lifecycle** — tone shifts as the relationship matures:

| Lifecycle stage | Tone direction | Magnitude | Why |
|---|---|---|---|
| **Onboarding** | warm, guiding | high | the user is new; teach and reassure |
| **Habitual use** | quiet, terse | low | don't narrate what the user already knows |
| **Error / billing** | calm, precise | steady | the voice under stress; no humour, no alarm |
| **Churn / cancel** | respectful | low | don't guilt; make leaving clean |
| **Resurrection** | welcoming | medium | acknowledge the return without grovelling |

### Code-switching

Name the **code-switch points** — where tone deliberately shifts and why (e.g. "from terse-habitual
to high-warmth at resurrection"). Code-switching is the voice *consciously* changing register for the
moment; it is principled, recorded, and bounded — never random drift.

---

## 5. Casual ≠ Conversational (the ruling)

A recurring stakeholder fight ("make it friendlier" → "make it casual"). Settle it explicitly:

- **Conversational** = write how a competent human *talks* — turn-taking, positive contractions
  ("you're", "we'll"), plain words. This is **always right** and non-negotiable for product copy.
  ("Conversational" means respecting the norms of a word-based interaction — *not* a casual register.)
- **Casual** = informal/buddy register: slang, jokes, exclamation, ultra-familiarity. Right for
  **some** brands only, and only as a **stated** choice tied to a product principle — never a default
  drift.

Record which one this product is. A bank can be conversational without ever being casual. Conflating
the two is how a serious product accidentally turns chummy.

> **Contraction note (carried into microcopy):** prefer **positive** contractions; be wary of
> **negative** ones in high-stakes copy — users scanning miss the "n't" and read the opposite. Use
> "do not" over "don't" where the negation is load-bearing; "don't" is fine in low-stakes copy.

---

## 6. Terminology governance & the glossary

A voice with a drifting lexicon isn't a voice. Govern the words.

- **One term per concept.** For each concept, the **one** approved term — and list the **rejected
  alternates** so drift is visible at a glance ("project" ✓ / ~~workspace~~ / ~~board~~).
- **Preferred / banned lexicon.** The house words and the forbidden ones (jargon, marketing fluff,
  the AI-tell words the brand refuses).
- **Inclusive-language bans** (shared with the error skill): never call a person's input
  **"invalid"** (blaming *and* ableist) or **"illegal"** — state what's expected instead; default to
  singular **"they"**; keep internal nouns (`null`, `token`, `exception`, raw codes) out of
  user-facing prose.
- **Governance rule.** State *who approves a new term*, *how a term is retired*, and that the
  glossary is the **single source of truth** writers and engineering pull from. Without an owner, the
  glossary rots back into synonyms within a release.

---

## 7. HAHAS — durable tenets for LLM/dynamic content (note)

When the voice governs **dynamic or LLM-generated** content, hold it to **HAHAS**: **H**elpfulness,
**A**ccuracy, **H**armlessness, **A**uditability, **S**ustainability (content length is compute /
carbon cost — terseness is also an ethic). The tenets are durable; the specific GenAI tooling/metric
names in the source books are **time-sensitive** — cite the principle, not the tool.

---

## 8. Build checklist

- [ ] Product principles fixed as the **columns** (2–4).
- [ ] All **six voice rows** filled with applicable rules (not adjectives) per column.
- [ ] Deliberate **tensions** left in (they generate options).
- [ ] **Ratification header** present: who ratified + decision mode (consensus / autonomous / hierarchical).
- [ ] **Voice Guide** written; every "We are not" passes the **three-traps** test.
- [ ] **Tone Map** drawn across a **flow** *and* the **lifecycle**, with **magnitude** and named
      **code-switch** points.
- [ ] **Casual ≠ conversational** ruling stated and principle-tied.
- [ ] **Glossary + governance rule** (one term/concept, banned/preferred, inclusive bans, owner).
- [ ] Pressure-tested on **real strings**; every rule survived contact.
- [ ] Seam wired: downstream microcopy + error skills point here for the voice.
