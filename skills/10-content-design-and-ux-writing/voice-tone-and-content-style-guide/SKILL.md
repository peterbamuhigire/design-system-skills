---
name: voice-tone-and-content-style-guide
description: Use when defining or governing a product's content voice and tone — building the operational voice/tone system that the microcopy and error skills consume. Produces the Voice Chart (Podmajersky's six voice rows × product-principle columns, with a ratified tiebreaker), the Voice Guide ("We are / We are not + 3 traps / Examples", Ben-David), the Tone Map (tone by magnitude across flow and user lifecycle), a terminology glossary with governance rules, and the casual≠conversational ruling. Triggers on "define the product voice", "voice and tone guide", "voice chart", "tone map", "content style guide", "what's our voice", "tone of voice spectrum", "terminology / lexicon governance", "voice tiebreaker", "is this on-voice". This is the upstream content-voice system; pairs with brand-style-guide (visual+verbal brand identity) and is consumed by ux-writing-and-microcopy and error-empty-and-system-messaging.
status: active
metadata:
  portable: true
  category: 10-content-design-and-ux-writing
  compatible_with:
    - claude-code
    - codex
---

# Voice, Tone & Content Style Guide (the operational content-voice system)

A product's **voice** is the consistent, recognizable set of word-choice characteristics across
the whole experience — what makes the copy legitimate, trustworthy, and unmistakably *this*
product. Its **tone** is the variability of that voice from moment to moment: the same voice
sounds different in a celebration than in a billing failure. This skill is where the voice is
*defined and ratified* and where tone is *mapped* — the upstream content system the microcopy
and error skills already cite as the missing dependency. It turns an intangible "brand
personality" into per-principle, per-aspect, **ratified** decision rules.

