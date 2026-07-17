# Worked example: paddle impact feedback

Evidence level: parameterised design example, not an implemented or player-observed result.

| Phase | Feedback | Alternative and gate |
|---|---|---|
| Input | Paddle pose changes immediately; quiet input tick | No haptic required; visible pose remains authoritative for input recognition |
| Contact | Short local splash, directional audio, one impact haptic, brief camera impulse on the lateral axis | Reduced: no camera impulse, fewer particles; haptic-off preserves all meaning |
| Result | Boat heading and wake change only when simulation confirms force | Never show success before authority; online scope must be defined by engineering |
| Recovery | Camera settles before the next steering decision; reticle/horizon remain stable | Repeated impacts must not accumulate shake or obscure the landing path |

The tuning log must identify build, device, input method, frame pacing, parameter set, capture and player observation. “More satisfying” is `not assessed` until representative players compare labelled variants.
