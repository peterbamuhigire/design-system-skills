# The Fidelity Ladder

**Provenance:** Chwezi Design Doctrine, group 05 (UX process). Synthesised from the established
HCI/UX-process literature on iterative low-cost prototyping (Buxton, *Sketching User Experiences*;
Snyder, *Paper Prototyping*; the Nielsen Norman Group fidelity guidance). Per the doctrine's
sourcing rule (`doctrine/design-doctrine.md` §2), authority here is the human design literature,
not AI-tool defaults.

## The one rule: fidelity is a cost, not a goal

Every increase in fidelity costs more to make and more to change, and biases reviewers toward
critiquing polish instead of structure. So the question is never "how good can I make this look" —
it is **"what is the lowest fidelity that resolves the decision this artifact exists to make?"**
Pick that rung. Climb only when a lower rung has done its job and a real, named question remains
that only higher fidelity can answer.

Two independent dials are often confused:

- **Fidelity** = how *finished* it looks (sketch → pixel-perfect).
- **Interactivity** = how much it *responds* (static → fully clickable/coded).

You can have a clickable lo-fi prototype (paper + "Wizard of Oz", or grey boxes wired in Figma) and
a static hi-fi mockup (a polished but dead PNG). Choose each dial for what you must test — see the
matrix at the end.

---

## The five rungs

### 1. Paper / quick sketch
- **What it is:** hand-drawn screens, marker on paper or whiteboard. Minutes per screen.
- **For:** generating and comparing *many* concepts fast; thinking with your hands; aligning a room
  in one session. Buxton's point — sketches are for *getting the right design*, before prototypes
  refine *the design right*.
- **Right when:** the space is open, you have several competing ideas, or you are exploring a flow's
  shape. Earliest, cheapest divergence.
- **Cannot tell you:** anything about precise layout, real content fit, visual hierarchy, or feel.
- **Interactivity option:** "paper prototyping" — a facilitator swaps sheets as the user "taps".
  Tests navigation and labels with zero tooling.

### 2. Lo-fi wireframe
- **What it is:** clean boxes-and-lines, greyscale, placeholder rectangles for media, real-*ish*
  labels and content lengths. Built fast in a wireframe tool or with simple shapes.
- **For:** validating **content priority, layout structure, and reading order** without the
  distraction of colour or type. The default working fidelity for most flow design.
- **Right when:** the concept is chosen and you need to get the *structure* right — what's on the
  screen, in what order, what the primary action is.
- **Cannot tell you:** brand feel, exact spacing/type decisions, or whether a transition feels good.
- **Interactivity option:** click-through to test **findability and navigation** — "can the user get
  from A to the saved state?"

### 3. Mid-fi greybox
- **What it is:** structure plus *real* spacing, true type scale, and accurate component sizing — but
  still greyscale (no brand colour, no final imagery). "Greyboxing."
- **For:** pressure-testing **hierarchy, density, and real content fit** — does the headline survive
  a 60-character title? does the card grid breathe at the true type scale? Resolves layout questions
  lo-fi is too loose to answer, without paying for visual design.
- **Right when:** structure is settled and you need to know it *holds up* at production sizing and
  content, before colour enters and starts hiding spacing sins.
- **Cannot tell you:** colour contrast, brand expression, motion feel.

### 4. Hi-fi mockup
- **What it is:** full visual design — colour, real type, imagery, final-ish copy, real components.
  Pixel-accurate, but typically still a *static* representation.
- **For:** validating **desirability and visual hierarchy**, getting sign-off, and serving as the
  source for handoff. This is where doctrine craft (typography, colour, layout) properly enters.
- **Right when:** structure and flow are *already validated* at lower fidelity and the remaining
  risk is look/feel, brand, or stakeholder approval.
- **Cost warning:** changes here are expensive. Do not arrive here to discover a structural problem
  a lo-fi test would have caught for 1/5 the effort.

### 5. Clickable / coded prototype
- **What it is:** wired and responsive — either a prototyping-tool click-through of hi-fi screens, or
  real front-end code for the slice. Can include real transitions, timing, and (coded) live data.
- **For:** testing what only motion and response can reveal — **transition clarity, perceived
  performance of waits, gesture feel, and technical feasibility**. A coded prototype also de-risks
  build.
- **Right when:** the *interaction itself* is the risk (a novel gesture, a tricky async wait, a
  multi-step flow whose feel matters), or you must prove feasibility before committing engineering.
- **Cost warning:** the most expensive rung. Reserve interactivity for the specific transitions or
  timings under test — do not wire the whole app to validate one path.

---

## Fidelity-vs-interactivity matrix — pick by what you must learn

| You must learn… | Fidelity | Interactivity | Typical artifact |
|---|---|---|---|
| Which of several concepts is worth pursuing | Paper sketch | Static (or paper-swap) | Sketch set, side by side |
| Is the content priority / layout right | Lo-fi wireframe | Static | Annotated wireframe |
| Can users find the path through the flow | Lo-fi wireframe | Clickable | Lo-fi click-through / wireflow |
| Does the layout hold at real type & content | Mid-fi greybox | Static | Greybox screens |
| Is it desirable; does the brand land; sign-off | Hi-fi mockup | Static | Hi-fi comp |
| Do transitions read; does the wait feel okay | Hi-fi | Clickable | Clickable prototype |
| Is the interaction technically feasible / does the gesture feel right | Hi-fi | Coded | Coded prototype of the slice |

**Reading the matrix:** climb the *fidelity* column only as the question demands; turn on
*interactivity* only for the transitions/timings under test. Most flow risk is resolved in the top
four rows — cheaply, before any pixel or line of code.

## When to make it clickable (decision shortcut)
Make it clickable **only if** the thing you must validate lives in the *transitions* — findability
of a path, clarity of a navigation model, the feel of a wait, or the legibility of a multi-step
sequence. If the open question is about a *single screen's* structure, content, or look, a static
artifact answers it for far less. Clickability is a tool for testing **motion through the system**,
not a badge of seriousness.

## Tie-back to doctrine
A wireframe is still an *authored* artifact (`design-doctrine.md` §0). Even greyscale boxes encode
deliberate choices — grid, reading order, the single primary action. Reflexively dropping
evenly-spaced cards is the AI-mean default the doctrine exists to defeat (§2); make the layout
choice on purpose, just without paying for colour and type yet.
