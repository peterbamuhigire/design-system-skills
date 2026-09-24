# Data Display Patterns: Helping People Understand and Act on Data

Parent skill: [interaction-design-patterns](../SKILL.md)

When to read: when a screen shows charts, tables or dashboards — deciding what the display must answer, how to direct attention, and how people explore, compare and drill into records. For chart colour and mark specifications, pair with the data-visualisation and colour skills.

The purpose of a data display is not to show data but to help someone understand it and decide what to do. Work out the question first, encode the most important relationship with position, then add the interactions people need to explore.

Each pattern block gives: **Problem**, **Use when**, **Do not use / caveats** (including touch and WCAG 2.2 accessibility), **How**, **Example** (original) and **Pairs with**.

---

## Task A — Decide what the display must answer

Answer these five questions before choosing any chart or table.

| Question | Design response | If skipped |
|---|---|---|
| How is the data organised? | Hierarchy → tree or treemap; time series → line chart; categories → bar chart; part of a whole → pie or donut, only with 2–5 slices | The chart shape fights the data and misleads |
| Which relationships matter most? | Encode them with preattentive variables (Task B) so they are seen before they are read | The key finding is buried among equals |
| How will people explore it? | Provide zoom, pan, filter and select | People export to a spreadsheet to answer simple questions |
| Can people rearrange it? | Offer sorting, grouping and pivoting — each reveals different patterns in the same data | One fixed view hides the pattern a given role needs |
| Can people narrow it to what they need? | Dynamic Queries that update the view immediately | Static views force repeated round trips |

**Accessibility baseline for every chart:** a text summary of the main finding and an accessible data table or download (WCAG 1.1.1); chart lines, bars and focus indicators at 3:1 contrast against adjacent colours (WCAG 1.4.11); no meaning carried by colour alone (WCAG 1.4.1).

---

## Task B — Direct attention to what matters

### Preattentive variables

Some visual attributes are picked up almost instantly, before conscious reading. Use them to point at the most important pattern.

| Variable | Best for | Avoid when |
|---|---|---|
| Colour hue | Categorical differences (type A versus type B) | Ordered data — use lightness or saturation |
| Colour lightness or saturation | Ordered quantity (more = darker) | Categorical data |
| Size | Quantity (larger = more) | Comparing several dimensions at once |
| Position (x / y) | The most precise comparison — the primary encoding | Never trade position for a weaker encoding |
| Shape | Categories, sparingly (at most 4–5 shapes) | Ordered data |
| Orientation | Direction, angle | Quantitative comparison |
| Motion | Drawing attention to a change | Any decorative use — motion is the strongest attractor; respect reduced-motion settings (WCAG 2.3.3) |

**Rule:** encode the most important relationship with position; use colour, size and shape only for secondary relationships.

(The commonly quoted timing for preattentive processing is omitted here; it varies by study and does not change the rule.)

### Data Spotlight
- **Problem:** significant points — anomalies, targets, thresholds, milestones — are missed if people must search for them.
- **Use when:** a dataset has one or more values that carry the story.
- **Do not use / caveats:** spotlighting everything spotlights nothing; one to three annotations per chart. Annotations must be real text, not baked into an image, and exposed in the text summary.
- **How:**
  - Annotate in place: "Target", "Budget exceeded", "Record high".
  - Use a distinct treatment: a labelled reference line, a shaded region or a differently marked point (shape as well as colour).
  - Keep annotation text to about five words.
  - Combine with Datatips: the annotation tells the story, the datatip gives the detail.
- **Example:** a district malaria dashboard draws a labelled line at the epidemic threshold, and the week that crosses it is marked "Threshold crossed — week 14".
- **Pairs with:** Datatips, preattentive variables.

---

## Task C — Reveal exact values on demand

