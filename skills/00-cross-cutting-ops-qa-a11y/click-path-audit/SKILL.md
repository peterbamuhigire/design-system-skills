---
name: click-path-audit
description: Use when debugging finds no crash but a button, toggle, or form action does nothing, or after a shared-state refactor. Trace each touchpoint for silent resets, races, stale closures, and final-state mismatches. Use design-qa-and-pre-launch-review for visual/a11y release gating; this is a behavioural-state audit.
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
  - claude-code
  - codex
---

# Click-Path Audit — Behavioural Flow Audit
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com. Imported and adapted from ECC's
community-sourced `click-path-audit` skill (PR-salvaged, attributed to `linus707`'s original
report). This is a debugging/state-tracing procedure, not an aesthetic judgment, so it does not
fall under the human-design-authority re-sourcing rule the same way a visual/typographic claim
would — its authority is the traced code itself, cited by file:line.

<!-- dual-compat-start -->
## Use When

- Systematic/root-cause debugging found no crash, no missing wiring, and no type mismatch, but a
  user still reports a button, toggle, or form action that "does nothing" or produces the wrong
  final state.
- After any refactor that touches a shared state store (Zustand, Redux, React context) — audit
  every consumer of the changed actions, not just the one you edited.
- Before release, on critical user flows (checkout, auth, data-mutating actions), as a targeted
  pass rather than the full visual QA gate.
- A component's individual functions all work in isolation, but the composed handler produces the
  wrong result — the classic sign of one call silently undoing another.

## Do Not Use When

- The bug is API-level (wrong response shape, missing endpoint, network failure) — that is
  systematic/root-cause debugging, not a state-trace problem.
- The issue is purely visual/layout — use direct inspection or `design-audit`.
- The issue is performance (jank, slow response) — use `performance-as-ux-and-core-web-vitals` or
  a profiler, not a state trace.
- You only need the final pre-ship visual + a11y + slop gate — use
  `design-qa-and-pre-launch-review`; pull this skill in first if a behavioural bug is suspected.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| The target area (page, component, or shared store) | User or bug report | yes | Scopes an audit that is expensive to run unbounded |
| Read access to the handler and store source | Codebase | yes | The trace is done by reading actual call order and side effects, not by guessing |
| The button/control's stated intent (its label or spec) | UI copy or spec | yes | The audit's verdict is "does final state match what the label promises" |

## Workflow

1. **Map every state-store action before auditing any touchpoint.** For each Zustand
   store/Redux slice/React context action in scope, document what fields it **sets** and,
   critically, what fields it **resets as a side effect** that it does not own. This map is the
   audit's load-bearing artefact — the canonical bug this skill was built to catch (a "New Email"
   button that called `setComposeMode(true)` then `selectThread(null)`, where `selectThread`
   silently reset `composeMode` back to `false`) is invisible without it.
   ```
   STORE: emailStore
     setComposeMode(bool) -> sets: {composeMode}
     selectThread(thread|null) -> sets: {selectedThread, ...} RESETS: {composeMode: false, ...}
   DANGEROUS RESETS (actions that clear state they don't own):
     selectThread -> resets composeMode (owned by setComposeMode)
   ```

2. **For each interactive touchpoint (button/toggle/form submit) in scope, trace the handler in
   call order.** For every function call: what does it read, what does it write, does it have a
   side effect on shared state, does it reset/clear state as a side effect. Then check:
   - Does a later call **undo** a state change an earlier call made (Sequential Undo)?
   - Are there async calls whose resolution order is not guaranteed, producing a race (Async
     Race)?
   - Does a closure capture a **stale** value across two sequential calls in the same handler
     (Stale Closure — e.g. `setCount(count+1); setCount(count+1)` incrementing by 1, not 2)?
   - Does the handler only validate/flag without performing the actual action the label promises
     (Missing State Transition)?
   - Is a branch's guard condition always false at that point in the flow (Conditional Dead Path)?
   - Does a `useEffect` watching the same field the handler just set immediately reset it
     (useEffect Interference)?

