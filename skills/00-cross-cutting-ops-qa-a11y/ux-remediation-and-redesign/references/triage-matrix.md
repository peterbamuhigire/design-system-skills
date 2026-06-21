# Reference: The Triage Matrix — sequencing the fixes

The prioritisation engine inside Phase 2 of `references/remediation-lifecycle.md`. It turns a flat
list of audit findings into a **defensible, ordered fix queue**. Without it, remediation order is
vibes ("fix the homepage, it's visible") — which is exactly the failure this file prevents.

Three lenses stack, then two override rules bind. Source: Maioli's *Fixing Bad UX Designs* (2018)
triage stack (Travis severity + effort-impact + MoSCoW + frequency weighting + business
alignment), updated to 2026 with the doctrine's hard-gate caps.

---

## Lens 1 — Red-route severity (the Travis test)

For each finding, answer three yes/no questions. The "red route" is a **critical path** — the few
flows that, if broken, break the business (sign-up, checkout, the core job-to-be-done). Identify
red routes *before* triaging; everything off them is a side road.

| Q | Question | Weighs |
|---|---|---|
| 1 | Is the finding **on a red route** (a critical path)? | business reach |
| 2 | Is it **hard for users to overcome** (no workaround, blocks the task)? | user pain |
| 3 | Is it **persistent / recurring** (hits every session, not a one-off)? | frequency |

Score the answers:

| Yes count | Severity | Meaning |
|---|---|---|
| 3 (or Q1+Q2) | **Critical** | on a red route AND blocking — fix first, full stop |
| 2 | **Serious** | meaningfully degrades a real flow |
| 0–1 | **Minor** | annoyance, edge case, or off the critical path |

A finding off every red route, easily worked around, seen once = **Minor**, however ugly. A
finding on checkout that blocks the task every time = **Critical**, however small the code change.

---

## Lens 2 — Effort × Impact (the quadrant)

Plot each finding on two axes. **Impact** = how much it hurts customers / the business if unfixed
(use the Travis severity as the impact proxy). **Effort** = design + dev cost to fix (token swap =
low; IA restructure, new component, re-platform = high).

```
            HIGH IMPACT
                │
  MAJOR PROJECT │ QUICK WIN        ← do the quick wins first,
  (schedule it) │ (do first)         then schedule the major projects
 ───────────────┼───────────────  EFFORT →
  THANKLESS     │ FILL-IN
  (avoid/defer) │ (when idle)
                │
            LOW IMPACT
```

| Quadrant | Impact | Effort | Action |
|---|---|---|---|
| **Quick win** | High | Low | **Do first** — best return per hour |
| **Major project** | High | High | **Schedule** — worth it, needs a slot |
| **Fill-in** | Low | Low | Batch when capacity is idle |
| **Thankless** | Low | High | **Defer / drop** — rarely justified |

The default build order is: **all quick wins → major projects → fill-ins → (thankless usually
never)**. Lens 3 then constrains this to the release.

---

## Lens 3 — MoSCoW (scope this release)

Bucket each finding for the **current** release window:

| Bucket | Meaning |
|---|---|
| **Must** | release fails its purpose without it (every gate-failer lands here — see overrides) |
| **Should** | important, painful to omit, but the release still works without it |
| **Could** | desirable; include only if effort allows |
| **Won't** (this time) | explicitly out of scope now — recorded, not forgotten |

MoSCoW is **per release**; a "Could" this sprint can be a "Must" next. Record the "Won'ts" so they
re-enter triage later rather than vanishing.

---

## The two override rules (these bind the lenses)

The lenses *propose*; these rules *bind*. They exist because the quadrant alone can mis-rank the
two things doctrine treats as non-negotiable.

1. **Gate-failing finding ⇒ always Must.** Any finding that fails a hard gate — **AI Slop**,
   **WCAG 2.2 AA**, or **Core Web Vitals** (`design-audit/references/audit-rubric.md` §1) — is a
   **Must**, regardless of where the effort-impact quadrant places it. A contrast failure that
   *looks* like a low-effort/low-impact token tweak is still a legal-floor / charter blocker and
   **caps the audit score until cleared**. It cannot be deferred to "Could."

2. **Frequency weighting ⇒ promote.** A finding seen **repeatedly** across research/tests outranks
   one seen **once**. A single-session test artifact is weaker evidence than a pattern; promote the
   recurring issue and treat the one-off as Minor until corroborated. (Business alignment rides
   here too: a conversion-blocking or KPI-denting finding outranks an aesthetic one at equal
   severity — money and red routes beat polish.)

---

## The combined scoring table (copy into the plan)

Run every finding through all three lenses, apply the overrides, sort:

```
| Finding (anti-pattern) | Red-route? | Hard? | Persistent? | Severity | Impact | Effort | Quadrant     | Gate? | MoSCoW | Rank |
|------------------------|-----------|-------|-------------|----------|--------|--------|--------------|-------|--------|------|
| Contrast fail (D3)     | Y (signup)| Y     | Y           | Critical | High   | Low    | Quick win    | A11y  | Must   | 1    |
| Keyboard focus (—)     | Y         | Y     | Y           | Critical | High   | Low    | Quick win    | A11y  | Must   | 2    |
| Slow/shifting hero(—)  | Y (entry) | Y     | Y           | Critical | High   | Med    | Quick win    | CWV   | Must   | 3    |
| Banned-font type (D2)  | N         | N     | Y           | Serious  | High   | Med    | Major project| Slop  | Must   | 4    |
| Missing states (C2)    | Y         | Y     | N           | Serious  | Med    | Med    | Major project| —     | Should | 5    |
| Uniform cards (D6)     | N         | N     | Y           | Minor    | Low    | Low    | Fill-in      | —     | Could  | 6    |
| Pure-white surfaces    | N         | N     | N           | Minor    | Low    | Low    | Fill-in      | —     | Won't  | —    |
```

**Rank** = sort by (1) Must-gate-failers first, by severity then effort; (2) remaining Musts; (3)
Shoulds by quadrant; (4) Coulds. "Won'ts" drop out of this release with a recorded reason.

> The example rows mirror the Aurora Analytics findings from
> `design-audit/examples/design-audit-filled.md`; the full worked remediation that consumes this
> ranking is in `examples/checkout-remediation-worked.md`.

---

## How to read the output

The top of the queue is what the team builds **this** sprint: the gate-failing quick wins that
lift the score caps with the least effort. The middle is scheduled work. The bottom is recorded and
deferred. Every position is **justified** by the three lenses and the two overrides — which is the
whole point: a stakeholder can see *why* contrast beats card-styling, not just *that* it does.

---

*Provenance: Maioli, *Fixing Bad UX Designs* (2018) — Travis red-route severity, effort-impact
matrix, MoSCoW, frequency weighting, business alignment — updated to 2026 with the doctrine's
three-gate caps (`design-audit/references/audit-rubric.md`) as a hard override. Right-pattern codes
(D1–D6, B1–B3, C1–C4, A2–A3) index `doctrine/references/interaction-anti-patterns.md`.*
