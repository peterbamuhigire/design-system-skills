# UX Psychology

Cognitive psychology and behavioural science applied to premium website design. Complements `universal-guidelines/ux-laws-and-psychology.md` (which covers Miller's Law, Hick's Law, Fitts's Law, Gestalt proximity/similarity overview, Cognitive Load Theory, Flow Theory, etc.). This skill covers the principles not in that file.

---

## 1. GESTALT PRINCIPLES

Perception rules that determine how users group, separate, and interpret visual elements.

### Law of Proximity
Elements close together are perceived as belonging together — no borders required.

- Image caption: gap between image and caption must be smaller than gap between caption and next paragraph. Equal spacing breaks the perceptual link.
- Navigation items grouped tightly = perceived as a single unit. Increase spacing between nav groups (e.g., primary links vs. utility links) to signal categories.
- Form question spacing: increase vertical gap between separate questions; keep label and its input tight. Space alone signals question boundaries — no box borders needed.
- Use whitespace (not dividers) to group related content in most layouts; dividers add visual noise.

### Law of Similarity
Elements sharing visual traits are perceived as the same category.

- ALL interactive elements (buttons, links, toggles) must share ONE consistent visual treatment per type.
- Decorative elements must NEVER use the same treatment as interactive elements — no hover states, underlines, or button-like styling on non-interactive components.
- Same font weight + colour + size = same type of content. Violating this forces users to re-learn the visual grammar on every page.
- If a card has a shadow and a hover state, every card must — inconsistency breaks the similarity rule.

### Law of Continuity
The eye follows lines and curves beyond their endpoints.

- Use alignment to guide the eye toward the next important element: hero headline → subheadline → CTA button must lie on a clean vertical or diagonal axis.
- Visual flow interrupted by unaligned elements = cognitive stumble. Audit every page for broken alignment paths.
- Horizontal rules and divider lines extend into visual infinity — place them intentionally or they will guide the eye off-page.

### Law of Closure
The brain fills in incomplete shapes and implies the rest.

- Partially revealed cards or carousel items at the right edge signal "scroll to see more" — use deliberately and consistently. Showing 80% of a card communicates the rest without labels.
- Do not rely on arrows or "swipe" labels when partial visibility already communicates scrollability.
- Incomplete circles and icons are resolved by the brain — minimalist iconography exploits this; overly detailed icons do not.

### Law of Figure/Ground
Users distinguish foreground content from background by contrast. If the contrast is insufficient, neither reads as primary.

- Modal overlays: backdrop opacity 70–80% (not 30–40%). Low opacity creates figure/ground confusion — the page behind competes with the modal.
- Cards need visible separation from the page background: shadow, border, or colour contrast. Cards that match the page background become invisible as distinct objects.
- Background textures and images behind text must be low-contrast or blurred — they must read unambiguously as ground.

### Gestalt Violations to Eliminate
- Equal spacing above and below an image caption = caption belongs to neither image nor paragraph.
- Decorative graphic styled with a shadow and hover state = users attempt to click it (false affordance).
- Same blue colour for external links AND decorative section headers = users click headers expecting navigation.
- Section with a drop shadow that is not a clickable card = violates the learned affordance of shadows.

---

## 2. NIELSEN'S 10 USABILITY HEURISTICS

Each heuristic with specific, implementable rules.

### H1: Visibility of System Status
Users need to know what is happening at all times.

- Show skeleton screens or loading spinners whenever content loads asynchronously — never a blank space.
- After form submission: show a clear confirmation message (not a blank or unchanged page).
- Submit buttons must change state on press: disabled + spinner while processing; success state on completion.
- Never leave users wondering if their action registered. If processing takes >1s, show progress.

### H2: Match System to Real World
Use the words and mental models of users, not internal technical terminology.

- "Shopping cart" not "order queue." "Inbox" not "message buffer." "Sign in" not "authenticate."
- Error messages in plain language: "That email address is already registered — try logging in instead" not "UNIQUE constraint violation on field: email."
- Navigation labels must use words users search for, not your client's internal category names.
- Date pickers, currency fields, and phone fields must match regional formats (DD/MM/YYYY not MM-DD-YYYY for UK/African markets).

### H3: User Control and Freedom
Users make mistakes; they need safe exits.

- Always provide "Back" or "Cancel" in multi-step flows. Never trap users mid-funnel with no retreat.
- Allow modal exits by clicking the backdrop AND pressing Escape — both, always.
- Destructive actions (delete, cancel subscription) require a confirmation dialog. Provide explicit Confirm AND Cancel with visual distinction.
- "Undo" functionality or a grace period (e.g., "Email will be sent in 5 seconds — Cancel") reduces anxiety and errors.

### H4: Consistency and Standards
Users transfer learned expectations. Violating consistency forces relearning.

- One word per concept: "sign in" OR "log in" — never both on the same site.
- Navigation position must not change between pages. A navigation that moves is a navigation that loses trust.
- Same button style = same action type, everywhere. Primary CTA: one colour. Secondary actions: a different treatment. Destructive actions: always red. Never deviate.
- Icons must be consistent: one icon per concept; one style library (never mix filled and outline variants of the same icon).

### H5: Error Prevention
The best error message is one that never needs to appear.

- Inline validation after the user leaves a field (on blur), not only on submit.
- Show confirmation dialogs before irreversible actions — "Are you sure? This cannot be undone."
- Disable the submit button until required fields are complete (with a visible tooltip explaining why it is disabled).
- Password fields: show requirements upfront, not after the user fails.
- Provide format examples inside form labels: "Phone (e.g., +256 700 000 000)."

### H6: Recognition Rather Than Recall
Never make users remember something from a previous screen.

- Navigation labels must always be visible text on desktop — icon-only navigation requires recall, not recognition.
- Show users their position in multi-step flows: "Step 2 of 4 — Shipping Details."
- Breadcrumbs on pages more than 2 levels deep.
- Never ask users for information they already provided (e.g., ask for name once; pre-fill it if shown again).
- "Recently viewed" or saved items reduce recall load for returning users.

### H7: Flexibility and Efficiency of Use
Novices and experts need different interfaces; serve both.

- Keyboard navigation for all interactive elements (Tab order, Enter to submit, Escape to close).
- Saved preferences and persistent filters for returning users.
- Quick-fill patterns for returning visitors (saved addresses, auto-populated fields).
- Shortcuts and power-user paths should not clutter the interface for novice users — layer them.

### H8: Aesthetic and Minimalist Design
Every element that is not essential is a competitor to the essential.

- One primary message per page. Establish hierarchy, then enforce it ruthlessly.
- One primary CTA per page — five equal-weight CTAs create decision paralysis (see Hick's Law in universal-guidelines).
- Every optional form field is a cognitive tax. Eliminate it or mark it clearly optional.
- No decorative text that does not serve the user's current task. Filler copy is not neutral — it buries signal in noise.
- Remove features until removing one more would break the minimum viable flow.

### H9: Help Users Recover from Errors
When errors happen, minimise damage and frustration.

- Error messages appear inline next to the offending field, not as a list at the top of the page.
- Error message format: [What went wrong] + [What to do]: "Password too short — must be at least 8 characters."
- NEVER clear a form after a failed submission. Repopulate all valid fields; highlight only the invalid ones.
- Offer alternatives in dead-ends: if no search results, suggest related content or a contact path.

### H10: Help and Documentation
When users need help, make it immediately findable and actionable.

- Contextual help at the point of need (inline tooltip, help icon next to the field) — not a separate help centre link.
- Help content must be task-oriented and specific: "Click the blue 'Add Service' button in the top-right corner" not "Services can be added in the admin panel."
- FAQ sections must be structured around user questions, not product features.

---

## 3. NORMAN'S THREE LEVELS OF DESIGN

Apply all three simultaneously. Failure at any level loses the user.

### Visceral Level — Automatic Emotional Response to Appearance
- First impressions form in under 100ms. Visual quality is not superficial — it is the first interaction.
- The Aesthetic-Usability Effect: beautiful interfaces are perceived as more usable, more trustworthy, and worth paying more for — even if the underlying UX is marginally inferior to an ugly competitor.
- This is what clients at the $20k–$50k level are paying for: a visceral experience their competitors cannot afford.
- Practical inputs to visceral quality: photography resolution and mood, whitespace generosity, typographic refinement, colour harmony, and animation smoothness.
- Visceral quality communicates "this business is serious" before a word is read.

### Behavioral Level — Usability: Does It Work?
- This is where Nielsen's heuristics and the UX laws in universal-guidelines operate.
- Frictionless task completion: the user achieves their primary goal (contact, purchase, enquiry) without confusion, dead-ends, or errors.
- If the behavioral level fails, no amount of visceral quality can rescue the site. Users leave frustrated regardless of how beautiful it was.
- Every page has one primary user task. Design the behavioral path for that task first; everything else is secondary.

### Reflective Level — Values, Identity, and Self-Image
- Users ask implicitly: "What does using this site say about me?"
- Brand consistency, ethical practices, and authentic voice all affect reflective assessment.
- Testimonials, case studies, and trust signals operate at this level — they provide social proof for the reflective judgement ("people like me trust this brand").
- Content that aligns with the user's values creates reflective-level loyalty: users return and refer others because the brand reflects who they are or aspire to be.
- Dark patterns destroy reflective-level trust irreversibly: once a user feels manipulated, no visceral quality recovers it.

### The 3-Level Audit for Any Page
1. **Visceral:** Does the design create an immediate positive emotional response?
2. **Behavioral:** Can users accomplish their goals efficiently and without confusion?
3. **Reflective:** Does the experience reinforce the client's values and the user's sense of self?

---

## 4. SYSTEM 1 vs SYSTEM 2 THINKING

Kahneman's dual-process model. Every website interaction is primarily System 1.

**System 1** — fast, automatic, pattern-matching, intuitive. Runs almost all the time.
**System 2** — slow, deliberate, effortful, analytical. Users resist switching to it.

**Design for System 1:**
- If users must think hard to use your interface, it has failed at the behavioural level.
- Use familiar patterns: novel interactions are interesting in demos and costly in production. Novelty forces System 2; familiarity enables System 1.
- Defaults are accepted by System 1 without scrutiny — set defaults that genuinely serve users.
- Familiar layouts (nav at top, logo left, CTA top-right) exploit learned patterns and reduce cognitive load.

### 10 Cognitive Biases with Direct Website Application

**1. Loss Aversion** — the pain of loss is twice as powerful as equivalent gain.
- Ethical use: "Your progress will be lost if you leave now" (when genuinely true).
- Dark pattern: fabricated scarcity ("Only 2 left!" when inventory is unlimited).

**2. Default / Status Quo Bias** — users keep defaults unless strongly motivated to change.
- Set defaults that serve users: opt-IN for marketing emails, most privacy-preserving data settings on by default.
- Dark pattern: pre-checked upsell boxes, auto-enrolled subscriptions, opt-out (not opt-in) recurring charges.

**3. Egocentric Bias** — we assume others experience the world as we do.
- "I find it intuitive" does not mean "it is intuitive." You are not your user.
- The solution is structured user testing with people who have never seen the site.

**4. Goal-Gradient Effect** — motivation increases as a goal approaches completion.
- Ethical use: progress bars in onboarding flows, "3 steps remaining," pre-filling Step 1 so users feel started.
- Dark pattern: streaks that reset to zero if one day is missed (designed to create anxiety, not progress).

**5. FOMO — Fear of Missing Out**
- Ethical use: honest limited-time sales with real deadlines; genuine low-stock notifications.
- Dark pattern: countdown timers that reset on page reload; "14 people viewing this now" with fake or inflated numbers.

**6. Confirmation Bias** — we seek information that confirms existing beliefs.
- The team that built the product cannot conduct unbiased usability tests. Independent user testing is not optional.
- Analytics that confirm your design choices should be scrutinised harder, not accepted more easily.

**7. Curse of Knowledge** — once you know something, you cannot simulate not knowing it.
- Test with people who have NEVER seen the site. They will immediately find the problems you are blind to.
- Never assume that a label, icon, or interaction is "obvious" — test before shipping.

**8. IKEA Effect** — we overvalue things we helped create.
- Product teams keep too many features. Use click analytics and completion rates, not team attachment, to decide what stays.
- Every unnecessary feature you ship imposes cognitive load on every user, forever.

**9. Sunk Cost Fallacy** — we continue investing because of past investment, not future value.
- If a page is not converting, rebuild it. The willingness to discard sunk work is a premium design quality indicator.
- Client expectation management: "We are rebuilding this section because the data shows it is failing" is a professional, not a failure, conversation.

**10. Anchoring** — the first number or option seen biases all subsequent judgements.
- Present the premium tier first in pricing tables. Anchor high; let users "choose down."
- In services lists, lead with the most comprehensive (and expensive) option.

---

## 5. EMOTIONAL DESIGN AND MICROINTERACTIONS

### Emotional Feedback Rules
- **Success states** deserve active celebration: positive colour change, motion, and human language when important tasks complete. "You're in! Check your inbox" not "Form submitted."
- **Error states** deserve empathy: acknowledge the frustration first, then give a clear path forward. "Something went wrong on our end — please try again or contact us directly."
- **Surprise and delight** moments (small unexpected positive touches) increase brand affinity without adding clutter. An animated tick after form submission; a warm thank-you page that sets expectations.
- Custom 404 pages with empathy and helpful next steps turn a negative moment into a brand touch: "We can't find that page, but here's where to go next."
- Onboarding copy should feel welcoming, not like a compliance exercise. Every instruction should feel like a helpful colleague, not a legal disclaimer.
- Write all system copy (confirmations, errors, empty states) in the same human voice as the marketing copy.

### Microinteraction Design Rules
- Button hover and press states communicate that the interface is alive and responsive. Absence of state changes communicates brokenness.
- Loading animations should feel purposeful and brand-consistent — not a generic grey spinner.
- Form field focus states (ring highlight) help users track their position, especially on mobile.
- Transition timing: 150–300ms for small UI feedback (hover, focus, button press); 300–500ms for larger state changes (modal open, panel slide); 500ms+ only for deliberate emphasis.
- Never animate purely for decoration. Every animation must help users understand a state change or spatial relationship.
- Reduced motion media query: always respect `prefers-reduced-motion`. Provide static fallbacks.

---

## 6. AFFORDANCES AND MENTAL MODELS

### Mental Models
Users bring expectations from other websites and from real-world objects. Designing against the dominant mental model is always wrong.

- If users predictably misuse a feature, the feature needs redesigning — not the user manual.
- The thermostat fallacy: users believe turning a thermostat to maximum heats a room faster; users believe more button clicks = faster processing. Design to correct these where it matters.
- Use onboarding to establish accurate mental models for genuinely novel interactions. For conventional interactions, exploit existing mental models — do not fight them.

### Four Types of Affordance

| Type | Definition | Web Application |
|------|-----------|----------------|
| Physical | Shape/size suggests interaction | Scrollbar thumb size implies drag; pill input implies typing |
| Cognitive (signifier) | Label/icon explains the action | Button text states the outcome; envelope icon = messaging |
| Sensory | Visual prominence signals importance | High-contrast CTA is visually "grabbable"; large font = important |
| Functional | Structure implies capability | Filter + sort tools signal that large content is navigable |

### False Affordances (Design Errors)
- Decorative card with a box shadow and hover state = users click expecting a link. If it has hover, it must link.
- Section heading styled to resemble a button = users attempt to click it.
- Segmented control with unclear active state = users cannot tell what is selected.
- Underlined text that is not a hyperlink = violates one of the most established web conventions.
- **Rule:** If it looks interactive, it must be interactive. If it is decorative, it must not look interactive.

### Mental Model Alignment Rules
- Navigation at page top: where users look first (Jakob's Law — covered in universal-guidelines).
- Search = magnifying glass icon. Always. No exceptions.
- Home = logo in top-left. Always.
- Close/dismiss = × in top-right corner. Always.
- Back = left-pointing arrow. Always.
- Never place the primary action in a non-standard location without a compelling, tested reason.

---

## 7. DARK PATTERNS TO AVOID

Premium clients pay to protect their brand. Dark patterns create legal risk and destroy the trust their brand depends on.

**Confirm-shaming:** Opt-out labels that guilt-trip users: "No thanks, I don't want to save money." Never use. Write neutral cancel options: "No thanks" or "Maybe later."

**Pre-checked boxes:** Always require explicit, deliberate opt-in for: marketing emails, upsells, add-on products, subscriptions, recurring charges. Pre-checked = assumed consent = legal risk in GDPR jurisdictions.

**Hidden subscription:** "GET STARTED FREE" that initiates a paid subscription without making the billing terms prominent and explicit. Fatal to trust; increasingly illegal.

**Fake scarcity / urgency:** "Only 2 left!" when inventory is unlimited; countdown timers that reset on page reload; "17 people are viewing this right now" with fabricated or inflated numbers. Users have seen these; they destroy credibility.

**Auto-play media:** Removes the user's decision to engage. Default-off for all audio and video. No exceptions.

**Roach motel:** Easy to sign up; nearly impossible to cancel, unsubscribe, or delete account. The cancellation path must be as accessible as the sign-up path.

**Bait and switch:** Advertising one product, price, or feature; delivering another. Especially common in pricing pages where the most prominent plan has asterisked exclusions.

**Misdirection:** Drawing attention to one area to prevent users from noticing another — e.g., a bold promotional graphic positioned to draw the eye away from a pre-checked upsell box beneath it.

**Disguised advertising:** Sponsored content or affiliate recommendations styled to look identical to editorial content without disclosure.

### The Ethical Test
For every design decision that could be a dark pattern, ask: **Will this feature be genuinely valuable to users, or is it primarily serving a business metric at users' expense?**

If the answer is "primarily at users' expense," it is a dark pattern — regardless of whether it temporarily improves a conversion metric.

### The Premium Client Standard
Clients investing $20k–$50k in a website are buying brand equity. One viral complaint about a dark pattern destroys months of that equity. When a client requests a dark pattern, name it clearly and recommend the ethical alternative. This is part of the expertise they are paying for.

---

## 8. TIDWELL BEHAVIORAL PATTERNS

Patterns from *Designing Interfaces* (Tidwell, Brewer, Valencia — O'Reilly 2020). Full pattern details in `book-extractions/tidwell-cognition-visual-patterns.md`.

### Safe Exploration — "Let me explore without getting into trouble."
- Every destructive action must be reversible or require confirmation.
- Auto-save so exploration costs nothing; any wrong turn is recoverable.
- Extra windows, pop-ups that hijack Back, or irreversible single-clicks break this pattern.

### Instant Gratification — "I want to accomplish something now."
- Predict the first thing a new user will do; make that action stunningly easy.
- Do NOT block first action behind registration, long instructions, or slow loads.
- Provide value before asking for something valuable (email, payment).
- Show partial results as they load — blank screen for >200ms damages confidence.

### Satisficing — "This is good enough; I'll stop here."
- Users stop at the first plausible choice — put the right choice FIRST in every list.
- Labels must be short and scannable; users guess rather than read every word.
- Use calls to action ("Type here," "Tap to begin") to direct users to the most likely first step.
- Visual layout communicates meaning faster than labels — use it to guide first-click behaviour.

### Deferred Choices — "I don't want to answer that now."
- Clearly distinguish required vs. optional fields — never make non-critical fields required.
- Use good defaults so skipped fields don't create broken states.
- A note like "You can change this later in Settings" reduces the anxiety of deciding now.

### Habituation — "That gesture works everywhere else; why not here?"
- Consistent placement of navigation, actions, and labels is the most critical usability rule.
- After first use, help text becomes invisible — layout must self-explain to returning users.
- Announce layout changes explicitly: "We've updated our navigation" prevents disorientation.

### Spatial Memory — "I remember where things were on the screen."
- NEVER move navigation items between pages — users remember locations, not labels.
- Pin primary actions to consistent screen positions (top-right on desktop, bottom on mobile).
- If layout must change (responsive breakpoint), animate the transition so users can follow elements.

### Prospective Memory — "Remind me where I was."
- Breadcrumbs, progress steps, and section titles remind users of their position.
- After any page load, visible context must make the current task obvious without reading body text.
- Email/notification reminders for deferred actions reduce abandonment.

### Incremental Construction — "Let me change this. That's better."
- Support frequent small saves; never require a complete form before any save is possible.
- Show work-in-progress continuously; feedback during creation is essential (Csikszentmihalyi).

---

## 9. LAWS OF UX — WEBSITE APPLICATION

Named laws from Yablonski (2024) *Laws of UX* (lawsofux.com). Laws already covered in earlier sections (Goal-Gradient, Hick's Law, Anchoring, IKEA Effect, Gestalt Proximity/Similarity/Closure/Continuity/Figure-Ground) are excluded here.

### Peak-End Rule
Users judge an entire experience by its most intense moment and its ending — not the average quality.
- Confirmation and thank-you pages are the **ending** of every web experience. They are disproportionately remembered — design them with warmth, personality, and a clear next step.
- The most intense moment is usually first load or form submission. Make it exceptional.
- Every 404, error state, and empty state is a potential pain peak. Each needs empathy + a clear exit path. Never leave users in a dead end.

### Von Restorff Effect
The element that differs most from its surroundings is the most noticed and remembered.
- One visually distinct primary CTA per page. When everything is bold, nothing is bold.
- Secondary actions must be visually subdued — differentiation is the mechanism of noticeability.
- Overuse of contrast destroys the signal. Every highlight added dilutes every other highlight on the page.

### Serial Position Effect
Users best remember the first (primacy) and last (recency) items in a sequence; middle items are least memorable.
- Navigation: place critical links first or last. Never bury the primary action in the middle of a nav.
- Service lists: lead with the flagship offer; close with the most memorable option.
- Form fields: first field sets tone; last field is remembered — end with a welcoming, clear submit.

### Zeigarnik Effect
Unfinished tasks persist in memory more than completed ones; open loops create cognitive pull to return.
- Progress bars, "Your profile is 60% complete," and multi-step indicators leverage this to re-engage.
- Persist partial form state — a half-filled form creates pull to return and complete.
- Onboarding checklists that remain incompletable by design keep users returning.

### Doherty Threshold
System response under 400ms keeps users engaged; above 400ms, focus breaks and users disengage.
- Target <100ms for button/hover feedback using CSS transitions — no JavaScript delay.
- For slower operations: optimistic UI (show success immediately, roll back on failure) or skeleton screens within 100ms.
- LCP (Largest Contentful Paint) ≤2.5s. Every additional 100ms of load loses measurable conversions.

### Tesler's Law (Law of Conservation of Complexity)
Every system has inherent complexity that cannot be eliminated — only transferred to a different actor.
- Simplifying the UI moves complexity to the backend, developer, or documentation. Decide consciously who bears it.
- When a client asks to "simplify," identify *where* the complexity goes — it does not disappear.
- Strip every element that does not serve the user's primary task; accept without apology the complexity that cannot be removed.

### Selective Attention
Users actively filter out anything outside their current goal path — it is effectively invisible to them.
- Never rely on banners, sidebars, or inline messages placed outside the task flow.
- Critical guidance must be placed inline, in the path of the action — not above, below, or beside it.
- Eye-tracking consistently shows users skip decorative images, stock photography, and elements that visually resemble ads.

### Postel's Law (Robustness Principle)
Be liberal in what you accept as input; be conservative and consistent in what you output.
- Accept phone numbers in any format — strip and normalise on submit.
- Accept dates in regional formats; accept email regardless of case; never reject special characters in names.
- Return clean, predictable, consistently formatted output: normalised numbers, standard date display, formatted addresses.

### Law of Common Region
Elements sharing a visible boundary are perceived as grouped — independent of their internal visual similarities.
- Cards and bordered panels create stronger grouping signals than proximity alone.
- Background colour blocks group page sections when whitespace alone is insufficient.
- Cards must have visible separation from the page background (shadow, border, or colour contrast) — an invisible card is an invisible group.

### Law of Uniform Connectedness
Elements connected by a visible line or border are perceived as more strongly related than elements that merely share proximity.
- Use connecting lines, arrows, and step-to-step connectors deliberately in multi-step flows and process diagrams.
- Navigation underlines and active states create explicit connection between label and state.
- Do not draw lines between elements you do not intend to imply as explicitly related.

### Laws Quick Reference for Common Website Decisions

| Decision | Law | Rule |
|----------|-----|------|
| How many nav items? | Hick's Law + Miller's | ≤7; group into ≤5 clusters |
| CTA button size/position | Fitts's Law | Large + near; 44px min touch target |
| Page load target | Doherty Threshold | LCP ≤2.5s; UI feedback <100ms |
| Number of options per group | Choice Overload | One primary CTA; filter large sets |
| List item order | Serial Position | Most important: first or last |
| Form input formats | Postel's Law | Accept any reasonable format |
| Feature prominence | Pareto Principle | 20% features = 80% use — make them obvious |
| Confirmation screens | Peak-End Rule | Endings are remembered — make them great |
| Card grouping | Law of Common Region | Visible boundary = strongest group signal |
| Stand-out element | Von Restorff | One contrast element per zone — no more |
| Returning user engagement | Zeigarnik Effect | Leave progress visible; persist incomplete states |
| User instructions | Paradox of Active User | Embed guidance in the UI — no one reads manuals |
| Chunking content | Miller's Law | ≤7 items per group; ≤5 is safer |

---

## SECTION 10: KRUG'S THREE FACTS OF REAL WEB USE

Grounded in Krug (2014) *Don't Make Me Think*, 3rd ed. Full reference: `book-extractions/dont-make-me-think-extraction.md`.

| Fact | Reality | Design Response |
|------|---------|-----------------|
| **We scan, not read** | Users are on a mission; they glance, find a plausible match, click. They ignore most of what's on the page. | Design billboards. Visual hierarchy, headings, bullets, bold key terms. No wall of words. |
| **We satisfice, not optimise** | Users take the first reasonable option — not the best. The first plausible link wins. Weighing options is rare. | Put the right path first and make it unmissable. Scent of information (link text must signal destination unambiguously). |
| **We muddle through** | Users never read instructions. They invent stories about how things work and proceed. | Make design self-explanatory. Eliminate instructions. Support successful muddling without requiring comprehension first. |

**Krug's billboard metaphor:** Pages must work at a glance. Designers imagine users reading brochures; users see billboards going 60mph. Clarity of the instant glance determines whether users stay.

**Clarity trumps consistency.** If making something slightly inconsistent makes it significantly clearer, choose clarity.

---

## SKILL INTEGRATION NOTES

- Run **alongside** `laws-of-ux` and `web-usability-krug` (global) skills for named-law reference and full Krug principles.
- Invoke during `page-builder` and `design-system` steps as a quality gate.
- Use the 3-level Norman audit (visceral / behavioral / reflective) as a pre-launch checklist for every page.
- Use the dark patterns list as a client communication tool when reviewing requirements.
- Cognitive bias awareness (Section 4) should inform copy decisions in `sales-copywriting` and `page-builder`.
- Section 8 Tidwell patterns govern multi-step flows, navigation stability, and form behaviour — cross-reference with `form-ux-design` and `page-builder`.
- Section 9 Laws of UX: apply the Quick Reference table as a checklist before finalising any page layout.
- Section 10 Krug facts: apply as a reality check before any copy or layout is marked complete.

---

## Working memory and cognitive load (added 2026-05-04 from Branson)

Source: `branson-ux-ui-design-extraction.md` Section 5 (Human Memory Limitations).

### Capacity rule (Miller, 1956)
- Working memory: **7 ± 2 chunks**, often less
- Span: ~30 seconds, extendable by repetition; intervening activities ("proactive interference") shrink it fast
- A "chunk" is one gestalt — a word, not a phoneme; a phrase, not a letter

### Web design implications
- Primary navigation: ≤ 7 items (chunk further if more needed)
- Form fields visible at once: ≤ 7 (split long forms into steps)
- Numeric strings (phone, account): chunk at 3-3-4 or 4-3 patterns
- Avoid stacking: don't ask the user to remember earlier-page values mid-flow

### The chunking trick
- `001010110111000` (15 digits) → ungroupable, fails capacity
- `001 010 110 111 000` (5 chunks of 3) → fits
- `NTHEDOGSAWTHECATRU` → move N to end → `THE DOG SAW THE CAT RUN` (1 sentence chunk)

### Stacking and cognitive load
**Stacking:** when a new task interrupts the current task, the user puts the current context on a memory "stack." Stacks are small, short, and defective — sufficient interruption → user forgets what they were doing.

**Cognitive load (Sweller):** the load on working memory at a moment in time. Cascading menus and long Web flows put users at risk of overload.

**Design rule:** break large complex tasks into a series of smaller activities. Plot working-memory load over time; whenever load reaches zero = task closure. Organize tasks to drive frequent closure.

### Recognition over recall
Computers are better at memory; humans at pattern recognition. Let the user **choose from a list** rather than **recall from memory**. Best for initial / infrequent use. For experienced users who memorize commands, GUI selection becomes slower than typing — provide keyboard shortcuts (Ctrl-S etc.) as physical-affordance bypasses.

---

## Four-stage cognitive affordance discipline (added 2026-05-04 from Branson)

Source: `branson-ux-ui-design-extraction.md` Section 6 (Cognitive Affordance).

For every important interactive element, walk through these four stages. Failure at any stage breaks the chain.

### Stage 1: Presence
Does the affordance exist at all?
- Show which UI object to manipulate
- Show how to manipulate it
- Indicate active defaults, system state, modes
- Remind about steps the user might forget
- Avoid "clueless consent" (user proceeds without understanding consequences)

### Stage 2: Visibility / Perceivability
Can it be seen at all?
- Is it actually rendered?
- Is it occluded by another item?
- Is it small or peripheral or lost in clutter?

**Anti-pattern (must fail design review):** "Where the hell is the sign in?" — small, indistinct sign-in box mixed with other items in the far top-right corner.

### Stage 3: Recognizability
Once visible, can it be detected/identified without searching?
- Location within central focus of attention
- Contrast, size, layout complexity
- Separation from background and other UI clutter

**Anti-pattern:** status lines / message lines at the very top or very bottom — notoriously unnoticed. Pop-ups near the cursor are far more recognizable.

### Stage 4: Intelligibility
Once recognized, is the *content* understandable?
- Legibility (font, size, weight, color, contrast) — *being readable*, not whether words are meaningful
- Meaning — does the user understand once they read?

### Use as a design-review heuristic
Walk every primary CTA on a template through Presence → Visibility → Recognizability → Intelligibility. Any missing stage = redesign required before launch.
