# Mobile Web Patterns

Parent skill: [`../SKILL.md`](../SKILL.md) (`responsive-and-adaptive-layout`).

**Load when:** a website or web app will be used mainly on phones in a browser (not a native app),
and the team must decide what the phone visitor sees first, how navigation, forms and fixed
actions behave, and how the page survives browser chrome, the on-screen keyboard and slow data.

Native iOS and Android conventions live in `07-mobile-ios-android-cross-platform`; gesture and
haptic detail in `touch-gesture-and-haptics`; navigation pattern choice in
`14-conversion-and-web-page-patterns/navigation-and-information-architecture`
(`nav-pattern-catalog.md`). This file covers the browser-specific layer between them.

---

## 1. Inputs

| Input | Source | If missing |
|---|---|---|
| Mobile job map: the three to five things phone visitors come to do | Analytics, search terms, staff interviews (method in `cross-platform-design-parity`) | Stop the first-screen decision; run five visitor interviews |
| Device and network reality (for example mid-range Android, prepaid mobile data) | Analytics or market data | Assume a mid-range Android on a slow connection and state the assumption |
| Contact channels the audience actually uses (calls, WhatsApp, SMS, USSD, email) | Client | Ask; do not default to a web form only |
| Content priority per page | `layout-grid-and-spacing` inventory | Derive from the job map and confirm |

## 2. Decision: one responsive site, or a different mobile experience

| Condition | Choose | Failure caused by the wrong choice |
|---|---|---|
| Phone and desktop visitors do the same jobs | One responsive site, re-composed per width | A separate mobile site duplicates content and drifts |
| Phone visitors do a narrower job (returning users who only log in, pay or check status) | Same URL, responsive, with a job-first mobile home that surfaces that job | Forcing the full marketing home on people who came to pay |
| The desktop interface is a dense tool that cannot become usable when stacked | A purpose-built mobile view of the top jobs, same URLs, with a route to the full tool | A shrunk desktop tool with unusable tables |
| Anyone proposes a separate `m.` domain | Reject; use responsive delivery on the same URLs | Split links, split search signals, stale duplicate content |

## 3. First-screen rule

On the smallest supported width, the first screen must show: what this is (one line), the primary
job's entry point, and a trust cue relevant to the job. Everything else is below or behind
navigation. Test by loading the page on a real phone and covering the bottom browser toolbar area:
if the primary action is not visible, the hero is too tall.

## 4. Pattern table

| Pattern | Use when | Rules | Anti-pattern |
|---|---|---|---|
| Menu disclosure (collapsed primary navigation) | More than four or five top-level items on a phone | A real button with a visible label (not a bare glyph), `aria-expanded`, Escape closes, focus returns to the button; the most-used destination can stay visible beside it | Icon-only toggle, focus lost behind the open panel |
| Priority-plus navigation | Four to eight items where the top two or three dominate | Show the items that fit, move the rest into "More" | Hiding every item including the one most visitors need |
| Bottom action bar (sticky) | One dominant action on long pages: call, WhatsApp, book, pay | One or two actions only, respects the safe area, does not cover form fields when the keyboard opens, hidden on pages where it competes with a form's own submit | A bar with five icons duplicating the header |
| Tap-to-contact links | Any business whose visitors call or message | `tel:` for calls, a WhatsApp click-to-chat link with a prefilled context message, `sms:` where SMS is common; show the number as text too so it can be copied | A contact form as the only route |
| Collapsible sections | Reference content visitors scan (FAQ, specifications, opening hours by branch) | Headings visible and descriptive; the most-needed section open by default; state preserved on back navigation | Collapsing the main content of the page |
| Horizontal scroller | A small set of peer items (categories, related products) | A visible partial next item as the scroll cue, scroll snap, and a "see all" route | Hiding primary navigation or long lists sideways |
| Full-height panel | Onboarding steps, media viewers | Size with `svh` so browser chrome never covers the controls (see `modern-css-capability-baseline.md`) | `100vh` with the action button under the toolbar |
| Data-light imagery | Visitors on metered data | Responsive sources with `sizes`, modern formats, lazy loading below the fold, reserved aspect ratio; decorative video off by default | A 4 MB hero photograph on the home page |