This is a doctrine concern, not decoration. Per
[`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md) §0–2, the moat is output
that looks **authored** — and a ratified voice is exactly the "looks authored" mission applied to
words: it gives every string a stated standard to be measured against, so the copy reads as the
work of skilled human hands rather than the convergent machine mean. A product with no defined
voice converges, by default, on slop.

<!-- dual-compat-start -->
## Use When
- **Defining a product's content voice from scratch** — the personality, the lexicon, the
  word-choice characteristics that must hold across every screen.
- Building the **Voice Chart**: the six voice aspects (Concepts, Vocabulary, Verbosity, Grammar,
  Punctuation, Capitalization) crossed with the product's principles, **with a ratified
  tiebreaker** so the chart can settle disputes.
- Writing the **Voice Guide** in the "We are / We are not / Examples" form — and getting the
  **"We are not"** right (avoiding the three traps).
- Building a **Tone Map**: how the one voice flexes by *magnitude* (subtle → strong) across a
  single flow and across the **user lifecycle** (onboarding → habitual use → churn → resurrection).
- Settling the recurring stakeholder fight with the **casual ≠ conversational** ruling.
- Establishing **terminology governance**: one term per concept, the glossary, the banned/preferred
  lexicon, and who owns changes.
- Auditing whether existing copy is **on-voice**, or training/checking an LLM that drafts copy
  against the ratified voice.

## Do Not Use When
- You need to **detect generic, machine-written prose** — the em-dash tell, "delve"-class diction,
  hedged transitions, list-of-three padding, "is this passage AI-generated?" That **textual
  AI-slop detection lives in the digital-research engine's writing-slop skills, NOT here.** The
  boundary is clean: **this skill decides what the product's words *should* be and whether they
  are on-voice; the research engine decides whether a passage *reads as machine-generated slop*.**
  Cross-reference; never duplicate. (Doctrine note, `docs/book-study/03-ux-writing.md`.)
- You are writing the **actual interface strings** — button/CTA labels, field labels, tooltips,
  confirmation copy → `10-…/ux-writing-and-microcopy` (it *consumes* the voice this skill defines).
- You are writing **error / empty / system messages** → `10-…/error-empty-and-system-messaging`
  (it *applies* this voice to the hardest moments).
- You are producing the **visual + verbal brand identity deliverable** for a client (logo rules,
  palette card, typography specimen, plus a voice section) →
  `02-color-brand-and-visual-identity/brand-style-guide`. That is the brand-level artifact; **this**
  is the operational content voice/tone *system* for interface copy. They reference each other and
  must not duplicate: brand-style-guide owns the brand-identity framing; this skill owns the Voice
  Chart, Tone Map, and lexicon governance the writers operate from day to day.
- You are designing the **visual** empty/error/loading states → `04-…/empty-error-and-loading-states`.

## Required Inputs
- The **product principles** (2–4) the experience is designed around — these become the **columns**
  of the Voice Chart. If none are documented, derive a provisional set with the team before
  building the chart; the chart is meaningless without them.
- The **brand personality / strategy** input (from `02-…/brand-style-guide` or brand-strategy):
  the adjectives, the audience, the positioning the voice must express.
- **Sample real strings** from the product (or close competitors) to test the voice against — a
  voice that can't be applied to actual copy is theatre.
- The **ratification authority**: who gets to settle a voice dispute, and by which mode (consensus
  / autonomous coin-flip / hierarchical-autocratic). The chart inherits the authority of whoever
  ratified it; without that, it cannot break ties.
- The **user lifecycle stages** and key flows the Tone Map must cover (onboarding, core use,
  failure/billing, churn, resurrection).

## Workflow
1. **Fix the columns: state the product principles first.** The Voice Chart is principles ×
   voice-aspects; the principles are the columns. Take the experience's 2–4 product principles
   (three is common, not magical) and write them across the top. Don't invent voice in a vacuum —
   voice is *how the product expresses its principles in words*. See
   `references/voice-chart-and-tone-map.md` §Voice Chart.

2. **Fill the six voice rows against each column.** For every principle, decide the rule on each of
   the **six aspects of voice**: **Concepts** (which ideas/metaphors we reach for), **Vocabulary**
   (the words we use and avoid), **Verbosity** (how much we say), **Grammar** (sentence shape,
   person, mood), **Punctuation** (what we use and ban — e.g. exclamation marks, em-dashes),
   **Capitalization** (sentence case vs title case vs lowercase). Write *specific, applicable*
   cells, not adjectives. Deliberate **tensions** between cells are a feature — they generate
   divergent drafting options under pressure. See `references/voice-chart-and-tone-map.md`.

3. **Ratify the chart and record the tiebreaker.** A Voice Chart's fourth and most important job is
   to **break ties** — but it can only do that with stated authority. Record, in the chart header:
   *who ratified it* and *the decision mode* (consensus / autonomous / hierarchical). Without a
   ratified tiebreaker the chart is a suggestion, not a standard; with one it ends the "which
   wording is more on-voice" argument by pointing to a cell. The chart then serves its four roles:
   (1) train new content designers, (2) inform/check LLM drafting, (3) design new text, (4) break
   ties.

4. **Write the Voice Guide: "We are / We are not / Examples".** Complement the chart with the
   leaner, classroom-ready Voice Guide (Ben-David). For each voice dimension: **We are** (the
   trait), **We are not** (the boundary), **Examples** (real strings). The hard part is **"We are
   not"** — it must **avoid the three traps**: (1) **opposites/antonyms** ("We are clear / we are
   not confusing" says nothing), (2) **things no product wants** ("we are not rude/sloppy" — nobody
   aims there), (3) **irrelevancies** (traits no one would mistake us for). A valid "We are not" is
   *a trait another product would legitimately want, that a writer might land on by accident while
   aiming at ours* — e.g. aiming "Approachable", accidentally landing "Best buds". See
   `references/voice-chart-and-tone-map.md` §Voice Guide & the three traps.

5. **Build the Tone Map: one voice, variable tone, by magnitude and lifecycle.** Voice is constant;
   tone flexes. Plot tone as a **spectrum with direction *and* magnitude** (not a binary), then map
   it two ways: (a) across a **single flow** (e.g. checkout: neutral → reassuring at payment →
   calm-precise on decline), and (b) across the **user lifecycle** (onboarding warm-and-guiding →
   habitual use quiet-and-terse → churn respectful → resurrection welcoming). Name the **code-switch
   points** where tone shifts and why. The map's job: a writer at any touchpoint knows *how far* to
   dial the voice. See `references/voice-chart-and-tone-map.md` §Tone Map.

6. **Issue the casual ≠ conversational ruling.** Settle it explicitly in the guide: **conversational**
   (write how a competent human talks; turn-taking; positive contractions) is **always right and
   non-negotiable**; **casual** (informal/buddy register, slang, jokes) is right for *some* brands
   only and must be a *stated* choice tied to a principle, never a default drift. Record which one
   this product is. (This prevents the perennial "make it friendlier" → "make it casual" slide.)

7. **Govern the terminology: one term per concept, with an owner.** Build the **glossary**: for each
   concept, the **one** approved term (and the rejected alternates, so drift is visible), plus a
   **preferred/banned lexicon** (including the **inclusive-language bans** the error skill enforces:
   never "invalid"/"illegal" of a person's input, default to singular **"they"**, no internal
   jargon — `null`, `token`, `exception` — in user-facing prose). State the **governance rule**: who
   approves a new term, how a term is retired, and that the glossary is the single source of truth
   engineering and writers pull from. Terminology drift ("project" here, "workspace" there) is a top
   clarity killer; the glossary is the fix.

8. **Pressure-test and ratify the system on real strings.** Take a handful of the product's actual
   strings and run them through the chart, guide, tone map, and glossary. If a rule can't be applied
   to a real string, it's an adjective, not a rule — rewrite it. Then ratify (step 3's authority)
   and version the guide. Note the **HAHAS** tenets for any LLM/dynamic content the voice will govern
   — Helpfulness, Accuracy, Harmlessness, Auditability, **Sustainability** (content length is compute/
   carbon cost); treat the specific GenAI tooling claims as time-sensitive, the tenets as durable.

9. **Hand off and wire the seam.** Deliver the guide as the upstream source the two downstream skills
   consume. Update their "voice source" pointer to *this* skill (they currently route to
   `02-…/brand-style-guide`). Keep the brand-style-guide ↔ this-skill reference mutual, not
   duplicated: brand identity there, operational content voice/tone here.

## Anti-Patterns
- **A voice "guide" that is just adjectives** — "friendly, clear, human" with no per-aspect rule a
  writer can apply. The Voice Chart exists precisely to make voice *operational*, cell by cell.
- **A chart with no ratified tiebreaker** — then it can't do its most valuable job (settling
  disputes); it's a poster, not a standard. Always record who ratified it and how.
- **"We are not" antonyms / strawmen / irrelevancies** — "we are not confusing / rude / a tractor".
  The three traps. A real "We are not" names a *legitimate adjacent trait* a writer might hit by accident.
- **A flat tone "matrix" with no magnitude** — tone is direction *and* how far; "formal vs casual"
  cells miss that the same voice dials up and down. Map magnitude across flow and lifecycle.
- **Confusing casual with conversational** — sliding "be friendlier" into slang and jokes by
  default. Conversational is always right; casual is an explicit, principle-tied choice.
- **No terminology owner** — a glossary nobody governs drifts back to synonyms within a release.
- **Defining voice with no product principles** — the chart's columns are the principles; without
  them you're decorating, not deciding.
- **Absorbing AI-prose detection** — trying to make this skill judge whether text "reads as
  AI-written". That is the research engine's job; this skill judges on-voice, not machine-origin.
- **A voice that can't be applied to a real string** — theatre. Every rule must survive contact
  with an actual button, label, or error.

## Outputs
- A ratified **Voice Chart** — six voice rows (Concepts, Vocabulary, Verbosity, Grammar,
  Punctuation, Capitalization) × the product-principle columns, with a header recording the
  **ratification authority and tiebreaker mode**.
- A **Voice Guide** in "We are / We are not (three-traps-clean) / Examples" form.
- A **Tone Map** — tone by magnitude across a key flow and across the user lifecycle, with named
  code-switch points.
- The **casual ≠ conversational ruling** for this product (stated, principle-tied).
- A **terminology glossary + governance rule** — one term per concept, preferred/banned lexicon,
  inclusive-language bans, and the owner/approval process.
- A short **voice statement** the downstream skills write against, and the updated seam pointer.

## Examples
- `examples/worked-voice-and-tone-guide.md` — a complete worked content style guide for a sample
  product (Ledgerly, a small-business invoicing app): a filled Voice Chart (six rows × three
  ratified principles, with the tiebreaker recorded), a Voice Guide with three-traps-clean "We are
  not" lines, a Tone Map across the checkout flow *and* the user lifecycle, the casual≠conversational
  ruling, and a terminology glossary with governance. No placeholders — the calibration target.

## References
- [`doctrine/design-doctrine.md`](../../../doctrine/design-doctrine.md) — §0–2: a ratified voice is
  the "looks authored" mission applied to words; state the standard before producing; no convergent
  default copy. The voice exists so every string has an authored standard to meet.
- `references/voice-chart-and-tone-map.md` — the core method: the **Voice Chart** (six aspects ×
  principles + the four roles + the ratified tiebreaker, Podmajersky), the **Voice Guide** with the
  **"We are not" three traps** (Ben-David), the **voice-vs-tone** distinction, the **Tone Map**
  (magnitude × flow × lifecycle, code-switching, Ben-David), **casual ≠ conversational**, and the
  terminology-governance pattern. Includes the boundary note (textual AI-slop → research engine).
- `10-content-design-and-ux-writing/ux-writing-and-microcopy` — the downstream skill that consumes
  this voice for interface strings; update its voice-source pointer here.
- `10-content-design-and-ux-writing/error-empty-and-system-messaging` — applies this voice to
  error/empty/system copy (where a voice is tested hardest); shares the inclusive-language bans.
- `02-color-brand-and-visual-identity/brand-style-guide` — the brand-level visual+verbal identity
  deliverable; references this skill for the operational content voice/tone system, not duplicating it.
- Provenance (named, not in-repo): Podmajersky, *Strategic Writing for UX* 2nd ed. (Voice Chart,
  voice-vs-tone); Ben-David, *The Fundamentals of UX Writing* (Voice Guide three traps, Tone Maps,
  casual≠conversational). Distilled in `docs/book-study/03-ux-writing.md`.
<!-- dual-compat-end -->
