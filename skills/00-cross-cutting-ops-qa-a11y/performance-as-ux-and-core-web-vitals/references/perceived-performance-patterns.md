# Reference: Perceived-Performance Patterns — designing speed, not just measuring it

Performance is craft. Two pages can hit the same network total and *feel* seconds apart,
because perceived speed is a function of **what loads first, what holds its place, and what
the wait looks like** — all design decisions. This reference operationalizes the canonical
budgets in `doctrine/references/web-performance-budgets-2026.md` into patterns you choose at
design time. The thresholds below are quoted from that ref; do not invent new numbers.

> **Canonical thresholds (field p75), from `web-performance-budgets-2026.md`:**
> LCP <= 2.5 s · INP <= 200 ms · CLS <= 0.1. Design to the *good* band, not "needs improvement".

---

## 1. The mental model: three moments of a page

| Moment | The user's question | The vital it maps to | The design lever |
|---|---|---|---|
| **Is it coming?** | "Did my click do anything?" | INP / first feedback | Immediate acknowledgement, skeletons, optimistic UI |
| **Is it here?** | "Can I see the main thing yet?" | LCP | Prioritise the LCP element; preload; don't lazy-load it |
| **Is it stable?** | "Will it stop jumping?" | CLS | Reserve space for everything that loads late |

Design each moment deliberately. A page that nails all three feels fast even on a mediocre
connection; a page that ignores them feels broken even on fibre.

---

## 2. LCP — make the main thing arrive first (<= 2.5 s)

The Largest Contentful Paint element is usually the hero image, the headline, or the first
content card. Design decisions that protect it:

- **Name the LCP element on the spec.** If you do not know what paints largest, you cannot
  prioritise it.
- **Preload the critical asset** — the hero image and the heading font face.
- **Never lazy-load the LCP image.** Lazy-loading below-the-fold media is correct; lazy-loading
  the hero is the single most common LCP regression.
- **Inline the critical CSS** for above-the-fold so the first paint does not wait on a stylesheet.
- **If the hero is over the image KB cap, redesign — don't just compress harder.** Options, in
  rough order of preference: tighter crop, switch to AVIF, use an art-directed smaller crop on
  mobile (`srcset`), use a CSS/typographic hero instead of a photo, or a low-cost gradient +
  small focal image. The budget is a constraint that shapes the composition.
- **Budget tie-in:** marketing/landing hero <= 200 KB; fonts <= 100 KB total
  (`web-performance-budgets-2026.md`, asset table).

---

## 3. CLS — design it to zero (<= 0.1)

Cumulative Layout Shift is almost entirely preventable at design time. Every element that can
arrive *after* first paint must have its space reserved before it.

- **Images & video:** always carry intrinsic `width`/`height` or an `aspect-ratio`. The box
  exists before the pixels do. (`web-performance-budgets-2026.md` §Image performance.)
- **Web fonts:** the swap from fallback to web font reflows text. Size the **fallback metrics**
  (`size-adjust`, `ascent-override`, or a metrics-compatible fallback) so the swap is invisible.
- **Embeds, ads, iframes, cookie/consent bars:** give them a fixed reserved slot. Never let a
  late banner push the page down. If height is unknown, reserve a sensible min-height and design
  for it.
- **Async content (recommendations, "you may also like", live regions):** reserve the block with
  a skeleton of the same height (see §4) so insertion causes no shift.
- **Spec annotation rule:** every late-loading box on the design carries its reserved dimensions.
  A design where content "settles" after load has an unstated CLS cost.

---

## 4. Perceived performance — design the wait

> "Skeletons over spinners; optimistic UI; mask latency with purposeful transitions;
> prioritise above-the-fold render. Perceived speed often beats raw speed."
> — `web-performance-budgets-2026.md` §Perceived performance.

### 4.1 Skeleton screens over spinners
A spinner is a contentless "something is happening *somewhere*". A skeleton is a low-fidelity
preview of the *actual* layout arriving in *this* spot — it sets expectations and reduces felt
wait. Design rules:

- The skeleton **mirrors the final layout's structure and dimensions** (same boxes, same
  positions) so the real content swaps in with **zero shift** (this is also your CLS reservation
  from §3 — one pattern, two wins).
- Use a calm shimmer or a static tint; avoid bouncy/elastic motion (anti-slop, and it draws the
  eye to the wait).