## 5. Forms on phones

- Use the input type and `inputmode` that summons the right keyboard (telephone, email, numeric,
  decimal) and `autocomplete` tokens so the browser can fill names, phone numbers and addresses.
- One column. Labels above fields and always visible; never placeholder-only labels.
- Phone numbers: accept the local format visitors actually type (for example `0772 123456`) and
  normalise to international format on the server; do not force `+256` entry.
- Place the submit action where the keyboard will not hide it; test with the keyboard open. The
  viewport meta `interactive-widget` key can change whether the keyboard resizes layout, but
  support varies by browser, so the form must work under the default behaviour.
- Mobile-money payment steps: show the amount, payee name and reference before the prompt goes to
  the phone, and state what the visitor will see on their handset.
- Full rules: `04-web-and-ui-design/form-ux-design`.

## 6. Browser-chrome and device constraints

- **Viewport meta:** `width=device-width, initial-scale=1`. Never disable zoom; add
  `viewport-fit=cover` only when the design deliberately extends under display cut-outs and then
  pads content with the `safe-area-inset-*` environment values.
- **No hover dependency.** Every hover reveal needs a visible, tappable equivalent. Use
  `@media (hover: hover)` to add hover styling, never to add function.
- **Target size.** WCAG 2.2 SC 2.5.8 sets a 24 by 24 CSS px minimum at level AA; platform
  guidance (Apple about 44 pt, Material 48 dp) is the premium target for primary controls. See
  `doctrine/references/wcag-2.2-criteria.md`.
- **Reflow.** Content must work at 320 CSS px wide without two-directional scrolling (WCAG 2.2 SC
  1.4.10), which is also the width produced by 400 percent zoom on a 1280 px window.
- **Reduced motion and data saving.** Honour `prefers-reduced-motion`; treat autoplaying media as
  opt-in.

## 7. Quality gate

- First-screen rule passes on the smallest supported width on a real device or is marked
  `NOT_ASSESSED`.
- Navigation disclosure passes keyboard and screen-reader checks.
- Sticky actions never cover focused fields or content at any tested width.
- Tap-to-contact routes work on a real handset (call, WhatsApp) or are marked `NOT_ASSESSED`.
- Page weight and Core Web Vitals checked against
  `doctrine/references/web-performance-budgets-2026.md` on a throttled mid-range profile.

## 8. Original worked example

A Gulu farm-inputs supplier's catalogue site: the mobile job map shows visitors check whether a
seed variety is in stock, ask the price on WhatsApp, and get directions. The phone home page leads
with a product search field and a category scroller, the product page shows stock status and
price per packet above the photograph, and a sticky bar holds "WhatsApp to order" (prefilled with
the product name) and "Call". The desktop layout adds a filter sidebar and a comparison table; the
phone layout replaces the table with one card per variety showing the three attributes farmers
compare first.

## Evidence and currentness

Accessed 2026-09-24: MDN viewport meta reference (zoom warning, `viewport-fit`,
`interactive-widget` support varies); W3C Understanding SC 1.4.10 Reflow; Baseline status for
viewport unit variants in `modern-css-capability-baseline.md`. Platform target sizes are carried
from the engine's WCAG and platform references and were not re-fetched here (`NOT_ASSESSED` for
this file). The separate-mobile-site guidance in older sources is superseded.

Sources: McNeil, P. (2013) *The Web Designer's Idea Book, Volume 3*, HOW Books (when a mobile job
differs from the desktop job); LaGrone, B. (2016) *Web Design Blueprints*, Packt (collapsing
navigation, fluid media; dated techniques replaced); Plumley, G. (2011) *Website Design and
Development*, Wiley (restyle versus reorganise for mobile); W3C WCAG 2.2; MDN.
