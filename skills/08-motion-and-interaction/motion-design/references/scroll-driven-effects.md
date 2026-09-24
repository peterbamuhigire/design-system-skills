# Scroll-Driven Effects (Safe Parallax)

Parent skill: [`../SKILL.md`](../SKILL.md) (`motion-design`).

**When to read:** when a brief asks for parallax, scroll-linked reveals or "storytelling on
scroll", or when auditing an older site that uses them. The storytelling principle (near things
move faster than far things) is durable; the older implementations are not. LaGrone (2016) *Web
Design Blueprints*, Packt, documents the JavaScript scroll-listener approach this file replaces;
treat its code as a counter-example.

---

## 1. Policy

- Use scroll effects only on **story pages** (brand story, campaign, tourism journey), never on
  service, form, checkout or task pages.
- The **static version is the default** and must carry the same content and call to action.
- Motion is added only inside `@media (prefers-reduced-motion: no-preference)` and, for
  scroll-linked timelines, inside `@supports (animation-timeline: view())`.
- **Never auto-scroll the user on load. Never scroll-jack** (override the scroll speed or snap the
  page against the user's intent).

## 2. Implementation order

1. **CSS scroll-driven animations** (`animation-timeline: scroll()` or `view()`) animating only
   `transform` and `opacity`. Browser support is still rolling out; check current compatibility
   tables and keep the static fallback.
2. **IntersectionObserver class toggles** where scroll timelines are unsupported: toggle a class
   when a section enters view; the CSS transition does the work.
3. If script is unavoidable: one `requestAnimationFrame`-throttled update, no layout reads inside
   the loop, passive listeners, `will-change` only while moving (layers cost memory).

Never animate `top`, `left`, `height`, `width` or `font-size` on scroll; they trigger layout on
every frame.

## 3. Budgets and checks

- Keep the whole effect small: one or two layers on a hero or chapter divider; aim for a few
  kilobytes of CSS and no added JavaScript where possible.
- Scenery as a few optimised SVGs or one layered image, never hundreds of DOM icons.
- The largest image on the first screen stays a real `<img>` with priority loading so the effect
  does not delay the main content.
- Test on a real mid-range Android phone for smoothness and with the operating system's reduce
  motion setting on. Check the page still meets the Core Web Vitals budget in
  `doctrine/references/web-performance-budgets-2026.md`.

## 4. Decision checklist

1. Is this a story page? If not, no scroll effect.
2. Does the reduced-motion version carry the same content and call to action?
3. Are only `transform` and `opacity` animated?
4. No auto-scroll, no scroll-jacking, no layout reads in a scroll listener?
5. Tested on a real mid-range phone and with reduced motion on?
