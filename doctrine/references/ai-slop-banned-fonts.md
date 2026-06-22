# Reference: The AI-Slop Banned Font List

**Rule:** None of these may appear as a **primary typeface** in any generated artifact —
website, DOCX, PPTX, PDF, or UI — regardless of how convenient or "clean" they seem.

**Evidence basis — and a hard asymmetry principle.** AI-vendor sources are admissible as
evidence ONLY for what to **BAN**, NEVER as authority for what to **APPROVE**. An AI tool
confessing *"I converge on X"* is the strongest possible evidence that X is a tell; an AI tool
saying *"use Y"* is worthless as approval grounds, because the tool's own recommendations are
exactly what the next wave of AI output will converge on. **Approvals trace only to human design
authority** — typographers, type foundries, and the design literature (Bonneville, Vignelli,
Segall; see `pairing-principles.md`).

Applying that: Anthropic's **Claude Cookbook**, *"Prompting for frontend aesthetics"* (the AI
vendor itself), is cited here **only as the AI confessing its own convergence** — verbatim:
*"Overused font families (Inter, Roboto, Arial, system fonts)"*, *"Never use: Inter, Roboto,
Open Sans, Lato, default system fonts"*, and on Space Grotesk: *"You still tend to converge on
common choices (Space Grotesk, for example)… Avoid this."* That is valid ban-evidence.
Its *recommendation* list (which includes several of our approved faces) is **deliberately not
used as a reason to approve anything** — those faces earn their place on human-design grounds,
and we note the convergence risk on any the cookbook also happens to push. Corroborated by
Vercel/shadcn defaults and designer commentary; verified via the digital-research engine's
source-verification pass (2026-06-21).

> **Label every ban by its failure mode — they are not all the same.** Three distinct reasons:
> **[AI]** = genuine AI-ecosystem default / tell · **[POP]** = generic-popular & overused (reads
> as "no design," predates AI) · **[SYS]** = lazy system default. Only **[AI]** is truly an "AI
> tell"; all three are still banned as a *primary* typeface for Chwezi work, but stating the
> right reason keeps the doctrine honest.

---

## 1. Hard ban (primary offenders)

- **Inter** — **[AI]** the single strongest tell; "the Helvetica of the LLM era"; shadcn's
  historic `--font-sans` default. Banned outright.
- **Geist** — **[AI]** *added 2026-06-21.* Vercel's own font, now the **v0 / shadcn / Vercel
  template default that replaced Inter** — the modern successor AI tell. Banned outright.
- **Roboto** — **[POP/AI]** on the Cookbook list; also the #1 Google Font and Android/Material
  system face. Banned.
- **Open Sans** — **[POP]** Cookbook "never use"; ~#2 Google Font. Banned.
- **Lato** — **[POP]** Cookbook "never use"; ~#3 Google Font. Banned.
- **Arial** — **[SYS]** "lazy default," reads as no-design. Banned as a deliberate choice.
- **Bare system-font stacks used alone** — **[SYS]** e.g. `-apple-system, BlinkMacSystemFont,
  "Segoe UI", sans-serif` with no deliberate face layered on top. (Note: a *deliberate,
  documented* system-font fallback chain is different — see `system-font-fallbacks.md`.)

## 2. Secondary ban (the "I tried" upgrades)

The fonts AI reaches for *after* being told to avoid the first list. Banned as a default reflex
for Chwezi work — but note the honest evidence label:

- **Space Grotesk** — **[AI]** named by the Claude Cookbook as *the* convergence trap. The most
  common "escape attempt." Do **not** treat it as the safe distinctive choice.
- **Instrument Serif** — **[AI]** *added 2026-06-21.* Repeatedly named as the AI serif-accent
  reflex. Avoid as the default serif accent.
- **Poppins** — **[POP]** *generic-popular cliché, weak AI-specific evidence.* Kept on the ban
  list as a Chwezi house rule (overused), but the honest reason is "modern-startup cliché," not
  "AI tell."
- **Montserrat** — **[POP]** ~#4 Google Font; popular human default. Banned as overused, not as
  an AI signature.
- **Nunito / Nunito Sans** — **[POP]** no direct AI-tell evidence found; banned as a Chwezi
  house preference (rounded-friendly cliché), not on evidence grounds.

## 3. Conditional — Source Sans 3 (paired body only)

- **Source Sans 3 / Source Sans Pro** — a competent, human-designed text face (Adobe / Paul D.
  Hunt). It is **overused as a standalone "neutral upgrade,"** so it is **banned as a primary /
  display / standalone face** but **permitted as a quiet paired body face** beneath a
  distinctive display font — matching the original Chwezi rule and the workhorse note. This is a
  human-design / overuse judgement, **not** an "an AI tool recommended it" approval.

---

## 4. Why the ban matters

Chwezi products compete on looking intentionally designed and trustworthy. The moment a
deliverable opens in Inter or Geist, a discerning client reads it as "no one thought about
typography," which corrodes the premium positioning across the portfolio and every external
client deliverable shipped under the Chwezi Core Systems name.

## 5. Edge cases

- **Code/monospace** in a technical artifact may need a monospace face — use an approved one
  (JetBrains Mono, IBM Plex Mono, Fira Code), never Roboto Mono as a *design* choice.
- **A client brand guideline that mandates a banned font** overrides this list for that client
  only — state it explicitly, record it, do not generalise it.
- **A deliberate device-common fallback** (e.g. Georgia, the system stacks in
  `system-font-fallbacks.md`) is **not** slop — slop is the *thoughtless* default, not every
  pre-installed face used on purpose.

When unsure whether a face is slop, treat it as slop and pick a deliberate alternative from
`font-groups-and-usage.md`.

## 6. Living refresh rule

Font defaults move. Before adding, removing, or reclassifying a banned face, run
`skills/00-cross-cutting-ops-qa-a11y/slop-doctrine-refresh-and-research-loop/` and
`doctrine/references/living-slop-refresh-protocol.md` with the digital-research engine's source
evaluation discipline. Record the observed shift, evidence grade, design consequence, scope, and
date checked. Weak evidence becomes a watchlist note, not a hard ban.
