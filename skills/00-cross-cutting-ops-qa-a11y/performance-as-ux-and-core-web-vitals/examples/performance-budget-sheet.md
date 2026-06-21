# Worked Example: Performance Budget Sheet — Marketing / Landing page

A fully filled budget for a real, common archetype: the **top-of-funnel SaaS landing page**
("Maduuka — point-of-sale for African retailers"). It shows the Core Web Vitals targets, the
asset budgets, the named LCP element, the CLS reservations, and — the point of the exercise —
**the specific design decisions that hit each number.** Budgets are copied from
`doctrine/references/web-performance-budgets-2026.md` (the canonical ref); they are not invented
here.

---

## 0. Page profile

| Field | Value |
|---|---|
| Page | `/` — Maduuka marketing landing |
| Archetype | **Marketing / landing** (selects the budget row) |
| Primary goal | Communicate value + drive "Start free" CTA |
| Target field condition | p75, mid-range Android, 4G |
| LCP element | **Hero headline + product screenshot** (the screenshot is the largest paint) |
| Build gate | Lighthouse-CI thresholds wired; page over budget fails CI and the QA gate |

---

## 1. Core Web Vitals targets (the "good" band)

| Metric | Target (canonical) | This page's plan |
|---|---|---|
| **LCP** | **<= 2.5 s** | Preload hero screenshot (AVIF) + heading font; inline critical CSS; hero **not** lazy-loaded |
| **INP** | **<= 200 ms** | CTA + nav show pressed state within one frame; no heavy JS on the input path; sticky-header scroll handler throttled |
| **CLS** | **<= 0.1** (aiming ~0) | Every image, the font swap, and the cookie bar have reserved space (§4) |

Source: `web-performance-budgets-2026.md` §Core Web Vitals.

---

## 2. Asset budget (marketing/landing row)

| Asset | Cap (canonical) | This page's budget | Design decision that hits it |
|---|---|---|---|
| JS (gz) | <= 150 KB | **~70 KB** | Static-first (Astro/MPA); JS only for menu toggle, carousel, analytics. No SPA framework on a brochure page. |
| CSS (gz) | <= 50 KB | **~22 KB** | Token-driven utility/CSS layer; critical CSS inlined (~6 KB), rest deferred. No unused UI-kit CSS. |
| Images | hero <= 200 KB | hero **~120 KB**; below-fold lazy | Hero = AVIF at 1600px, `srcset` down to 640px (mobile crop ~45 KB). Logos as inline SVG. |
| Fonts | <= 100 KB | **~58 KB** | One variable display family (subset, ~34 KB) + one variable body family (subset, ~24 KB). 2 weights used. |
| **Total** | **<= 1 MB** | **~0.42 MB** first load | Above-the-fold only on first paint; testimonials/FAQ images lazy-load on scroll. |

Source: `web-performance-budgets-2026.md` §Asset budgets.

---

## 3. The LCP element — named and protected

- **Element:** the hero product screenshot (paired with the H1 headline).
- **Decisions:**
  - `preload` the AVIF hero and the display-font critical face.
  - Hero is **eager** (`loading="eager"`, `fetchpriority="high"`) — never lazy-loaded.
  - Critical above-the-fold CSS inlined; web-font swap sized so the H1 does not reflow.
  - Mobile gets an art-directed lighter crop (`<picture>`) so phones do not pay desktop weight.
- **Result target:** hero meaningfully painted < 2.0 s on 4G, leaving headroom under the 2.5 s cap.

---

## 4. CLS reservations (design it to zero)

| Late-loading thing | Reservation |
|---|---|
| Hero screenshot | `aspect-ratio: 16 / 10` + explicit width/height — box exists before pixels |
| Heading & body fonts | Metrics-matched fallback (`size-adjust`/`ascent-override`); swap is invisible |
| "Trusted by" logo strip | Fixed-height row; SVG logos inline so no reflow on load |
| Testimonial avatars | 48x48 reserved circles; lazy images load into fixed boxes |
| Cookie/consent bar | Fixed-height footer slot reserved at design time (does not shove content up) |
| Below-fold feature images | Each in an `aspect-ratio` box; skeleton tint until in-view load |

Net designed CLS: **~0** — nothing shifts after first paint.

---

## 5. Perceived-performance treatments

| Surface | Treatment | Why |
|---|---|---|
| Hero on first load | Above-the-fold-first render; instant H1 (system fallback) -> invisible font swap | Reads as instant text, no FOIT |
| "Start free" CTA | Immediate pressed state + inline spinner-in-button on submit (`Creating your store…`) | INP feedback within a frame; names the operation |
| Pricing toggle (monthly/annual) | Optimistic UI — prices switch instantly, no fetch | Feels instant; low-risk client action |
| Testimonials / FAQ (below fold) | Skeleton blocks mirroring final card dimensions, then lazy content | Zero shift; sets expectation (doubles as CLS reservation) |
| Section-to-section nav (anchor) | 180 ms ease-out scroll + reduced-motion fallback | Purposeful, masks no real latency; not decorative jank |

Patterns per `references/perceived-performance-patterns.md` §4.

---

## 6. Font & image contract (the weight commitments)

**Fonts (<= 100 KB, ~58 KB used):**
- Display: one variable family, Latin subset, weights 600 + 800 only, `font-display: swap`,
  `preload` the 800 face for the H1.
- Body: one variable family, Latin subset, weights 400 + 600.
- No third family. No static weight files. (Restraint = faster *and* more authored — anti-slop.)

**Images:**
- All raster as **AVIF** with WebP fallback.
- `srcset`: hero at 640 / 1024 / 1600; cards at 1x/2x.
- Below-the-fold: `loading="lazy"`, every image with width/height.
- Decorative shapes as CSS/SVG, never raster.

Ties to `doctrine/references/embedding-by-format.md` (subsetting) and
`web-performance-budgets-2026.md` §§Font/Image performance.

---

## 7. Enforcement — Lighthouse-CI threshold block

```jsonc
// lighthouserc — landing budget (mirrors this sheet; numbers trace to the canonical ref)
{
  "assert": {
    "assertions": {
      "largest-contentful-paint": ["error", { "maxNumericValue": 2500 }],
      "interaction-to-next-paint": ["error", { "maxNumericValue": 200 }],
      "cumulative-layout-shift":   ["error", { "maxNumericValue": 0.1 }],
      "resource-summary:script:size":     ["error", { "maxNumericValue": 150000 }],
      "resource-summary:stylesheet:size": ["error", { "maxNumericValue": 50000 }],
      "resource-summary:font:size":       ["error", { "maxNumericValue": 100000 }],
      "resource-summary:total:size":      ["error", { "maxNumericValue": 1000000 }]
    }
  }
}
```

A build that exceeds any line **fails CI** and fails the `design-qa-and-pre-launch-review` gate
(`web-performance-budgets-2026.md` §Enforcement). If a future change must exceed a cap, record the
reason and trade-off on this sheet before raising a threshold — never silently above the canonical ref.

---

*Budgets and thresholds: `doctrine/references/web-performance-budgets-2026.md` (canonical).
Patterns: `references/perceived-performance-patterns.md`.*
