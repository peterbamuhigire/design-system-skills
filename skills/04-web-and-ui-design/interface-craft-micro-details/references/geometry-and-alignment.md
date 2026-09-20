# Reference: Concentric Geometry, Optical Alignment, Image Edges

## Concentric radius — derivation

For two rounded rectangles sharing a common corner centre point (the inner surface inset from the
outer by a uniform padding `p`), the relationship between their corner radii falls directly out of
circle geometry: if the outer corner's arc is centred at the same point as the inner corner's arc,
and the two surfaces are offset by `p` on every edge, the outer radius must exceed the inner radius
by exactly `p` for the two arcs to remain concentric (same centre, radii differing by the gap
between them):

```
outer_radius = inner_radius + padding
```

Worked example: an inner card with `border-radius: 8px` padded `16px` inside an outer panel wants
`border-radius: 24px` on the panel, not `8px` or an arbitrary rounder value — anything else puts
the two arcs' centres at different points, which reads as a subtle but real visual conflict at the
corner.

When `padding` is large relative to both radii, forcing this formula stops making visual sense
(e.g. a tiny inner radius padded by 64px inside an outer panel — the outer radius the formula
implies may be far larger than anything else in the system's radius scale). In that case, treat
the two surfaces as independent rather than nested, and pick the outer radius from the system's own
scale.

**Authority note:** Apple's Human Interface Guidelines documents this same relationship under
"concentricity" for nested rounded shapes (corner radius should be defined relative to the padding
of the shape it's nested within) — cited here as the design-authority precedent, not this skill's
own invention. Confirm current HIG wording before citing a specific guideline number, as Apple
revises HIG text between OS releases.

## Optical vs geometric alignment

An icon's bounding box is a geometric abstraction; its *visual mass* — where the ink actually
sits — is what a viewer perceives as centred. A play triangle, for instance, has more ink toward
its point than its flat edge, so geometric centering of its bounding box leaves it reading as
shifted left. This is the same phenomenon type designers have handled for centuries via
**overshoot**: round and pointed letterforms (O, C, A, V) are drawn slightly taller and/or wider
than flat-topped letters (H, E) so that all appear optically the same size when set together —
documented across the type-design literature (e.g. Jost Hochuli, *Detail in Typography*, and
standard type-design pedagogy on overshoot/optical correction). The UI-icon case is the same
principle applied to interface glyphs rather than letterforms.

Fix order of preference:
1. Re-export the SVG with corrected internal padding so the icon's own bounding box already
   accounts for its visual mass.
2. If the source asset can't be touched, apply a small pixel-level margin/padding offset in CSS
   and record the value (e.g. as a code comment or a token override) so it isn't silently lost the
   next time the icon set is regenerated.

## Tabular numerals

```css
.counter, .price, .timer, table td.numeric {
  font-variant-numeric: tabular-nums;
}
```

`font-variant-numeric` is a standard property in the W3C CSS Fonts Module Level 3 specification.
`tabular-nums` selects digit glyphs with equal advance width (vs. proportional figures, whose width
varies per digit) — the correct fix for any UI element where digits change in place and should not
cause neighbouring content to reflow.

## Image edge treatment

```css
img {
  outline: 1px solid rgba(0, 0, 0, 0.1);
  outline-offset: -1px;
}

@media (prefers-color-scheme: dark) {
  img {
    outline-color: rgba(255, 255, 255, 0.1);
  }
}
```

Use neutral black/white alpha only — do not tint with the brand palette (a tinted outline implies
brand/state meaning the outline does not carry). When the boundary is load-bearing for
distinguishing the image from an adjacent similarly-toned surface (not purely decorative), verify
the outline clears WCAG 1.4.11's 3:1 non-text contrast minimum against that surface, since 10%
alpha may not be sufficient on every background.
