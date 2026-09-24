# Low-Literacy, Low-Bandwidth and Emerging-Market Design

Parent skill: [`../SKILL.md`](../SKILL.md) (`inclusive-and-assistive-design`).

**When to read:** when a product will be used by people with limited reading ability, limited
digital experience, costly or intermittent data, entry-level or shared phones, or who complete
tasks through an intermediary (agent, community health worker, teacher, child, shop attendant);
typically consumer, government, health, agriculture, education, savings-group and mobile-money
products in East Africa. Pairs with the cultural adaptation audit in
`internationalization-and-rtl-design/references/cultural-adaptation-beyond-translation.md` and the
field methods in
`ux-research-and-usability-testing/references/field-research-in-low-resource-and-cross-cultural-settings.md`.

These are design decisions and inspection checks. They do not replace testing with the people
concerned, and nothing here certifies WCAG conformance.

---

## 1. Frame the user honestly

Write down, before any screen is drawn, the answers below. Each "unknown" is a research task, not
an assumption to fill in.

| Question | Why it changes the design |
|---|---|
| What can the user read, in which language, and how comfortably? Numerals only, short words, full sentences? | Decides the balance of text, icon, image, audio and numerals |
| Which phone: feature phone, entry-level Android, mid-range smartphone? Whose phone? | Decides channel (USSD, SMS, voice, app, web), storage and memory budget, and identity model |
| How is data paid for and how reliable is it? Bundles, Wi-Fi at a hub, none? | Decides page weight, offline behaviour and whether the product may download anything unasked |
| Who helps? Child, agent, VHT, teacher, shopkeeper? | Decides whether to design for assisted use and how to protect the user from the helper |
| What is at stake if it goes wrong: money, health, school place, land, reputation? | Decides how many layers of prevention and how much confirmation (see error patterns) |
| Which trusted institution stands behind it? | Decides the trust signals to show |

Literacy and digital skills are reported by GSMA as leading barriers to mobile internet use in
Sub-Saharan Africa, alongside handset affordability. Treat this as the planning default for mass
consumer products, then confirm locally.

## 2. Channel choice

| Situation | Primary channel | Required companion | Failure if wrong |
|---|---|---|---|
| Users mostly on feature phones; transaction is short and structured | USSD menu | SMS receipt; voice helpline | A smartphone-only app excludes the majority |
| Users receive information more than they act | SMS or pre-recorded voice (IVR) in their language | Human callback for questions | Text-heavy SMS unread by low-literacy users |
| Users on entry-level Android, occasional data | Lightweight web app or small native app with offline store | USSD or agent fallback for the core task | Large app deleted to free storage; task abandoned on no data |
| Trained intermediary (agent, health worker) serves many users | Intermediary app designed for speed and accountability | Receipt the end user can keep (SMS or printed) | End user cannot verify what the intermediary did |
| Messaging apps are the normal communication habit | Messaging-app flow for notifications and simple requests | Clear data-handling notice; an official channel for disputes | Sensitive data exposed on shared chats; impersonation |

Design the core task so its **mental model survives across channels**: the same step names, the
same order, the same reference numbers in USSD, SMS, app and on the agent's screen.

## 3. Low-literacy interface patterns

| Pattern | Do | Avoid |
|---|---|---|
| Text plus meaning carriers | Pair every critical label with an icon or image the target group has been tested on, and offer audio playback for instructions | Icon-only controls; abstract icons borrowed from Western office metaphors |
| Numerals as an anchor | Many people read numbers more easily than words: use large numerals for amounts, quantities, dates and step counts | Amounts written out in words only; long reference codes mixing letters and digits |
| One decision per screen | Short sequence of simple screens with clear progress ("Step 2 of 4") | Long forms; multiple choices competing on one screen |
| Recognition over entry | Choose from pictures, lists and recent recipients; pre-fill from the SIM or registry where lawful | Free-text entry of names, addresses or medical terms |
| Voice in and out | Voice prompts, read-aloud of the confirmation, and voice notes where the platform supports them | Voice as the only path (noise, privacy, dialect) |
| Plain local language | Everyday words in the user's language; name the local term for the thing ("SACCO", "VHT", "boda") | Literal translation of English UI jargon ("Authenticate", "Submit", "Beneficiary") |
| Explicit money and health amounts | Currency code and numerals, repeated at confirmation, with the consequence stated | Abbreviations like "1.2M" without the full number at commit |
| Visible help person | A named way to get help (agent location, call number, "ask the teacher") | Help that is only a text FAQ |

Reading level target: WCAG 2.2 SC 3.1.5 (AAA) asks for supplemental content when text needs more
than lower-secondary reading ability. For low-literacy audiences, treat that as a ceiling, not a
goal: aim well below it and add audio or visual supplements.

## 4. Shared and assisted use

Many phones are shared across a household, and many tasks are completed with help. Design for it:

- **Identity per person, not per phone.** Let several people use one handset with separate PINs
  or profiles; show *whose* account is active on every sensitive screen (name plus initial or
  photo).
- **Protect the user from the helper.** Hide PINs as they are typed, never show full balances or
  diagnoses on a screen the helper will see by default, and send the receipt to the account
  holder, not the helper.
- **Intermediary accountability.** Agent and health-worker apps record who did what, for whom, and
  what was shown; the end user gets a receipt they can check later.
- **Resume safely.** When a session is interrupted and picked up by someone else, require the
  account holder to re-confirm before any commit.

## 5. Low-bandwidth and cost-aware behaviour

Hand the numeric budget to `performance-as-ux-and-core-web-vitals`; the design decisions are:

