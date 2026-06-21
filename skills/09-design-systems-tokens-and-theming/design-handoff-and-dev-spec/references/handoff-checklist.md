# Reference: The Handoff Readiness & Completeness Checklist

A handoff is "ready" when a developer can build the unit with **zero design questions** and a
reviewer can sign it off with **zero judgement calls**. This checklist is the gate. If any line
fails, the design is not ready to hand off — fix the design or the spec, do not push the gap onto
the developer. Provenance: Figma Dev Mode handoff practice, Nielsen Norman Group design-spec
guidance, the GOV.UK / GitHub Primer / Atlassian handoff conventions, and the Chwezi doctrine
(`doctrine/design-doctrine.md` §0, §2).

---

## A. Readiness — is there even a design to hand off?

- [ ] **The unit is named and scoped.** One component, or one screen with its components listed.
- [ ] **The library components it composes are identified** with name + variant + version
      (`Button / primary / md @ library v2.3`), not re-described from scratch.
- [ ] **Tokens exist and are named.** The semantic role names this spec will cite are real and come
      from `09-…/design-tokens-and-naming` — not invented in the handoff.
- [ ] **Every required frame exists** (see section B). A missing frame = not ready.
- [ ] **Open questions are closed.** No "designer to confirm" notes. An open question in a handoff
      becomes a developer guess.

## B. Frame completeness — the frames the spec is drawn from

Missing frames are the #1 cause of low-fidelity builds. Require ALL of:

- [ ] **Default / resting** state.
- [ ] **Every variant** (size, emphasis, type) the screen actually uses.
- [ ] **Every interactive state:** hover, focus-visible, active/pressed, disabled, loading,
      selected/checked, read-only — whichever apply to each control.
- [ ] **Every feedback state:** error / invalid, success, warning, info.
- [ ] **Every content/data edge case:** empty / zero-items, single item, typical, overflow / many
      items, the **longest realistic + longest localized** string (account for ~30–40% expansion;
      pair with `00-…/internationalization-and-rtl-design` if RTL is in scope).
- [ ] **Every breakpoint / container size** the design supports — and the *intermediate* behaviour
      between them (fluid vs snap), not just the two endpoints.
- [ ] **Loading / skeleton** and **error** frames for any async region (not a blank box).
- [ ] **Dark mode** (and any other theme), if the product themes — each theme is its own set of the
      above where it differs.

## C. Per-element redline completeness — for each element in the frame

- [ ] **Box model:** width/height behaviour (fixed / fill / hug / min / max).
- [ ] **Spacing:** internal padding (inset tokens) and gaps to siblings (stack/inline gap tokens) —
      as **token references**, resolved value in parentheses for sanity only.
- [ ] **Layout primitive:** flex/grid, direction, wrap, justify, align — so auto-layout is rebuilt,
      not pixel-approximated.
- [ ] **Type:** the type token / role (`text.body.md`), not a raw size+weight pair.
- [ ] **Colour:** fill, text, border, icon — all as **semantic token names**, never raw hex.
- [ ] **Radius, border, elevation/shadow:** token references.
- [ ] **Iconography:** which icon (from the icon set), size token, colour token.

## D. Behaviour & motion

- [ ] **What each control does** — the action / navigation / mutation.
- [ ] **Validation rule and timing** — what's checked and *when* (on change / blur / submit).
- [ ] **Async behaviour** — loading affordance, optimistic vs pending, success path, error path.
- [ ] **Focus management** — where focus goes on open/close/submit/error.
- [ ] **Motion** — duration + easing **tokens**, trigger, what it communicates, and the
      **`prefers-reduced-motion` fallback**. (Pairs with `08-…/motion-and-interaction`.)

## E. Accessibility annotations (inline on the spec, not post-launch)

`doctrine/references/wcag-2.2-criteria.md`:

- [ ] **Semantic role / element** — `<button>` vs `<a>` vs `<div role=…>`; landmark/heading level.
- [ ] **Accessible name** and its source (visible label / `aria-label` / `aria-labelledby`).
- [ ] **Focus order** is specified and logical; **focus-visible** ring is a named token, **≥3:1** vs
      adjacent surface (WCAG 1.4.11 / 2.4.11–2.4.13).
- [ ] **Keyboard interactions** — Enter / Space / Esc / arrow / Tab behaviour per control.
- [ ] **Live-region announcements** for async, validation, and toast/error.
- [ ] **Target size ≥ 24×24px** (WCAG 2.5.8), or the spacing exception is noted.
- [ ] **No colour-only signalling** — every state also has text / icon / shape (WCAG 1.4.1).
- [ ] **Contrast** — text ≥4.5:1 (≥3:1 large), UI/icon/focus ≥3:1, asserted per theme.

## F. Acceptance criteria & sign-off

- [ ] **Each criterion is binary and token-specific** — pass/fail with no judgement
      (see `redline-and-spec-format.md`). "Matches Figma" is not a criterion.
- [ ] **Criteria cover:** visual (tokens), every state, responsive behaviour, behaviour/validation,
      motion + reduced-motion, and the full a11y set above.
- [ ] **Owner + version** on the sheet; date; link to the source frames.
- [ ] **The criteria are testable** by a reviewer and, where possible, by visual-regression /
      interaction tests.

---

> **The one-line gate:** if a developer would have to *guess* anything, or a reviewer would have to
> *interpret* anything, the handoff is incomplete. Author the decision; don't outsource it to the build.
