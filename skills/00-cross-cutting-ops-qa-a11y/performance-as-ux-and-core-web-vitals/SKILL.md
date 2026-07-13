---
name: performance-as-ux-and-core-web-vitals
description: >-
  Use when page speed, loading perception, Core Web Vitals, asset budgets, image or font weight, FOIT/FOUT, or layout shift must be treated as design constraints. Use engineering performance skills for code-level profiling and remediation.
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
  - claude-code
  - codex
---

# Performance as UX & Core Web Vitals
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When

- You are designing a page/screen and want LCP, INP, and CLS treated as first-class
  design constraints — not handed off to engineering after the visuals are "done".
- A page reads as slow, janky, or shifts as it loads, and the fix is a *design* decision
  (what loads first, what holds space, what the wait looks like).
- You need a filled performance budget sheet for a page archetype before build —
  CWV targets plus JS/CSS/image/font KB caps and the design choices that hit them.
- You are choosing a loading treatment (skeleton vs spinner vs optimistic UI), a hero
  image strategy, or a font-loading strategy, and want the performant-by-design option.
- You are pre-launch and need the performance half of the QA gate (the rest lives in
  `design-qa-and-pre-launch-review`).

## Do Not Use When

- The work is deep runtime profiling, server/CDN tuning, bundle-splitting code, or
  Lighthouse-CI pipeline wiring — that is engineering execution. This skill sets the
  *design* targets and patterns; hand the enforcement to the build.
- You only need WCAG conformance — use `accessibility-wcag-2-2-compliance`.
- You need the full pre-ship checklist across slop/a11y/perf — start at
  `design-qa-and-pre-launch-review`, which composes this skill's gate.
- The artifact is a static document (DOCX/PDF) with no runtime — font subsetting still
  applies, but CWV does not; use the group-13 document skills.

## Required Inputs

| Input | Supplied by | Required? | Why |
|---|---|---|---|
| Page archetype and critical journey | Product/design brief | yes | Selects the correct budget |
| Candidate assets, fonts, and states | Design and content teams | yes | Exposes weight and shift risk |
| Field or lab measurements | Performance owner | recommended | Establishes current evidence |

- The **page archetype** (marketing/landing, web-app shell, or document/long-form) —
  this selects the budget row in `web-performance-budgets-2026.md`.
- The **LCP element** for the page (usually the hero image, headline, or first card).
- The intended **font set** (families, weights, whether self-hosted or web-fetched) and
  the **key imagery** (hero, above-the-fold media) with rough source dimensions.
- Network/device target (default to field p75 on mid-range mobile, 4G).
- Whether a Lighthouse-CI build gate exists (if not, recommend one — see Enforcement).

## Workflow

1. **Set the budget first, from the archetype.** Open
   `doctrine/references/web-performance-budgets-2026.md` and copy the matching row into a
   budget sheet: the CWV "good" thresholds (LCP <= 2.5s, INP <= 200ms, CLS <= 0.1) and the
   JS/CSS/image/font/total KB caps. These are the canonical numbers — operationalize them
   here, do not invent new ones. Treat the sheet as a design constraint that every later
   choice must respect. Template: `examples/performance-budget-sheet.md`.
2. **Name the LCP element and protect it.** Decide what paints largest above the fold,
   then design so it renders fast: `preload` the critical image/font, inline its critical
   CSS, never lazy-load the LCP image, and keep it inside the image KB cap. If the hero is
   over budget, that is a *design* decision — crop tighter, change the format, or replace a
   photo with a typographic hero. See `references/perceived-performance-patterns.md` §LCP.
3. **Reserve space for everything that loads late — design CLS to zero.** Every image,
   embed, ad slot, font swap, and async block gets a reserved box (`width`/`height` or
   `aspect-ratio`) at design time. Annotate dimensions on the spec. A layout that "settles"
   after load is a design failure, not a tuning problem. See §CLS.
4. **Design the wait, not just the arrival (perceived performance).** Choose the latency
   treatment per surface: skeleton screens that mirror final layout (not spinners),
   optimistic UI for high-confidence actions, purposeful transitions that mask fetches,
   and above-the-fold-first render order. Specify each loading state as a real frame in
   the design, with its own copy. See §Perceived performance and pair with
   `empty-error-and-loading-states`.
5. **Make image performance a design decision.** Specify modern formats (AVIF, then WebP),
   responsive `srcset`/`sizes` so each breakpoint ships only the pixels it needs, lazy-load
   below the fold, and compress every asset to the budget. Always carry width/height. Art
   direction (different crops per breakpoint) lives with `photography-art-direction` but the
   *weight* contract lives here. See §Images.
6. **Make font performance a design decision.** Prefer one variable font file over many
   statics; `font-display: swap` to avoid invisible text (FOIT); **subset** to the glyphs
   actually used; `preload` only the critical face; cap custom weights (this also serves the
   anti-slop "always pair, never over-proliferate" rule). Account for the swap reflow in the
   CLS budget by sizing fallback metrics. See §Fonts and `references/perceived-performance-patterns.md`.
