---
name: component-states-and-interaction-fidelity
description: Use when specifying the full INTERACTIVE-STATE FIDELITY of a single component — the
  spec-grade state matrix (default / hover / focus-visible / active-pressed / disabled / loading /
  selected-checked / error-invalid / read-only) and, critically, the TRANSITIONS between those
  states (what triggers each move, what the duration/easing is, what happens to focus and the
  cursor). Owns focus-visible to WCAG 2.4.7 / 2.4.11 / 1.4.11, target size 2.5.8, and the
  reduced-motion transition path. Triggers on "state matrix", "interactive states", "hover/focus/
  active states", "focus-visible spec", "focus ring", "disabled state", "selected state",
  "pressed/active state", "state transitions", "interaction fidelity", "per-component state table",
  or any review/QA of whether a component's states are all defined. This skill owns the per-component
  STATE FIDELITY spec; it pairs with `09…/component-library-architecture` (which owns the variant/
  API model) and `04…/empty-error-and-loading-states` (which owns empty/error/loading content-states).
status: active
metadata:
  portable: true
  category: 04-web-and-ui-design
  compatible_with:
    - claude-code
    - codex
---

# Component States & Interaction Fidelity — the state matrix and the moves between states

Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com, +256 784 464178.

<!-- dual-compat-start -->
## Use When
- Specifying the **full interactive-state matrix** of one component — every reachable cell of
  **default · hover · focus-visible · active/pressed · disabled · loading · selected/checked ·
  error/invalid · read-only** filled with a concrete, token-backed treatment, not left to chance.
- Specifying the **transitions between states** — the move from default→hover→active, the
  focus-in/focus-out behaviour, what happens to the cursor, the duration and easing of each move,
  and the reduced-motion fallback. The *matrix* says what each state looks like; **this skill also
  pins how the component travels between them**, which is where fidelity is usually lost.
- Writing the **focus-visible specification** to the WCAG 2.2 bar: a real, ≥3:1 indicator that is
  never obscured by sticky chrome, never `outline:none` with no replacement.
- Producing a **spec-grade state table** for a component sheet, QA gate, or dev handoff — the
  artifact a developer and a tester can both check off cell by cell.
- Reviewing/auditing a component for **state gaps** (the empty cell that ships as a bug).

## Do Not Use When
- You are deciding the component's **variant / size / API model** (intent enums, props vs slots,
  atomic level) — that is `09-design-systems-tokens-and-theming/component-library-architecture`.
  That skill owns the *axes*; this skill owns the *state cells and the transitions between them*.
- You are designing **empty / error-page / loading-content** states of a screen or flow (zero-data
  blank slates, 404/500, skeletons vs spinners, offline) — that is
  `04-web-and-ui-design/empty-error-and-loading-states`. It owns *content-level* states; this skill
  owns the *control-level* interactive states (hover/focus/active/disabled/selected) of one
  component. (A component's `loading` and `error` cells here link out to that skill for the
  region-level treatment.)
- You are defining the **token tiers/names** the states consume — use `design-tokens-and-naming`.
- You are choosing **motion language** for the whole product (a motion system, choreography) — use
  `08-motion-and-interaction/*`; here motion is scoped to per-state transitions and pulls durations
  from motion tokens.
- You only need **field-level** validation affordances inside a form — `04…/form-ux-design`.

