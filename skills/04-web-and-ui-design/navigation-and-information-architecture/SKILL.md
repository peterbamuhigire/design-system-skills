---
name: navigation-and-information-architecture
description: Use when structuring how a product's content and screens are organised and found — defining the information architecture (sitemap, content inventory, taxonomy, labelling), choosing and specifying navigation systems (global/primary nav, mega-menu, sidebar, tabs, hamburger, bottom bar, footer nav), and designing wayfinding (breadcrumbs, active/current state, "you are here", section landmarks), search and filtering, and the page/URL hierarchy. Reach for it when a product has grown a confusing menu, users can't find things, you're adding a section and don't know where it goes, you're planning a redesign's IA, or you need a navigation spec to hand to engineering. Produces a sitemap + navigation specification with labels, structure, states, and keyboard/ARIA behaviour. This is the skill that decides structure *before* pages are designed — start here, not at the page level.
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
    - claude-code
    - codex
---

# Navigation And Information Architecture
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com.

<!-- dual-compat-start -->
## Use When

- Planning the **information architecture** of a new product or a redesign: the content inventory,
  the grouping/taxonomy, the labelling system, the sitemap, and the URL hierarchy.
- A menu has **grown past comprehension** — too many top-level items, overlapping labels, things
  buried three levels deep, a "Misc/Other/More" dumping ground — and needs restructuring.
- Choosing and **specifying a navigation system**: global/primary nav, mega-menu, sidebar/rail,
  tabs, hamburger drawer, mobile bottom bar, local/in-section nav, utility nav, footer nav.
- Designing **wayfinding**: breadcrumbs, active/current-page state, section landmarks, the
  "you are here" signal, and how deep pages tell the user where they sit.
