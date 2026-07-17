# Worked example: exploration-to-pause interface

Evidence level: documented example only.

| State | Player question | Treatment and alternatives |
|---|---|---|
| Exploration | Where am I going and what can I inspect? | World landmark leads; compact objective appears on request; audio cue has subtitle/icon equivalent |
| Hazard | What changed and how urgent is it? | Persistent directional threat cue, contrast-safe edge marker, captioned sound and optional haptic |
| Dialogue | Who is speaking and what can I choose? | Large speaker/name region, controller focus, touch targets, history and auto-advance off by default |
| Pause | Can I safely stop, change settings, save or exit? | Immediate stable pause where authority permits; settings/save/exit are never covered by an ad |
| Resume | What changed while I was away? | Brief non-blocking recap and correct input prompts; no forced animation |

Controller, keyboard/mouse and touch share semantic actions but have distinct focus, prompt and target rules. Long names and translated objectives are included in the handoff content set. A post-level ad is conditional and only eligible after save completes and the map/continue choice is visible; decline, no-fill or SDK error returns to that choice without penalty.