## Required Inputs
- The **component** and which states it can actually *reach* (a link can't be `loading`; a trigger
  Button can't be `selected`). Run `references/state-matrix-method.md` to enumerate before designing.
- The **anatomy** of the component (its named parts) so each state names *which part* changes — use
  `references/component-anatomy.md` for the Book-3 per-component anatomy/number baseline.
- A **semantic token layer** to bind every state value to (`design-tokens-and-naming`): color
  per state, border, radius, **focus-ring**, and **motion durations/easing**. No literals.
- The **WCAG 2.2 AA floor** (`doctrine/references/wcag-2.2-criteria.md`) — focus-visible, target
  size, contrast, reduced motion, name/role/value.

## Workflow
1. **Enumerate the reachable states first; mark the rest N/A explicitly.** Run
   `references/state-matrix-method.md`. Fill only the states the component can enter; mark the
   others **N/A with the correct alternative** (e.g. a Button has no `selected` → use a
   ToggleButton with `aria-pressed`). A silently dropped cell is a state gap; an explicit N/A is a
   decision. **An empty cell is a bug, not a default.**
2. **Give every reachable state a token-backed treatment.** For each cell name what changes and
   to which token: bg / fg / border / shadow / cursor, on which **anatomy part**. Default, hover,
   active/pressed, disabled, loading, selected/checked, error/invalid, read-only. Bind to tokens
   (`--color-…-hover`, `--radius-control`, `--duration-fast`) — a literal hex/px in a state cell is
   a defect (`09…/component-library-architecture` §5; `doctrine/design-doctrine.md`).
3. **Specify focus-visible to the WCAG 2.2 bar — non-negotiable.** A visible indicator with
   **≥3:1 contrast** against *both* the component and the page (1.4.11, 2.4.7), an offset so it
   reads on every variant, and **never obscured** by sticky headers/footers (2.4.11). Distinguish
   `:focus` from `:focus-visible` (don't show the ring on mouse-press where it's noise; do show it
   for keyboard/AT). `outline:none` without a token-driven replacement is **forbidden**. Give
   `destructive`/danger controls a distinct-but-still-≥3:1 ring. See `references/state-matrix-method.md`
   §Focus and `doctrine/references/wcag-2.2-criteria.md`.
4. **Specify the transitions, not just the endpoints.** For each adjacent pair, state the
   **trigger** (pointerenter, pointerdown, blur, `aria-busy` set…), the **property animated**
   (bg/opacity/transform), the **duration + easing token** (`--duration-fast` ~120–160 ms for
   hover/press; instant for focus-ring appearance — never fade a focus ring in slowly), and the
   **reduced-motion path** (`prefers-reduced-motion` → drop transform/scale, keep an instant
   color/opacity change; the state must still be perceivable). Define focus-OUT and the
   loading→done / error→recovered return moves, not only the forward moves. Pressed `scale .98` is
   the canonical reduced-motion casualty — keep the state, drop the motion (2.3.3).
5. **Hold accessibility across *every* state, not just default.** Contrast holds in hover/active
   (1.4.3); **disabled ≠ invisible** and is communicated by more than color (1.4.1); **loading**
   exposes `aria-busy` + a live status and stays focusable but not activatable; **error/invalid**
   pairs color with text + `aria-invalid` + `aria-describedby`; **selected/checked** exposes
   `aria-pressed`/`aria-checked`/`aria-selected`. Target stays **≥24×24 CSS px** in every state
   (2.5.8), aiming 44×44 touch. Name/role/value correct per state (4.1.2).
6. **Emit the spec-grade table + transition table.** Produce the per-component artifact: an
   anatomy line, the **state matrix** (one row per state × the parts that change), the
   **transition table** (one row per adjacent move × trigger/property/duration/easing/reduced-
   motion), the focus-visible clause, and a per-state a11y line. This is the handoff a dev builds
   from and QA checks off. Use the worked `examples/input-state-matrix.md` as the pattern.
7. **Make the one authored choice and apply it systematically.** The convergent AI default is a
   flat control with a generic blue ring, no real pressed state, and a hover that just darkens.
   Make a *specific, defensible* move — a considered pressed shift, a brand focus ring, an
   intentional hover — and route it through tokens so it reads as one skilled hand across every
   state and variant (`doctrine/design-doctrine.md` §0).

## Anti-Patterns
- **State gaps.** default + hover only; focus-visible, active, disabled, loading, selected, error
  forgotten. The matrix exists so nothing is missed — an empty cell is a bug.
- **`outline:none` with no replacement** — the single most common a11y regression (2.4.7 fail).
- **Focus ring obscured** by a sticky header/footer (2.4.11 fail), or a ring under 3:1 (1.4.11).
- **Designing endpoints, not transitions** — the states look fine in static frames but the
  component snaps or jank-fades between them because no duration/easing/trigger was ever specified.
- **Ignoring reduced-motion** on hover/press/selection transitions (2.3.3).
- **State-by-color-alone** — disabled only paler, error only a red border, selected only a tint.
  Fails 1.4.1; pair with icon/shape/text/`aria-*`.
- **Hard-coded values in a state cell** — can't theme, can't go dark. Token it.
- **`:focus` styled like `:focus-visible`** so a mouse press flashes the keyboard ring (noise), or
  the reverse — suppressing the ring for keyboard users.
- **Loading that loses focus or shifts layout** — reserve label width; keep focus on the control.

## Outputs
- A **per-component state matrix**: every reachable state (default/hover/focus-visible/active/
  disabled/loading/selected/error/read-only) given a token-backed treatment; non-reachable states
  marked N/A with the correct alternative.
- A **transition table**: each adjacent state move with trigger, animated property, duration +
  easing token, and the reduced-motion fallback (incl. focus-out and loading/error returns).
- A **focus-visible specification** meeting 2.4.7 / 2.4.11 / 1.4.11.
- A **per-state a11y line** (contrast, target size, name/role/value, live regions, color-not-alone).
- A handoff-ready, cell-by-cell checkable spec for dev and QA.

## Examples
- See `examples/input-state-matrix.md` — a complete worked state-fidelity spec for one real
  component (a text Input / form field): anatomy, all nine interactive states each given a
  token-backed treatment, the **transition table** (focus-in/out, hover, error-appears, loading),
  the focus-visible clause to WCAG 2.4.7/2.4.11/1.4.11, and the per-state a11y notes. Never lorem.

## References
- `doctrine/design-doctrine.md` — the Anti-Slop Charter; §0 "looks human-made" applied to states
  and transitions (one authored move — pressed shift, brand focus ring — applied via tokens).
- `doctrine/references/wcag-2.2-criteria.md` — the a11y floor cited throughout: focus-visible &
  contrast (2.4.7, 1.4.11), focus-not-obscured (2.4.11), target size 24px (2.5.8), reduced motion
  (2.3.3), color-not-alone (1.4.1), name/role/value (4.1.2), live regions (4.1.3).
- `references/state-matrix-method.md` — the method: enumerate reachable states, the nine-state
  set, the focus-visible spec, and the transition-specification model.
- `references/component-anatomy.md` — the Book-3 (*How to Design Better UI Components*) per-component
  anatomy + numbers (button/input/dropdown/checkbox/card heights, paddings, hit areas) so each state
  names a real part with a real measure.
- Pair: `09-design-systems-tokens-and-theming/component-library-architecture` — owns the variant/
  size/API model; **this skill owns the per-component state fidelity** that fills its state column.
- Pair: `04-web-and-ui-design/empty-error-and-loading-states` — owns content-level empty/error/
  loading (skeletons, 404, offline); this skill owns control-level interactive states and links to
  it for the region-level loading/error treatment.
- Consumes: `design-tokens-and-naming` (state + motion tokens); aligns with `08-motion-and-interaction`
  for transition durations/easing.
<!-- dual-compat-end -->