- Skeletons are right for **content you are confident will arrive** (a feed, a profile, a table).
  For unknown/empty outcomes, pair with `empty-error-and-loading-states`.

### 4.2 Optimistic UI
For high-confidence, low-risk actions (like, add-to-cart, toggle, send message), render the
*successful end state immediately* and reconcile when the server confirms; roll back visibly on
the rare failure. The interaction feels instant (helps INP perception) because the UI does not
wait on the round-trip. Reserve a clear, non-alarming rollback treatment for the failure path.

### 4.3 Transition masking
A purposeful transition (a 150-250 ms cross-fade, a shared-element move, a route slide) **occupies
the user's attention during a fetch**, so a sub-second wait reads as "responsive motion" rather
than "stall". The transition must be functional, GPU-friendly (transform/opacity only), and honour
`prefers-reduced-motion`. Do not animate to *look* premium at the cost of the input path (§5).

### 4.4 Above-the-fold-first
Render order is a design decision. Stream/prioritise the above-the-fold region; defer, lazy-load,
or progressively hydrate the rest. The user should be reading the top of the page while the
bottom is still arriving.

---

## 5. INP — every input gets a frame of feedback (<= 200 ms)

INP measures how fast the UI responds to interactions. The design commitment: **every tap/click
shows visible acknowledgement within ~100 ms**, even if the result is still computing.

- Show the pressed/active state and (if needed) an inline skeleton or optimistic state immediately;
  do the heavy work after the paint.
- Keep expensive handlers off the critical input path — debounce/throttle search-as-you-type,
  defer non-urgent work, avoid synchronous layout reads/writes in handlers (layout thrash).
- Animate **transform and opacity only**; never animate layout properties on interaction.
- Decorative motion must never delay feedback. A premium-feeling interaction is a *fast* one.

---

## 6. Image performance as a design decision

Ties to `photography-art-direction` (art direction) — but the *weight contract* lives here.

| Decision | Rule (from `web-performance-budgets-2026.md` §Image performance) |
|---|---|
| Format | Modern first: **AVIF**, then **WebP**, with a JPEG/PNG fallback only if required |
| Responsive | `srcset` + `sizes` so each breakpoint downloads only the pixels it shows |
| Loading | Lazy-load **below the fold**; never the LCP/hero image |
| Stability | **Always** set width/height or `aspect-ratio` (CLS, §3) |
| Weight | Compress to the archetype's image cap (landing hero <= 200 KB) |
| Art direction | Different crops per breakpoint via `<picture>`; the mobile crop is also lighter |

A "beautiful" 1.5 MB hero is a design *defect* on a 1 MB page budget. The constraint is part of
the brief, not a tax applied afterward.

---

## 7. Font performance as a design decision

Ties to `doctrine/references/embedding-by-format.md` (subsetting/embedding mechanics) and the
anti-slop charter (pair intentionally; do not over-proliferate weights).

| Decision | Rule (from `web-performance-budgets-2026.md` §Font performance) |
|---|---|
| File strategy | One **variable font** file over many static weights where possible |
| Flash | `font-display: swap` — never invisible text (FOIT); size fallback metrics to kill the swap-reflow (§3) |
| Size | **Subset** to the glyphs actually used (Latin subset, used punctuation/numerals) |
| Critical face | `preload` only the face the LCP text needs |
| Restraint | Cap custom weights — 2-3 intentional weights, not 6. Slow *and* a slop tell otherwise |
| Budget | All faces within the font cap (<= 100 KB total across archetypes) |

The design move and the performance move are the same move: a tight, intentional type system is
both faster and more authored.

---

## 8. Enforcement (the budget is a build gate)

Record the budget as **Lighthouse-CI thresholds** so a page over budget **fails the build** and,
per `web-performance-budgets-2026.md` §Enforcement, fails the `design-qa-and-pre-launch-review`
gate. The budget sheet (see `examples/performance-budget-sheet.md`) is the source of those
threshold numbers — keep them in sync with the canonical ref, never ahead of it.

---

*Sources: web.dev Core Web Vitals; `doctrine/references/web-performance-budgets-2026.md`
(canonical thresholds & asset budgets); `doctrine/references/embedding-by-format.md`
(font subsetting/embedding). Perceived-performance framing per Nielsen Norman Group on
response-time limits and skeleton screens.*
