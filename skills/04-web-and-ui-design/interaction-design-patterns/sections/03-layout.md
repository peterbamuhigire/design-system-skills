# Layout Patterns: Structuring a Screen for Scanning and Focus

Parent skill: [interaction-design-patterns](../SKILL.md)

When to read: when deciding how a screen is divided — what is fixed, what gets the most space, how long or dense content is broken up. For the visual system itself (type scale, colour tokens, spacing), pair with `practical-ui-design` and the typography and colour skills.

A clean layout rests on four things: a visible information hierarchy, a clear reading flow, alignment to a grid, and grouping that follows Gestalt proximity and similarity.

---

## Task A — Make importance readable at a glance

### Visual hierarchy tools

| Tool | How to use it | If misused |
|---|---|---|
| **Size** | Larger means more important: headings over body, primary action over secondary | Everything large means nothing stands out |
| **Position** | Top and left are read first in left-to-right scripts (F-pattern); upper-right draws the eye after the main focal point; the bottom reads as footer | Key actions placed bottom-left are missed |
| **Density** | Tight grouping signals relatedness; isolation with generous space signals importance | Even spacing everywhere hides the structure |
| **Background / contrast** | A tinted or high-contrast area draws attention | Same treatment everywhere implies equal importance |
| **Rhythm** | Consistent spacing between list items, cards and grid cells lowers reading effort | Irregular spacing reads as error |

**Squint test:** blur your view of the layout. What reads first, and what last? If everything is equally loud, nothing stands out.

### Center Stage
- **Problem:** when navigation and toolbars compete with the content, people do not know where to look.
- **Use when:** any screen whose main purpose is one piece of content or one task.
- **Do not use / caveats:** multi-pane tools (inbox, dispatch console) need balanced panes — pick the dominant pane per task. At 400 % zoom content must reflow into one column without horizontal scrolling (WCAG 1.4.10).
- **How:** primary content gets about 60–75 % of desktop width; navigation never matches the content's visual weight; on mobile the content goes full width and navigation moves to a bottom bar or menu; one obvious focal point per screen.
- **Example:** a hospital lab-result screen gives the result table centre stage; patient details sit in a slim header and actions in a right rail.

---

## Task B — Give people stable landmarks

### Visual Framework
- **Problem:** if the application skeleton changes from page to page, people cannot build spatial memory.
- **Use when:** every multi-page product.
- **Do not use / caveats:** a framework that hides content behind a fixed header at high zoom fails WCAG 2.4.11 (focus not obscured); use landmarks (`header`, `nav`, `main`, `footer`) so assistive technology can jump between regions.
- **How:** header with logo, global navigation, search and account menu; sidebar with section navigation and relevant filters or tools; content area that changes per page and gets most space; footer with utility, legal and secondary links. Keep it visually stable. Give sidebars the same background as the content, separated by a border — contrasting colours fragment the space.
- **Rule:** never move navigation between pages; even helpful rearrangement forces relearning.
- **Example:** every screen of a Kenyan county revenue system keeps the county crest top-left, search centre, officer menu top-right and module list on the left.

---

## Task C — Show many items of equal weight

### Grid of Equals
- **Problem:** a collection with no ranking needs to read as a set of peers.
- **Use when:** product listings, image galleries, staff directories, category menus.
- **Do not use / caveats:** not for items with a clear priority — use a list with emphasis on the top items. Not for data people compare field by field — use a table (`05-data.md`). Card grids must keep a logical reading and focus order when columns reflow.
- **How:** identical container treatment (border, shadow, padding); content inside may vary; equal horizontal and vertical gutters; responsive columns 4 → 3 → 2 → 1; avoid mixed card sizes unless deliberately featuring an item.
- **Example:** a Mombasa hotel's room-types page shows six room cards of identical size, each with photo, rate and "Check dates".

---

## Task D — Break a long or dense page into parts

| Pattern | Use when | Do not use when |
|---|---|---|
| Titled Sections | One page has several distinct content groups | More than five or six groups — split into tabs or pages |
| Module Tabs | Several views of the same record or container | People need to compare content across tabs at once |
| Accordion | Many categories, only one or two needed at a time | Multi-step forms or wizards |
| Collapsible Panels | Optional or secondary panels on a complex screen | The panel holds information needed for every decision |

### Titled Sections
- **Problem:** complex pages are hard to scan without labels on each group.
- **How:** headings larger and heavier than body text and marked up as real headings (WCAG 1.3.1, 2.4.6); visual separation by space, a divider or a background change; the page's structure should be understandable from the headings alone; at most five or six sections per scroll.
- **Example:** a loan application summary: Applicant, Business, Collateral, Guarantors, Decision.

