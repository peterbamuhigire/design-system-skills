# Worked Example — Sitemap & Navigation Specification

**Product:** *Tala Books* — a multi-tenant SMB accounting & invoicing SaaS (web app + responsive
mobile web), aimed at small-business owners and their bookkeepers in East Africa. Worked end-to-end
to show the full skill: inventory → grouping → scheme → sitemap → labels → nav regions (with states
and breakpoints) → search/filter → keyboard/ARIA contract.

This is a *task/app* product (a tool of verbs over a set of business objects), so the IA spine is
**task-based**, the big collections (invoices, transactions) are **faceted**, and **search** spans
both. Per doctrine Mission §0, the deliberate structural choice — a **persistent left sidebar**, not
a generic top bar — is the authored call: accounting is a deep, multi-section tool used in long
working sessions, where a stable rail and visible context beat a hamburger or a crowded top bar.

---

## 1. Content inventory (abridged)

Objects: Dashboard, Invoices, Bills, Customers, Vendors, Bank/Transactions, Chart of Accounts,
Reports (P&L, Balance Sheet, Cash Flow, Tax/VAT, Aged Receivables), Products & Services, Tax Settings,
Users & Roles, Company Profile, Integrations, Notifications, Help, Account/Billing (the SaaS
subscription itself).

**Audit of the legacy build (why we're redesigning):** 11 undifferentiated top-tab items; a "More"
tab holding Reports + Settings + Tax; "Settings" and "Setup" both existed (label overlap); Reports
buried at depth 4; no breadcrumb anywhere; active tab shown by colour only; no search.

---

## 2. Grouping (closed card sort, n=18: 12 owners, 6 bookkeepers)

Tasks clustered cleanly into five working areas plus utility. Strong agreement (>80%) on Sales,
Purchases, Banking, Reports; "Chart of Accounts" split between Banking and a new **Accounting** group
(bookkeepers filed it under Accounting, owners under Banking) → placed under **Accounting**, with a
cross-link from Banking. "Tax/VAT" sorted into both Reports (the return) and Settings (the rates) →
the *report* lives in Reports, the *rates* in Settings.

---

## 3. Organisation scheme & shape

- **Governing scheme:** task-based spine (Sales / Purchases / Banking / Accounting / Reports), the
  high-volume lists (Invoices, Transactions) are **faceted**, global **search** across all objects.
- **Shape decision:** **6 primary sidebar sections, max depth 3**, catalogue-style lists browsed by
  facets rather than a tree. Everything reachable in ≤3 clicks. Settings is utility, not primary.

---

## 4. Sitemap (with routes)

```
Dashboard                                   /
Sales                                       /sales
 ├─ Invoices            (faceted list)      /sales/invoices            → /sales/invoices/{id}
 ├─ Customers                               /sales/customers           → /sales/customers/{id}
 └─ Products & Services                     /sales/items
Purchases                                   /purchases
 ├─ Bills               (faceted list)      /purchases/bills           → /purchases/bills/{id}
 └─ Vendors                                 /purchases/vendors         → /purchases/vendors/{id}
Banking                                     /banking
 ├─ Accounts                                /banking/accounts
 ├─ Transactions        (faceted list)      /banking/transactions
 └─ Reconcile                               /banking/reconcile
Accounting                                  /accounting
 ├─ Chart of Accounts   (×-link from Banking) /accounting/chart-of-accounts
 └─ Journal Entries                         /accounting/journals
Reports                                     /reports
 ├─ Profit & Loss                           /reports/profit-loss
 ├─ Balance Sheet                           /reports/balance-sheet
 ├─ Cash Flow                               /reports/cash-flow
 ├─ Aged Receivables                        /reports/aged-receivables
 └─ Tax / VAT Return                        /reports/tax-return

Utility (top bar, not primary):  Search · Notifications · Help · {Company switcher} · {Account ▾}
Account menu:  Company Profile /settings/company · Tax Settings /settings/tax ·
               Users & Roles /settings/users · Integrations /settings/integrations ·
               Billing & Plan /settings/billing · Sign out
```

URLs mirror the IA (readable, hierarchical, stable). Each list deep-links to its record.

---

## 5. Label system (taxonomy)

| Label | Denotes (must hold) | Why this word |
|---|---|---|
| Sales | Everything you bill *out* | User vocabulary; "Sales" beat "Income/Receivables" in the sort |
| Purchases | Everything you're billed *for* | Parallel to Sales (both plural nouns) |
| Banking | Bank accounts, feed, reconciliation | Owners' word; not "Cash management" (jargon) |
| Accounting | Ledger-level: CoA, journals | Bookkeepers' word; segregates "deep" tools from daily |
| Reports | Generated statements & the tax return | Distinct from Settings; the *output* |
| Customers / Vendors | People you sell to / buy from | Not "Contacts" (too vague, overlapped) |

Rules held: all primary labels are **parallel** (plural nouns), **distinct** (no two hold the same
object), **specific** (no "More/Other/Misc" — the legacy "More" tab is deleted; its contents went to
Reports and the Account menu). "Settings" vs "Setup" overlap resolved: one **Account menu**, no
"Setup."

---

## 6. Navigation regions — specification

### 6.1 Primary — left sidebar (desktop ≥1024px)
- **Pattern:** persistent vertical sidebar, 240px, sections as a single flat list of 6 + Dashboard;
  each section expands inline to its children (disclosure), one open at a time.
- **Item:** 16px icon + label, 40px row height (≥24px target ✔, comfortably ≥44px touch ✔).
- **Active state:** filled brand-tint background **+** a 3px leading indicator bar **+** label weight
  600 — three signals, never colour alone. Programmatic: `aria-current="page"` on the active leaf.
- **Collapsed rail:** user can collapse to a 64px icon-only rail; labels appear on hover and on
  focus (tooltip with accessible name).

### 6.2 Utility — top bar
- Right cluster: global **Search**, Notifications (badge), Help, **Company switcher** (multi-tenant),
  **Account ▾** disclosure menu. Visually subordinate (smaller, top-right). Icon-only items carry
  accessible names. Company switcher is a `combobox`/menu, announces current company.

### 6.3 Local nav
- Inside a record (e.g. an Invoice), **tabs** for views of *that object*: Details · Activity ·
  Payments. Tabs = same object, different facet — not cross-section nav. `role="tablist"`, roving
  tabindex, `aria-selected`.

### 6.4 Breadcrumbs (wayfinding)
- Shown on every page ≥3 levels deep (records, reports):
  `Dashboard › Sales › Invoices › INV-2041`. Wrapped in `<nav aria-label="Breadcrumb">`, ordered
  list, **current crumb is text (not a link)** with `aria-current="page"`. It is an up-the-tree
  control, not a back button.

### 6.5 Footer
- Thin: Help Center · Status · Privacy · Terms · © Tala Books. Not a primary-nav substitute.

---

## 7. Responsive collapse rules

| Region | ≥1024px (desktop) | 640–1023px (tablet) | <640px (mobile) |
|---|---|---|---|
| Primary | Full 240px sidebar | Collapsed 64px **rail** | **Bottom bar**: Dashboard · Sales · Banking · Reports · **More** (drawer holds Purchases, Accounting + Account menu) |
| Utility | Full top-right cluster | Condense to icons | Search + Notifications icons in top bar; rest in **More** drawer |
| Local (tabs) | Inline tab row | Inline tab row | Horizontally scrollable tab row |
| Breadcrumb | Full path | Full path | Truncated: `… › Invoices › INV-2041` (parent + current) |

No region vanishes without a replacement — bottom bar + "More" drawer covers every primary item, so
no section becomes an orphan on mobile.

---

## 8. Search & filtering spec

- **Scope:** global search (top bar) across customers, vendors, invoices, bills, transactions,
  reports, and help. In-list search inside each faceted list, scope shown and switchable.
- **Autosuggest:** as-you-type, grouped by object type ("Customers", "Invoices"…), top 5 each, with
  the matched field shown; Enter on a suggestion deep-links; Enter on the query opens full results.
- **Faceted lists** (Invoices, Bills, Transactions): facets mirror the taxonomy/object fields —
  Status (Draft/Sent/Paid/Overdue), Customer, Date range, Amount range, Tax rate. Facets are
  additive, current filters shown as removable chips (attribute-breadcrumb style), URL-encoded so a
  filtered view is shareable/bookmarkable.
- **Zero-results (designed, not a dead end):** "No invoices match *overdue + last 7 days*." +
  one-tap **clear filters**, a **broaden** suggestion (drop the narrowest facet), and a **create
  invoice** action. Pairs with `04-web-and-ui-design/empty-error-and-loading-states`.

---

## 9. Keyboard & ARIA contract (gate — `doctrine/references/wcag-2.2-criteria.md`)

- **Skip link** "Skip to main content" is the first focusable element, visible on focus. (2.4.1)
- **Landmarks:** `<nav aria-label="Primary">` (sidebar), `<nav aria-label="Utility">` (top bar),
  `<nav aria-label="Breadcrumb">`, `<main>` for content. (1.3.1)
- **Focus order** matches visual order: skip-link → utility → sidebar → main. Visible high-contrast
  focus ring on every item. Sticky top bar uses scroll-padding so it never obscures a focused sidebar
  item. (2.1.1, 2.4.3, 2.4.7, 2.4.11)
- **Sidebar disclosure groups:** trigger exposes `aria-expanded`; Enter/Space toggles; Arrow Up/Down
  move between items; Escape collapses an open group. (4.1.2, W3C APG disclosure)
- **Account menu & company switcher:** `aria-haspopup` + `aria-expanded`; Escape closes and returns
  focus to the trigger; arrow-key navigation within. (APG menu)
- **Record tabs:** `role="tablist"`/`tab`/`tabpanel`, roving tabindex, `aria-selected`. (APG tabs)
- **Active item:** `aria-current="page"` on the current sidebar leaf and breadcrumb tail. (4.1.2)
- **Targets:** all nav rows/icons ≥24×24px (sidebar 40px, bottom-bar 56px — both ≥44px touch). (2.5.8)
- **Icon-only controls** (rail icons, hamburger/More, search, notifications) all have accessible
  names. (4.1.2)
- **Testing:** axe + Lighthouse, **then** a manual keyboard traversal of the entire nav (sidebar,
  menus, tabs, breadcrumb, bottom bar + drawer) and an NVDA/VoiceOver smoke test.

---

## 10. Why this is the authored choice (anti-slop note)

The default SaaS template would have shipped a top bar with a logo, 5–6 links, and a ghost-button
CTA — convergent and wrong for a deep accounting tool. The deliberate calls here: a **persistent
left rail** (long working sessions, many sections, stable context), **task-based** primary labels in
the *users'* words (validated by card sort, not the org chart), **faceted** high-volume lists with
shareable URLs, and a **bottom-bar + More** mobile model that orphans nothing. Each is a defensible
structural decision stated before build, per doctrine Mission §0 and Anti-Slop Charter §2.