- **Nothing large downloads without consent.** Show the size before downloading media, updates or
  offline packs ("Download lessons for Term II: 18 MB").
- **Offline-first core task.** The primary task can be started, saved and queued offline; the
  queue is visible ("3 records waiting to send"); sync state is explicit on every record.
- **Text and structure before media.** Images are optional enhancements with small defaults.
- **Respect data-saver signals where available**, but do not depend on them: the `Save-Data`
  request header and the `prefers-reduced-data` media query are experimental and not Baseline.
  The low-data path must be the default for this audience, not an opt-in.
- **Degrade to SMS or USSD** for the core outcome when the data path fails, and say so.
- **SMS length and alphabet.** A single SMS holds 160 characters in the GSM 7-bit alphabet but 70
  when any character falls outside it (for example the Luganda letter "ŋ"), and multipart
  messages cost more. Write and test receipts in each language within the single-part limit.

## 6. Trust and dignity

- Show the accountable institution (ministry, school, cooperative, licensed provider) and how to
  reach a person. Trust in these markets is often carried by known people and places, not by the
  interface.
- Explain why each piece of personal data is needed, in the user's language, at the point it is
  asked. Uganda's Data Protection and Privacy Act, 2019 defines consent as freely given, specific,
  informed and unambiguous; legal detail belongs with counsel, the design obligation is to make
  that consent real for someone who cannot read a policy.
- Never use urgency, shame or hidden fees to push action (see `design-ethics-and-anti-dark-patterns`).
- Do not design a "lite" experience that looks second-class. Low-data and low-literacy paths get
  the same care in typography, spacing and imagery as the main product.

## 7. Inspection checklist (heuristic, not measured)

Mark each Pass / Weak / Fail with evidence; any Fail on a money, health or identity step is
release-blocking until tested with representative users.

1. The core task can be completed by someone who reads numerals but little text.
2. Every critical instruction has an audio or image equivalent tested with the target group.
3. No step requires free-text entry that a picker, list or lookup could replace.
4. The active account holder is visible on every sensitive screen on shared devices.
5. The core task works offline or has a USSD/SMS/agent fallback, and sync state is visible.
6. No download over the agreed threshold starts without showing its size.
7. Amounts show currency and full numerals at commit, and receipts reach the account holder.
8. Receipts and alerts fit a single SMS in each supported language.
9. The accountable institution and a human help route are visible.
10. The low-data path looks as finished as the main path.

## 8. Worked example (original): village health team referral app

**Context.** Village Health Team (VHT) volunteers in a rural district record household visits and
refer sick children to the health centre. Phones are entry-level Android, often shared; data is
bought in small bundles; volunteers read Runyankore-Rukiga well and English partially.

| Decision | Why |
|---|---|
| Home screen shows four large picture-and-word tiles (Visit, Refer, Follow-up, Sync) with counts | One decision per screen; numerals carry status |
| Symptoms chosen from tested illustrations with audio names, not typed | Recognition over entry; avoids spelling of medical terms |
| Danger signs trigger an interlock: referral cannot be saved without the "referred today" confirmation and the caregiver's phone number | Forcing function on the highest-stakes step |
| All records save offline; a banner shows "5 visits waiting to send"; sync runs on Wi-Fi at the health centre or on request | Offline-first, cost-aware |
| Caregiver receives an SMS in Runyankore-Rukiga with the referral number and the health centre's name, under 70 characters when the text needs characters outside GSM-7 | Receipt to the person affected; single-part SMS |
| Each volunteer signs in with a short PIN; the active name shows on every screen | Shared-device identity |

Heuristic verdict: passes checklist items 1-9 in design review; item 10 not assessed until the
visual system is rendered on the target device. Field testing with volunteers is required before
release.

## 9. Premium versus generic output

| Generic | Senior |
|---|---|
| "Use simple language and icons." | Names the language, the reading level, which icons were tested with whom, and the audio fallback |
| Assumes one user per phone and constant data | Designs identity, receipts and sync for shared phones and bundles |
| Ships a stripped "lite" version | Ships one product whose low-data path is its default and looks authored |
| Treats agents and helpers as users to ignore | Designs for assisted use and protects the account holder |
| Claims "accessible for low-literacy users" | Reports inspection results and the test still required |

## Evidence and currentness

Accessed 2026-09-24.
- GSMA, *The State of Mobile Internet Connectivity 2025* (press release 2025-09-09): usage gap of
  3.1 billion people globally; barriers include device affordability, literacy and digital
  skills, relevance and safety. Country-level literacy and skills figures for Uganda, Kenya and
  Tanzania were not verified in this pass and are `NOT_ASSESSED`; obtain current national
  statistics (UBOS, KNBS, NBS Tanzania) and GSMA country data before quoting numbers.
- W3C, *Understanding SC 3.1.5 Reading Level* (Level AAA; updated 2026-06-28).
- MDN, *Save-Data* header (experimental, not Baseline; page modified 2025-12-17).
- Uganda, *Data Protection and Privacy Act, 2019* (ULII consolidated text): definition of consent.
  Current regulator requirements (PDPO registration, research exemptions) are `NOT_ASSESSED`.
- SMS alphabet limits follow the GSM 7-bit default alphabet (3GPP TS 23.038), a stable standard;
  operator-specific USSD session timeouts and menu limits vary and are `NOT_ASSESSED`.
- Concept inputs: Lahiri, Prabhu and Schaffer (eds) (2026) *Innovative Solutions: Advanced User
  Experience Design*, 2nd edn, CRC Press (low-literacy research tools, culturally appropriate
  design, stakeholder-mediated systems); Norman (2013) *The Design of Everyday Things*, Basic
  Books (knowledge in the world, constraints).
