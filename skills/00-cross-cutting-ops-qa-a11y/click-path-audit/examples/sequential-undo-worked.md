# Worked Example: Sequential Undo ("New Email" button does nothing)

The case that motivated this skill (ECC source material). Reproduced as the worked template.

## Step 1 — state-store map (excerpt)

```
STORE: emailStore
  setComposeMode(bool) -> sets: {composeMode}
  selectThread(thread|null) -> sets: {selectedThread, selectedThreadId, messages, drafts,
    selectedDraft, summary} RESETS: {composeMode: false, composeData: null, redraftOpen: false}
  setDraftGenerating(bool) -> sets: {draftGenerating}

DANGEROUS RESETS (actions that clear state they don't own):
  selectThread -> resets composeMode (owned by setComposeMode)
```

## Step 2 — touchpoint trace

```
TOUCHPOINT: "New Email" button in ThreadList.tsx:142
  HANDLER: onClick -> {
    call 1: useEmailStore.getState().setComposeMode(true)   sets {composeMode: true}
    call 2: useEmailStore.getState().selectThread(null)     RESETS {composeMode: false}  <- CONFLICT
  }
  EXPECTED: Clicking "New Email" opens the compose pane (composeMode: true)
  ACTUAL: composeMode ends false; the button visibly does nothing
  VERDICT: BUG — Sequential Undo
```

## Step 3 — finding

```
CLICK-PATH-001: CRITICAL
  Touchpoint: "New Email" button in ThreadList.tsx:142
  Pattern: Sequential Undo
  Handler: inline onClick
  Trace:
    1. setComposeMode(true) -> sets {composeMode: true}
    2. selectThread(null)   -> RESETS {composeMode: false}  <- CONFLICT
  Expected: compose pane opens
  Actual: compose pane never opens; no error, no crash
  Fix: call selectThread(null) BEFORE setComposeMode(true), or have selectThread accept an
       options flag ({ preserveComposeMode: true }) so it does not reset a field it does not own.
```

## Why prior debugging missed it

- The handler has an onClick (not dead code).
- Both `setComposeMode` and `selectThread` exist and are correctly imported (no missing wiring).
- Neither function throws (no runtime error).
- The argument types are correct (no type mismatch).

All four are exactly what systematic/root-cause debugging checks — none of them catches a
handler that runs correctly end-to-end but produces the wrong final state because a later call
silently reset an earlier one's effect.
