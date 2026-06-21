# fonts/ - Premium font drop-in folders and scan protocol

These folders hold purchased or manually downloaded font files that are available on this
device. Font binaries are gitignored; the tracked `MANIFEST.md` files are the durable routing
and licence records. Agents must classify by design intent before scanning.

```text
fonts/
├── 01-formal-institutional/        MANIFEST.md  - official, legal, finance, board, SRS
├── 02-editorial-literary/          MANIFEST.md  - authored reports, essays, whitepapers
├── 03-modern-product-grotesque/    MANIFEST.md  - SaaS, startup, product, pitch decks
├── 04-technical-data-code/         MANIFEST.md  - dashboards, admin, API docs, code/data
├── 05-friendly-humanist/           MANIFEST.md  - healthcare, education, civic/service UI
├── 06-expressive-display-artistic/ MANIFEST.md  - campaigns, posters, cultural/hero display
├── 07-script-cursive-handwritten/  MANIFEST.md  - signatures, cursive, handwritten accents
└── 08-body-ui-workhorses/          MANIFEST.md  - quiet body/UI layer under a display face
```

## Selection protocol

1. Classify the artifact by context: document, site, app UI, dashboard, deck, campaign, etc.
2. Classify the desired voice: formal, editorial, product, technical, friendly, expressive, or
   script/cursive.
3. Classify the role: display, body, UI, code/data, or accent.
4. Scan the matching category folder for present `.ttf`, `.otf`, or `.woff2` files.
5. Read that folder's `MANIFEST.md` and confirm role, avoid-for notes, pairing, licence,
   embedding permission, and file redistribution permission.
6. If a present premium family fits the voice and licence, use it. Otherwise use the named OFL
   baseline from `doctrine/references/font-groups-and-usage.md`.
7. State the typeface pair and reason before producing the artifact.

## Manifest schema

Each manifest uses this schema so agents can make defensible choices:

```markdown
| Family | Role | Voice | Best for | Avoid for | Pair with | Licence | Embed? | Redistribute file? | Present? |
```

## Licence policy

- OFL families are safe to use and embed, but font files are still kept out of git by policy.
- Fontshare families such as Clash Display, Satoshi, Cabinet Grotesk, and General Sans may be
  used and embedded, but raw files may not be redistributed.
- Premium commercial families must be added to the right category manifest with explicit
  embedding and redistribution notes before use.
- Geist is banned. Do not place it in any category.

Drop files directly into the category folder, or into family subfolders inside it. Update the
manifest only when the licence or intended routing changes; actual file presence is detected by
scanning the device.
