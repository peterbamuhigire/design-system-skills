# Research Method Selector — when to use which method

Pick the **cheapest method that actually answers the question**. The two axes that decide everything:

- **Generative vs. Evaluative** — are you discovering what to build (generative / discovery), or judging something that already exists (evaluative)?
- **Attitudinal vs. Behavioural** — are you capturing what people *say* (attitudinal), or what they *do* (behavioural)? When the two disagree, behaviour wins. (Axes after Christian Rohrer's landscape of UX research methods, Nielsen Norman Group.)

A third axis — **qualitative (why / how to fix)** vs. **quantitative (how many / how much)** — decides whether you get explanations or numbers. Small-n qual tells you *why*; large-n quant tells you *how widespread*.

---

## The decision table

| Your question sounds like… | Phase | Best method | Why | Typical n |
|---|---|---|---|---|
| "Who are our users and what do they actually do all day?" | Generative | **Contextual inquiry / field study** | Behaviour in real context; surfaces needs users can't articulate | 5–12 |
| "What problems do they have? What's the unmet need?" | Generative | **In-depth interviews** (past-behaviour) | Depth, the "why" behind a need | 5–8 per segment |
| "How do they think about this domain / what labels make sense?" | Generative | **Card sort** (open) | Reveals users' mental model for IA | 15–30 (quant) |
| "Does our navigation/IA let people find things?" | Evaluative | **Tree test** (+ first-click test) | Tests findability without visual design noise | 30–50 |
| "Can people complete the core tasks? Where do they get stuck?" | Evaluative · Behavioural · Qual | **Moderated usability test** | Watch the struggle, ask why; cheapest deep diagnosis | **5** finds ~85% of issues |
| "How does completion rate / time compare across many users or two designs?" | Evaluative · Behavioural · Quant | **Unmoderated usability test** (remote tool) | Cheap scale, A/B of task success | 20–50+ |
| "How satisfied / how loyal / which of these do they prefer?" | Evaluative · Attitudinal · Quant | **Survey** (SUS, CSAT, NPS, preference) | Scale, trend over time | 100+ for stable rates |
| "How do they use it over days/weeks, in their own life?" | Either · Behavioural | **Diary study** | Longitudinal, real context, infrequent moments | 8–15 |
| "Which variant drives the metric in production?" | Evaluative · Behavioural · Quant | **A/B test / analytics** | True behaviour at full scale; but tells *what*, not *why* | thousands |
| "Where are users dropping off and on which screen?" | Evaluative · Behavioural · Quant | **Analytics / funnel analysis** | Pinpoints *where*; pair with qual for *why* | all traffic |

---

## Fast routing rules

1. **"Why" or "how do I fix it" → qualitative, small-n.** 5 moderated sessions beat a 200-person survey for diagnosing usability problems.
2. **"How many / how much / which is bigger" → quantitative, large-n.** Don't quote percentages off 5 people.
3. **They're asserting future behaviour ("would you / how much would you pay") → don't survey it.** Replace with past behaviour, a fake-door test, or a behavioural signal.
4. **Designing something new → generative first.** Evaluating something built → evaluative. Doing evaluative research to answer a generative question is the classic mismatch (you "test" a solution to a problem you never validated).
5. **Disagreement between what they say and what they do → trust the behaviour.** Attitudinal data explains; behavioural data decides.
6. **Mixed methods beat any single one.** Analytics finds *where* the drop-off is (quant/behavioural); a handful of moderated sessions on that exact step find *why* (qual/behavioural). Pair them.

---

## The 5-user rule — and its limits

Nielsen's curve: ~5 users surface ~85% of usability problems in a single qualitative test; returns diminish sharply after that. **But** this holds only for *qualitative* problem-finding within *one homogeneous user group*. It does **not** apply to:
- **Quantitative** claims (success rates, SUS scores) — those need 20+ for stability.
- **Multiple distinct segments** — run ~5 per segment.
- **Comparative / A-B** evaluation — needs more for statistical power.

So: 5 to *find* problems qualitatively; many to *measure* anything.

---

## Cost vs. answer-fit (choose down this list before going up)

1. **Analytics you already have** — free, instant, behavioural; tells *what/where*, never *why*.
2. **5-user moderated test** — a day of work; the highest insight-per-hour for diagnosis.
3. **Unmoderated remote test** — cheap scale, no scheduling; weaker depth (no follow-up "why").
4. **Survey** — scales cheaply but only attitudinal; easy to write badly (leading, double-barrelled).
5. **Field study / diary** — richest, most expensive; reserve for genuine generative gaps.

Spending more than the decision is worth is itself a failure. Match the rigour to the stakes.

---

## Provenance
Axes and the generative/evaluative + attitudinal/behavioural framing follow Christian Rohrer / Nielsen Norman Group's "landscape of UX research methods"; the 5-user finding is Nielsen & Landauer. Method authority traces to the UX research literature and human practitioners, never to AI-tool recommendations (`doctrine/design-doctrine.md` §2, sourcing-authority rule).
