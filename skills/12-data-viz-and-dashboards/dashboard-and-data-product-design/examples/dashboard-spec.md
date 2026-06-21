# Worked Example: "Revenue Health" Dashboard Spec

A complete dashboard spec produced by applying this skill end-to-end, for a sample product:
**a subscription-billing platform's internal "Revenue Health" console.** It shows what a real
spec looks like — decision, persona, KPI tiers, layout zone map, interaction model, and the
real-time/freshness model — not a template to copy blindly.

---

## 0. Decision & persona (state first — doctrine §2)

> **Decision:** "Does the Head of Revenue need to act this week on a retention or churn problem,
> and if so, where?" — a weekly + ad-hoc glance, plus a daily check during a known billing
> incident.
>
> **Persona:** Head of Revenue (and the RevOps analyst supporting her). Desktop primary; checks
> on phone during incidents. Looks for ~60 seconds weekly; wants to confirm health or jump
> straight to the segment that's bleaking.

Everything below serves that sentence. The dashboard is **not** "all billing data."

---

## 1. KPI hierarchy (per `references/kpi-hierarchy.md`)

Driver tree used to rank metrics:

```
Net Revenue Retention (T1)
├── Expansion MRR (T2) ── upgrades / seat adds (T3)
├── Contraction MRR (T2) ── downgrades by plan (T3)
└── Churned MRR (T2) ──┬ voluntary churn by cohort (T3)
                       └ involuntary (failed-payment) churn (T3)
MRR Growth Rate (T1) ── new vs expansion vs churned MRR bridge (T2)
Failed-Payment Recovery Rate (T1) ── dunning funnel stages (T2) ── failures by gateway (T3)
```

### Tier 1 — headline (4 tiles, the decision metrics)

| KPI | Value (sample) | Comparison | Trend | Direction |
|---|---|---|---|---|
| **Net Revenue Retention** | 104.2% | ▲ 1.2 pts vs target (103%) | 8-wk sparkline | up = good |
| **MRR Growth Rate (MoM)** | +3.1% | ▼ 0.6 pts vs last month | 6-mo sparkline | up = good |
| **Gross Churn (MRR)** | 2.4% | ▲ 0.5 pts vs prior (worse) | 8-wk sparkline | down = good |
| **Failed-Payment Recovery** | 71% | ▼ 4 pts vs 30-day avg | 30-day sparkline | up = good |

Each tile: value + comparison (sign + %) + trend, with **arrow + sign** as a non-colour cue
alongside the up/down-good colour (WCAG — not colour-only).

**Demoted to Tier 3 (vanity):** "Total lifetime revenue," "total active subscriptions" — both
only ever rise, so neither can signal a problem.

### Tier 2 — diagnostic drivers (mid-grid charts, each a `data-visualization`-compliant tile)

- **MRR bridge** (waterfall): start → +new → +expansion → −contraction → −churn → end.
- **NRR by segment** (horizontal bars, sorted): SMB / Mid-market / Enterprise.
- **Dunning funnel** (stacked bar): retry → updated card → recovered → lost.
- **Churn by cohort** (line / small multiples): voluntary vs involuntary over time.

### Tier 3 — operational detail (behind drill-down only)

Account-level MRR changes, per-gateway failure rates, individual cohort tables. Not on the
default view.

---

## 2. Layout (per `references/dashboard-layout-patterns.md`)

**Archetype chosen: KPI strip + grid** — justified: the persona scans 4 headline numbers first,
then dives into whichever is off. F-pattern weighting within the grid (primary driver top-left).

