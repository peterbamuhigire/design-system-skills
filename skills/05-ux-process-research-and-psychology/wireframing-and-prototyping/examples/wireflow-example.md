# Worked Example — Wireflow for "Save a Search & Get Notified"

A real, branch-complete wireflow for a sample feature on a property-listings web app (Maduuka-style
marketplace). Shows the fidelity decision, the screen inventory, the decision/response wiring, the
real branches (success / error / empty / first-run / loading), and the pair-with-research test plan.
Content is representative, not lorem.

---

## 0. The feature
A user has run a search ("3-bed houses, Kololo, under UGX 800m"). We want them to **save that
search** and **get notified** when new matching listings appear, so they return to the app.

## 1. Fidelity decision (state it first)
- **The artifact's job:** resolve *structure and flow* — does the save+notify path make sense, can
  users find it, and are the empty/error/permission branches handled? **Not** look or feel yet.
- **Chosen rung:** **lo-fi wireframe, made clickable** for the path only.
  - *Why this rung:* the risk is findability and flow logic (especially the notification-permission
    and empty-result branches), which lo-fi resolves at ~1/5 the cost of hi-fi. Per
    `references/fidelity-ladder.md`, "can users find the path" → lo-fi + clickable. We climb to
    hi-fi only after this is validated.
  - *Why not hi-fi:* colour/type here would be fidelity theatre (`design-doctrine.md` §0) and would
    bias reviewers toward the gradient instead of the journey.

## 2. Screen inventory (lo-fi, greyboxed media)
| # | Screen | Key blocks (top → bottom) | Primary action |
|---|---|---|---|
| S1 | Search results | Search bar (filled query) · result count · **[Save this search]** · result cards (greybox images) | Save this search |
| S2 | Save-search sheet | Title (editable, prefilled "3-bed Kololo <800m") · notify toggle (default ON) · frequency (Instant / Daily) · **[Save]** | Save |
| S3 | Notify-permission prompt | Explanation line · **[Enable alerts]** · [Not now] | Enable alerts |
| S4 | Saved confirmation | Success line · "Manage in Saved Searches" link · **[Done]** | Done |
| S5 | Saved Searches list | List of saved searches · per-row: last-match date, edit, delete | (manage) |
| S6 | Notification → matches | New-match count header · matching result cards | open listing |

## 3. The wireflow — screens wired by user decision + system response
Notation: `Screen --[user decision]--> ( system response ) --> Screen`

```
S1 Results
  │
  └─[tap Save this search]
        │
        ├─( signed in )──────────────► S2 Save-search sheet
        │
        └─( NOT signed in )──────────► Sign-in screen ──(success)──► S2
                                              └─(cancel)──► back to S1

S2 Save-search sheet
  │
  └─[tap Save]
        │
        ├─( notify toggle ON & OS permission NOT yet granted )──► S3 Permission prompt
        │        │
        │        ├─[Enable alerts]──( OS grants )──► S4 Confirmation
        │        ├─[Enable alerts]──( OS denies )──► S4 Confirmation (banner: "Saved. Alerts off — enable in Settings")  ◄ recovery branch
        │        └─[Not now]────────────────────────► S4 Confirmation (in-app alerts only)
        │
        ├─( notify ON & permission already granted )──► (save) ──► S4 Confirmation
        │
        ├─( notify OFF )──────────────────────────────► (save) ──► S4 Confirmation (no alerts)
        │
        └─( save FAILS — network )──► S2 with inline error  ◄ ERROR branch
                                       "Couldn't save. Retry?" · [Retry] → re-attempt save

S4 Confirmation ──[Done]──► back to S1 (now shows "Saved ✓" state on the Save button)
S4 Confirmation ──[Manage…]──► S5 Saved Searches list

— later, async —
( new listing matches a saved search )
  ├─( OS alerts enabled )──► OS notification ──[tap]──► S6 Matches
  └─( OS alerts off )──────► in-app badge on Saved Searches ──[open]──► S6 Matches
```

## 4. The real branches (this is what makes it a wireflow, not a screen list)
- **First-run vs return:** not-signed-in detour at S1→S2; signed-in users skip it.
- **Permission grant / deny / defer:** three outcomes at S3, each with a *different* end state — the
  most common place this feature is designed badly (assuming "Enable" always succeeds).
- **Empty result on the saved search at save time:** if the current query has **0 results**, S1
  shows a zero-state and the **[Save this search]** button changes label to "Save & notify when
  available" — saving an empty search is a *valid* and valuable case. (Empty-state visual spec is
  out of scope here → `empty-error-and-loading-states`, group 04; we only wire the branch.)
- **Loading branch:** S6 fetch shows a skeleton list, not a spinner-on-blank — the wireflow notes a
  loading state so the perceived-performance wait is designed, not discovered
  (`doctrine/references/web-performance-budgets-2026.md`).
- **Error + recovery:** the save-fails inline error on S2 with retry; the permission-denied recovery
  banner on S4. Happy-path-only would have hidden both.

## 5. Interactivity scope (what we actually wire)
Clickable **only** along: S1 → S2 → S3 (all three permission outcomes) → S4 → back to S1. That is
the path whose *findability and branch logic* is the open question. We do **not** wire S5 management
or live data — those aren't the risk. (Matrix: "can users find the path" → lo-fi + clickable; we add
no fidelity beyond that.)

## 6. Pair with research to test it (hand to `ux-research-and-usability-testing`)
- **Method:** moderated, think-aloud, 5 participants (3 first-time/not-signed-in, 2 returning).
- **Tasks:** (a) "You like these results — set it up so the app tells you when new ones appear."
  (b) "You'd rather not get phone notifications, just see it in the app." (tests the *Not now* path)
- **Success criteria:** finds **[Save this search]** unaided; completes save; makes a *deliberate*
  choice at the permission prompt (not a blind tap); understands the end state ("am I getting
  alerts?").
- **What we're really testing:** is the permission step understood, and is the off/denied end state
  clear? Those are the branches lo-fi can validate now, cheaply.

## 7. After validation → promote, don't restart
Fold findings back as **lo-fi edits** (e.g. if users miss the Save button, move it before iterating
visuals). Once flow is settled, hand the annotated wireflow to **group 09** (handoff / tokens /
components) for hi-fi — starting from resolved questions, not a blank canvas. Only at that hi-fi
stage do typography, colour, and target-size/contrast checks
(`doctrine/references/wcag-2.2-criteria.md`) properly enter.
