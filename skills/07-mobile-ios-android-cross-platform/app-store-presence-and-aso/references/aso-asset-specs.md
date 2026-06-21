# ASO Asset Specs — App Store & Google Play (2026)

The canonical asset geometry and field model for an app-store listing treated as a design
surface: the **app icon** (both stores' masking, safe zones, alpha rules, and iOS Liquid Glass
variants), the **screenshot** dimensions per device class, the **app preview / promo video**
specs, the **listing copy** field model and character limits, and the **pre-flight / common
rejection** checklist.

Stores revise exact pixel requirements over time; the values below are the **current 2026**
baselines and the rules that change least (masking behavior, no-alpha, safe zones, narrative
order, field models). When App Store Connect / Play Console state a different number for a new
device, **the console is authority** — re-snap to it, keep the principles. This reference exists
so a screenshot exported next week sits at the same dimensions and reads on the same grid as one
exported today. See `doctrine/design-doctrine.md` §2: state the choice, then apply it everywhere.

---

## 1. App icon

### 1.1 Delivery masters

| Store | Upload master | Format | Color | Rounding | Alpha / transparency |
|---|---|---|---|---|---|
| **App Store (iOS/iPadOS)** | **1024 × 1024** px | PNG (flattened) | Display P3 or sRGB | **Square, full-bleed — do NOT pre-round** | **No alpha channel** (flatten on opaque bg) |
| **Google Play** | **512 × 512** px | **32-bit PNG (with alpha allowed)** | sRGB | **Square, full-bleed — do NOT pre-round** | Alpha allowed, but icon must read on any bg |

- **Each store applies its own mask.** iOS rounds with its **superellipse (squircle)**; Play
  applies an **adaptive-icon mask** (circle/squircle/rounded-square depending on launcher).
  Pre-baking a corner radius double-rounds and clips — ship the **square** master.
- **No text-as-logo gimmicks**, no "free"/price, no store badges, no screenshots-of-the-app
  inside the icon.

### 1.2 Safe zone (keep critical content inside)

| Surface | Safe-zone guidance |
|---|---|
| iOS squircle | Keep the mark within the central **~80%**; corners are clipped by the squircle. |
| Play **adaptive icon** | Icon is **108 × 108 dp** with the inner **66 dp** *guaranteed visible* (the **central ~61%**); the outer ring is mask/parallax bleed. Ship **foreground + background layers** full-bleed to 108dp; keep the mark inside the 66dp circle. |

### 1.3 iOS Liquid Glass icon variants (current Apple SDK era)

iOS composites app icons through the **Liquid Glass** material and renders multiple appearance
variants from a **layered** source. Provide art that holds up as:

| Variant | What to deliver / verify |
|---|---|
| **Light (default)** | Full-color, layered so the system can apply specular/lensing. |
| **Dark** | A dark-background treatment; the mark must not vanish on dark. |
| **Tinted (monochrome)** | A grayscale/mono layer the system tints; design so the silhouette reads as one weight. |
| **Clear / glass** | Reads as translucent glass; avoid heavy full-bleed backgrounds that fight the material. |

- Build the icon in the **layered (Icon Composer / asset-catalog)** workflow so all variants
  derive from one source; verify each variant at **every home-screen grid size** and in the
  App Store thumbnail. Don't bake Liquid Glass highlights into the master — the system adds them.
- See `ios-ui-ux-design` → `references/hig-liquid-glass.md` for the in-OS icon behavior.

---

## 2. Screenshots

### 2.1 Required / accepted dimensions

**App Store (iOS)** — you must supply at least the largest size for each device family you
support; smaller families can scale from it.

| Device family | Portrait (px) | Landscape (px) | Notes |
|---|---|---|---|
| iPhone **6.9"** (current largest) | **1290 × 2796** | 2796 × 1290 | Primary required set. |
| iPhone **6.5"** | 1242 × 2688 / 1284 × 2778 | swapped | Accepted/legacy-large. |
| iPad **13"** | **2064 × 2752** | 2752 × 2064 | Required if iPad-supported. |
| Count | **up to 10** per device family / localization | — | First 2-3 are what sell. |

**Google Play**

| Asset | Spec |
|---|---|
| Phone screenshots | **min 2, max 8**; PNG/JPG (24-bit, no alpha); **min side 320px, max side 3840px**; ratio between **16:9 and 9:16**; max 2:1 dimension ratio. Recommend ~**1080 × 1920**. |
| 7" / 10" tablet | Separate sets if tablet-supported; same ratio rules, larger min. |
| **Feature graphic** (required) | **1024 × 500** px, PNG/JPG, **no alpha**; shown atop the listing and in promos — treat as a hero banner, no critical text near edges (it gets cropped/overlaid by the play button). |

### 2.2 Composition rules

