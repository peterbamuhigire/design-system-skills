# Error placement taxonomy — Inline / Detour / Blocking

Podmajersky's error pattern (from *Strategic Writing for UX*, 2nd ed.) splits errors **by how much
they interrupt** the person — *where* the error appears and *how disruptive* it is. This is the
companion to the severity→channel map in `error-message-formula.md` §4: severity tells you the
**stakes**; this taxonomy tells you the **interruption** and therefore the **message style**. Use
them together — the two agree most of the time, and where they diverge, the interruption level
decides the wording.

Provenance: Podmajersky, *Strategic Writing for UX* 2nd ed. (the Errors pattern, split three ways by
interruption). Pairs with WCAG 2.2 (3.3.1, 3.3.3) — see `error-message-formula.md`.

---

## The three placements

| Placement | Where it appears | How disruptive | The person can… | Message style |
|---|---|---|---|---|
| **Inline** | *Beside or under the thing* that's wrong — the field, the row, the cell. The rest of the screen is untouched. | Lowest — nothing else stops. | …keep working everywhere else and fix this in place. | **Terse, located, corrective.** Name the subject + the fix. No reason needed if the fix is obvious. |
| **Detour** | *In the flow but redirecting it* — a panel, an inline block, or a step that offers a **different path** to the goal. The original path is blocked but an alternative exists. | Medium — the path changes, the goal doesn't. | …take the offered alternate route to still get what they came for. | **Instruction-most-prominent.** Lead with the *alternative action*, not the diagnosis. The detour (what to do instead) is the headline; the cause is secondary. |
| **Blocking** | *Over or instead of the screen* — a modal dialog or a full page. Nothing proceeds until it's resolved. | Highest — the flow halts. | …only decide or dismiss; they cannot continue past it. | **Calm, complete, decision-framing.** State what happened, reassure (data/money safe), give the one decision. Earn the interruption — never block for something fixable in place. |

---

## How to choose

1. **Can the person fix it right where they are, without leaving the screen?** → **Inline.**
   (A bad email, a too-short password, a past date.) Default to inline — it's the least disruptive
   and keeps the person in flow.
2. **Is the original path blocked, but a genuine alternative gets them to the same goal?** →
   **Detour.** (Account not found → *create one*; this card declined → *use another card*; search
   empty → *try a wider range*.) The detour's defining move: **the instruction (the alternate path)
   is the most prominent words**, because that's what un-sticks the person. A Detour is a Blocking
   error that you were kind enough to give an exit from — prefer it whenever an exit exists.
3. **Must the flow stop for a decision or because nothing can proceed?** → **Blocking.**
   (Destructive confirmation; session expired; 403/404/500; maintenance.) Reserve it — a Blocking
   message for something the person could have fixed inline is the most common over-interruption.

> **The downgrade rule.** Always push an error *down* the interruption ladder if you can:
> Blocking → Detour (add an alternate path) → Inline (let them fix it in place). The best error is
> the one the person barely notices because the fix was right there.

---

## Style per placement — worked

**Inline** (terse, located):
> **Phone numbers need 10 digits — you entered 9.**

**Detour** (instruction most prominent — the alternate path leads):
> **Use another card to finish — your bank declined this one. Nothing was charged.**
> *(not "Your card was declined. [reason]. You could use another card." — the action leads, the
> diagnosis follows.)*

**Blocking** (calm, complete, one decision):
> **You've been signed out after a while away.** Your work is saved. Sign in again to pick up where
> you left off. `[ Sign in ]`

---

## Mapping to the severity→channel map

| Interruption (this file) | Typical severity (formula §4) | Typical channel |
|---|---|---|
| **Inline** | inline | field error text |
| **Detour** | persistent (sometimes transient) | banner, inline block, or a non-modal panel offering the alternate path |
| **Blocking** | blocking | modal dialog or full page |

They usually agree. When a message *feels* blocking but a real alternate path exists, write it as a
**Detour** (action-led) and host it in the least disruptive channel that still gets seen — that is
the kinder, more usable choice.
