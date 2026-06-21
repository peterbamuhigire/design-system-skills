# Worked Product Design Audit — "Tenda Books"

> A fully worked, product-level, multi-platform audit produced by the `product-design-audit`
> skill. The product is real-ish (not a real company): **Tenda Books**, a small-business
> invoicing + bookkeeping tool used by East-African traders and SMEs. It ships **three** surfaces:
> a marketing **website**, a **SaaS web app**, and an **iOS app** (iPhone + iPad). No banned
> fonts appear in any recommendation; thresholds and skill names are concrete.

---

## Header

- **Product:** Tenda Books — invoicing & bookkeeping for SMEs
- **Surfaces in scope:** Marketing website (`tendabooks.example`) · SaaS web app (`app.tendabooks.example`) · iOS app (iPhone 15, iPad Air, iPadOS 18)
- **Users / JTBD:** Non-accountant shop owners and freelancers; "send a professional invoice in under a minute," "see who owes me," "know my month." Mixed device literacy; many mid-range Android *and* iPhone; metered data common.
- **Brand personality:** Trustworthy, calm, locally credible — "your books, sorted." Not playful, not clinical.
- **Design system in place:** Partial — a Tailwind config with ad-hoc values; no token names; iOS app built in SwiftUI separately with its own colours.
- **Stated type/colour choice on file?** **No.** (First slop finding — see Gate 1.)
- **Evidence basis:** Live website + staging web app walked through invoice-create, client-list, dashboard, settings, auth; iOS TestFlight build walked through onboarding, invoice-create, dashboard. CrUX p75 available for the website; web-app measured via RUM sample (labelled lower-confidence). Desktop and Android apps **not in scope** (product does not ship them).
- **Date / auditor:** 2026-06-21 / Codex (AI-assisted), `product-design-audit`.

---

## Product-wide AI-Slop Verdict: **FAIL** (caps the website + web app)

Run first, product-wide, via `visual-product-slop-audit` + `ai-slop-typography-audit`:

