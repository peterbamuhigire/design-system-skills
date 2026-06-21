# Reference: Triage & Prioritization — turning findings into a fix order

The scored audit answers *how bad is it* (the 0–100 rubric). This reference answers the next
question the rubric does **not**: *in what order do we fix it?* It converts the severity-tagged
findings list into a **defensible, sequenced remediation queue** rather than a vibes-based one.

**Provenance.** The triage stack is distilled from Lisandra Maioli's *Fixing Bad UX Designs*
(2018), aligned to 2026 doctrine. It runs **after** scoring (see `SKILL.md` §2.5 Triage) and
feeds the **Prioritised Recommendations** section of the report. The fix itself is executed by
the companion **`ux-remediation-and-redesign`** skill — this audit *diagnoses and triages*; that
skill *redesigns, re-validates, and measures the uplift*.

> Detection vocabulary lives in `doctrine/references/interaction-anti-patterns.md` (the
> behavioural anti-pattern checklist). Severity for any match it surfaces is set **here**.

---

## 1. The triage stack (apply in order)

Each finding from the audit is run through four lenses. The first two set **severity**; the last
two set **sequence within a severity band**.

### 1.1 Red-route / Travis severity test (sets the band)

Three yes/no questions per finding (Travis severity matrix):

| Question | Meaning |
|---|---|
| **(a) Red route?** | Is the issue on a *critical path* — a task many users must complete (sign-up, checkout, primary CTA, core flow)? |
| **(b) Hard to overcome?** | Once hit, is it difficult for a user to work around or recover from? |
| **(c) Persistent / recurring?** | Does it happen repeatedly, or to many users, rather than as a one-off edge case? |

Map the answers onto the audit's existing severity bands (keep the band names — do not invent new
ones):

| Pattern | Audit severity |
|---|---|
| Red route **and** (hard to overcome **or** persistent) | **Critical** |
| Red route, or hard-to-overcome + persistent off the red route | **High** |
| Off red route, recoverable, recurring | **Medium** |
| Off red route, recoverable, one-off / cosmetic | **Low** |

> A failed **hard gate** (AI Slop / WCAG 2.2 AA / CWV) from the rubric is **always at least
> Critical/High** regardless of this test — the gate cap and the legal/distinctiveness floor
> bind first. Triage *orders* gate-failing findings; it never demotes them below the cap.

### 1.2 Effort-vs-impact map (sets sequence within a band)

Plot each finding on impact (harm to users/business) × effort (design + dev cost):

| Quadrant | Impact | Effort | Action |
|---|---|---|---|
| **Quick wins** | High | Low | **Do first** — fix immediately. |
| **Major projects** | High | High | Plan and schedule — high value, needs a sprint. |
| **Fill-ins** | Low | Low | Batch when convenient. |
| **Thankless** | Low | High | **Defer / drop** — rarely worth it. |

Within each severity band, sequence **Quick wins → Major projects → Fill-ins**; park Thankless.

### 1.3 MoSCoW (the release commitment)

Tag each finding for the *next* release: **Must** / **Should** / **Could** / **Won't (this time)**.

- **Must** = gate-failing or red-route Critical — ship is blocked without it.
- **Should** = High that materially degrades the experience but has a workaround.
- **Could** = Medium polish that improves quality if budget allows.
- **Won't** = Low / Thankless — explicitly deferred, recorded so it is not silently dropped.

### 1.4 Tie-breakers (apply when sequence is still ambiguous)

1. **Frequency weighting** — an issue seen repeatedly in research/testing outranks a one-off.
2. **Business alignment** — conversion-blocking / KPI-affecting issues outrank pure aesthetics.

---

## 2. Triage worksheet (copy into the report)

```
| # | Finding (short)         | Red route? | Hard? | Persistent? | Severity | Impact×Effort | MoSCoW | Order |
|---|-------------------------|-----------|-------|-------------|----------|---------------|--------|-------|
| 1 |                         | Y/N       | Y/N   | Y/N         | Crit/High/Med/Low | Quick win / Major / Fill-in / Thankless | M/S/C/W | 1.. |
```

The **Order** column is the output: the integer sequence the remediation skill executes in. Sort
by severity band first (Critical → Low), then by effort-impact within the band, then tie-breakers.

---

## 3. Hand-off to `ux-remediation-and-redesign`

The ordered queue (the worksheet above + the Prioritised Recommendations list) is the **input
contract** to the companion `ux-remediation-and-redesign` skill. The split is deliberate:

| This skill (`design-audit`) | `ux-remediation-and-redesign` |
|---|---|
| Detects (10 dimensions + anti-pattern checklist) | Redesigns lo-fi → hi-fi |
| Scores (rubric, gates, caps) | Validates (5-user usability / A/B / tree test) |
| **Triages (this reference) → ordered fix queue** | Measures the uplift (SUS/NPS/HEART, KPI delta) |

`design-audit` stops at the triaged queue. It does **not** redesign or re-test — that is the
remediation skill's job. Downstream of that, `design-qa-and-pre-launch-review` is the ship gate.

---

*Composes the severity bands in `SKILL.md` §2 and the gate caps in `references/audit-rubric.md`.
Detection vocabulary: `doctrine/references/interaction-anti-patterns.md`. Triage method after
Maioli (2018), aligned to 2026 doctrine.*
