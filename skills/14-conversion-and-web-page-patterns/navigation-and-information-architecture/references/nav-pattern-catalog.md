# Reference: Navigation Pattern Catalog

The navigation pattern library — when to use each, its responsive transform, and its keyboard/ARIA
contract. Provenance: Nielsen Norman Group navigation research; W3C **WAI-ARIA Authoring Practices
Guide (APG)** patterns (menu, menubar, disclosure, breadcrumb, tabs); Material 3 and Apple HIG
navigation guidance (for idioms, not as design *authority* per doctrine §2). Every pattern's
contract is gated by `doctrine/references/wcag-2.2-criteria.md`.

A navigation system is usually **several patterns layered**: a *primary* region, a *local/in-section*
region, *utility* nav, *breadcrumbs*, and a *footer*. Pick each region's pattern by the structure's
shape — not by what's fashionable. The nav is the most template-converged surface on the web; an
authored structural choice is the doctrine's anti-slop move (Mission §0).

---

## 1. Primary navigation patterns

### Top horizontal bar
- **Use when:** a content/marketing site or a shallow app with **≤7±2** primary sections.
- **Strengths:** instantly visible, conventional, low cognitive cost. **Limits:** runs out of room
  past ~7 items; can't express a deep tree on its own.
- **Mobile transform:** collapse to a **hamburger drawer** (off-canvas) or, for a focused app with
  3–5 destinations, a **bottom bar**.

### Mega-menu
- **Use when:** a **broad** structure — many sections each with many children (e-commerce,
  enterprise, large docs). Reveals a wide, *organised* second level in one panel.
- **Strengths:** surfaces breadth without deep clicking; can group + show structure visually.
  **Limits:** demands disciplined grouping/labels; a common keyboard/SR failure point (see §6).
- **Rule:** open on click/Enter (not hover-only), with grouped columns and parallel labels.

### Sidebar / nav rail (vertical)
- **Use when:** a **deep tool/app** with many sections and persistent context (dashboards, admin,
  SaaS, docs). Scales to more items than a top bar and supports nested/collapsible groups.
- **Variants:** full sidebar (label + icon), collapsed **rail** (icon-only, label on hover/expand).
- **Mobile transform:** off-canvas drawer, or a bottom bar for the top 3–5 destinations + "More".

### Tabs
- **Use when:** switching **views of the same object/context** (a record's Overview / Activity /
  Settings) — *not* for navigating between unrelated sections. Tabs imply "same place, different
  facet." Keep to a single row; if they wrap, it's not a tab set.

### Hamburger / drawer
- **Use when:** *mobile* primary nav, or a genuinely secondary desktop menu. **Do NOT** hide primary
  desktop nav behind a hamburger where there's room — it tanks discoverability (NN/g). The icon
  needs an accessible name ("Menu") and exposed expanded/collapsed state.

### Bottom navigation bar (mobile)
- **Use when:** a mobile app with **3–5 top-level, equally-important** destinations reachable from
  anywhere. Always-visible, thumb-reachable. Not for >5 items and not for hierarchical drill-down.

---

## 2. Supporting navigation regions

- **Local / in-section nav** — a secondary menu *within* a section (left list in docs, sub-tabs on a
  settings page). Lets users move among siblings without returning to the top.
- **Utility nav** — account, search, notifications, language, help. Visually subordinate to primary
  nav (smaller, often top-right). Don't mix utility items into the primary content nav.
- **Footer nav** — the "fat footer": secondary/long-tail links, legal, sitemap-in-miniature, contact.
  A findability safety net, not a substitute for primary nav.

---

## 3. Breadcrumbs (wayfinding)

- **Use when:** any hierarchy **≥3 levels deep**. They answer "where am I" and give an **up-the-tree
  control** — they are *not* a back button (back = browser history; breadcrumb = parent path).
- **Form:** `Home › Section › Subsection › Current` — the current page is the **last crumb, not a
  link**. Separators are decorative (hide from SR).
