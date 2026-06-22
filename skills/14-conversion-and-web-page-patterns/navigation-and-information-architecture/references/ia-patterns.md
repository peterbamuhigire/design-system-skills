# Reference: Information Architecture Patterns

The structural rules for organising content so people can find it. Provenance: Rosenfeld, Morville
& Arango, *Information Architecture for the Web and Beyond* (4th ed., the "polar-bear book");
Nielsen Norman Group IA research; Donna Spencer, *A Practical Guide to Information Architecture* and
*Card Sorting*. Aligned to the Chwezi design doctrine (Mission §0, Anti-Slop Charter §2) and the
WCAG 2.2 floor (`doctrine/references/wcag-2.2-criteria.md`).

IA is the *invisible* design discipline: when it's right, no one notices; when it's wrong, every
page feels hard and search is the only escape. It decides **structure before pixels** — get it
wrong and no amount of visual polish on the nav bar saves it.

---

## 1. The four anatomy parts of IA

Per Rosenfeld/Morville/Arango, every IA is built from four interlocking systems:

| System | What it does | Owned where |
|---|---|---|
| **Organisation systems** | How content is grouped and structured (the scheme + the hierarchy) | §2–4 here |
| **Labelling systems** | What each group/item is *called* (the taxonomy) | §5 here |
| **Navigation systems** | How users *move* through the structure | `nav-pattern-catalog.md` |
| **Searching systems** | How users *query* the structure when browsing won't scale | §8 here |

This skill owns all four; navigation gets its own catalogue because it's the largest.

---

## 2. Organisation schemes — pick one to govern, then hybridise

**Exact (unambiguous) schemes** — there's one right bucket for each item:
- **Alphabetical** — directories, glossaries, A–Z indexes. Good only when users know the term.
- **Chronological** — news, releases, changelogs, history.
- **Geographical** — by place. Stores, regions, offices.

**Ambiguous (subjective) schemes** — the useful, hard ones, where grouping is a judgement:
- **Topical / hierarchical** — by subject. *The default for most content sites.* The whole design
  problem is defining the topics so they match user mental models.
- **Task-based** — by what the user is doing ("Send money", "File a return"). Best for tools/apps
  where the product is a set of verbs, not a library of nouns.
- **Audience-based** — by who the user is ("For Patients" / "For Clinicians"). Powerful *only* when
  audiences need genuinely disjoint content; it costs a self-identification step and duplicates
  shared content, so use sparingly and never as the *only* spine.
- **Faceted / database** — items described by multiple independent attributes (price, brand, colour,
  size) that users combine via filters. The right model for catalogues, listings, large datasets —
  there is no single tree, so don't force one.