```
┌──────────────────────────────────────────────────────────────────────┐
│ Revenue Health   [Time: Last 30d ▾] [Segment: All ▾]  Updated 09:41:12 │  ← header zone
├───────────────┬───────────────┬───────────────┬───────────────────────┤
│  NRR 104.2%   │ MRR +3.1% MoM │ Gross Churn   │ Pmt Recovery 71%      │  ← T1 strip
│  ▲1.2 vs tgt  │ ▼0.6 vs LM    │ 2.4% ▲0.5 ✗   │ ▼4 vs 30d avg         │     (primary scan)
├───────────────┴───────────────┼───────────────┴───────────────────────┤
│  MRR bridge (waterfall)        │  NRR by segment (sorted h-bars)        │  ← T2 grid
├────────────────────────────────┼────────────────────────────────────────┤
│  Dunning funnel (stacked bar)  │  Churn by cohort (small multiples)     │  ← T2 grid
└────────────────────────────────┴────────────────────────────────────────┘
   ↓ click any T2 tile → master–detail panel slides in with T3 detail
```

- Density decreases top→bottom: big numbers up top, denser charts below, tables only on drill.
- Tiles aligned to a 12-col grid (gutters per layout-grid skill), consistent upper-left titles.
- Grouped by question: the two churn-related tiles (dunning, cohort) sit in the lower zone.

---

## 3. Interaction model

- **Global filters:** Time range (default **Last 30 days**) and Segment (default **All**), in
  header, persisted to URL (`?range=30d&segment=all`) so the view is shareable and survives
  refresh. Default state already answers "are we healthy?" with zero clicks.
- **Cross-filter:** clicking a segment bar in "NRR by segment" filters the whole board to that
  segment. Affordance: bars show pointer + hover state; an **active-filter chip** ("Segment:
  Enterprise ✕") appears in the header; clicking the bar again or the chip's ✕ clears it.
- **Drill-down (master–detail):** clicking a T2 tile opens a right-side panel with that driver's
  T3 detail (e.g. dunning funnel → per-gateway failure table + recovery by retry attempt). The
  overview stays visible. **Breadcrumb** shows `Revenue Health › Dunning › Stripe gateway`; a
  back arrow and ✕ close it; the panel **inherits** the current time-range + segment filters.

---

## 4. Real-time / data UX

- **Refresh model:** poll every **60s** (billing data isn't sub-second; the weekly decision
  doesn't need faster). Manual "Refresh" button for on-demand.
- **Freshness:** header shows `Updated 09:41:12`. Acceptable staleness window = 5 min.
- **Stale state:** if a poll fails or data age >5 min, header badge turns to
  `⚠ Data may be stale — last updated 6m ago`; numbers dim slightly so they don't read as live.
- **Empty vs error:** new account with no MRR history → zero-state tile ("No billing events in
  this range — widen the time filter"). A single failed query (e.g. dunning service down) fails
  *that tile* with a retry link; the rest of the board stays live.
- **Calm updates:** KPI deltas animate over ~300ms, throttled to ≤1 visible update/sec;
  `prefers-reduced-motion` → snap, no animation. Scroll position, open drill panel, and active
  cross-filter all survive the 60s refresh; layout never reflows on update.

---

## 5. Accessibility gate (per `doctrine/references/wcag-2.2-criteria.md`)

- [x] Filter dropdowns, refresh, clear-chip, drill targets all ≥24×24px (44px on the phone view).
- [x] Time-range supports preset options (single-pointer) — no drag-only brush (2.5.7).
- [x] Sticky header does not obscure focused tile controls when tabbing (2.4.11).
- [x] Board reflows to a single column at 320px / 200% zoom; KPI strip stacks (1.4.10/1.4.4).
- [x] Auto-refresh honours `prefers-reduced-motion`; nothing flashes (2.3.1/2.3.3).
- [x] KPI status uses arrow + sign + label, not colour alone; deltas meet ≥4.5:1 / ≥3:1.
- [x] Each chart tile independently passes the `data-visualization` per-chart checklist.

---

## 6. Why this is "authored," not slop

No gauges, no 3D, no donut KPIs, no rainbow tiles (doctrine `ai-slop-taxonomy.md`). Flat,
grey-based tiles with one accent per status; a deliberately chosen archetype tied to a named
decision and persona; a real KPI hierarchy with vanity metrics demoted; drill-down and live-data
behaviour designed as first-class. A templating tool would have produced a 4×3 grid of equal
gauges with no comparisons and no freshness — exactly what this spec refuses.