### Module Tabs
- **Problem:** related views of one thing crowd a single page.
- **How:** three to seven tabs per group (more → dropdown or side list); a clearly marked active tab; content shown instantly without a page reload; URL reflects the active tab (Deep Links); horizontal for short labels, vertical side list for long labels or many tabs; use the ARIA tabs pattern (arrow keys move between tabs).
- **Caveats:** horizontal tabs that overflow on phones must scroll visibly or collapse to a select.
- **Example:** a patient record with Summary / Visits / Prescriptions / Billing.

### Accordion
- **Problem:** long lists of categories overwhelm when all shown open.
- **How:** short, scannable headers acting as a table of contents; a chevron or +/− showing state, exposed via `aria-expanded`; headers are buttons, keyboard operable; allow several sections open unless there is a strong reason not to.
- **Avoid:** all sections starting open (defeats the pattern); accordions in multi-step forms (known usability problems).
- **Example:** a mobile-money help page: "Sending money", "Withdrawing at an agent", "Reversing a wrong transfer".

### Collapsible Panels
- **Problem:** secondary panels (filters, details, configuration) consume space when not needed.
- **How:** a labelled toggle ("Show filters" / "Hide filters"); remember the collapsed or expanded preference between sessions; the layout reflows gracefully when collapsed; especially useful on mobile.
- **Example:** a stock-report screen whose filter panel collapses to give the table full width on a laptop.

---

## Task E — Let experienced people shape their workspace

### Movable Panels
- **Problem:** in analysis tools and dashboards, one fixed arrangement cannot suit every role.
- **Use when:** customisation genuinely adds value (dashboards, analysis tools, development environments).
- **Do not use / caveats:** not on mobile — use fixed layouts. Drag-to-arrange needs a non-drag alternative such as "Move up/Move down" (WCAG 2.5.7), and the reading order must follow the new visual order.
- **How:** a well-designed default for new users; persist the arrangement between sessions; a "Reset to default" option.
- **Example:** a cooperative's operations dashboard lets the manager move "Milk intake today" above "Payments due".

---

## Task F — Visual finish that earns trust

These rules belong to the visual system but affect layout decisions; the detailed doctrine lives in the colour, typography and composition skills.

- **Credibility:** people judge credibility heavily on visual appearance — an unfinished-looking interface undermines trust whatever its function. Check: show the screen to three target users for five seconds and ask whether they would trust it with their money or data.
- **Colour:**
  - Warm (red, orange, yellow, brown) versus cool (blue, green, purple, grey): match temperature to the product's intent.
  - Light backgrounds are the readable default; dark backgrounds need a deliberate reason.
  - High contrast conveys strength and tension; low contrast conveys calm — choose deliberately, but text must still meet WCAG 1.4.3 contrast minimums.
  - Saturated colours attract but tire the eye: one or two saturated accents, muted tones elsewhere.
  - Avoid complementary text/background pairs that vibrate (blue on red, red on green).
  - Never use colour as the only signal; pair it with shape, icon or text (WCAG 1.4.1). (A prevalence statistic for colour-vision deficiency is omitted here; cite a current source if needed.)
- **Typography:**
  - Body line height about 1.6 × font size (16 px text → about 26 px).
  - Avoid pure black on white; use a near-black such as #1A1A1A or #333333.
  - At most three font sizes per page section.
  - Sentence case for interface labels.
  - Sans-serif for interface labels; serif or sans for content depending on the product's character (font choice follows the engine's font doctrine).
  - A four-level text hierarchy — primary, secondary, tertiary, muted — used consistently.
- **Visual style:** commit to one style across every element; mixing styles signals incoherence.

| Style | Character | Use when |
|---|---|---|
| Skeuomorphic | Imitates physical objects | People need help mapping digital to physical concepts |
| Illustrated | Custom illustration, distinct personality | Consumer apps, onboarding, brand-led products |
| Flat | No shadows or gradients, solid colours | Clean, fast-loading interfaces |
| Minimal | Generous space, near-invisible structure | Focus-heavy tools, reading apps, premium positioning |
| Adaptive / parametric | Generated from data or context | Data-heavy and AI-driven interfaces |

## Checks

1. The squint test shows one clear focal point per screen.
2. The framework (header, navigation, sidebar) is identical in position on every page.
3. Every long page can be understood from its headings alone.
4. Collapsed and tabbed content is keyboard operable and announces its state.
5. Content reflows at 320 CSS px width without horizontal scrolling (WCAG 1.4.10).

Sources: pattern names follow Tidwell, Brewer & Valencia, *Designing Interfaces* (3rd ed.); Stanford Web Credibility Project (Fogg et al.); W3C, WCAG 2.2.
