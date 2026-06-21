# Reference: Web Performance Budgets (2026) — performance is a design constraint

Performance is craft, not an afterthought — a slow, janky, layout-shifting page reads as
unconsidered. Cited by the performance, responsive, font, imagery, motion, and QA skills. Source:
web.dev Core Web Vitals; verified via `docs/initial-analysis/06-2026-standards-benchmark.md`.

## Core Web Vitals — "good" thresholds (field p75)
- **LCP (Largest Contentful Paint) ≤ 2.5 s** — main content visible fast.
- **INP (Interaction to Next Paint) ≤ 200 ms** — input feels instant (INP replaced FID in 2024).
- **CLS (Cumulative Layout Shift) ≤ 0.1** — nothing jumps as it loads.
"Needs improvement" / "poor" bands sit above these; design to the *good* band.

## Asset budgets (per page archetype — tune, then enforce)
| Archetype | JS (gz) | CSS (gz) | Images | Fonts | Total target |
|---|---|---|---|---|---|
| Marketing/landing | ≤ 150 KB | ≤ 50 KB | hero ≤ 200 KB | ≤ 100 KB | **≤ 1 MB** |
| Web app shell | ≤ 300 KB | ≤ 75 KB | lazy | ≤ 100 KB | budget per route |
| Document/long-form | minimal | ≤ 40 KB | inline-lazy | ≤ 100 KB | ≤ 800 KB |

## Font performance (ties to `embedding-by-format.md`)
- `font-display: swap`; **subset** to used glyphs; one **variable font** file over many statics;
  `preload` the critical face; cap custom weights.

## Image performance (ties to `photography-art-direction`)
- Modern formats (**AVIF**, then WebP); responsive `srcset`/`sizes`; lazy-load below the fold;
  **always set width/height** (or aspect-ratio) to prevent CLS; compress to the budget.

## Perceived performance (ties to state + motion skills)
- Skeletons over spinners; optimistic UI; mask latency with purposeful transitions; prioritise
  above-the-fold render. Perceived speed often beats raw speed.

## Enforcement
Set these as **Lighthouse CI thresholds** (a build gate). A page over budget fails the
`design-qa-and-pre-launch-review` gate.
