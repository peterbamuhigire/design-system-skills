# Reference: The AI-Slop Banned Font List

**Rule:** None of these may appear as a **primary typeface** in any generated artifact —
website, DOCX, PPTX, PDF, or UI — regardless of how convenient or "clean" they seem. They are
the statistical centre of AI output and a recognisable tell of unconsidered, machine-generated
work.

---

## 1. Hard ban (primary offenders)

- **Inter** — the single most recognisable AI tell; "the Comic Sans of AI." Banned outright.
- **Roboto**
- **Arial**
- **Open Sans**
- **Lato**
- **Bare system-font stacks used alone** — e.g. `-apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif`
  with no deliberate typeface layered on top.

## 2. Secondary ban (the "I tried" upgrades)

The fonts AI reaches for *after* being told to avoid the first list. Equally forbidden as a
default reflex — they are second-order slop:

- **Space Grotesk** — the most common "escape attempt." Do **not** treat it as the safe
  distinctive choice.
- **Poppins**
- **Montserrat**
- **Nunito** / **Nunito Sans**
- **Source Sans Pro / Source Sans 3** *as a standalone "neutral upgrade"* — Source Sans 3 is
  permitted **only** as a body face paired with a distinctive display font (see the workhorse
  note in `font-groups-and-usage.md`), never alone and never as the headline.

---

## 3. Why the ban matters

Chwezi products compete on looking intentionally designed and trustworthy. The moment a
deliverable opens in Inter (or on a generic system stack), a discerning client reads it as
"no one thought about typography," which corrodes the premium positioning across the whole
portfolio and every external client deliverable shipped under the Chwezi Core Systems name.

---

## 4. Edge cases

- **Code/monospace inside a technical artifact** may legitimately need a monospace face — use
  an approved one (JetBrains Mono, IBM Plex Mono, Fira Code), never Roboto Mono or Consolas
  as a *design* choice.
- **A client brand guideline that mandates a banned font** overrides this list for that client
  only — state it explicitly, record it, and do not generalise it to other work.
- **Body text** may use an approved workhorse; the ban targets *defaults chosen without
  thought*, not every sans-serif in existence.

When unsure whether a face is slop, treat it as slop and pick a deliberate alternative from
`font-groups-and-usage.md`.
