# Reference: Dashboard Layout Patterns, Drill-Down & Real-Time UX

How the tiered metrics from `kpi-hierarchy.md` become one coherent screen, how users move
through it, and how it behaves when the data is live. The underlying column grid / gutters /
spacing rhythm comes from the layout-grid skill; this reference governs the **dashboard-specific**
concerns: zone sequence, tile density, drill-down, cross-filtering, and streaming-data UX.

---

## 1. Scan order is the layout (place by attention, not by availability)

Users scan a screen in predictable paths. Match the KPI tier to the path:

- **Top-left is the most valuable pixel.** Tier-1 headline KPIs go in the top strip, left-to-right
  in priority order.
- **F-pattern** (text/analytical-dense dashboards): eyes sweep top row, then scan down the left
  edge with shorter rightward sweeps. Put primary KPIs top, secondary down the left column.
- **Z-pattern** (sparse executive dashboards): top-left → top-right → diagonal → bottom-right CTA.
  Good for a few big tiles plus a "go here next" action.
- Never bury a Tier-1 metric bottom-right; never force the eye to travel up-and-left to read.

**Density gradient:** density should *decrease* as importance decreases left-to-right / top-to-
bottom — big numbers and whitespace up top, denser charts and tables lower. A uniformly dense
grid has no hierarchy.

---

## 2. Layout archetypes (pick one to match the persona)

| Archetype | Shape | Best for | Tier mapping |
|---|---|---|---|
| **KPI strip + grid** | Horizontal band of 3–5 number tiles across the top, chart grid below | The default analytics dashboard | T1 = strip; T2 = grid; T3 = drill |
| **F-pattern analytical** | Dense multi-column grid, primary metrics top + left | Power-user consoles, product analytics | T1 top row; T2 left-weighted |
| **Z-pattern executive** | Few large tiles, generous whitespace, one CTA | Exec/board summary, weekly glance | 3–4 T1 tiles only; T2 on drill |
| **Master–detail** | List/overview pane + detail pane (side-by-side or list→panel) | Entity dashboards (accounts, hosts, orders) | Overview = T1/T2; detail = T3 |
| **Monitoring wall** | Status-first tiles (green/amber/red), incident timeline | Ops/SRE/NOC, always-on screens | T1 = health states; T2 = signals |

State which archetype you chose and why, in the spec — that is the "authored choice" the doctrine
requires, not a default 4×3 widget grid.

---

## 3. Tile/zone composition rules

