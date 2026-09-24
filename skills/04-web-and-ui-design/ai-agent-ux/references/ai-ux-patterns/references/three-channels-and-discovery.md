# Capturing Intent and Getting AI Features Found

**When to read:** when designing the input side of an AI feature (how people tell it what they
want) and its entry point (how people find it). The output side lives in `ai-output-design`;
agentic behaviour in `ai-agentic-ui`.

## 1. Inputs to gather

- The common operations people perform with the feature, from research or analytics.
- What the product already knows at the moment of use (selection, open file, page, locale, plan).
- How often, and how urgently, people need the feature.

## 2. Three ways intent reaches the system

| Channel | Carries | Design rule | Failure if ignored |
|---|---|---|---|
| Context the product already has | Selection, open document, page, device, locale, time | Show it as visible, editable context chips ("Using: selected paragraph", "Location: Kampala") | The system acts on assumptions the person cannot see or correct |
| What the person types or says | Free-text or voice requests | Offer it, but never alone; add starter prompts and controls | People stare at an empty box not knowing what to ask |
| Controls the person operates | Sliders, selectors, format buttons, selection handles | Turn the most common parameters into controls | Every adjustment needs a re-typed prompt |

**Decision rule:** when the common operations are known, build a hybrid of controls plus a
free-text field for the long tail. Keep chat-only interfaces for open-ended exploration. Test the
choice with your own users; published comparisons favour hybrids but products differ.

## 3. Structured request composer

For tasks where people under-specify requests, replace the blank prompt with four slots:

| Slot | Control | Pre-fill |
|---|---|---|
| Situation | Short text field | From the context the product already has |
| Action | Verb selector (summarise, draft, translate, compare) | Most common action |
| Result settings | Length, audience, format, tone as controls | Last used or plan default |
| Example | Paste or upload "make it like this" | Optional |

## 4. Where to put the entry point

Plot each AI feature on two axes before designing its entry point:

|  | Person rarely seeks it | Person actively seeks it |
|---|---|---|
| **Product rarely offers it** | Let people find it: empty-state hints, onboarding mentions, examples from peers; no interruptions | Make it one step away: visible button, command palette, keyboard shortcut |
| **Product offers it when it notices a signal** | Offer with a clear reason and an unmistakable "Not now" and "Never" | Run it automatically with a visible summary and a prominent Undo |

Entry-point families:
1. **Triggered by input** - slash or @ commands, gestures, empty-state prompts; for people who
   know roughly what they want.
2. **Triggered by context** - offered because of the current content or task ("This looks like a
   tenancy agreement; check the clauses?").
3. **Proactive** - the system starts, from an anomaly or prediction; use sparingly and always
   allow dismissal.
4. **Progressive** - advanced features unlock as usage shows readiness, with short contextual
   tutorials.

## 5. Starter prompts are positioning

Starter prompts show what the product is for. Write them from the product's own data and
integrations, vary them with context (day, document type, plan), and refresh them like content.
A school-management system's starter might be "List pupils with fees unpaid after 30 days by
class", not "Write a professional email".

## 6. Anti-patterns

- A free-text box as the only way to use a feature with well-known common operations.
- Hidden context the person cannot see or correct.
- Proactive suggestions with no dismissal or "never again".
- Generic starter prompts that could belong to any product.
- A separate "AI" tab that strips the feature of the context that makes it useful.

## 7. Example (original)

A Kenyan logistics dashboard adds AI route summaries. Context chip: "Using: today's 42
deliveries, Nairobi depot". Controls: summary length, audience (driver or manager), language
(English or Kiswahili). Free text handles unusual questions. Entry point: dispatch managers seek
it daily, so it sits as a visible button; a proactive offer appears only when late deliveries pass
a threshold, with "Not now" and "Stop suggesting".

## See also

- `skills/ai-ux-patterns/SKILL.md`, `skills/ai-output-design/SKILL.md`, `skills/ai-agentic-ui/SKILL.md`.

Sources: Macfadyen, *Designing AI Interfaces* (O'Reilly, 2025) for the intent channels and the
discovery grid; the four-slot composer adapts Nielsen Norman Group's CARE prompt structure.
