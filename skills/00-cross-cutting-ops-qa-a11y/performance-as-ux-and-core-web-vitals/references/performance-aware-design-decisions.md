# Performance-Aware Design Decisions

Parent skill: [`../SKILL.md`](../SKILL.md) (`performance-as-ux-and-core-web-vitals`).

**When to read:** while choosing fonts, imagery, art-direction routes and motion for anything that
ships to the web, so the design is fast before engineering starts. This file covers design
implications only. Code-level profiling, CI gates, RUM and third-party governance belong to the
website engine (`website-skills`: deploy performance gate, observability, image compression,
Africa low-bandwidth patterns); when that engine delivers the site, its stricter route budgets
govern and this engine's budgets in `doctrine/references/web-performance-budgets-2026.md` are the
ceiling for design proposals.

Sources: Osmani, A. (2026) *Web Performance Engineering in the Age of AI*, O'Reilly Media
(loading moments, critical-path and compositor principles); LaGrone, B. (2016) *Web Design
Blueprints*, Packt (counter-examples). Current thresholds: web.dev Core Web Vitals, recorded in
the currentness register as claim CW-01 (LCP 2.5 s, INP 200 ms, CLS 0.1 at the 75th percentile
of field data, per device class; checked 2026-09-23, review 2027-03-23). INP replaced FID on
12 March 2024 (claim CW-02).

---

## 1. Four loading moments (use to explain design choices to clients)

| Moment | User question | Design lever |
|---|---|---|
| Is it happening? | "Did the page respond?" | A background colour or shell appears at once; no blank white wait |
| Is it useful? | "Can I see the main content?" | Hero text or image is the largest element and loads first |
| Is it usable? | "Does it respond when I tap?" | Light interactions; immediate visual acknowledgement of taps |
| Is it stable and pleasant? | "Does anything jump?" | Reserved space for images, embeds and banners; compositor-only motion |

## 2. Fonts

- Choose families with a variable font or few weights; every extra weight is a download.
- Subset to the languages used (check Kiswahili, Luganda and French glyphs are kept).
- Self-host WOFF2; preload only the one or two faces that render above the fold.
- `font-display: swap` for body text (or `optional` where a late swap would be worse), with a
  fallback stack tuned with `size-adjust` and ascent/descent overrides so the swap does not shift
  layout. Check current browser support for the override descriptors.
- Display faces used once (a campaign headline) may be better as live text in a subset file than
  as an image.

## 3. Images

- The hero is a real `<img>` in the HTML (not a CSS background, not injected by script), so the
  browser finds it early; give it high fetch priority and never lazy-load it.
- Width-based `srcset` with `sizes`; AVIF then WebP; cap mobile hero density at about 2x, because
  3x files cost far more bytes for little visible gain on mid-range phones.
- Always give width and height (or `aspect-ratio`) to reserve space.
- Lazy-load below the fold only.
- Art-direction routes that depend on full-bleed photography (for example immersive photographic
  or tactile craft routes) carry an explicit image weight note on the direction board.
- Replace heavy embeds with facades: a video poster that loads the player on tap, a static map
  image with an "Open in Maps" link, a WhatsApp click-to-chat link instead of a chat widget.

## 4. Motion

- Animate `transform` and `opacity` only; avoid animating layout properties.
- Use `will-change` sparingly and only during motion; each layer costs memory on low-end phones.
- Acknowledge any tap within about 100 ms; show progress for waits beyond about one second;
  skeletons match the final layout geometry.
- Scroll effects follow `motion-design/references/scroll-driven-effects.md`.

## 5. Design review questions for AI-drafted UI

1. How will this affect the largest content paint on a mid-range phone?
2. Does any interaction do heavy work before giving feedback?
3. Will anything inserted later push content down?
4. Are loading, empty, error and success states designed?

## 6. Measurement honesty

Never promise a Lighthouse score or a percentage uplift to a client. Present published case
studies only as the direction of an effect; commit to measuring the client's own before and
after with field data. Label every number as lab or field, with percentile and period.
