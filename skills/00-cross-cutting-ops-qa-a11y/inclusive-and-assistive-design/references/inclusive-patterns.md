# Reference: Inclusive & Assistive Patterns (by ability dimension)

The accommodation playbook for designing **above** the WCAG 2.2 AA floor. The floor itself —
target-size 24px minimum, reflow at 200%/320px, 3.3.7 redundant entry, 2.5.7 dragging
alternatives, contrast minimums — is certified by `accessibility-wcag-2-2-compliance` against
[`doctrine/references/wcag-2.2-criteria.md`](../../../../doctrine/references/wcag-2.2-criteria.md).
**Everything here assumes the floor is met and pushes past it.** Source model: Microsoft
Inclusive Design (persona spectrum / "solve for one, extend to many" / mismatched-interaction
framing); W3C Cognitive Accessibility (COGA) guidance; WCAG 2.2 as the baseline to exceed.

---

## Persona spectrum — frame every ability as permanent → temporary → situational

Disability is a **mismatch between a person and their environment**, not a personal health
attribute. The same interaction barrier excludes a far larger group than the permanently
disabled population once you include temporary and situational mismatches. Design for the
**permanent** end and you serve the whole spectrum.

| Ability dimension | Permanent | Temporary | Situational |
|---|---|---|---|
| **Vision** | Blind / low vision | Cataract, post-eye-surgery, eye infection | Bright sunlight, glare, cracked screen, dim room |
| **Hearing** | Deaf / hard of hearing | Ear infection, blocked ear | Noisy café, must keep phone muted, no headphones |
| **Motor / dexterity** | Missing/limited limb, tremor, paralysis | Sprained wrist, arm in a cast, RSI flare | Holding a baby, carrying bags, gloves, on a moving bus |
| **Speech** | Non-verbal | Laryngitis, sore throat | Strong accent vs voice control, must stay quiet |
| **Cognitive** | Learning disability, ADHD, memory impairment | Concussion, medication side-effect | Sleep-deprived new parent, stressed, distracted, second language |

**Rule of thumb:** "solve for one, extend to many." Captions made for Deaf users serve everyone
in a noisy bar; one-handed reach for an amputee serves every parent holding a child; plain
language for a cognitive disability serves every stressed or second-language reader.

---

## Exclusion audit — the method

Walk the real flow step by step. At each step, for each ability dimension, ask: **"Who gets a
mismatch here, and why?"** Record it as *interaction → who is excluded → why → accommodation*.
Name the **interaction barrier**, not the person.

| Flow step | Dimension | Who is excluded (P/T/S) | Why (the mismatch) | Accommodation (above floor) |
|---|---|---|---|---|
| _e.g._ "Enter the 12-digit code" | Cognitive / motor | tremor (P), tired (S) | must hold 12 digits + type precisely | accept any spacing, autofill, paste, save-and-resume |

P = permanent, T = temporary, S = situational. Prioritise barriers that hit a primary task or a
large temporary/situational population. The worked example applies this end to end.

---

## Cognitive accessibility — reduce three loads

The largest, most-ignored exclusion. Aim below your audience's reading ceiling (often ~Grade 8 /
lower-secondary) and design so people don't have to *remember, calculate, or decode*.

**1. Plain language (intrinsic load).**
- Short sentences; one idea each; common words over jargon; active voice; front-load the point.
- Define the few unavoidable terms inline; expand acronyms on first use.
- Use lists and clear headings so the eye can skim; avoid walls of text.
- *Owner of the actual words:* `10-content-design-and-ux-writing`. Set the **target** here
  (reading level, tone), hand off the crafting.