- **Group by question, not by chart type.** Tiles that answer one question (e.g. "where is churn
  coming from?") sit together; use proximity/enclosure (Gestalt — see `data-visualization`) to
  bind a zone.
- **One message per tile.** A tile answers one question with one (declutter-compliant) chart or
  number. Multi-message tiles belong split.
- **Consistent tile chrome** — same title position (upper-left), same comparison treatment, same
  padding. Inconsistent tiles read as a slop pile.
- **Alignment is non-negotiable** — clean vertical and horizontal lines across tiles; ragged
  tile edges are the #1 "unauthored dashboard" tell.
- **Reserve a header zone** for: dashboard title (a "so what" where possible), the global
  filter/time-range control, and the **freshness timestamp** (§6).

---

## 4. Filtering & cross-filtering

- **Global controls** (time range, segment, environment) live in the header, apply to the whole
  board, and **persist** (URL/query-state so a view is shareable and survives refresh).
- **Cross-filtering** (clicking a bar in one tile filters the others) is powerful but must be:
  **discoverable** (cursor/affordance shows the tile is interactive), **visible** (an active-
  filter chip shows what's applied), and **reversible** (one obvious "clear" / click-again-to-
  deselect). Silent cross-filtering that rescopes half the board is the "mystery filter"
  anti-pattern.
- **Default state must answer the headline question with zero clicks** — sensible default time
  range and segment, so the first paint is already useful.
- Filter controls obey `wcag-2.2-criteria.md`: ≥24px targets; any range *brush/drag* has a
  single-pointer alternative (2.5.7, e.g. preset ranges or numeric inputs).

---

## 5. Drill-down (detail on demand without losing the user)

Three patterns, in increasing context-shift:

1. **In-place expand / detail-on-hover** — tooltip, expand-row, popover. Lowest cost; keeps the
   overview fully visible. Best for one extra layer of Tier-3 detail.
2. **Master–detail panel** — selecting an entity opens a side/bottom panel with its Tier-3 detail;
   overview stays on screen. Best for per-entity dashboards.
3. **Navigate-to-page** — full drill to a dedicated detail view. Highest context shift — use only
   when the detail truly needs the whole screen.

**Non-negotiable for all three: preserve and *show* the trail.** A visible breadcrumb (Overview ›
EMEA › Acme Corp), a working back button, and **carried-through filters** (the drill inherits the
overview's time range/segment). "Drill-down that teleports" — new context, no breadcrumb, filters
reset — is the cardinal drill-down sin. The driver tree in `kpi-hierarchy.md` defines *what* each
drill reveals (T1 → its T2 drivers → their T3 leaves).

---

## 6. Real-time / streaming data UX

Live data is where dashboards most often become untrustworthy or unreadable. Design these:

### Refresh model
- **Manual** (user clicks refresh) — for expensive queries / analyst control.
- **Poll** (fixed interval) — most dashboards; pick an interval matching how fast the decision
  needs it (don't refresh a weekly metric every 5s).
- **Push / stream** (websocket/SSE) — for true monitoring; needs the most careful UX below.

### Freshness & staleness (always, non-optional)
- Show a **"Updated HH:MM:SS" / "as of"** timestamp in the header. A live-looking board with no
  data age silently launders stale numbers into false confidence.
- Define and render a distinct **stale state**: when data exceeds the acceptable staleness window
  (or a fetch fails), show a clear "Data may be stale — last updated 4m ago" banner/badge, not a
  frozen-but-confident screen.
- Distinguish **"no data yet"** (empty) from **"data is old"** (stale) from **"fetch failed"**
  (error) — three different states, three different treatments.

### Don't make live data twitchy
- **Throttle/debounce** UI updates — humans can't read a number flickering many times a second.
  Batch pushes into a calm cadence (e.g. ≤1 visible update/sec).
- **Transition gently** — animate value/bar changes smoothly, and **honour
  `prefers-reduced-motion`** (snap instead of animate) per `wcag-2.2-criteria.md`; never flash.
- **Preserve user state across refresh** — scroll position, current selection, expanded
  drill-down, and active filters must survive an update. Resetting them on every tick is hostile.
- **Stable layout** — refresh must not reflow tiles or jump the page. Reserve space; update in
  place. (Echoes Core Web Vitals CLS as a UX constraint.)

### Loading, empty, error — first-class
- **Loading:** show a **skeleton** that previews the tile/grid structure, not a spinner per
  widget or a blank grid.
- **Empty / zero-state:** explain *why* it's empty and what to do (adjust filter, no events yet),
  not a blank tile.
- **Error / partial:** if one tile's query fails, fail *that tile* gracefully (retry affordance)
  without blanking the whole board.

---

## 7. Layout & real-time checklist

- [ ] One layout archetype chosen and justified (not a default grid).
- [ ] Tier-1 KPIs in the primary scan zone (top strip / top-left), priority order.
- [ ] Density decreases with importance; tiles aligned to clean vertical/horizontal lines.
- [ ] Tiles grouped by question; one message per tile; consistent chrome.
- [ ] Global filters in header, persisted in URL/state, sensible defaults answer the headline.
- [ ] Cross-filtering is discoverable, shows active-filter chips, and is reversible.
- [ ] Drill-down preserves a visible breadcrumb + back path + carried filters.
- [ ] Refresh model chosen to match decision cadence.
- [ ] Freshness timestamp shown; distinct stale + empty + error states designed.
- [ ] Live updates throttled, gently transitioned (reduced-motion honoured), state preserved,
      layout stable.
- [ ] Loading = skeleton; all controls ≥24px; reflows at 320px / 200% zoom.
