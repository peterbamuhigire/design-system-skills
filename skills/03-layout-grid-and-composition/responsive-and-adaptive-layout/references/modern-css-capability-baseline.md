# Modern CSS Capability Baseline for Layout Decisions

Parent skill: [`../SKILL.md`](../SKILL.md) (`responsive-and-adaptive-layout`).

**Load when:** a responsive specification names a modern CSS capability (container queries,
subgrid, `:has()`, dynamic viewport units, view transitions, anchor positioning, popover,
scroll-driven animation) and the designer must decide whether it can carry the design or only
enhance it; or when an inherited site uses an older technique that a current capability replaces.

This is a design-decision table, not an implementation tutorial. Implementation patterns for the
widely available capabilities are in `container-queries-and-intrinsic.md`; motion capabilities
are owned by `08-motion-and-interaction/motion-design` (`view-transitions.md`,
`scroll-driven-effects.md`).

---

## 1. Support status (verified 2026-09-24)

Status terms follow Baseline: **Widely** = supported in all core browsers for 30 months or more;
**Newly** = supported in all core browsers recently; **Limited** = at least one core engine lacks it.

| Capability | Status | Since | Design may depend on it? |
|---|---|---|---|
| Container size queries (`container-type`, `@container`) | Widely | 2025-08 | Yes |
| Container query units (`cqi`, `cqb`) | Treat as with size queries | - | Yes, with `rem` floor in `clamp()` |
| Container style queries (`@container style(...)`) | Newly | 2026-05 | Enhancement; provide a class-based fallback for older browsers |
| Subgrid | Widely | 2026-03 | Yes |
| `:has()` relational selector | Widely | 2026-06 | Yes, for styling; never the only carrier of state that assistive technology needs |
| Small, large and dynamic viewport units (`svh`, `lvh`, `dvh`) | Widely | 2025-06 | Yes |
| Same-document view transitions | Newly | 2025-10 | Enhancement; the change must be complete without the animation |
| Cross-document view transitions (`@view-transition`) | Limited (no Firefox) | - | Enhancement only |
| Scroll-driven animations (`animation-timeline`) | Limited (no Firefox) | - | Enhancement only; static layout must be complete |
| Popover API (`popover` attribute) | Newly | 2025-01 | Yes for menus and non-modal overlays, with keyboard testing |
| CSS anchor positioning | Conflicting sources; see note | - | Enhancement with a non-anchored fallback position |
| `text-wrap: balance` | Newly (Widely expected 2026-11) | 2024-05 | Yes; harmless where unsupported |
| Navigation API | Newly | 2026-01 | Implementation choice; see chwezi-dev-engine `frontend-architecture` |

**Anchor positioning note.** web.dev announced it as Baseline Newly available in January 2026
when Firefox 147 enabled it. The web-features explorer consulted on 2026-09-24 lists the feature
as limited availability with only Safari 27 counted, which suggests the tracked feature definition
changed. Until the two agree, treat anchor positioning as an enhancement: the popover or tooltip
must still be usable in a fixed fallback position. Status: `NOT_ASSESSED` for dependence.

## 2. Decision rules

| Design need | Use | Instead of | Wrong-choice failure |
|---|---|---|---|
| A component must change layout by where it is placed | Container size query | Viewport media query | The card breaks in sidebars and embeds at the same window width |
| Nested items (card titles, prices, buttons) must align across sibling cards | Subgrid on the card rows | Fixed heights or JavaScript equalising | Uneven baselines; clipped text when content or font size grows |
| A parent must change when it contains something (a form group with an invalid field, a card with an image) | `:has()` | Extra modifier classes toggled by script | Class drift between state and styling |
| A full-height mobile panel or hero | `svh` for a height that must never be covered by browser chrome; `dvh` only when resizing during scroll is acceptable | `100vh` | Bottom actions hidden behind the mobile browser toolbar |
| Menu, disclosure or non-modal overlay | `popover` or `<details>`; `<dialog>` for modal | Custom div overlays with hand-built dismissal | Missing Escape, focus return and top-layer stacking |
| A tooltip or menu tied to its trigger | Anchor positioning with a fallback position | A positioning library by default | Overlay detached from the trigger when unsupported and no fallback exists |
| A state change should feel continuous | Same-document view transition, reduced-motion aware | Animated layout properties in script | Janky, inaccessible motion; see `motion-design` |
| Headings wrap with a single orphan word | `text-wrap: balance` on headings only | Manual line breaks | Breaks that fail at other widths and in translation |

## 3. Procedure

1. List the capabilities the design relies on, per component.
2. Classify each against section 1: **carry** (the design may depend on it) or **enhance**
   (the design must be complete without it).
3. For every enhance item, specify the fallback appearance in the handoff
   (`design-handoff-and-dev-spec`), not only the enhanced one.
4. Re-check status on the web-features explorer or MDN on the day of specification; record the
   access date. Statuses above change with each browser release.
5. Test the fallback in a browser that lacks the feature, or mark the fallback `NOT_ASSESSED`.

## 4. Replacements for older techniques found in inherited sites

| Older technique | Current replacement |
|---|---|
| Float grids with percentages derived from a fixed desktop mock-up | Grid with `fr`, `minmax()` and `gap`; subgrid for nested alignment |
| Padding-bottom trick for video and iframe ratios | `aspect-ratio` |
| Device-named pixel breakpoints, overlapping `max-width` and `min-width` ranges | Content-derived `em` breakpoints in range syntax (`width >= 40em`) and container queries |
| `device-width` and orientation queries as the main switch | `width` queries and container queries |
| Root font size shrunk to 62.5% or 60% for easy arithmetic | Leave the root at the user default; use `rem` tokens and `clamp()` |
| Viewport meta that disables zoom | `width=device-width, initial-scale=1`; zoom always allowed (WCAG 1.4.4) |
| `100vh` full-screen sections | `svh` or `dvh` per the rule above |
| Vendor-prefixed transforms and transitions written by hand | Unprefixed properties; build-time prefixing only where a support policy requires it |
| Hand-built ellipsis and fixed-width horizontal scrollers | Multi-line clamping (the prefixed `-webkit-line-clamp` form is the interoperable one; unprefixed support `NOT_ASSESSED`), scroll snap with a visible overflow cue, and a way to reveal the full text |
| Icon fonts | Inline SVG or a sprite with text labels (see `iconography-system-design`) |
| JavaScript scroll listeners for parallax | Scroll-driven animations as enhancement, reduced-motion static version |

## Evidence and currentness

Accessed 2026-09-24: web-features explorer pages for container-queries, container-style-queries,
subgrid, has, viewport-unit-variants, view-transitions, cross-document-view-transitions,
scroll-driven-animations, popover, anchor-positioning, text-wrap-balance and navigation
(web-platform-dx.github.io/web-features-explorer); web.dev "New to the web platform in January"
(2026) for anchor positioning and Navigation API; MDN viewport meta reference; W3C Understanding
SC 1.4.10 Reflow (320 CSS px). Re-verify at the next Kaizen cycle.

Sources: LaGrone, B. (2016) *Web Design Blueprints*, Packt (older techniques catalogued as
replacements, not recommendations); Marcotte, E. *Responsive Web Design*; Bell, A. and Pickering,
H. *Every Layout*; the CSS specifications and Baseline data above.
