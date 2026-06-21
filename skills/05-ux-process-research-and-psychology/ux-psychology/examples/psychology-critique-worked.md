# Worked Psychology Critique — One Real Screen Through Named Lenses

A single screen, critiqued through five named human authorities. Each finding states what the principle predicts, what the screen actually does, and the **design change** the principle implies. This is the output shape the skill should produce: not abstract theory, but findings tied to changes you can ship.

---

## The screen under review

**Context:** Desktop checkout page for a mid-market specialty-coffee subscription (premium brand, ~$28/mo plan). One primary user task: **complete the subscription purchase**. The page is the pain peak of the whole funnel, so it carries disproportionate weight.

**What is on the screen, top to bottom:**

1. A sticky header: logo (centre), and in the far top-right a small group of three same-styled text items — `Account` · `Help` · `Cart (1)`.
2. A two-column body. Left column: an order-summary card with the same background colour as the page (no border, no shadow), holding the plan name, price, and a thumbnail.
3. Right column: a form of **11 fields shown at once** — email, first name, last name, address line 1, address line 2, city, region, postcode, card number, expiry, CVC.
4. Each field has its label *above* it, with **equal vertical spacing** between every element (label-to-input gap = input-to-next-label gap).
5. A blue underlined line of text mid-form: "Delivery every 4 weeks — change frequency". It is *not* a link; it is a static descriptor styled blue and underlined.
6. Two buttons of identical size, colour, and weight sit side by side at the bottom: `Place order` and `Save for later`.
7. A 13-character order reference is printed as `A1B2C3D4E5F6G`.
8. Validation errors, when they occur, are collected in a red list at the **top of the page**; the form is **cleared on a failed submit**.

---

## Lens 1 — Gestalt grouping (Wertheimer / Koffka, via the skill's Gestalt section)

**Proximity — finding.** Equal spacing around every label and input means the eye cannot tell which label binds to which field. Proximity says elements closer together are read as one unit; equal gaps destroy that signal, so the form reads as an undifferentiated stack rather than discrete questions.
**Change:** tighten the label-to-input gap and widen the gap between successive fields (e.g. 6px label-to-input, 20px between fields). No borders needed — spacing alone does the grouping.

**Similarity / Common Region — finding.** The order-summary card shares the page background with no border or shadow, so it does not read as a distinct object (figure/ground fails; Common Region has no visible boundary). The user does not perceive "this is your order" as a bounded group.
**Change:** give the summary card a visible boundary — a subtle shadow or 1px border and a faint surface tint — so it reads as one grouped region separated from the page ground.

**Figure/Ground — finding.** Because the summary blends into the background, the priced item the user is committing to is the *least* visually present element on a purchase screen.
**Change:** raise the card's contrast against the page; it should be unambiguously foreground.

---

## Lens 2 — Nielsen's 10 heuristics (Jakob Nielsen)

**H9, Help users recover from errors — finding.** Errors are pooled in a red list at the top, far from the offending fields, and the form is **cleared on failed submit**. This is the single most damaging defect on the screen: it forces re-entry of correct data and breaks the [what went wrong] + [what to do] standard.
**Change:** show each error inline beside its field on blur; never clear valid fields; repopulate everything and highlight only the invalid inputs. Message format: "Card number looks incomplete — enter all 16 digits."

**H5, Error prevention — finding.** No inline validation; the user discovers problems only at submit.
**Change:** validate on blur, show format hints in labels ("Postcode, e.g. SW1A 1AA"), and disable `Place order` until required fields are valid (with a tooltip saying why).

**H8, Aesthetic and minimalist / H4, Consistency — finding.** Two equal-weight buttons (`Place order`, `Save for later`) give the primary action no visual priority, and `Help` looks identical to `Cart`. Consistency of *type* is broken: actions of different importance share one treatment.
**Change:** one primary CTA only — `Place order` as the single high-emphasis button; demote `Save for later` to a quiet text/secondary style.

**H1, Visibility of system status — finding.** No described press/processing state on the submit button.
**Change:** on press, disable + spinner; show an explicit success state on completion.

---

## Lens 3 — Norman's affordances and signifiers (Don Norman)