- **Typography:** Website and web app both render in **Inter** as the primary face — the single
  strongest AI tell (`ai-slop-banned-fonts.md` §1, `[AI]`). No type choice was ever stated
  (violates the Mission's "state the choice first"). → **Slop gate FAIL** on web surfaces.
- **Palette:** Website hero is a **blue→purple gradient** with white centred card — a convergent
  tell (`ai-slop-taxonomy.md`). Web-app accent is a near-cyan on dark grey.
- **iOS app:** Uses **SF Pro** (the platform face — *not* a banned default; correct) and a
  system-derived palette. **Slop gate PASS** on iOS.

The slop gate is binary and product-wide: the **website and web app are capped at ≤ 59** until
the banned font + stated-choice issues are fixed (`recommendation-format.md` §2). The iOS surface
is not capped by slop.

---

## Per-Surface Scorecards

### Surface 1 — Marketing Website

```
Gates:  AI Slop [FAIL — Inter primary, unstated, purple-gradient hero]
        A11y WCAG 2.2 AA [FAIL — hero CTA 2.8:1]
        Perf [FAIL — field p75 LCP 3.9s]
Caps applied: ≤59 (slop) AND ≤59 (a11y) AND ≤74 (perf) → effective cap ≤59
```

| # | Dimension | Wt | Score 0–4 | Weighted | Note |
|---|---|---|---|---|---|
| 3 | Accessibility | 20% | 1 | 5.0 | Hero CTA `#7C8CF8` on white = **2.8:1** (fail 1.4.3); skip-link missing; focus ring removed on nav |
| 2 | Visual Hierarchy | 15% | 2 | 7.5 | Hero competes with three equal cards; no single focal point |
| 7 | Interaction States | 12% | 2 | 6.0 | Nav links have hover but no visible `focus-visible`; pricing toggle no active state |
| 9 | Content & Microcopy | 12% | 2 | 6.0 | "Submit" on the newsletter; "Learn more" links ×4; otherwise readable |
| 4 | Typography | 10% | 1 | 2.5 | **Inter** primary (banned); single weight; centred long paragraphs |
| 5 | Colour | 8% | 1 | 2.0 | Purple gradient + cyan; pure `#FFF`/`#000`; no token system; contrast fails |
| 6 | Layout & Responsive | 8% | 2 | 4.0 | Breaks to 2-col oddly at 480px; container width unconstrained (measure ~120ch) |
| 10 | Performance | 6% | 1 | 1.5 | p75 **LCP 3.9s** (hero JPG 1.4 MB, not next-gen, no dims → CLS 0.18) |
| 8 | Motion | 5% | 3 | 3.75 | Restrained; fades only; reduced-motion respected |
| 1 | AI Slop | 4% | 0 | 0 | Gate FAIL |
| | **RAW TOTAL** | 100% | | **38.25** | |
| | **AFTER CAPS** | | | **38/100** | Cap ≤59 not binding — raw already below |
| | IA/Nav | — | 3 | — | Simple, learnable nav |
| | Trust | — | 2 | — | Testimonials present but no attribution; pricing CTA vague ("Get started") |

**Band: Fundamental (< 40).** The web font + contrast + LCP failures stack; this surface needs
structural work, not polish.

### Surface 2 — SaaS Web App

```
Gates:  AI Slop [FAIL — Inter primary, unstated]
        A11y WCAG 2.2 AA [FAIL — table row contrast 3.9:1; redundant entry in invoice flow]
        Perf [PASS — RUM p75 LCP 2.1s, INP 180ms, CLS 0.05 (lower-confidence sample)]
Caps applied: ≤59 (slop), ≤59 (a11y) → effective cap ≤59
```

| # | Dimension | Wt | Score 0–4 | Weighted | Note |
|---|---|---|---|---|---|
| 3 | Accessibility | 20% | 1 | 5.0 | Table secondary text `#8A8A8A` on `#F5F5F5` = **3.9:1** (fail 1.4.3); invoice flow re-asks the client's address already entered (fail 3.3.7 Redundant Entry); modal does not return focus on close |
| 2 | Visual Hierarchy | 15% | 3 | 11.25 | Dashboard KPI cards clear; primary action ("New invoice") prominent |
| 7 | Interaction States | 12% | 2 | 6.0 | Loading is a blank flash, not a skeleton; save has no success toast; disabled buttons unexplained |
| 9 | Content & Microcopy | 12% | 2 | 6.0 | Error on failed save reads "Error 500"; empty client list is a blank table |
| 4 | Typography | 10% | 1 | 2.5 | **Inter**; tabular figures **not** enabled on money columns (digits jitter) |
| 5 | Colour | 8% | 2 | 4.0 | Near-cyan accent doubles as both link and "success"; no semantic separation |
| 6 | Layout & Responsive | 8% | 3 | 6.0 | Good density; sidebar collapses sanely; table sticky header present |
| 10 | Performance | 6% | 3 | 4.5 | Within budget on the sampled flows |
| 8 | Motion | 5% | 3 | 3.75 | Reasonable; reduced-motion respected |
| 1 | AI Slop | 4% | 0 | 0 | Gate FAIL |
| | **RAW TOTAL** | 100% | | **49.0** | |
| | **AFTER CAPS** | | | **49/100** | Cap ≤59 not binding — raw already below |
| | IA/Nav | — | 3 | — | Clear shell; current location obvious |
| | Trust | — | 3 | — | Honest, but "Error 500" erodes confidence at the worst moment |

**Band: Major redesign (40–59).** Strong bones (hierarchy, IA, density) dragged below 50 by the
slop + a11y gate failures and weak states/content.

### Surface 3 — iOS App (iPhone + iPad)

```
Gates:  AI Slop [PASS — SF Pro, system palette, no tells]
        A11y WCAG 2.2 AA [PASS with one High finding — Dynamic Type clipping at AX5]
        Perf [PASS — cold-start ~0.9s, no scroll jank on iPhone 15]
Caps applied: none
```

| # | Dimension | Wt | Score 0–4 | Weighted | Note |
|---|---|---|---|---|---|
| 3 | Accessibility | 20% | 3 | 15.0 | VoiceOver labels present; **but** invoice-total label clips at AX5 Dynamic Type (High, not a gate fail) |
| 2 | Visual Hierarchy | 15% | 3 | 11.25 | Clear; large-title nav used well |
| 7 | Interaction States | 12% | 3 | 9.0 | Native states good; pull-to-refresh has haptic |
| 9 | Content & Microcopy | 12% | 3 | 9.0 | Mostly verb+noun; one "OK" alert |
| 4 | Typography | 10% | 3 | 7.5 | SF Pro + Dynamic Type; correct (not a banned face) |
| 5 | Colour | 8% | 3 | 6.0 | System semantic colours; good dark mode |
| 6 | Layout & Responsive | 8% | 2 | 4.0 | **iPad runs the iPhone layout stretched** — no split view, no multitasking adaptation (lens C finding) |
| 10 | Performance | 6% | 4 | 6.0 | Fast cold-start, 60fps |
| 8 | Motion | 5% | 3 | 3.75 | System transitions; Reduce Motion respected |
| 1 | AI Slop | 4% | 4 | 4.0 | Distinctive-enough, native, stated-by-platform |
| | **RAW TOTAL** | 100% | | **85.5** | |
| | **AFTER CAPS** | | | **86/100** | No cap |
| | IA/Nav | — | 3 | — | Tab bar idiomatic |
| | Trust | — | 3 | — | Feels native and safe |

**Band: Good foundation (75–89).** The strongest surface; main debts are iPad adaptation and one
Dynamic-Type clip.

---

## Cross-Platform Parity Note (→ `cross-platform-design-parity`)

- **Terminology drift:** the web app says **"Clients"**; the iOS app says **"Customers"** for the
  same entity. → finding, route `cross-platform-design-parity`.
- **Brand colour mismatch:** web accent (near-cyan) vs iOS accent (system blue) — same product,
  two identities. The fix is a shared colour intent (not pixel-identical), → `color-system-and-palette`
  + `cross-platform-design-parity`.
- **Good parity:** the invoice-create *flow order* is consistent across web and iOS — keep it.

---

## Prioritized, Skill-Routed Recommendations

| # | Pri | Surface | Dimension | Sev | Finding (evidence) | Standard | Fix | → Skill |
|---|-----|---------|-----------|-----|--------------------|----------|-----|---------|
| 1 | **P0** | Web site + app | Typography / Slop | Critical | **Inter** is the primary face on both web surfaces; no type choice ever stated | `ai-slop-banned-fonts.md` §1; Mission | Choose + **state** a real pair from `font-groups-and-usage.md` cat-03 (e.g. Bricolage Grotesque → Hanken Grotesk for product) or cat-05 for the friendly SME voice; remove Inter | `font-selection-and-pairing` (+ `ai-slop-typography-audit`) |
| 2 | **P0** | Website | Accessibility | Critical | Hero CTA `#7C8CF8` on white = **2.8:1** | WCAG 1.4.3 (≥4.5:1) | Darken CTA / pair text-on-fill to ≥4.5:1; restore focus ring | `accessible-color-and-contrast` |
| 3 | **P0** | Web app | Accessibility | Critical | Table secondary text **3.9:1**; invoice flow re-asks already-entered address; modal loses focus | WCAG 1.4.3, **3.3.7 Redundant Entry**, 2.4.3 | Raise contrast to ≥4.5:1; auto-fill prior entry; return focus on modal close | `accessible-color-and-contrast`, `accessibility-wcag-2-2-compliance` |
| 4 | **P0** | Website | Performance | Critical | field p75 **LCP 3.9s**, CLS 0.18 (1.4 MB JPG hero, no dims) | `web-performance-budgets-2026.md` (LCP ≤2.5s, CLS ≤0.1) | AVIF/WebP + `srcset` + explicit dimensions + preload LCP image | `performance-as-ux-and-core-web-vitals` |
| 5 | **P1** | Web app | Interaction States / Content | High | Blank loading flash; no success toast; **"Error 500"** shown to users; empty client list is blank | states completeness; UX-writing | Skeletons; success confirmation; error = what+why+how; empty-state with first-invoice CTA | `empty-error-and-loading-states`, `error-empty-and-system-messaging` |
| 6 | **P1** | iOS (iPad) | Layout / Platform | High | iPad runs **stretched iPhone layout** — no split view / multitasking adaptation | HIG (iPad multitasking) | Add split-view/list-detail, support arbitrary window sizes | `ios-ui-ux-design`, `responsive-and-adaptive-layout` |
| 7 | **P1** | Website | Colour / Slop | High | Purple gradient hero + cyan; pure `#FFF`/`#000`; no tokens | `ai-slop-taxonomy.md`; colour system | Replace with a tinted, tokenised palette (60-30-10); kill the gradient | `color-system-and-palette`, `distinctive-by-design` |
| 8 | **P1** | All | Parity | High | "Clients" (web) vs "Customers" (iOS); two accent identities | parity | Unify terminology + shared colour intent across surfaces | `cross-platform-design-parity` |
| 9 | **P2** | Web app | Typography | Medium | Money columns lack tabular figures (digits jitter) | type/data | Enable `font-variant-numeric: tabular-nums` on numeric columns | `dashboard-and-data-product-design` |
| 10 | **P2** | iOS | Accessibility | Medium | Invoice-total label clips at AX5 Dynamic Type | Dynamic Type | Allow text to grow / reflow at AX sizes | `ios-ui-ux-design` |
| 11 | **P2** | Website | Content | Medium | "Submit" newsletter button; 4× "Learn more" | UX-writing | Verb+noun labels; descriptive link text | `ux-writing-and-microcopy` |
| 12 | **P2** | Website | Trust | Low | Testimonials without attribution; vague "Get started" CTA | premium-readiness | Add named/attributed proof; concrete pricing CTA | `landing-page-and-conversion-design`, `premium-ui-ux-design` |

---

## Overall Product Verdict

**Not ready to position as premium — blocking design-quality issues on the two web surfaces.**

| Surface | Score | Band | Blocking gate(s) |
|---|---|---|---|
| Marketing website | **38/100** | Fundamental | Slop + A11y + Perf |
| SaaS web app | **49/100** | Major redesign | Slop + A11y |
| iOS app | **86/100** | Good foundation | none |

The **iOS app proves the team can ship distinctive, native, accessible work** — but the two web
surfaces drag the product down hard, and the **product is only as shippable as its weakest blocking
gate**. The single highest-leverage move (P0 #1) is to **replace Inter with a stated, intentional
type pairing across both web surfaces** — it clears the product-wide slop gate, lifts both web
scores off their caps, and is low effort. Pair it with P0 #2–#4 (contrast + LCP) and both web
surfaces move out of "redesign" into "good foundation" within one focused sprint.

**Recommended sequence:** P0 #1–4 (this sprint, clears all hard gates) → P1 #5–8 (next sprint,
states + iPad + parity) → P2 polish. Re-audit the two web surfaces after P0 to confirm the caps
lift.

---

*Composed `visual-product-slop-audit` + `ai-slop-typography-audit` (slop gate),
`accessibility-wcag-2-2-compliance` (a11y gate), `performance-as-ux-and-core-web-vitals` (perf
gate), `ios-ui-ux-design` (Apple lens), and `cross-platform-design-parity` (parity). Scoring per
`design-audit/references/audit-rubric.md`; routing per `references/recommendation-format.md`.
Thresholds from `doctrine/references/wcag-2.2-criteria.md` and
`doctrine/references/web-performance-budgets-2026.md`. No banned font appears in any recommendation.*