### Datatips
- **Problem:** labelling every point clutters the chart, but people who need an exact value have no other way to get it.
- **Use when:** any interactive chart with more points than can be labelled.
- **Do not use / caveats:** tooltips must appear on keyboard focus as well as hover, stay while the pointer moves onto them, and be dismissible with Escape (WCAG 1.4.13). On touch, the finger hides whatever is beneath it — place the tip above the touch point and make it larger.
- **How:**
  - Show the value, label, timestamp and relevant context (comparison with target or previous period).
  - Trigger on hover or focus on desktop; on touch, tap to show and tap elsewhere to dismiss.
  - Place it above or to the right of the point, never covering the point.
  - Keep the styling plain: a light or dark card with a subtle shadow.
- **Avoid:** charts with no datatips at all.
- **Example:** tapping a bar in a mobile-money agent's weekly float chart shows "Tue 3 Sep — UGX 1.8 m float, 22 % below Monday".
- **Pairs with:** Data Spotlight, Overview + Detail.

---

## Task D — Narrow and explore

### Dynamic Queries
- **Problem:** an "Apply" step hides the link between a filter and its effect and slows exploration.
- **Use when:** filtering lists, tables and charts where results can be computed quickly.
- **Do not use / caveats:** where each query is slow or costly (large server-side datasets, poor mobile connections), batch changes behind an explicit "Show results" button and say why. Announce the result count through a status message, not a focus move (WCAG 4.1.3).
- **How:**
  - Update the view as controls change, within about 200 ms.
  - Show the count: "Showing 47 of 312 customers".
  - Show "Clear all filters" whenever any filter is active.
  - Keep filter state in the URL so results can be shared and bookmarked.
  - Use sliders, checkboxes, date ranges and text search as query controls; sliders need a keyboard and a single-pointer alternative such as number inputs (WCAG 2.5.7).
- **Example:** a Kampala clinic's appointment list narrows as the receptionist ticks "Paediatrics" and drags the date range, showing "18 of 240 appointments".
- **Pairs with:** Data Brushing, Deep Links (`02-navigation.md`).

### Data Brushing
- **Problem:** in a dashboard, people need to see how a subset in one view relates to the others.
- **Use when:** dashboards and analysis tools where several charts share one dataset.
- **Do not use / caveats:** brushing by drag must have a click or keyboard alternative (WCAG 2.5.7). On phones, stacked charts rarely fit on one screen — use a shared filter chip instead.
- **How:**
  - Selecting a subset in one chart highlights the same records in every linked chart.
  - Highlight the selection in the source chart; fade the unselected data elsewhere.
  - Reset with "Clear selection" or a click on empty space.
- **Example:** selecting the "Masaka" bar in a cooperative's deliveries-by-district chart highlights Masaka farmers in the price-trend and payments charts beside it.
- **Pairs with:** Dynamic Queries, Small Multiples.

---

## Task E — Compare series and categories

| Situation | Choose | If chosen wrongly |
|---|---|---|
| Fewer than 4 categories | Overlay them on one chart | Needless repetition |
| 4–20 categories, same metric | Small Multiples | An overlaid chart becomes unreadable |
| More than 20 categories | Filter first (Dynamic Queries), then compare | A wall of tiny charts nobody reads |
| Two related metrics on very different scales | Multi-Y Graph | One series is flattened against the axis |
| Three or more metrics on different scales | Separate charts | Readers cannot tell which axis applies |

### Small Multiples
- **Problem:** comparing the same measure across categories is hard when each lives on a different chart with different scales.
- **Use when:** one metric across 4–20 products, regions, periods or segments.
- **Do not use / caveats:** on phones, stack the multiples in one column with the shared scale repeated. Provide the underlying table for screen-reader users.
- **How:**
  - Use the same chart type and the same axis scales in every panel — essential for honest comparison.
  - Order logically: by value (highest first), by time or alphabetically.
  - Size each panel to fit the grid but still show trend.
  - Give each panel a clear category label and, if helpful, a colour marker.
- **Example:** a county health office shows twelve identical monthly-attendance charts, one per sub-county, on a shared 0–4,000 scale.
- **Pairs with:** Grid of Equals (`03-layout.md`), Data Brushing.