**False affordance / missing signifier — finding.** The blue underlined "Delivery every 4 weeks — change frequency" carries every web signifier of a link (blue + underline) but does nothing — a false affordance. Meanwhile the actual frequency control (if any) is not signified at all. Norman: a signifier must point to a real action; an underline that is not a hyperlink violates one of the web's most established conventions.
**Change:** if frequency is editable, make this an actual control with a real signifier (a styled `change` link or a select). If it is not editable, strip the blue + underline so it reads as plain descriptive text.

**Mapping / convention — finding.** The logo is centred and the sign-in/account cluster sits tiny in the far top-right — colliding with the skill's documented anti-patterns "Home = logo top-left, always" and "where the hell is the sign-in?"
**Change:** move the logo to top-left (home convention); enlarge and clarify the account affordance so it survives a glance.

---

## Lens 4 — Cognitive load and working memory (Miller 7±2; Sweller, via the skill's working-memory section)

**Capacity — finding.** **11 fields are shown at once**, exceeding Miller's 7±2 ceiling for items held in view; the screen presents an undifferentiated load with no closure point.
**Change:** split into chunked steps that each drive a working-memory closure: Step 1 Contact (email), Step 2 Shipping (name + address), Step 3 Payment (card). Plot the load so it returns toward zero between steps.

**Chunking — finding.** The order reference `A1B2C3D4E5F6G` is an ungroupable 13-character string — exactly Miller's "fails capacity" case.
**Change:** chunk it: `A1B2 C3D4 E5F6 G` (4-4-4-1) so it can be read, repeated, and quoted to support.

**Recognition over recall — finding.** Region and country are free-text; the user must recall exact spelling/format.
**Change:** offer region/country as a selectable list — recognition beats recall, especially for infrequent use; keep typing fast for experts via type-ahead.

---

## Lens 5 — Hick's Law and Fitts's Law (William Hick / Paul Fitts)

**Hick's Law — finding.** Two equally weighted bottom buttons double the decision the user must make at the exact moment of commitment; choice time rises with the number of equal options.
**Change:** collapse the decision — one dominant `Place order`, `Save for later` demoted so it is not weighed as an equal alternative. (Reinforces the H8/Von Restorff finding above.)

**Fitts's Law — finding.** Two side-by-side equal buttons make the primary target smaller and place a same-sized distractor immediately adjacent, raising mis-click cost; the small top-right account cluster is a tiny target far from where the eye starts.
**Change:** make `Place order` a large, full-width (or clearly widest) target — short movement, big area, ≥44px touch height; keep adjacent low-priority targets visually and spatially separated so the primary action is the easy hit.

---

## Findings-to-changes summary

| # | Lens | Authority | Finding | Design change |
|---|------|-----------|---------|---------------|
| 1 | Gestalt — Proximity | Wertheimer/Koffka | Equal spacing dissolves label↔field binding | Tighten label-to-input, widen field-to-field gaps |
| 2 | Gestalt — Common Region / Figure-Ground | Wertheimer/Koffka | Summary card blends into page ground | Give the card a visible boundary + contrast |
| 3 | Nielsen H9 | Nielsen | Top error list + form cleared on failure | Inline errors on blur; never clear valid fields |
| 4 | Nielsen H5 | Nielsen | No prevention, only post-submit failure | Validate on blur; format hints; disable until valid |
| 5 | Nielsen H8 / Von Restorff | Nielsen / Yablonski | Two equal-weight CTAs, no hierarchy | One primary CTA; demote secondary |
| 6 | Norman — signifier | Norman | Blue underline that is not a link (false affordance) | Make it a real control or strip link styling |
| 7 | Norman — convention | Norman | Logo centred; sign-in tiny top-right | Logo top-left; enlarge account affordance |
| 8 | Cognitive load | Miller / Sweller | 11 fields at once, no closure | Chunk into 3 steps, drive load to zero between |
| 9 | Chunking | Miller | 13-char ungroupable order ref | Chunk to `A1B2 C3D4 E5F6 G` |
| 10 | Recognition over recall | Branson/Miller | Free-text region/country | Selectable list with type-ahead |
| 11 | Hick's Law | Hick | Two equal end-of-funnel choices | Collapse to one dominant action |
| 12 | Fitts's Law | Fitts | Small primary target beside equal distractor | Large, separated, ≥44px primary target |

**Single highest-priority fix:** #3 — stop clearing the form on failed submit and move errors inline. It is the most expensive failure on a pain-peak screen and violates Nielsen H9 directly.
