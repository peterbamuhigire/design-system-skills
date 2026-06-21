# 03 — Book Study: UX Writing & Content Design (Group 10, our thinnest group)

**Engine:** `C:\wamp64\www\design-system-skills`
**Group under study:** `10-content-design-and-ux-writing` — currently **2 skills**
(`ux-writing-and-microcopy`, `error-empty-and-system-messaging`), the engine's thinnest group.
**Date:** 2026-06-21
**Doctrine note (boundary):** This engine owns **interface/product copy as a design surface**
(microcopy, voice/tone, errors, empties, content structure). The **TEXTUAL anti-slop** doctrine —
detecting and removing generic AI prose, em-dash tells, hedging, "delve"-class diction — lives in the
**digital-research engine's writing-slop skills**, NOT here. Where these books touch generic-AI-prose
detection (Podmajersky's "voice as a tiebreaker against the convergent mean"; Ben-David's GenAI bias
chapter), we treat it as *evidence the boundary matters* and cross-reference, never absorb.

Books examined (all in `C:\Users\Peter\Downloads\uiux_markdown\`):
1. **Strategic Writing for UX, 2nd ed.** — Torrey Podmajersky (O'Reilly, 2025) — *the field-defining text.*
2. **The Fundamentals of UX Writing** — Yael Ben-David (Apress Pocket Guide, 2026) — *the teachable on-ramp.*
3. **Robotics for Writers** — August Niehaus (2023) — **MISFILED; not a UX book** (judged below).

---

## BOOK 1 — Podmajersky, *Strategic Writing for UX*, 2nd ed.

### (a) Load-bearing frameworks

**Dual-goal strategic spine.** Every string must serve **the organization's goals AND the person's
goals at once**. Operationalized as the **virtuous cycle**: the org *attracts → converts → onboards →
engages → supports → transforms*; the person, in parallel, *investigates → verifies → commits → sets up
→ uses → fixes → prefers → champions*. Content types map to stages (marketing → setup → core UX text →
error/support → intrinsic value). This is the strategic scaffolding the whole book hangs on.

**Voice vs. Tone — the central, durable distinction.**
- **Voice** = the *consistent, recognizable* set of word-choice characteristics across the whole
  experience (what makes a brand recognizable, legitimate, trustworthy).
- **Tone** = the *variability* of that voice from one moment to another (error vs. celebration vs.
  notification). Her metaphor: overhearing her mother on the phone — tone signals the relationship, but
  you are never confused about *whose voice* it is.

**The Voice Chart — her signature artifact** (the single most-copied idea in the discipline). A matrix:
- **Columns = the experience's Product Principles** (she uses 3 per example; says 3 isn't magic).
- **Rows = the six aspects of voice**: **Concepts, Vocabulary, Verbosity, Grammar, Punctuation,
  Capitalization**.
- **Four roles**: (1) train new content designers, (2) inform/check LLM training & prompting,
  (3) design new text, (4) **break ties** — the chart inherits the authority of whoever ratified it
  (consensus / autonomous coin-flip / hierarchical-autocratic). Deliberate internal **tensions** in the
  chart are a *feature* — they generate divergent drafting options.

**Conversational = turn-taking, NOT folksiness.** A deep reframe: "conversational" means the text is
recognizable as a *word-based interaction respecting the norms of turn-taking* — not a casual register.
This grounds **content-first design**: lead with words before screens via a **role-play / improv
exercise** (intention → desired-result arrow; person's goals vs. org's goals; one person plays the
experience as a "thoughtful host," one plays the user). Then translate to **side-by-side text-message
bubbles** → the experience's lines become *titles/labels/descriptions*; the person's lines become
*buttons/options* → only then wireframe.

**The 11 UX Text Patterns** — a stable pattern *language*, each documented as **Purpose / Patterns
(`{curly}` = replaceable, `[square]` = omittable) / Tips**: Titles, Buttons & Menus, Descriptions,
Empty States, Labels, Controls, Text Input Fields, Transitional Text, Confirmation Messages,
Notifications, Errors. (Errors split three ways by interruption: **Inline / Detour / Blocking**.)

**The four-phase editing model** — "UX writing is **90% editing**." Sequential goals with a deliberate
**word-count curve** (balloons, then contracts): **Purposeful → Concise → Conversational → Clear**.
Concise target: ~**40 chars wide × 3 lines** for English, use only **½–⅔** of the space if localizing.
Rule: **always edit inside the design**, and **always propose up to three ranked options** with rationale.

**Measurement (the content "goals" framework).** Three method families: **direct behavior measurement**
(A/B), **UX research** (why), **heuristic analysis** (when no data). Six direct metrics: onboarding pace,
engagement, retention, completion, referrals, cost reduction — with explicit **ethical candor** (Goodhart's
law; engagement-maximization → addiction; "how much is too much?"). The **UX Content Scorecard** scores
**Usability (~⅔: Accessible, Purposeful, Concise, Conversational, Clear) + Voice (~⅓, mirroring the six
voice rows)** against **Nielsen heuristics + WCAG 2.2** success criteria.

**LLM content design (new Ch.5).** The content designer shifts "from static content to **designing
probabilistic systems of dynamic content**." Process: define the problem → **define "good"** (expert-audit
hundreds of items, extract attributes of good/acceptable/unacceptable) → plan ethics → prompt/complete →
measure → align → integrate. Durable tenets = **HAHAS** (Helpfulness, Accuracy, Harmlessness,
Auditability, **Sustainability** — content length = compute/carbon cost). The **"Four P's"** systematize
the practice: **Principles, Personality, Patterns, Practicalities.**

### (b) Critical — world-class vs. dated; boundary with the research engine

**Genuinely world-class & durable (~85% of the book):** the voice/tone distinction and the **voice-chart
matrix**; conversational-as-turn-taking + the content-first role-play pipeline; the **11 text patterns**
(platform-independent, with embeddable `{}`/`[]` notation); the **four-phase editing + word-count curve**;
the dual-goal/virtuous-cycle scaffolding; and unusually high **intellectual honesty** (Goodhart, addiction
caution, admitting reading-level formulas are not academically validated for UX, that her pattern research
was English-only).

**The decay layer:** **Chapter 5 (LLMs)** is most perishable — "ChatGPT 3.5," "as of May 2025,"
ROUGE/perplexity as named exemplars (already superseded by LLM-as-judge / embedding evals), unsettled-
regulation framing. The *principles* (HAHAS, define-good-by-audit, probabilistic testing, humans-in-loop)
endure; the tooling/metric names do not. Also dated: specific tool names (Figma/Ditto/Frontitude/Jira…)
and the **career/compensation advocacy** in the reprinted Content Design Manifesto (a 2023–2025 industry
moment genAI is actively reshaping).

**Boundary with the research engine's writing-slop skills:** Podmajersky's voice-as-tiebreaker is a
*design* mechanism (does this string match our authored voice?), which is exactly our doctrine's "looks
authored" moat applied to words — **keep**. But detecting *generic AI prose itself* (the em-dash tell,
"delve," hedged transitions, list-of-three padding) is **textual anti-slop = research engine**. The clean
split: **we decide what the product's words should be and whether they're on-voice; the research engine
decides whether a passage reads as machine-generated slop.** Cross-reference, don't duplicate.

**What's genuinely world-class:** the voice chart is the artifact no other book operationalizes this well —
it converts an "intangible brand" into per-principle, per-aspect, *ratified* decision rules. This is the
book's permanent contribution and the strongest single thing to extract.

---

## BOOK 2 — Ben-David, *The Fundamentals of UX Writing*

### (a) Load-bearing frameworks (her process & contributions)

**Positioning:** a short Apress *Pocket Guide* built from a university intro course — **pedagogical,
exercise-driven, an on-ramp**, not a reference tome. She reviewed Podmajersky's 2nd ed and positions this
as the "deep breath" after the 2019 Yifrah/Podmajersky wave. Treats **UX writing / microcopy / content
design** as a spectrum (content design = the broader mandate incl. *where* content sits and *whether* an
element exists at all).

**The core principle triad — "Clear, Concise, Helpful"** (attributed to Google I/O '17), framed as a hard
*simultaneous* balance (a four-way Venn drafting exercise: only-clear / only-concise / both / neither).
Her sharpest insight: **"Concise ≠ short"** — it means "everything they need and nothing more; every word
earns its real estate," and she rigorously separates **cutting words** (concision) from **removing
messaging** (a separate content decision). Durable and teachable.

**Process (distributed, bottom-up, not a named pipeline):** research conventions via **SME relationships**
("a UX writer is an expert in UX writing, not the vertical") → draft against heuristics → iterate (the Venn)
→ **zoom out** to conform the set to a template ("the setup is as important as the words") → test/measure →
**break heuristics where warranted** → codify in a style guide. Backed by a **four-source epistemology** of
where best practices come from: common sense / trial-and-error / testing / consensus.

**"Breaking Best Practices" — her signature contribution.** Four explicit triggers to override a heuristic:
(1) the underlying assumption doesn't apply; (2) it doesn't serve the user (e.g. *make* a mortgage user slow
down — anti-"scannable"); (3) it doesn't serve the product/business; (4) it puts copy at odds with product
voice. Reframing heuristics as *overridable-with-reasons* rather than commandments is mature and rarely
taught this cleanly.

**Voice & Tone (leaner, more classroom-ready than Podmajersky):**
- **Voice Guide = "We are… / We are not… / Examples."** The **"We are not"** carries her best teaching: it
  must NOT be antonyms — she names **three traps** (opposites; things no product wants; irrelevancies). A
  valid "We are not" is *something another product would want to be, that a writer might hit by accident*
  (aiming "Approachable," accidentally landing "Best buds").
- **Tone Maps** — tone plotted per touchpoint as a **spectrum with direction AND magnitude**, mappable across
  a single flow or a whole **user lifecycle** (onboarding → churn → resurrection). Introduces **code-switching**.
- **"Casual ≠ Conversational"** — *conversational* (write how a human talks, use positive contractions) is
  **always right**; *casual* (informal/buddy register) is right for *some* brands only. Solves a recurring
  stakeholder fight. Embeds the **avoid-negative-contractions** rule ("do not" > "don't" — users miss the
  scanned "not") except in low-stakes copy.

**Pattern coverage (strongest = empty states):** her **three-part empty-state framework** —
(1) confirm the void is on purpose, (2) motivate filling it (how + *why*/value prop), (3) facilitate the
action (give the actual button). Plus: actionable CTAs (verbs, person-ambiguity, "Done/Next" exceptions),
**title-CTA continuity** (each must make sense read alone), **frontloading**, **reading patterns**
(F / Z / ping-pong / lawnmower / bypassing), **progressive disclosure** (balanced pros/cons), casing
discipline, ampersand avoidance, **labels-beside-icons** advocacy. Error messages are covered via examples
only — **no systematic error taxonomy** (Podmajersky owns that).

**Style guide as the collaboration instrument** (documentation → maintenance → education → governance → QC;
"influence without authority"; a governance committee; **train your LLMs on the style guide too**). She is
unusually **business/ROI-fluent** for a craft book (microcopy = cheap, everywhere, powerful).

**Testing/measurement** is lightweight (A/B with control; trial-and-error *general* vs. testing *specific*
takeaways; Hemingway/Writer tools) — a real gap past beginner level.

### (b) Critical — vs. Podmajersky; durable vs. dated; boundary

**vs. Podmajersky:** decisively **more beginner-oriented** — an on-ramp where Podmajersky is a
practitioner's operating system. He is deeper on systematic patterns, the voice-chart, measurement, and org
strategy. **She is genuinely better** on a handful of crisp, teachable frames: **Breaking Best Practices
(4 triggers)**, **concise ≠ short / cutting words ≠ removing messaging**, the **"We are not" three traps**,
**Tone Maps with magnitude**, **casual ≠ conversational**, and the consolidated **reading-pattern set**. Her
**accessibility / plain-language / i18n** through-line is woven throughout and research-updated (honest "I
used to teach X, then research changed my view" moments).

**Dated/weak:** the **entire GenAI chapter** is the most perishable — well-balanced for 2026 but model names
and capability claims ("LLMs can't do voice/tone") are already shifting; keep the meta-principles (human
accountability, verify-everything, built-in bias, "train your LLM on your guide"), discard the capability
specifics. Tooling references date; measurement is thin; some "best practices" rest on anecdote/consensus
rather than evidence (which her epistemology at least admits).

**Boundary with the research engine:** her GenAI chapter flags **bias in machine prose** (masculine-default
translation; the em-dash as "cultural colonialism") — this is *textual-slop / generic-AI-prose territory =
research engine*, not ours. We take her *design* artifacts (voice guide, tone map, empty-state framework);
we leave "is this passage machine-written" to the research engine.

**World-class:** the **"Breaking Best Practices" 4-trigger framework** and **"concise ≠ short"** are the two
things every group-10 skill should absorb — they make our skills *defensible under pressure* instead of
dogmatic.

---

## BOOK 3 — Niehaus, *Robotics for Writers* — JUDGED: MISFILED, not a UX book

**What it actually is:** a short practical guide for **fiction authors** on using ChatGPT/Bing Chat as a
brainstorming/research *aid* (explicitly NOT to generate prose). "Robotics" is whimsical metaphor for the AI
assistant (dedicated "To Clippy / To Cortana"). Structure = an LLM literacy primer + a sustainability/ethics
argument + **36 fiction-craft tips** (choose a title, generate character names, fix tense/POV, worldbuilding,
spot plot holes…), each with a "what to do instead (usually a non-AI tool)" section. The author worked on
Cortana but offers only one paragraph of historical color on intent-modeling — **no conversation/voice-UI
methodology, no microcopy, no product content design of any kind.**

**Relevance verdict: NO.** Zero coverage of interface copy, errors, empty states, voice/tone systems, or
conversation design *as a product experience*. The only transferable nuggets (basic prompt discipline, LLM
hallucination/bias literacy) are generic and far better sourced elsewhere. **Recommendation: exclude from the
design engine — it is misfiled in the `uiux_markdown` collection.** (Its sustainability theme weakly echoes
Podmajersky's HAHAS "Sustainability" tenet, but Podmajersky already covers that better.)

---

## ENGINE IMPACT

### Harden the 2 existing group-10 skills

**`ux-writing-and-microcopy`** — already strong (clarity-first, verb+object buttons, terminology glossary,
a11y/i18n pass). Add from the books:
1. **Podmajersky's 11-pattern notation** (`{replaceable}` / `[omittable]`) as the house format for stating
   button/title/label patterns — embeddable, design-system-ready. Currently the skill prose-describes; the
   notation makes patterns *spec-grade*.
2. **Ben-David "concise ≠ short" + "cutting words ≠ removing messaging"** into the "Cut, then cut again" step
   — guards against over-deletion that strips needed messaging.
3. **The four-phase editing curve (Purposeful → Concise → Conversational → Clear) + "always propose 3 ranked
   options"** as the explicit editing workflow (currently step 8–9 conflate this).
4. **"Casual ≠ conversational" + avoid-negative-contractions** into the voice-check step.
5. **Title-CTA continuity** (each must make sense read alone) — a missing, high-value microcopy rule.
6. **Reading patterns (F/Z/ping-pong/lawnmower)** as a one-line frontloading rationale.

**`error-empty-and-system-messaging`** — already excellent (what+why+fix formula, three empty-state types,
severity-to-channel, a11y live-regions, i18n expansion). Add:
1. **Podmajersky's three-way error taxonomy by interruption — Inline / Detour / Blocking** — sharper than the
   current severity-to-channel map for *errors specifically*; the Detour pattern (offer the alternate path,
   instruction most prominent) is missing.
2. **Ben-David's three-part empty-state framework** (confirm-on-purpose / motivate / facilitate) — aligns
   with and tightens the skill's existing three empty-state *types*.
3. **Ben-David's "Breaking Best Practices" 4 triggers** — license to override the no-humour / be-concise
   rules *with stated reason* (e.g. deliberately verbose to build trust in a sensitive flow).
4. **Podmajersky on "invalid" = ableist** and singular-"they" defaults — strengthens the no-blame rule with
   specific inclusive-language bans.

### New group-10 skills / refs justified

| Candidate | Verdict | Justification |
|---|---|---|
| **`voice-tone-and-content-style-guide`** (Phase-2 P1) | **CONFIRM — build, highest value** | Both books converge hard here. It is the *upstream* skill the existing two already cite as a missing dependency (microcopy cites `02-…/brand-style-guide` for voice). Must carry **Podmajersky's Voice Chart (6 rows × principle columns + ratified tiebreaker)** AND **Ben-David's Voice Guide ("We are / We are not + 3 traps / Examples") + Tone Maps (magnitude + lifecycle)**. The single biggest gap-closer for the thinnest group. |
| **`content-modeling-and-information-design`** (P2) | **CONFIRM but RESCOPE → "content-structure-and-readability"** | Real gap, but the books support the *readability / plain-language / content-structure* half far more than database-style "content modeling/taxonomy." Anchor it on **plain language** (Ben-David's research-backed audience expansion: neurodivergence, working memory, rushed reading, "even experts prefer it"), **progressive disclosure**, **reading patterns**, and **legalese-to-plain patterns** (Pinterest summaries, Typeform parallel). Keep IA/taxonomy light (that overlaps `04-…/navigation-and-information-architecture`). |
| **`conversation-and-agent-content-design`** | **DEFER / P2 — justified but NOT from these books** | Podmajersky's "conversational = turn-taking" + content-first role-play is the seed, and the gap doc already lists a cross-cutting `conversational-and-voice-ui` (P2). Worth a group-10 *content* counterpart (agent persona, turn-taking, error recovery copy) — but **Niehaus gives nothing usable** for it; source elsewhere. Do not let the misfiled book justify building this now. |
| **Ref: `voice-chart-template.md`** | **ADD** | The single most-extractable artifact (Podmajersky). Belongs in the new voice-tone skill's `references/`. |
| **Ref: `breaking-best-practices.md`** | **ADD (cross-cutting within group 10)** | Ben-David's 4 triggers — a shared decision-rule all three+ group-10 skills cite, keeping them defensible rather than dogmatic. |

### Phase-2 P1-wave: CONFIRM / CHANGE / REDUNDANT

- **`voice-tone-and-content-style-guide`** (the only group-10 item in the P1 spec): **CONFIRM, with an
  upgraded brief.** Current spec lists `refs: tone-matrix.md; ex: content-style-guide-worked.md`.
  **CHANGE the refs** to add **`voice-chart-template.md`** (Podmajersky 6×principles matrix + tiebreaker) and
  rename `tone-matrix.md` → **`tone-map.md`** (Ben-David's magnitude+lifecycle model, richer than a flat
  matrix). The worked example should show **both** a filled voice chart and a tone map for one product.
- **Boundary guard to add to the spec:** the skill must **defer textual-AI-slop detection to the research
  engine** (state it in "Do Not Use When"), consistent with the doctrine note above. It owns *defining* the
  voice; the research engine owns *detecting generic machine prose*.
- **No P1 group-10 item is REDUNDANT.** `voice-tone-…` is genuinely upstream of the two existing skills and
  is the dependency they already reference but that does not yet exist as a group-10 skill (today it points
  out to `02-…/brand-style-guide` — see Note below).

> **Note (cross-group seam to resolve):** `ux-writing-and-microcopy` currently routes the voice definition to
> `02-color-brand-and-visual-identity/brand-style-guide`. Once `voice-tone-and-content-style-guide` ships in
> group 10, decide the seam: brand-style-guide = *visual+verbal brand identity*; the new group-10 skill =
> *operational content voice/tone system for interface copy*. They should reference each other, not duplicate.
> Update the two existing skills' "voice source" pointer to the new group-10 skill when it lands.

---

## EXTRACT-INTO TABLE

| Framework / artifact | Source | Extract into |
|---|---|---|
| **Voice Chart** (6 rows × product-principle columns; 4 roles incl. ratified tiebreaker) | Podmajersky | **NEW** `voice-tone-and-content-style-guide` → `references/voice-chart-template.md` |
| Voice vs. Tone distinction (consistent voice / variable tone) | Podmajersky | NEW `voice-tone-and-content-style-guide` (core) |
| **Voice Guide "We are / We are not (3 traps) / Examples"** | Ben-David | NEW `voice-tone-and-content-style-guide` |
| **Tone Maps** (direction + magnitude, mapped over flow/lifecycle) | Ben-David | NEW `voice-tone-and-content-style-guide` → `references/tone-map.md` |
| **"Casual ≠ Conversational"** + avoid negative contractions | Ben-David | `ux-writing-and-microcopy` (voice-check step) |
| **Conversational = turn-taking**; content-first role-play → text-bubbles → wireframe | Podmajersky | DEFER `conversation-and-agent-content-design` (P2); seed note in `voice-tone-…` |
| **11 UX Text Patterns** + `{replaceable}`/`[omittable]` notation | Podmajersky | `ux-writing-and-microcopy` (adopt notation) + `error-empty-and-system-messaging` (error/empty/confirmation/notification patterns) |
| **Error taxonomy: Inline / Detour / Blocking** | Podmajersky | `error-empty-and-system-messaging` (add the Detour pattern) |
| **Empty-state 3-part: on-purpose / motivate / facilitate** | Ben-David | `error-empty-and-system-messaging` (tighten existing 3-types) |
| **Four-phase editing + word-count curve**; "always propose 3 ranked options" | Podmajersky | `ux-writing-and-microcopy` (editing workflow) |
| **"Concise ≠ short" / cutting words ≠ removing messaging** | Ben-David | `ux-writing-and-microcopy` ("Cut, then cut again" step) |
| **"Breaking Best Practices" — 4 override triggers** | Ben-David | **Shared** `references/breaking-best-practices.md` cited by all group-10 skills |
| **Title-CTA continuity**; reading patterns (F/Z/ping-pong/lawnmower) | Ben-David | `ux-writing-and-microcopy` (frontloading/CTA rules) |
| **Plain language** (research-backed audience expansion; legalese→plain patterns) | Ben-David | RESCOPED `content-structure-and-readability` (was `content-modeling-…`, P2) |
| Progressive disclosure (pros/cons, a11y caveats) | Ben-David | RESCOPED `content-structure-and-readability` (P2) |
| **UX Content Scorecard** (Usability ⅔ + Voice ⅓, mapped to Nielsen + WCAG 2.2) | Podmajersky | `00-…/heuristic-evaluation-and-design-critique` (cross-cutting) — content-review rubric |
| Inclusive-language bans ("invalid"=ableist; singular "they"; "person responsibilities") | Podmajersky | `error-empty-and-system-messaging` + `voice-tone-…` (no-blame / vocabulary rules) |
| **HAHAS** (Helpfulness, Accuracy, Harmlessness, Auditability, Sustainability) for dynamic/LLM content | Podmajersky | `voice-tone-…` (note); flag GenAI specifics as time-sensitive |
| Textual-AI-slop / generic-machine-prose detection (em-dash tell, bias) | Podmajersky Ch.5 / Ben-David Ch.5 | **OUT — route to digital-research engine's writing-slop skills** (boundary preserved) |
| *Robotics for Writers* (any content) | Niehaus | **NOTHING — misfiled, exclude** |
