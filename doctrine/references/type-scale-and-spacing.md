# Reference: Type Scale, Line Height, and Spacing

The numbers that turn a font pair into a hierarchy. Sourced from Ruben Gingerich
(*UX/UI in 45 Minutes*), Elisa Paduraru (*Fundamentals of Great UI/UX*), and the Chwezi
anti-slop rules.

---

## Type scale (use a real ratio, not arbitrary sizes)

- **Base body size:** 16px for web/mobile body, 14–16px for dense UI. Never below **12px**.
- **Scale ratio:** build the steps off the base with a consistent ratio. The Golden Ratio
  (**1.618**) gives a confident, editorial scale; **1.25** (major third) is a safer minimum.
  Aim for *at least* 1.25 between steps. (Gingerich; Paduraru.)
- **Real jumps, not timid ones.** Hero-to-body can be 3× or more. Sizes that sit almost the
  same are a slop signal — make the steps obvious. (Chwezi rule.)
- **Limit sizes per section:** at most ~3 font sizes in a single section keeps it coherent.
  (Gingerich; Paduraru.)

Example 1.25 scale off 16px: 12 · 16 · 20 · 25 · 31 · 39 · 49 · 61.

---

## Line height (inverse to size)

- **Small text (under 32pt):** line-height ≈ font-size × **1.6**. (16px body → ~26px leading.)
- **Large text (32pt+):** font-size × **1.3** down to **1.1** — big type needs tighter leading.
  (Gingerich.)

---

## Weight

- Use weight **extremes** for contrast: 100/200 against 800/900, not 400 against 600.
- Build hierarchy with **weight + size together**, not size alone.

---

## Letter-spacing (tracking)

- **Confident headings:** slightly tight, around **-0.01em**.
- **Body:** neutral (0).
- **Short uppercase labels only:** wider, **0.04–0.08em**.
- **Never wide-track body text** — it slows reading and reads as decorative filler.

---

## Colour of text (not pure black)

- Avoid pure `#000000` on white for body — use a dark grey/near-black to cut eye strain.
- Ensure text-on-image always has a contrast overlay; never place type on a busy field unaided.

---

## Spacing rhythm

- Establish one spacing unit (e.g. 4px or 8px) and use multiples of it throughout — consistent
  rhythm is what separates "designed" from "assembled."