**2. Memory load (working memory).**
- Never make people carry a value across screens — persist it, prefill it, show it back.
- Keep instructions **beside** the step they govern, not on a prior screen.
- Show a **summary/review before commit** so nothing must be held in the head.
- Prefill what you already know (extends WCAG 3.3.7 well past its minimum).
- One primary action per screen; reduce choices to the relevant set (Hick's law).

**3. Error tolerance (recoverable mistakes).**
- **Forgiving input:** accept spaces/dashes in card & phone numbers, any date format you can
  parse, trim whitespace — don't reject what you could interpret.
- **Prevention before correction:** inline help and examples *before* the field; constrain with
  good defaults and pickers.
- **Cheap recovery:** undo, confirm destructive actions, **save-and-resume** long flows, never a
  dead-end. Error messages say *what happened, where, and how to fix it* — in plain language,
  tied to the field.
- **No tight timers** (WCAG 2.2.1 is the floor; here, prefer *no* time pressure at all on
  cognitive tasks, or generous, extendable limits).

---

## Low vision — beyond the contrast minimum

Meeting 4.5:1 is the floor, not legibility. (Palette/contrast ramps are owned by
`02-color-brand-and-visual-identity/accessible-color-and-contrast`; this sets the
low-vision *experience* targets.)

- **Zoom & reflow past the floor.** WCAG asks for 200% / 320px. Design to stay usable at **400%**
  and OS text-enlargement — no truncated labels, clipped buttons, overlap, or horizontal scroll
  of body text. Use relative units (`rem`/`em`, `ch`), fluid layouts, container queries.
- **Respect text-spacing overrides** (WCAG 1.4.12 is the floor). Layout must survive user CSS:
  line-height ≥1.5, paragraph spacing ≥2× font size, letter-spacing ≥0.12em, word-spacing
  ≥0.16em. Design *comfortably* above the minimum: roomy line-height, measured line length
  (~45–75 chars), real paragraph spacing.
- **Reading & dyslexia-friendly options.**
  - A clean **reading mode** (strip chrome, single column, generous spacing).
  - Let users choose a **dyslexia-friendly typeface and looser spacing**; never justify body
    text (rivers of white space hurt tracking); left-align.
  - Avoid pure `#000` on pure `#FFF` glare — offer a softer light theme and a true **dark mode**;
    honour `prefers-color-scheme`.
  - Don't rely on colour alone for meaning (pair with icon/text); honour high-contrast OS modes.
- **Typeface choice** follows the engine font doctrine — pick legible, open-aperture faces from
  the approved categories; **no banned defaults**, even for the "accessible option".

---

## Motor / dexterity — beyond the 24px target

- **Comfortable targets, not minimum ones.** 24px is the WCAG floor; make the *norm* 44×44px
  (Apple HIG) / 48dp (Material), larger for primary actions and tremor/one-handed use, with
  generous spacing so a slip doesn't hit the neighbour.
- **Forgiving interactions.** Always provide a tap/click/key path — no precision drags (extends
  WCAG 2.5.7), no hover-only reveals, no fine-motor gestures as the only route. Big hit areas
  (extend the clickable region past the visible icon). No tight time limits.
- **One-handed reach.** Put primary actions in the thumb zone on mobile; avoid forcing two-handed
  stretches or top-corner taps for common actions.
- **Switch access.** Ensure a logical, predictable single-switch **scan order** (follows DOM/
  reading order), clear focus highlight, and that every action is reachable without a
  sustained/precise gesture. Group related controls so scanning isn't endless.
- **Voice control (Voice Control / Voice Access).** Every actionable control needs a **stable,
  visible name** that matches its accessible name, so "tap *Pay now*" works. Avoid icon-only
  controls with no visible label, and duplicate ambiguous names.
- **Dwell / eye-gaze.** No action may require holding a precise gesture; provide click-equivalent
  dwell targets that are large and well-separated.

---

## Assistive-tech compatibility — test the experience, not the validity

Valid ARIA is necessary but not sufficient. Walk the **whole flow** with each tool and judge the
*experience*:

- **Screen readers** (NVDA + Firefox/Chrome on Windows; VoiceOver + Safari on macOS/iOS;
  TalkBack on Android): is the reading order sensible? Are there real **headings** to navigate by?
  Are dynamic changes **announced** (polite live regions) without chatter? Are controls named with
  *purpose* ("Pay £42.10", not "button")? Decorative images silent, meaningful ones described?
- **Screen magnifier** (OS zoom at 2–4×): when focus moves or feedback appears, does it show up
  **where the magnified viewport is looking**? Off-screen errors/toasts are invisible at high
  zoom — anchor important feedback near the action or focus.
- **Voice control:** can you drive the flow by speaking visible labels? Are there unlabeled or
  duplicate-named controls that block it?
- **Switch / dwell:** can you complete the primary task with one switch and a logical scan, no
  precise gesture, no timeout?
- **OS reading/dyslexia tools, Reader mode, Immersive Reader:** does your content survive being
  re-flowed by them (semantic HTML, real text not images of text)?

A control can be WCAG-valid and still read as noise. Fix the *experience*, not just the audit.

---

## Situational & temporary — make the default robust

Bake these into the baseline so the product holds up in the real world:

- **One hand / on the move:** thumb-reachable primary actions; tolerant of imprecise taps.
- **Glare / outdoors:** don't rely on subtle contrast or thin type; offer a high-contrast path.
- **Muted / noisy:** never rely on sound alone — pair audio cues with visual/haptic; caption media.
- **Slow / expensive / flaky connection:** lightweight, resilient, offline-tolerant; save-and-resume;
  optimistic UI with clear recovery. Hand the budget to `performance-as-ux-and-core-web-vitals`.
- **Tired / stressed / distracted / second language:** low memory load, plain language, one clear
  next step, forgiving errors — the cognitive accommodations above serve this population directly.

---

## Provenance
Microsoft Inclusive Design toolkit (persona spectrum; "recognise exclusion, solve for one,
extend to many"; mismatched-interaction definition of disability). W3C WAI Cognitive
Accessibility (COGA) objectives. WCAG 2.2 (w3.org/TR/WCAG22/) as the **floor** these patterns
exceed — see [`wcag-2.2-criteria.md`](../../../../doctrine/references/wcag-2.2-criteria.md).
All font/option choices remain subject to the Anti-Slop Charter in
[`design-doctrine.md`](../../../../doctrine/design-doctrine.md) §2.
