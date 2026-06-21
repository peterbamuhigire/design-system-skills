# Reference: KPI Hierarchy — Tiering Metrics into a Decision Surface

A dashboard is not a list of numbers; it is a *ranked* list of numbers. The single most common
dashboard failure is the **flat KPI wall** — a dozen equal tiles with no tier, no comparison, no
direction. This reference is how you turn a candidate metric list into a three-tier hierarchy
that drives the layout in `dashboard-layout-patterns.md`.

> Scope boundary: this reference decides **which** metrics matter and how they rank. How to
> *draw* each one (chart type, declutter, colour, axes) belongs to the sibling
> `data-visualization` skill. Don't restate its rules here.

---

## 1. What makes a real KPI (the gate every metric must pass)

A number is a **KPI** only if all four are true. Fail any → it is context, not a headline.

| Test | A real KPI… | A non-KPI… |
|---|---|---|
| **Tied to a decision** | changes what someone *does* this week | is "interesting" but actionable by no one |
| **Has a comparison** | carries a target, prior period, or benchmark | is a bare value floating with no reference |
| **Has a direction-of-good** | up-is-good or down-is-good is defined | is ambiguous (e.g. raw "sessions") |
| **Is sensitive & timely** | moves on the cadence the decision needs | is so smooth/laggy it never informs a choice |

**Three numbers, always, per Tier-1 KPI:** the **value**, the **comparison** (Δ vs target /
vs prior / vs benchmark — with sign and %), and the **trend** (sparkline or arrow over the
relevant window). A value alone is not a KPI; it is a fact.

---

## 2. The three tiers

### Tier 1 — Headline / decision metrics (3–5 maximum)

The numbers that answer "is the thing this dashboard exists for OK or not?" in one glance.
These own the **primary scan zone** (top strip / top-left). Hard cap ~5: beyond that the eye
can't rank them and you've rebuilt the flat wall.

- Prefer **rates and ratios** over cumulative totals (conversion %, MRR growth %, error rate,
  p95 latency) — they reflect *current health*, not history.
- Each gets value + comparison + trend, and a **status colour cue paired with a non-colour cue**
  (arrow + sign), per `wcag-2.2-criteria.md` (not colour-only).
- If two Tier-1 metrics always move together, one is redundant — demote it.

### Tier 2 — Diagnostic / driver metrics

The "why is Tier 1 doing that?" layer. These live in the **mid grid** as charts (the tiles the
`data-visualization` skill governs). They decompose each headline: if Tier-1 is "Net Revenue
Retention," Tier-2 is expansion vs contraction vs churn over time, by segment.

- Usually time series, breakdowns, or comparisons — they earn a chart, not just a number.
- Should map clearly back to a Tier-1 metric (the driver tree below makes this explicit).

### Tier 3 — Operational / detail metrics

Row-level, per-entity, long-tail. **Not shown by default** — reached via drill-down, detail
panels, or a linked table. Putting Tier-3 on the front page is the wall problem again.

---

## 3. The driver tree (how to find the tiers, not guess them)

Decompose each headline metric into the inputs that mathematically or causally move it. The root
is Tier 1; the branches are Tier 2; the leaves are Tier 3.

```
Net Revenue Retention (T1)
├── Expansion MRR (T2)
│   ├── seats added per account (T3)
│   └── plan upgrades (T3)
├── Contraction MRR (T2)
│   └── downgrades by plan (T3)
└── Churned MRR (T2)
    ├── voluntary churn by cohort (T3)
    └── involuntary (failed-payment) churn (T3)
```

The tree does three jobs: it **ranks** metrics objectively, it **wires drill-down** (clicking a
T2 driver opens its T3 leaves), and it kills duplicates (anything not on a branch toward a
decision metric is probably vanity).

---

## 4. Vanity-metric demotion

Demote (or cut) any metric that mainly exists to look good:

| Vanity (demote) | Decision-grade replacement (promote) |
|---|---|
| Total registered users (only goes up) | Active rate / WAU-MAU ratio (can fall) |
| Cumulative revenue to date | Period-over-period growth %, or MRR |
| Total page views | Conversion rate, task-completion rate |
| Followers / total downloads | Activation rate, retention curve |
| Tickets closed (volume) | First-response time, reopen rate, CSAT |

Rule of thumb: **if a metric can only ever go up, it cannot signal a problem, so it cannot
drive a decision** — it is at best Tier 3 context.

---

## 5. Comparison framing (the "vs what" that turns a number into a signal)

Every Tier-1 (and most Tier-2) metric needs an explicit comparison basis. Pick deliberately:

- **vs Target / SLA / budget** — when there's a committed goal (best for accountability views).
- **vs Prior period** (WoW, MoM, YoY) — when trend/momentum is the question. State the period.
- **vs Benchmark / peer / forecast** — when "good" is relative to a baseline.

Show the delta **with sign, magnitude, and direction-of-good colour** — e.g. `▲ 4.2% vs target`
in the up-is-good colour, `▼ 1.1% vs last month` in the down-is-bad colour. Always include a
non-colour cue (arrow + sign) so the signal survives for colour-blind users and B&W print
(doctrine + `wcag-2.2-criteria.md`).

---

## 6. KPI hierarchy checklist

- [ ] One sentence: the decision this dashboard supports and who makes it.
- [ ] Tier 1 has **3–5** metrics, all rates/ratios where possible, no two redundant.
- [ ] Every Tier-1 metric carries value + comparison + trend.
- [ ] Comparison basis (target / prior / benchmark) is stated, with sign + non-colour cue.
- [ ] Vanity metrics demoted to Tier 3 or cut.
- [ ] A driver tree links each Tier-1 metric to its Tier-2 drivers and Tier-3 detail.
- [ ] Tier-3 metrics are behind drill-down, not on the default view.
- [ ] Direction-of-good is defined for every metric.
