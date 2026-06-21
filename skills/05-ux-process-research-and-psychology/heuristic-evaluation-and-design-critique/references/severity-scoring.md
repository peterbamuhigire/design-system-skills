# Reference: Severity Scoring — the 0–4 scale and how to rate

A heuristic evaluation that does not rate its findings is un-prioritisable noise. This reference
is the **severity rating method**: the canonical **0–4 scale** and the **three factors** that set
each finding's rating, plus the multi-evaluator protocol and the gate floors. It runs as Workflow
Step 5 in `SKILL.md`, after a finding has its location · heuristic · issue · evidence.

**Provenance.** The 0–4 severity scale and the frequency × impact × persistence factors are
Jakob Nielsen's *Severity Ratings for Usability Problems*. Aligned here to 2026 / WCAG 2.2 AA and
`doctrine/design-doctrine.md`. (The scored `design-audit` skill uses a separate triage stack —
Travis red-route + effort-vs-impact — to *order* fixes; this file *rates* the finding. The two
are compatible: rate here, then sequence there if a fix queue is needed.)

---

## 1. The 0–4 severity scale

Rate every finding on this scale. The rating is a **combined judgement** of the three factors in
§2 — not a guess and not a measure of how annoying it felt to you.

| Rating | Name | Meaning — act on it… |
|---|---|---|
| **0** | Not a usability problem | On reflection, this is not a problem at all. Drop it (do not pad the report). |
| **1** | Cosmetic only | Need not be fixed unless extra time is available; no real effect on task success. |
| **2** | Minor | Fixing has low priority; users are slowed or mildly confused but recover easily. |
| **3** | Major | Important to fix; users are significantly impeded and recovery is hard — schedule it this cycle. |
| **4** | Catastrophe | **Imperative** to fix before release; users cannot complete the task, lose work, or are blocked. |

> Report the **0** ratings as resolved/dismissed (it shows the evaluation was thorough), but never
> let a 0 occupy a finding slot in the prioritised list.

---

## 2. The three factors that set the rating

Severity is a function of three independent factors. Judge each, then combine into the 0–4 above.
**Do not rate on annoyance** — a mildly annoying issue that hits every user on every visit
out-ranks a dramatic issue that one user hits once.

| Factor | Question | Pushes severity… |
|---|---|---|
| **Frequency** | How often is the problem encountered? (common vs rare path) | Up if common |
| **Impact** | How hard is it for users to overcome once encountered? (blocks vs slows) | Up if blocking |
| **Persistence** | Is it a one-off the user learns around, or does it recur every time? | Up if recurring |

A fourth modifier — **market impact** — can lift a finding (a problem that drives users away or
breaks a red-route conversion task scores higher than its raw usability cost).

**Worked combinations:**
- High frequency + blocking + persistent → **4 (catastrophe).** (e.g. the only "submit" control is
  off-screen on mobile — every user, every time, cannot complete.)
- Rare + blocking + one-off recoverable → **2–3** depending on how hard the recovery is.
- Common + mild slowdown + recoverable → **2 (minor).**
- Rare + cosmetic + once → **1 (cosmetic).**

Frequency and persistence are *why a "cosmetic" issue can still rate 2–3* — never auto-floor
visual issues to 1 (see `SKILL.md` Anti-Patterns).

---

## 3. Gate floors (these bind first)

Some violations carry a **minimum** severity regardless of the factor math, because a legal or
distinctiveness floor applies (consistent with `doctrine/design-doctrine.md` and the rubric gates
in `design-audit`):

| Violated standard | Minimum severity | Why |
|---|---|---|
| **WCAG 2.2 AA** failure (contrast, focus, target size, keyboard, etc.) | **≥ 3 (major)** | Legal/accessibility floor — blocks a class of users. |
| **Loss of the user's work / data** (T7 violation) | **4 (catastrophe)** | Irrecoverable; never acceptable. |
| **Red-route task cannot complete** | **4 (catastrophe)** | The product fails its core job. |
| **AI-slop / convergent-default** finding (doctrine) | **≥ 2 (minor)**, higher if on a first-impression surface | Distinctiveness is the moat; a slop tell on the hero is not cosmetic. |

A gate floor *raises* a rating; it never lowers one. The factor math can push above the floor but
not below it.

---

## 4. Multi-evaluator protocol (independent, then aggregate)

The reliability of severity ratings comes from **independence then aggregation** — single-rater
severity is noisy.

1. Merge the evaluators' findings into one deduplicated list (collapse duplicates; keep the
   clearest wording; record **how many evaluators independently caught each** — multi-catch issues
   are higher-confidence and rarely 0–1).
2. Each evaluator rates the **whole merged list** 0–4 **independently** (rating the merged list,
   not just their own finds, removes "my finding matters more" bias).
3. The facilitator takes the **mean** of the independent ratings per finding (round to nearest
   integer; on a tie, round toward the higher severity — under-rating a real problem costs more
   than over-rating).
4. Nielsen's guidance: ~**3 evaluators** rating gives a usefully stable mean; more raters tighten
   it. A single-evaluator rating is acceptable but **state the lower confidence** in the report.

---

## 5. Recording severity in a finding

Each finding card (see `SKILL.md` §2) ends with:

```
- **Severity:** 3 — common path, hard to recover, recurs every visit (freq High × impact Hard × persistent)
- **Caught by:** 4 of 5 evaluators
```

Then the report's **severity-ordered table** sorts findings **4 → 0**, breaking ties by red-route
position (a tied finding on the critical path ranks above one off it). That ordered list is the
hand-off contract to `ux-remediation-and-redesign` (the fix backlog) or `design-audit`'s triage.

---

*Provenance: Nielsen, "Severity Ratings for Usability Problems" (0–4 scale; frequency × impact ×
persistence). Aligned to WCAG 2.2 AA and `doctrine/design-doctrine.md`. Companion to
`heuristics-catalog.md`.*
