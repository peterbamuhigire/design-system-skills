# Reference: View Transitions API

The modern, browser-native way to animate **between two DOM/page states** without manually
choreographing FLIP, clones, or absolute-positioned overlays. Replaces hand-rolled shared-element
code. Source: W3C CSS View Transitions Module Level 1 (same-document) & Level 2 (cross-document);
MDN; Chrome 111+ (same-doc), 126+ (cross-doc MPA). Cross-cuts `doctrine/references/wcag-2.2-criteria.md`
(2.3.3 — every transition must collapse under `prefers-reduced-motion`).

---

## 1. Same-document transitions (SPA, tab/route swap)

Wrap the DOM mutation; the browser snapshots **before** and **after**, then cross-fades the
`::view-transition` pseudo-tree:

```js
function update() { /* mutate the DOM: swap route, toggle list, etc. */ }

if (document.startViewTransition) {
  document.startViewTransition(() => update());
} else {
  update(); // graceful fallback: instant, no animation
}
```

**Always feature-detect** (`if (document.startViewTransition)`) — never assume support.

### Default + custom CSS

```css
/* The default cross-fade — tune duration/easing here */
::view-transition-old(root),
::view-transition-new(root) {
  animation-duration: 300ms;
  animation-timing-function: cubic-bezier(0.25, 1, 0.5, 1); /* ease-out-quart */
}
```

---

## 2. Shared-element morph (`view-transition-name`)

Give the element a unique name in **both** states; the browser morphs position/size/shape between
them (replaces the old `matchedGeometryEffect`/FLIP hack):

```css
.product-thumb   { view-transition-name: hero-product; } /* list view */
.product-hero    { view-transition-name: hero-product; } /* detail view */

::view-transition-group(hero-product) {
  animation-duration: 400ms;
  animation-timing-function: cubic-bezier(0.16, 1, 0.3, 1); /* ease-out-expo */
}
```

Rules:
- A `view-transition-name` must be **unique per snapshot** (only one element may hold it at a time).
- Assign it just-in-time (on the element being navigated from/to), then clear it, for long lists.

---

## 3. Cross-document transitions (MPA — no JS framework needed)

For classic multi-page navigations within the same origin, opt in via CSS only:

```css
@view-transition { navigation: auto; }
```

Both the outgoing and incoming pages must declare it. Shared elements still use matching
`view-transition-name`s across the two documents.

---

## 4. Directionality & flow (honour navigation direction)

Use a transition **type** to slide forward vs back (reverse the animation on back-nav, per SKILL §4.4):

```js
const t = document.startViewTransition({ update, types: ["forward"] });
```
```css
:root:active-view-transition-type(back) ::view-transition-old(root) { /* reverse */ }
```

---

## 5. Reduced-motion (MANDATORY — WCAG 2.3.3)

View Transitions are **not** exempt. Collapse them to an instant swap (or ≤100 ms opacity-only):

```css
@media (prefers-reduced-motion: reduce) {
  ::view-transition-group(*),
  ::view-transition-old(*),
  ::view-transition-new(*) {
    animation: none !important; /* instant state swap, no morph/slide */
  }
}
```

See `reduced-motion.md` for the full strategy.

---

## 6. Pitfalls

- Snapshots are **rasterised** — animating huge subtrees can jank; scope names to the elements that
  actually move.
- Don't animate `width`/`height` of the groups manually; let the API morph (it uses transforms).
- Feature-detect; provide the instant fallback for Firefox/older Safari.
- Cross-doc transitions need same-origin and the `@view-transition` opt-in on **both** ends.

## Checklist
- [ ] `document.startViewTransition` is feature-detected with an instant fallback.
- [ ] Shared elements have a unique `view-transition-name` per snapshot.
- [ ] Durations/easing follow SKILL §1–2 (300 ms swap / 400 ms morph, ease-out curves).
- [ ] A `prefers-reduced-motion: reduce` block disables the transition animation.