7. **Tune INP into the interaction design.** Keep main-thread work off the critical input
   path: debounce/throttle expensive handlers, show immediate visual acknowledgement on tap
   (<= 100ms), avoid layout-thrashing animations (animate transform/opacity only). The design
   commitment is "every input gets visible feedback within a frame". See §INP.
8. **Write the enforcement line.** Record the budget as Lighthouse-CI thresholds so a page
   over budget fails the build. A page that blows the budget fails the
   `design-qa-and-pre-launch-review` gate — state that on the sheet.

## Quality Standards

- Budgets are copied from `web-performance-budgets-2026.md`, not improvised; if a page needs
  to exceed a cap, the sheet states why and what was traded.
- Every loading and shift-prone surface has a named, designed treatment (no bare spinners, no
  unreserved space).
- The LCP element, the CLS reservations, and the font/image weight contract are all explicit
  on the spec before build.

## Anti-Patterns

- **Perf as an afterthought.** Designing the "happy, fully-loaded" frame only, then asking
  engineering to "make it fast" — the slow/janky result is baked into the design.
- **Spinners as the default wait.** A spinner says "something is happening somewhere";
  a skeleton that mirrors the final layout says "your content is arriving here".
- **Unreserved late content.** Letting images, ads, embeds, or font swaps push content down
  after paint — every point of CLS is a design decision that was skipped.
- **Lazy-loading the LCP image** or deferring the hero font, then wondering why LCP is poor.
- **Font/weight proliferation.** Six custom weights and three families — slow *and* a slop
  signal. One variable font, subset, two or three intentional weights.
- **Decorative motion on the input path** that delays INP or causes jank to look "premium".
- **Inventing thresholds.** Any number not traceable to the canonical 2026 budgets ref.

## Outputs

| Output | Consumer | Evidence / acceptance |
|---|---|---|
| Performance budget sheet | Designer and engineer | CWV targets, asset caps, LCP element, and reservations |
| Loading-state specification | Component implementer | Skeleton, optimistic, error, and transition frames |
| Performance gate record | QA and release owner | Measured thresholds and unresolved exceptions |

- A **filled performance budget sheet** for the page archetype: CWV targets, asset KB caps,
  the named LCP element, CLS reservations, and the specific design decisions that hit each
  number (see `examples/performance-budget-sheet.md`).
- Designed **loading/skeleton/optimistic states** as real frames with copy.
- An **image + font performance contract**: formats, srcset breakpoints, subsetting,
  preload list, and per-asset KB.
- The **Lighthouse-CI threshold line** to wire into the build gate.

## Examples

- See `examples/performance-budget-sheet.md` for the required evidence-backed budget format.

## Decision Rules

| Condition | Decision | Wrong-choice failure |
|---|---|---|
| Element is the likely LCP | Prioritise and never lazy-load it | Largest content appears late |
| Late content has known dimensions | Reserve its final space | Layout shifts after interaction |
| Wait is predictable and structural | Use a content-shaped skeleton | Spinner provides no spatial continuity |
| Field p75 fails a CWV target | Block release or approve a documented exception | Lab-only success hides user harm |

## Capability Contract

Read and design inspection are required; measurement execution is strongly preferred. Editing needs implementation authority. Code-level profiling and production remediation route to engineering performance skills.

## Degraded Mode

Without field data, use lab measurements as a conditional proxy and identify the required RUM follow-up. Without execution, deliver the budget and designed states but mark the gate unverified.

- `examples/performance-budget-sheet.md` — a fully filled budget for a real page archetype
  (a marketing/landing page): LCP/INP/CLS targets, JS/CSS/image/font KB budgets, the named
  LCP element, the CLS reservations, and the concrete design decisions that hit each number.

## References

- `doctrine/design-doctrine.md` — the anti-slop charter; font/weight restraint and "state the
  choice" apply to performance decisions too.
- `doctrine/references/web-performance-budgets-2026.md` — **canonical** CWV thresholds and
  per-archetype asset budgets. This skill operationalizes that ref; it does not restate or
  override its numbers.
- `doctrine/references/embedding-by-format.md` — font embedding/subsetting mechanics the font
  budget relies on.
- `references/perceived-performance-patterns.md` — the skeleton/optimistic/transition-masking,
  LCP/CLS/INP, and image/font-as-design patterns, with the budget thresholds cited from the
  canonical ref.
<!-- dual-compat-end -->
## Plugins (Load Alongside)

| Companion Skill | When to Load |
|---|---|
| `design-qa-and-pre-launch-review` | Pre-ship — this skill is its performance gate |
| `responsive-and-adaptive-layout` | srcset/breakpoint and fluid-layout decisions that affect image weight and CLS |
| `empty-error-and-loading-states` | Designing the skeleton/loading/optimistic frames as first-class states |
| `photography-art-direction` | Hero/imagery weight and art-directed crops per breakpoint |

---

*Sources: web.dev Core Web Vitals; `doctrine/references/web-performance-budgets-2026.md`
(verified via `docs/initial-analysis/06-2026-standards-benchmark.md`).*
