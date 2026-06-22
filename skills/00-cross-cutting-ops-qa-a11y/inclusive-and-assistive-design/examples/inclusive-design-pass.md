# Worked Example — Inclusive-Design Pass on a Clinic Appointment-Booking Flow

A pass that goes *beyond* WCAG 2.2 compliance (that floor is owned by
`accessibility-wcag-2-2-compliance`) into inclusive/assistive accommodations. Method: find the
**exclusions** per ability dimension, then design the accommodation. (Microsoft Inclusive Design:
solve for one, extend to many.)

## Flow audited
"Book an appointment" — 4 steps: choose service → pick date/time → enter details → confirm.
Already WCAG 2.2 AA-passing (contrast, focus, labels, target size). This pass asks: *who is still
excluded, permanently / temporarily / situationally?*

| Ability dimension | Exclusion found (persona) | Permanent / Temp / Situational | Accommodation designed |
|---|---|---|---|
| **Cognitive** | Anxious patient mis-reads a long dense form; abandons | Perm (dyslexia) / Temp (illness stress) / Sit (rushed) | One question per screen option; plain-language labels ("When works for you?" not "Select appointment slot"); progress + "you can stop and resume"; no time-pressure countdown |
| **Memory / load** | Re-enters the same info across steps | Perm (cognitive) / Sit (distraction) | Carry values forward (WCAG 3.3.7 + beyond): pre-fill from the patient record; a visible "what you've chosen so far" summary; no confirm-email field |
| **Low vision** (beyond contrast) | Can read at AA but loses place at 200% zoom on the date grid | Perm / Temp (eye strain) / Sit (sun glare) | Reflow date grid to a single-column list at zoom; spacing ≥ 1.5× line; respects OS text-size; offers a high-contrast + larger-text toggle that persists |
| **Motor** | Tremor mis-taps adjacent time slots | Perm (Parkinson's) / Temp (injured hand) / Sit (on a bus) | Time slots ≥ 48dp with ≥ 8dp gaps; generous hit area; no drag-to-select (tap alternative); undo on accidental confirm; switch/voice operable |
| **Assistive tech** | Screen-magnifier user loses the inline error far from the field | Perm | Error placed adjacent + announced (`aria-live`), and a summary at top that moves focus to the field; tested in VoiceOver + ZoomText |
| **Situational / temporary** | One-handed parent holding a child; low bandwidth | Sit | Thumb-reachable primary action; works image-off; SMS confirmation fallback (no app required); low-data mode |
| **Language / literacy** | Non-native speaker, low health-literacy | Perm / Sit | Plain language (grade-8); key terms have a tap-to-define; offers Swahili; icons + text, never icon-only |

## Outcome
12 accommodations, none of which weaken the AA baseline; 4 are "solve-for-one-extend-to-many"
wins (the resume-later, the carry-forward summary, the SMS fallback, and the persistent text-size
toggle help *everyone*, not just the target persona). Hand any new WCAG *conformance* checks to
`accessibility-wcag-2-2-compliance`; this pass is the inclusivity layer above it.

*Illustrative personas/values — copy the method, not the specifics.*