3. **Check the final state against the label's promise.** The audit's core question is not "did
   the code run" but "does the resulting UI state match what the control's label told the user
   would happen." A handler with no crash, correct types, and full wiring can still fail this.

4. **Record each finding with a trace, not just a conclusion:**
   ```
   CLICK-PATH-NNN: [severity]
     Touchpoint: [Button label] in [file:line]
     Pattern: [Sequential Undo / Async Race / Stale Closure / Missing Transition / Dead Path / useEffect Interference]
     Trace: 1. [call] -> sets {field: value}
            2. [call] -> RESETS {field: value}  <- CONFLICT
     Expected: [what the label promises]
     Actual: [what actually happens]
     Fix: [specific fix]
   ```

5. **Scope the audit to the actual risk.** A full-app audit is expensive — reserve it for launch
   or after a major refactor, and split it across parallel agents by page/area, with the state-map
   step (step 1) run once and shared as input to every other agent, since it must complete before
   the per-area traces can be trusted.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| Systematic debugging reports "no bugs found" but users report a broken control | Run this audit on that control before looking elsewhere | The actual bug (a silent state reset) is invisible to crash/type-level debugging |
| A shared-store action was just modified | Audit every consumer of that action, not only the edited call site | A caller relying on the old reset behaviour breaks silently |
| Full-app audit requested | Run the state-store map (step 1) first, as shared input to all subsequent area audits | Per-area audits without the shared map re-derive it inconsistently or skip it |
| A finding is reported | Cite file:line and the literal call trace, not a general description | An unverifiable claim cannot be fixed or reviewed |

## Capability Contract

Read access to the component/handler and state-store source is required; this is a static trace,
not a runtime observation, so no execution capability is required to complete it (though running
the flow to confirm a finding is preferred where available). Editing is allowed only when a fix is
explicitly requested.

## Degraded Mode

Without read access to the actual store/handler source, this skill cannot produce a verifiable
finding — report that the audit could not run rather than guessing at a plausible-sounding bug.
Without the ability to run the flow, mark each finding as a static-trace hypothesis rather than a
confirmed reproduction, and say so explicitly in the report.
Stop the audit when the required source or stated control intent is unavailable; record the gap
and do not infer a failure from an unobserved path.

## Anti-Patterns

- **Skipping the state-store side-effect map** and going straight to tracing handlers — the map is
  what makes an invisible reset visible; without it the audit misses the exact bug class it exists
  to catch.
- **Reporting a finding without file:line and the literal call trace** — unverifiable claims waste
  the fix cycle.
- **Running a full-app audit with no shared state map**, so parallel agents re-derive inconsistent
  or partial maps.
- **Treating "no crash, no type error, correctly wired" as proof of correctness** — this is exactly
  the false-negative pattern systematic/root-cause debugging produces on this bug class.
- **Confusing this with a visual or performance audit** — it traces state, not pixels or timing.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| State-store side-effect map | Engineering, subsequent audits | Every in-scope action's sets/resets documented, dangerous resets flagged |
| Click-path finding(s) | Engineering | Each finding cites file:line, a literal call trace, expected vs actual, and a specific fix |

## Examples

- `examples/sequential-undo-worked.md` — the canonical "New Email button does nothing" bug: full
  state-store map, handler trace, and finding write-up, reproduced from the case that motivated
  this skill.

## References

- Pairs with `00-cross-cutting-ops-qa-a11y/design-qa-and-pre-launch-review` (the broader pre-ship
  gate; run this skill first when a behavioural bug is suspected, then the full gate).
- Provenance: ECC community-sourced `click-path-audit` skill. Imported near-verbatim because its
  content is a debugging procedure (verifiable against actual code, cited by file:line), not a
  design/aesthetic recommendation — it does not require re-sourcing to human design authority the
  way a typographic or colour claim would.
<!-- dual-compat-end -->