**Reality:** most products are a **hybrid** — a topical/task spine for primary nav, a faceted browse
for the big collection, and search across everything. State which scheme *governs* and why; a
muddled mix of schemes inside one level is itself a smell (the "mixing chronological with topical
with audience in one menu" failure).

---

## 3. Mental-model grouping (the core move)

Group items by **how users think things relate**, in **the users' own words** — never by the
internal org chart. "Our Divisions / Departments / Business Units" as a top level is the single most
common, most damaging IA failure: it makes users learn your structure to find their goal.

To discover the grouping, **card sort**:
- **Open card sort** — give users the items, let them form *and name* their own groups. Use when you
  don't yet know the categories. Reveals the user's mental model and vocabulary.
- **Closed card sort** — give users the items *and* your proposed categories; they file items. Use
  to validate or refine a proposed scheme.
- 15–20 participants per audience surfaces the major patterns; look for items that everyone groups
  together (strong signal) vs. items that scatter (ambiguous — needs a clearer label or to live in
  two places via cross-linking).

---

## 4. Depth vs. breadth — the click-economy

- **Favour breadth over depth** for findable content. Shallow, wide trees outperform deep, narrow
  ones: each extra *level* of depth sheds users who must guess correctly to descend.
- Target: most content reachable in **≤3 clicks** from home. Flag anything at **depth ≥4** for
  promotion, cross-linking, or a search-first path.
- But don't over-flatten the *top* level: a primary bar holds about **7±2** comfortable items.
  Past that, the answer is a **mega-menu** (reveals a wide second level) or a **sidebar** — *not*
  twelve cramped top links and *not* burying everything under "More".
- Depth and breadth genuinely trade off. Decide the shape on purpose (and write it in the spec):
  e.g. "6 primary sections, max depth 3, catalogue browsed by facets not tree."

---

## 5. Labelling — the taxonomy is design, not copy garnish

A label is the contract between the user's intent and your structure. The label system must be:

- **Distinct** — no two labels could plausibly hold the same item. Overlap ("Products" vs
  "Solutions" vs "Services") forces users to guess and is the #1 cause of "I clicked the wrong one."
- **Specific** — avoid empty catch-alls ("Resources", "Solutions", "Information") unless the scope is
  genuinely that and nothing better exists. **"Other / More / Misc"** is never a category — it's the
  visible symptom of a taxonomy that failed to classify its own contents.
- **Parallel** — one grammatical form per level (all nouns, or all verb phrases — not a mix).
- **In the users' vocabulary** — match the words real users used in the card sort / search logs, not
  internal jargon or brand-speak.
- **Stable & scannable** — front-load the distinguishing word ("Tax filing", "Tax history"), keep to
  1–2 words where possible, and don't rename established labels casually (it breaks learned paths).

The denotation (what each label *must* mean) is owned here; tone/voice is reconciled with
`10-content-design-and-ux-writing/ux-writing-and-microcopy`.

---

## 6. The sitemap & URL hierarchy

- The **sitemap** is the canonical tree: every node, its parent, and its route/URL path. It is the
  artifact engineering builds from and the thing you tree-test.
- **URLs should mirror the IA** — readable, hierarchical, stable (`/billing/invoices/{id}`, not
  `/p?id=738`). The URL is wayfinding too: a user who reads it should know where they are.
- One canonical home per item. If an item legitimately belongs in two places, pick one canonical
  location and **cross-link** from the other — don't duplicate the page (splits authority and rots).

---

## 7. Validating the IA — tree testing

Card sort builds the structure; **tree test** (a.k.a. reverse card sort) checks it. Give users the
*bare* hierarchy (labels only, no visual design, no search) and real find-tasks ("Where would you go
to change your billing address?"). Measure **success rate** (found the right node), **directness**
(no backtracking), and **time**. It isolates the *structure and labels* from the visual design —
a low success rate here means the IA is wrong, not the UI. Run it before you design pages.

---

## 8. Search as the complementary findability path

Browsing (the tree) and searching (the query) are complements, not alternatives — provide both for
any non-trivial inventory. Search-relevant decisions:

- **Scope** — global vs in-section search; if both, make the current scope obvious and switchable.
- **Autosuggest / autocomplete** — surface matches and popular queries as the user types; reduces
  typos and reveals vocabulary.
- **Query persistence** — keep the query in the box on the results page; let users refine, not retype.
- **Faceted results** — for catalogues, results filter by facets that mirror the taxonomy (§2).
- **Zero-results is a designed state, never a dead end** — acknowledge, suggest corrected/related
  queries, offer to broaden scope, and give an escape (browse links, contact). Pairs with
  `04-web-and-ui-design/empty-error-and-loading-states`.

---

## 9. The IA audit checklist (for an existing product)

Run before any redesign. Each "yes" in the right column is a defect to fix.

| Check | Smell if… |
|---|---|
| Top-level count | > ~9 undifferentiated primary items with no mega-menu/sidebar |
| Max depth | content at depth ≥4 with no search/cross-link path |
| Dumping ground | an "Other / More / Misc / Resources" catch-all exists |
| Label overlap | two items could each hold the same page |
| Org-chart mirroring | top level reads as departments, not user tasks |
| Orphan pages | pages with no nav path in (only reachable by direct URL/search) |
| Active state | you can't tell which section you're in from the nav |
| Breadcrumbs | deep pages (≥3 levels) have no up-the-tree orientation |
| Search | large inventory with no search, or a dead-end zero-results page |
| Mobile | primary nav vanishes behind a hamburger even where room exists |
| Keyboard / SR | menus open on hover only, trap focus, no Escape, no `aria-current` |

---

## 10. Accessibility & anti-slop ties

- IA failures are accessibility failures first: screen-reader and keyboard users feel a deep,
  mislabeled tree far more acutely than sighted mouse users. Logical structure, parallel labels,
  landmark regions, and `aria-current` are IA deliverables, not afterthoughts — see
  `doctrine/references/wcag-2.2-criteria.md` and the keyboard/ARIA contract in `nav-pattern-catalog.md`.
- Per doctrine Mission §0: the navigation bar is the most template-converged surface on the web
  (logo-left, 5 links, ghost CTA). A *defensible* structural choice — a left rail for a deep tool,
  a clearly-organised mega-menu for a broad catalogue — is itself the authored, anti-slop move.
  State the structural choice and its rationale before building (Anti-Slop Charter §2).
