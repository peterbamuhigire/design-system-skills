# fonts/ — Premium font drop-in folders & scan protocol

These four folders mirror the user's own `Downloads\Fonts` taxonomy exactly. They hold the
**premium font files** the user purchases and drops in per device. The `premium-font-scan`
skill reads them to decide whether a premium family should override the OFL baseline.

```
fonts/
├── 1-Editorial-Authoritative/   MANIFEST.md   ← reports, proposals, business plans, SRS
├── 2-Developer-Technical/       MANIFEST.md   ← dashboards, code UI, API docs
├── 3-Startup-Product/           MANIFEST.md   ← landing pages, SaaS marketing, decks
└── 4-Body-Workhorses/           MANIFEST.md   ← body layer under a display face
```

## The protocol (standard-first, premium-when-present)

1. A skill classifies the artifact into a group (see `doctrine/references/font-groups-and-usage.md`).
2. It **scans the matching folder** for actually-present families (binaries are gitignored, so
   presence varies per device).
3. It **reads the group's `MANIFEST.md`** for licence/embedding permission.
4. If a present premium family fits better *and* the licence allows the needed use → use it.
   Else → use the named OFL baseline. Always **state which and why**.

## Why binaries are gitignored

- Keeps the repo light (a single family across weights is hundreds of KB to MB).
- Respects licences uniformly — the **Fontshare** families (Clash Display, Satoshi, Cabinet
  Grotesk, General Sans) **forbid file redistribution**, so they must never enter git.
- The tracked **MANIFEST.md** files are the durable record of *what should be here* and *what
  each licence permits* — they sync via git; the files themselves you place per device.

Drop files directly into the group folder (subfolders per family are fine). Update the
MANIFEST's "Present?" column if you want a per-device note, but the MANIFEST's licence columns
are canonical.