- **Device-frame** in the *correct current device* (or a clean borderless bezel); never frame an
  iOS screenshot in an Android device or vice-versa (review/policy issue + credibility break).
- **Caption per frame** in the **app's approved type** (`doctrine/references/ai-slop-banned-fonts.md`),
  fixed position, one headline idea (optional sub-line). Caption-on-background contrast meets
  **WCAG 2.2 §1.4.3** (`doctrine/references/wcag-2.2-criteria.md`) — verify at the **thumbnail**
  size search results render, where most decisions happen.
- **Narrative order** (the conversion spine): F1 hook → F2 proof → F3 differentiator → F4-N depth.
  A **continuous color/shape field** across frames signals one authored set.
- **Accuracy:** screenshots must reflect the shipped app (review rejects misleading ones); real
  data, not lorem.

---

## 3. App preview / promo video

| Store | Spec |
|---|---|
| **App Store — App Preview** | **15-30 s**; same resolutions as the device screenshots; **must be captured from the actual app** (not a pure motion-graphics ad); choose a deliberate **poster frame**; up to **3** per localization/device. |
| **Google Play — promo video** | Provided as a **YouTube URL** (not an uploaded file); landscape recommended; avoid age-gated/auto-play-with-issues videos; shown before screenshots when present. |

- **Assume muted autoplay** — open on the value proposition in **~3 s**, carry meaning with
  on-screen captions, don't depend on audio.

---

## 4. Listing copy field model

### 4.1 App Store (iOS)

| Field | Limit | Role |
|---|---|---|
| **App name** | **30 chars** | Brand + at most one keyword phrase. |
| **Subtitle** | **30 chars** | The value proposition in one line; high ASO weight. |
| **Promotional text** | **170 chars** | Above the description; editable without review — use for timely lines. |
| **Keywords** | **100 chars total** | **Comma-separated, NO spaces** (a space costs a character); singular forms, no plurals/competitor names; not shown to users. |
| **Description** | **4000 chars** | First ~3 lines show before "more" — front-load value. Not keyword-indexed the way the keyword field is. |

### 4.2 Google Play

| Field | Limit | Role |
|---|---|---|
| **Title** | **30 chars** | Brand + primary keyword; **indexed**. |
| **Short description** | **80 chars** | The hook shown under the icon; **indexed**, high weight. |
| **Full description** | **4000 chars** | **Indexed** — use target terms naturally; **keyword-stuffing is a policy violation** and is penalized. First line shows before "more". |

- Front-load the **first line** of the long description in both stores.
- Map the **same value proposition** through name/subtitle/short-description so icon + F1
  screenshot + copy tell **one** story.

---

## 5. Localization

- Each **localization** can carry its own screenshots, preview, and copy. Translate captions and
  copy; localize **screenshot UI language** where it materially helps conversion.
- Keep a **fixed layout template** per device class so each locale is a *fill-in*, not a redesign.
- Verify **text overflow** in longer languages (German, Russian, Finnish) within caption zones,
  and **RTL** mirroring (Arabic, Hebrew) of both layout and directional UI
  (`internationalization-and-rtl-design`).

---

## 6. Pre-flight / common-rejection checklist

- [ ] Icon is **square, full-bleed, not pre-rounded**; **App Store icon has no alpha**; Play
      adaptive layers keep the mark inside the **66 dp** safe circle.
- [ ] iOS **Liquid Glass** variants (light/dark/tinted/clear) all read at every grid size.
- [ ] Screenshots at the **correct current dimensions** per supported device family; **first
      2-3 frames** sell standalone; captions legible at **thumbnail** size and meet WCAG 1.4.3.
- [ ] No **cross-platform device frames**; no **misleading/lorem** screenshots; data is real and
      matches the shipped app.
- [ ] **No price/"free"/store badges** baked into the icon or used as the icon.
- [ ] App Preview is **real app footage**, 15-30 s, works **muted**, has a chosen poster frame.
- [ ] Copy fits each field's **exact char limit**; first description line carries the value prop;
      **no keyword-stuffing** in the Play description; iOS keyword field is **comma-no-space**.
- [ ] **Localized** sets don't overflow caption zones; RTL mirrors correctly.
- [ ] **Age rating / content rating** and **privacy labels / Data safety** are consistent with
      what the screenshots and copy depict.

---

## Provenance
Dimensions and field models follow current **App Store Connect** and **Google Play Console**
asset requirements as of 2026 (icon 1024/512, iPhone 6.9" 1290×2796, iPad 13" 2064×2752, Play
feature graphic 1024×500, App Preview 15-30 s, the stated character limits) and Apple's
**Liquid Glass** layered-icon model. Where a console states a newer number, the console is
authority. Applied per the Chwezi anti-slop doctrine (`doctrine/design-doctrine.md`): the
listing is a designed conversion surface, not a metadata form.