### Multi-Y Graph
- **Problem:** two related metrics on very different scales (money and a percentage) cannot share one axis.
- **Use when:** exactly two related series whose relationship matters.
- **Do not use / caveats:** a second axis invites false correlation; never more than two Y-axes. Differentiate the series by line style or marker as well as colour (WCAG 1.4.1).
- **How:**
  - Left axis for the primary metric in the primary colour; right axis for the secondary metric in the secondary colour.
  - Colour each series to match its axis.
  - Label both axes with units.
- **Example:** a SACCO performance chart plots total loans (UGX millions, left) against the default rate (%, right).
- **Pairs with:** Datatips.

---

## Task F — Work through records

### Sortable Table
- **Problem:** people need to find extremes and order records their own way.
- **Use when:** any data table with more than a handful of rows.
- **Do not use / caveats:** sort controls must be buttons in the header cells with the state exposed through `aria-sort`. On phones, wide tables need a card layout or a horizontal scroll with a frozen first column.
- **How:**
  - Every column header sorts by that column; show direction with an arrow (↑ ascending, ↓ descending).
  - First activation ascending, second descending, third returns to the default.
  - Default sort matches the commonest need — usually most recent first for time-based data.
  - Shift+click on a second header adds a secondary sort.
- **Example:** a stores ledger defaults to "Last movement, newest first"; the storekeeper sorts by "Quantity" to find items running out.
- **Pairs with:** Dynamic Queries, Overview + Detail.

### Overview + Detail
- **Problem:** complex records (invoices, patients, projects) are too large to show in full in a list, but people must triage many of them.
- **Use when:** browsing and triaging records one after another.
- **Do not use / caveats:** on phones, the detail replaces the list and Back returns to the same scroll position. Move focus to the detail heading when it opens, and back to the item when it closes.
- **How:**
  - Overview: three to five key fields, enough to identify and triage.
  - Detail: the full record, in a side panel or a dedicated page.
  - Prefer the Two-Panel Selector (list and detail side by side) when people click through items quickly.
- **Example:** a clinic's lab-results queue shows patient, test, status and time; selecting a row opens the full result in a right-hand panel while the queue stays visible.
- **Pairs with:** Two-Panel Selector, Datatips, Sortable Table.

### Pagination, Infinite Scroll or Load More

| Approach | Use when | If misapplied |
|---|---|---|
| Pagination | People jump to a position, bookmark it or share a specific page | — |
| Infinite scroll | Sequential browsing is the main activity (feeds, galleries) | On data tables, people cannot reach "page 50" of an order history or keep their place |
| Load More button | A middle ground where the user controls loading; lists with a natural end | — |

Infinite scroll must not trap keyboard users before the footer (WCAG 2.1.1); new items should be announced.

---

## Anti-patterns and their consequences

| Anti-pattern | Consequence |
|---|---|
| 3D charts | Values are distorted; precise comparison is impossible |
| Pie chart with more than five slices | Angles cannot be compared — use a bar chart |
| Y-axis truncated above zero on a bar chart | Differences are exaggerated and magnitude misread |
| Dual Y-axes for unrelated data | Readers cannot tell which axis applies to which series |
| Colour as the only differentiator | People with colour-vision deficiency cannot distinguish series — add shape, label or pattern (a prevalence statistic is omitted; cite a current source if needed) |
| Animation on every load | Decorative motion is noise; reserve it for transitions that communicate change |
| Missing axis labels or units | The numbers cannot be interpreted |
| Showing all data at all times | Noise hides the signal — filter by default and let people expand |

## Checks

1. Each chart states the question it answers and its main finding in text.
2. The most important relationship is encoded by position, with a shared scale wherever charts are compared.
3. Every value shown on hover is also reachable by keyboard focus and on touch.
4. Filters show a result count, a visible "Clear all", and survive a page reload via the URL.
5. An accessible table or download accompanies every chart.

## Related

- `03-layout.md` — Grid of Equals, Center Stage for dashboards.
- `04-actions.md` — bulk actions and Hover / Pop-Up Tools on table rows.
- Companion skills: data-visualisation and colour skills in this engine.

Sources: pattern names follow Tidwell, Brewer & Valencia, *Designing Interfaces* (3rd ed.); Tufte, *The Visual Display of Quantitative Information* (small multiples); W3C, WCAG 2.2.