- **Variants:** *location* breadcrumbs (position in the tree — most common) vs *attribute*
  breadcrumbs (selected facets, e-commerce). Don't conflate.
- **ARIA:** wrap in `<nav aria-label="Breadcrumb">`, an ordered list, current crumb marked
  `aria-current="page"`.

---

## 4. Active / current-state (the "you are here")

Every navigation system **must** mark the user's current location:
- **Visually** — and never by colour alone (doctrine + WCAG 1.4.1): use weight, an indicator
  bar/underline, a filled background, *plus* colour.
- **Programmatically** — the current item carries `aria-current="page"` (or `="true"`/`="step"` for
  tabs/wizards) so screen readers announce it. Missing active state is a top IA defect.

---

## 5. Responsive collapse rules (state them per region)

Write, per breakpoint, exactly what each region does:

| Region | Desktop (≥ lg) | Tablet (md) | Mobile (< sm) |
|---|---|---|---|
| Primary | Top bar / mega / sidebar | May condense | Hamburger drawer or bottom bar |
| Local | Inline sub-nav | Inline or collapsible | Collapsible accordion / select |
| Utility | Top-right cluster | Condense to icons | Inside drawer or icon row |
| Breadcrumb | Full path | Full path | Truncate middle (`Home › … › Current`) or show parent only |

Never let a region simply *vanish* on mobile with no replacement — that's how items become orphans.

---

## 6. Keyboard & ARIA contract (the gate, per `wcag-2.2-criteria.md`)

Nav is the most-traversed, most keyboard-dependent surface — these are pass/fail, not polish.

- **Skip link** — a "Skip to main content" link is the **first focusable element**, visible on focus
  (lets keyboard/SR users bypass the nav). (2.4.1)
- **Landmarks** — primary nav in `<nav aria-label="Primary">`; multiple navs each get a distinct
  `aria-label`. Main content in `<main>`. (1.3.1)
- **Keyboard operable, logical order** — every item reachable and activatable by keyboard, focus
  order matches visual order. (2.1.1, 2.4.3)
- **Visible focus** — a clear, high-contrast focus indicator on every item; never `outline:none`
  without a stronger replacement. (2.4.7)
- **Focus not obscured** — a sticky header must not hide the focused nav item (scroll-padding /
  offset). (2.4.11)
- **Menus / mega-menus / dropdowns** — open on click/Enter/Space (not hover-only); Arrow keys move
  within; **Escape closes** and returns focus to the trigger; the trigger exposes
  `aria-expanded` and `aria-haspopup`; the popup has the right role (`menu`/`true` group). This is
  the #1 nav accessibility defect — get it right. (4.1.2; W3C APG menu/disclosure patterns)
- **Tabs** — `role="tablist"`/`tab`/`tabpanel`, Arrow-key roving tabindex, `aria-selected`. (APG)
- **Current item** — `aria-current="page"`. (4.1.2)
- **Target size** — pointer targets ≥ **24×24 CSS px**; aim 44×44 (touch). (2.5.8)
- **Names** — icon-only items (hamburger, rail icons, search) have an accessible name. (4.1.2)
- **Testing** — automated (axe/Lighthouse) plus **manual keyboard traversal** of the entire nav and
  a **screen-reader smoke test** (NVDA/VoiceOver). Per WebAIM, navigation menus are among the most
  common failure sites — passing this is a real differentiator.

---

## 7. Pattern-selection quick guide

| Structure shape | Primary pattern | Plus |
|---|---|---|
| Shallow marketing/content site, ≤7 sections | Top bar | Footer nav, breadcrumbs if ≥3 deep |
| Broad catalogue/enterprise, many×many | Mega-menu **+** faceted browse | Search-first, breadcrumbs |
| Deep tool / SaaS / admin / docs | Sidebar or rail | Local sub-nav, breadcrumbs, utility bar |
| Object with multiple views | Tabs (within the object) | Breadcrumb to the object |
| Focused mobile app, 3–5 destinations | Bottom bar | Drawer for overflow ("More") |