- Designing **search and filtering** as a findability path (when browsing won't scale), including
  scoped search, autosuggest, zero-results, and faceted filter structure.
- You need a **navigation spec to hand to engineering** — labels, hierarchy, states, responsive
  collapse behaviour, keyboard order, and ARIA roles.

## Do Not Use When

- You are styling an *already-decided* nav — colour, type, spacing, hover polish. That's surface
  craft: `04-web-and-ui-design/practical-ui-design` and the colour/type doctrine, not this skill.
- The structure is settled and you're laying out *one page's* internal blocks — that's layout
  (`03-layout-grid-and-composition/layout-grid-and-spacing`).
- It's a single landing/marketing page with no real hierarchy to architect — use
  `04-web-and-ui-design/landing-page-and-conversion-design` (its nav is a thin top bar + CTA).
- You're writing the *words* on the nav as a microcopy/voice exercise — pair with
  `10-content-design-and-ux-writing/ux-writing-and-microcopy`; this skill owns the *label system*
  (the taxonomy and what each label must denote), the copy skill owns tone.
- You're validating the IA with users (card sort / tree test as a *research study*) — run
  `05-ux-process-research-and-psychology/ux-research-and-usability-testing`; this skill *consumes*
  those results and *specifies* the methods inline, but the study itself is research's job.

## Required Inputs

- A **content inventory** (or the means to build one): the real list of pages/sections/objects the
  product must hold, ideally with rough volumes and priorities. You cannot architect an unknown set.
- The **primary user tasks and mental models** — what people come to do, and the words *they* use
  for things (not the org chart's words). IA mirrors user mental models, never the internal team
  structure.
- **Platform & breakpoints** — web, app, both; the smallest viewport the nav must survive. The nav
  pattern choice is partly a breakpoint decision.
- Whether the structure is **mostly hierarchical** (marketing/docs/content site), **mostly task/app**
  (a tool with objects and actions), or **mostly database/faceted** (catalogue, listings) — this
  picks the dominant pattern (see `references/ia-patterns.md`).

## Workflow

1. **Inventory and audit before you draw a single menu.** List every existing/intended content
   item. For a redesign, audit the current IA: depth, top-level count, orphan pages, duplicate or
   ambiguous labels, the "Other/More" bucket (always a smell), and where analytics show people get
   lost. You are mapping reality, not the wished-for site. See `references/ia-patterns.md`.

2. **Group by the user's mental model, not the org chart.** Cluster items by how users think they
   relate (validate with a **card sort** — open if you don't yet know the categories, closed to test
   proposed ones). The single most common IA failure is mirroring internal departments
   ("Our Divisions") instead of user goals. Name the groups with the users' own words.

3. **Choose the organisation scheme deliberately.** Pick the structure that fits the content:
   *hierarchical/topical* (the default for most sites), *task-based*, *audience-based* (only when
   audiences truly need disjoint paths — it forces a self-identification step, so use sparingly),
   or *faceted/database* (catalogues, where filtering beats a fixed tree). Most real products are a
   **hybrid**: a hierarchical spine + faceted browse + search. State which scheme governs and why.

4. **Set the hierarchy depth and breadth on purpose.** Favour **breadth over depth** for findable
   content — shallow, wide trees beat deep, narrow ones (every extra click level sheds users).
   Keep most content reachable in **≤3 clicks** from home; flag anything at depth ≥4 for promotion
   or search-first access. But don't over-flatten a top bar past ~7±2 primary items — past that,
   adopt a mega-menu or a sidebar rather than cramming. Depth and breadth trade off; choose, don't drift.

5. **Build the label system as a system.** Labels must be: *distinct* (no two could hold the same
   item), *specific* (no "Solutions/Resources" catch-alls unless genuinely scoped), *parallel* (same
   grammatical form across a level), *in the users' vocabulary*, and *stable*. This is the taxonomy,
   not decoration — a bad label is an IA bug, not a copy nit. Reconcile the label set with
   `10-content-design-and-ux-writing/ux-writing-and-microcopy` for tone, but the *denotation* is yours.

6. **Select the navigation pattern(s) to express the structure.** Map the chosen IA onto concrete
   patterns from `references/nav-pattern-catalog.md`: primary (top bar, mega-menu, sidebar/rail,
   tabs), local/in-section, utility, breadcrumb, footer, and the mobile transform (top bar →
   hamburger drawer or bottom bar). Pick by structure shape and depth — *not* by fashion. State the
   responsive collapse rule: exactly what happens to each nav region at each breakpoint.

7. **Specify wayfinding so deep pages are never disorienting.** Every page must answer "where am I,
   what's around me, how do I get back/up." That means a persistent **active/current-page state**
   (visually *and* `aria-current="page"`), **breadcrumbs** for any hierarchy ≥3 levels deep (they
   are orientation + an up-the-tree control, not a back button), section landmarks, and a clear path
   home. See `references/nav-pattern-catalog.md` (Breadcrumbs, Active state).

8. **Design search and filtering as the second findability path.** Browsing (the tree) and finding
   (search) are complements. Provide search whenever the inventory is large or users arrive knowing
   the exact thing. Specify: scope (global vs in-section), autosuggest, query persistence, a *useful*
   **zero-results** state (suggestions, scope-broaden, contact), and—for catalogues—a faceted filter
   structure whose facets mirror the taxonomy. Empty/zero-results states pair with
   `04-web-and-ui-design/empty-error-and-loading-states`.

9. **Make the whole navigation keyboard-operable and announced — this is a gate, not a polish.**
   Nav is the most-traversed, most-keyboard-dependent surface in the product. Every nav item must be
   reachable and operable by keyboard in a logical order, with a **visible focus indicator**; the
   current item carries `aria-current="page"`; menus/disclosures expose name+role+state and toggle
   with Enter/Space + Arrow keys and close on Escape; provide a **"skip to main content"** link as
   the first focusable element; and don't let a sticky header obscure the focused nav item. Pointer
   targets ≥ **24×24 CSS px** (aim 44×44 touch). All per
   `doctrine/references/wcag-2.2-criteria.md` (2.1.1 keyboard, 2.4.3 focus order, 2.4.7 focus
   visible, 2.4.11 focus not obscured, 2.5.8 target size, 4.1.2 name/role/value).

10. **Write the sitemap + navigation spec.** Deliver: the sitemap (tree + URL paths), the
    organisation scheme and rationale, the label system, the per-region nav pattern with states and
    responsive behaviour, the wayfinding rules, the search/filter spec, and the keyboard/ARIA
    contract — enough for engineering to build without re-deciding structure. See
    `examples/sitemap-and-nav-spec.md`.

## Anti-Patterns

- **Mirroring the org chart** ("Our Departments", "Divisions") instead of user tasks and mental
  models — the classic IA failure that makes everything hard to find.
- **The "Other / More / Misc / Resources" dumping ground** — a bucket of unclassifiable items is the
  visible symptom of a broken taxonomy, not a category.
- **Deep, narrow trees** that bury content 4–6 clicks down when breadth would have surfaced it;
  conversely, a top bar with 12+ undifferentiated items because no one chose a mega-menu/sidebar.
- **Ambiguous, overlapping, or non-parallel labels** — two menu items that could each hold the same
  page; vague "Solutions" next to vague "Products"; mixed grammatical forms in one level.
- **Breadcrumbs used as a back button**, or omitted on deep pages so users have no up-the-tree path
  and no "you are here."
- **No (or only-colour) active state** — the user can't tell which section they're in; nothing sets
  `aria-current`.
- **Hamburger-everything**, including on desktop where there's ample room — hiding primary nav behind
  a menu icon tanks discoverability for the sake of minimalism.
- **Mega-menus and dropdowns that fail keyboard/screen-reader users** — open only on hover, trap or
  skip focus, no Escape, no roles — the single most common nav accessibility defect.
- **No search on a large catalogue**, or a search with a dead-end zero-results page.
- **A nav that looks like every template** — a generic centered logo + 5 links + ghost-button CTA
  with no authored point of view, against the doctrine's anti-slop Mission.

## Outputs

- A **sitemap** (hierarchy tree with URL/route paths), the stated **organisation scheme** and why it
  fits, a **label system** (taxonomy with each label's denotation), the **navigation specification**
  per region (pattern, items, states, responsive collapse rule), the **wayfinding rules**
  (breadcrumbs, active state, landmarks), the **search & filtering spec** (scope, autosuggest,
  zero-results, facets), and the **keyboard + ARIA contract**. Hands off cleanly to page layout,
  component, and content-design skills.

## Examples

- `examples/sitemap-and-nav-spec.md` — a complete, real IA + navigation specification for a sample
  product (a multi-tenant SMB accounting SaaS): content inventory, card-sort-derived grouping,
  organisation scheme, full sitemap with routes, the label system, every nav region specified
  (sidebar, top utility bar, breadcrumbs, mobile bottom bar) with states and breakpoint behaviour,
  search/filter spec, and the keyboard/ARIA contract.

## References

- `doctrine/design-doctrine.md` — Mission §0 (authored over convergent — the nav is the most
  template-prone surface in a product; make a defensible structural choice, don't ship the generic
  bar) and Anti-Slop Charter §2 (state the structural choice and its rationale before building).
- `doctrine/references/wcag-2.2-criteria.md` — the keyboard, focus-order, focus-visible,
  focus-not-obscured, target-size, and name/role/value floors that nav must pass as a gate.
- `references/ia-patterns.md` — organisation schemes, mental-model grouping, depth-vs-breadth,
  taxonomy/labelling rules, card sort & tree test methods, and the IA audit checklist.
- `references/nav-pattern-catalog.md` — the navigation pattern library: when to use each (top bar,
  mega-menu, sidebar/rail, tabs, hamburger, bottom bar, breadcrumb, utility, footer), the responsive
  transforms, active-state and breadcrumb rules, and the per-pattern keyboard/ARIA contract.
- Upstream: `05-ux-process-research-and-psychology/ux-research-and-usability-testing` (runs the card
  sort / tree test this skill specifies). Downstream: `03-layout-grid-and-composition/...` (lays out
  the pages the IA defines), `04-web-and-ui-design/empty-error-and-loading-states` (zero-results),
  `10-content-design-and-ux-writing/ux-writing-and-microcopy` (label tone).
- Standards (named for provenance, not in-repo): Rosenfeld/Morville/Arango, *Information
  Architecture* (the polar-bear book); Nielsen Norman Group IA & navigation guidance; W3C WAI-ARIA
  Authoring Practices (menu, menubar, disclosure, breadcrumb patterns).
<!-- dual-compat-end -->
