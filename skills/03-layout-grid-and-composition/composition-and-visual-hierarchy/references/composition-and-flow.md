# Reference: Composition And Flow

How the eye *moves* through a composition, and how to build the tension that makes it read as
authored. This is the "path and force" companion to `hierarchy-techniques.md` (which owns "what
wins"). Grounds in the Swiss/asymmetric tradition (Tschichold, Müller-Brockmann), Arnheim's
perceptual forces, and the F/Z scanning heuristics from `docs/book-study/01-ui-ux-craft.md` —
used as *heuristics under* the doctrine, never as laws (`doctrine/design-doctrine.md` §2).

---

## Eye-path — choose the route on purpose

Place the **focal point at the entry** and the **primary action at the exit** of a deliberately
chosen path:

| Path | Shape | Use when | Place focal point / action |
|---|---|---|---|
| **Z-pattern** | Top-left → top-right → diagonal → bottom-right | Sparse, visual, scan-fast layouts (landing hero, deck slide, ad) | Logo top-left, focal headline upper band, CTA at bottom-right exit |
| **F-pattern** | Down the left edge, with rightward scans on the top lines | Text-dense pages; users scan left edges and first words | Strongest words at left edge + first line; CTA where the F's bars end |
| **Diagonal / radial** | The eye is pulled from one dominant anchor outward | One image, number, or face anchors the field | Anchor at the optical centre or a third; supporting elements radiate from it |

Rules:

- **The path is a heuristic, not a law.** F/Z describe how eyes *tend* to scan unfamiliar pages;
  they are subordinate to the focal-point rule (`hierarchy-techniques.md`). A strong focal point
  *overrides* the default scan — the eye goes to the loudest element first, then follows the path.
- **One path, composed deliberately** beats hoping the eye finds its own way. A page with no
  intended path reads as the *everything-equal* slop (`ai-slop-taxonomy.md`).
- Lead the eye with alignment and direction: a shared edge, a pointing image, a line of motion all
  carry the gaze along the path.

---

## Asymmetry and tension

Dead-centre symmetry is the zero-decision default — it reads as a placeholder, not a composition
(`ai-slop-taxonomy.md`: dead-centre symmetry as the only structure). Authored compositions use
**intentional asymmetry**:

- **Pull the focal point off the centre line.** A hero pinned left with open air to its right; a
  number anchored at a third; an image bleeding off one edge. Asymmetry is a choice a templating
  tool would not make (Mission, §0).
- **Create tension by opposing weights across space.** A large element on one side *pulls* against
  a small one on the other, with open space between them as the field of force (Arnheim). That pull
  is **tension** — and tension is what makes a composition feel alive. A composition with no tension
  is inert.
- **Balance asymmetrically, not symmetrically.** Visual weight = size × value × colour × isolation.
  A small, dark, isolated element can balance a large, pale one across the field. You are balancing
  *forces*, not mirroring shapes.
- **Restraint plus one strong move.** One decisive off-centre pull beats many small hedged shifts
  (Vignelli). Do not scatter asymmetry everywhere; place one clear tension and let it carry.

Rule of thirds is a useful starting heuristic for *where* to place the focal point off-centre —
but it is a default to depart from, not a grid to obey.

---

## Figure-ground

The eye must instantly separate the **subject (figure)** from its **background (ground)**.
Ambiguous figure-ground — subject and background at the same value/weight on a busy field — is
fatiguing and reads as machine-flat. Establish a clear figure with at least one of:

- **Value contrast** — a dark subject on a light field (or vice versa). The most reliable separator.
- **Scale contrast** — a large mark in open space sits in front of small scattered detail.
- **Focus contrast** — a sharp subject over a blurred/de-emphasised ground.
- **Isolation** — open space around the figure lifts it off the ground.

Hard rules:

- **Never place type on a busy field unaided** — use a contrast overlay or a solid plate
  (`doctrine/references/type-scale-and-spacing.md`). Text-on-image without a ground treatment is a
  legibility and slop failure.
- **One figure per region.** If everything claims to be the figure, nothing is — the field goes
  flat.
- **Do not use glassmorphism / frosted-blur to fake figure-ground.** It is a convergent slop tell
  and usually fails contrast (`ai-slop-taxonomy.md` §Counter-doctrinal). Use a deliberate, legible
  surface and real value separation instead.

---

## Flow across viewports

Composition is not "set once." At each width the focal point, eye-path, and tension must be
**re-established**, not merely reflowed (own the depth in
`03-layout-grid-and-composition/responsive-and-adaptive-layout`):

- A Z-pattern desktop hero often becomes a **single vertical path** on mobile — the focal point
  must still lead at the top, and the primary action still land at the natural exit (often pinned).
- A desktop diagonal anchor may need to **re-anchor** when the image stacks above the copy — keep
  one element clearly dominant so the column does not flatten into equal stacked cards (the
  *uniform card grid* slop on a narrow screen).
- Re-run the Authored-Composition Checklist (`SKILL.md`) at every breakpoint, not just at desktop.

---

## What this prevents

- **No deliberate eye-path** — the *everything-equal* slop; the eye wanders, nothing leads.
- **Dead-centre symmetry as the only structure** — inert, tensionless, placeholder-looking pages.
- **Ambiguous figure-ground** — fatiguing, machine-flat fields; type lost on busy imagery.
- **Glassmorphism as fake separation** — a convergent slop tell refused here.
