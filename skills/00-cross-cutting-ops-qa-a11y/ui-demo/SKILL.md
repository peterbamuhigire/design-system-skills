---
name: ui-demo
description: Use when recording a web-application demo video, screen recording, walkthrough, or tutorial with Playwright. Produces a WebM with an injected cursor, paced story, and discovered/rehearsed selectors. Use demo-driven-design-process to decide what to demo; this skill records it.
metadata:
  portable: true
  category: 00-cross-cutting-ops-qa-a11y
  compatible_with:
  - claude-code
  - codex
---

# UI Demo Video Recorder
Acknowledgement: Shared by Peter Bamuhigire, techguypeter.com. Imported and adapted from ECC's
`ui-demo` skill. This is a production/engineering mechanism (Playwright automation), not a design
opinion, so it is imported close to source rather than re-sourced to design authority — its
correctness is verifiable by running it, which is the discipline this skill itself enforces
(Discover -> Rehearse -> Record).

<!-- dual-compat-start -->
## Use When

- The user asks for a "demo video," "screen recording," "walkthrough," or "tutorial video" of a
  web application.
- Showcasing a feature or workflow visually for documentation, onboarding, or a stakeholder
  presentation.
- You already have `demo-driven-design-process`'s answer to *what* to show and need the actual
  recording produced.

## Do Not Use When

- The deliverable is a static screenshot or a design mock, not a video — use ordinary capture.
- The task is deciding what flow deserves a demo in the first place, or crafting the narrative
  around it — that is `05-ux-process-research-and-psychology/demo-driven-design-process`; this
  skill takes that decision as an input.
- No Playwright-automatable target exists (native mobile app, desktop app) — this skill is
  web-only.

## Required Inputs

| Artefact or context | Source | Required? | Why |
|---|---|---|---|
| A running instance of the target web app | User or project | yes | Discovery and recording both require a live target |
| The flow/story to demonstrate | User, or `demo-driven-design-process` output | yes | Determines the script's step order |
| Playwright installed in the project | Project | yes | The recording mechanism itself |

## Workflow

Three phases; never skip discovery or rehearsal before recording.

### Phase 1 — Discover
Before writing any script, navigate to each page in the flow and dump its actual interactive
elements (inputs, selects, buttons, `contenteditable` regions) via a `page.evaluate` DOM walk.
**Do not assume field types** — a "dropdown" may be a custom combobox, not a native `<select>`; a
comment box may support `@mentions`/`#tags`. Record exact button label text, which fields are
required, and whether content appears dynamically after other fields are filled. Output a field
map per page (see `references/discover-and-rehearse.md`).

### Phase 2 — Rehearse
Run every step **without recording**, using an `ensureVisible` helper that logs and fails loudly
on any selector that does not resolve, dumping the actual visible elements on failure so the
correct selector can be found immediately. Fix every failing selector and re-run until rehearsal
passes clean. Silent selector failures during an actual recording are the main reason demo
recordings break — rehearsal exists to catch them before a wasted take. See
`references/discover-and-rehearse.md` for the full helper and script structure.

### Phase 3 — Record
Only after discovery and rehearsal both pass:
1. **Storytelling flow.** Entry (login/navigate) -> Context (pan the surroundings) -> Action (the
   main workflow) -> Variation (a secondary feature) -> Result (outcome/confirmation), unless the
   user specifies a different order.
2. **Pacing.** After login 4s; after navigation 3s; after a button click 2s; between major steps
   1.5-2s; after the final action 3s; typing delay 25-40ms per character.
3. **Cursor overlay.** Inject an SVG arrow cursor that follows `mousemove`, re-injected after
   **every** navigation (the overlay is destroyed on navigate).
4. **Never teleport the cursor.** Move to the target (`page.mouse.move` with `steps: 10`) before
   clicking; every click/type helper takes a descriptive `label` for debugging.
5. **Type visibly**, not instant-fill — `pressSequentially` with a per-character delay.
6. **Smooth scroll**, not jump-scroll, for content reveal.
7. **Pan dashboards** — move the cursor across key elements (max ~6) rather than a static shot.
8. **Subtitles.** A bottom subtitle bar (`Step N - Action`, under ~60 characters), re-injected
   after every navigation alongside the cursor overlay, cleared during long pauses.
   Full helper code (`injectCursor`, `ensureVisible`, `moveAndClick`, `typeSlowly`,
   `injectSubtitleBar`, `showSubtitle`, `panElements`) and the script template:
   `references/recording-helpers.md`.

## Decision Rules

| Condition | Action | Wrong-choice failure |
|---|---|---|
| A selector fails during rehearsal | Fix it and re-run rehearsal before recording | Silent failure discovered mid-recording, wasted take |
| Field type not yet confirmed | Discovery's DOM dump, not assumption | Script written against the wrong element type breaks |
| Cursor overlay after a page navigation | Re-inject `injectCursor`/`injectSubtitleBar` | Overlay is destroyed on navigate; cursor disappears silently |
| A popup/new tab opens mid-flow | Capture the popup page explicitly | `context.close()` at the end otherwise misses a separate video stream |

## Capability Contract

Execution (Playwright, a running target app) is required for all three phases — this skill cannot
produce a verified result without it. Read access to the target app's rendered DOM is required for
Discovery. Editing is scoped to the demo script itself.

## Degraded Mode

Without a running target app or Playwright available, produce the script structure and field-map
template only, explicitly marked as unrehearsed and unrecorded — never claim a recording exists
without having actually run Phase 3.
Stop before recording if discovery or rehearsal has not passed; retain the failure log and fix the
selector or environment before attempting another take.

## Anti-Patterns

- **Skipping Discovery and assuming field types/labels** — the primary cause of scripts that break
  against the real UI.
- **Recording before Rehearsal passes** — silent selector failures show up mid-take instead of
  being caught cheaply beforehand.
- **Cursor/subtitle overlay not re-injected after navigation** — disappears without warning.
- **Teleporting the cursor** directly to click targets — reads as robotic, not a human demo.
- **Silent `catch` blocks in helpers** — swallows exactly the failures rehearsal exists to surface;
  every helper must log a warning on failure.
- **Assuming a placeholder select option (`value="0"`, text containing "Select...") is real data.**
- **Leaving the output video at a random Playwright-generated path** instead of copying it to a
  stable, named output file.

## Outputs

| Artefact | Consumer | Evidence and acceptance condition |
|---|---|---|
| Field map per page (Discovery) | Rehearsal script authoring | Every selector used in the demo script traces to a confirmed element |
| Passing rehearsal run | Recording phase | `ensureVisible` reports OK for every step before recording starts |
| WebM demo video at a stable output path | Documentation, onboarding, stakeholders | Cursor and subtitle overlays present throughout; no unhandled script errors during the run |

## Examples

- `examples/demo-script-template.md` — the full Playwright script template (helpers +
  discover/rehearse/record phases wired together) ready to adapt to a specific flow.

## References

- `references/discover-and-rehearse.md` — the DOM-dump discovery snippet and the `ensureVisible`
  rehearsal helper, with the rehearsal script structure.
- `references/recording-helpers.md` — cursor overlay, subtitle bar, `moveAndClick`, `typeSlowly`,
  and `panElements` helper implementations, plus the pacing table.
- Pairs with `05-ux-process-research-and-psychology/demo-driven-design-process` (decides what to
  demo) and `browser-qa`-equivalent skills for functional verification before recording.
- Provenance: ECC `ui-demo` skill, imported close to source — a Playwright production mechanism,
  verifiable by running it, not a design-authority claim requiring re-sourcing.
<!-- dual-compat-end -->
