# Printer Specification and Preflight

Parent skill: [`../SKILL.md`](../SKILL.md) (`print-production-and-finishing`).

**When to read:** at job set-up (questions and specification sheet) and immediately before export
(preflight). Printer answers override every default in this file. Record the date each answer
was given.

---

## 1. Questions for the printer (ask before final artwork)

1. Which process will run this job: sheet-fed litho, web offset, digital (toner or inkjet), large
   format or screen print?
2. Which colour profile should the PDF target, and what is the total ink limit for this stock?
3. What bleed and what safety margin do you need? Any special requirement at the spine?
4. What is your rich black recipe, and your minimum printable tint?
5. Do you want black text set to overprint? How do you handle overprint on spot and metallic inks?
6. Which PDF standard and version do you accept (for example PDF/X-4 or PDF/X-1a), and do you want
   crop marks, registration marks or a cutter guide on a separate layer?
7. For folded work: what panel widths do you need for this stock weight?
8. For bound work: what is the maximum extent for saddle stitching on this stock, and what creep
   and gutter allowance does your imposition apply?
9. For packaging and die-cuts: please supply your die-line template and glue areas.
10. Which stocks do you hold locally, and what are the lead times for imported stock?
11. Can you show a drawdown or printed sample on this stock? What proof do you offer (contract
    proof, wet proof, digital proof on the actual stock)?
12. Can we attend a press check? At what time, and who signs off?
13. What finishes can you do in-house (lamination, spot varnish, foil, embossing, die-cutting),
    and which are subcontracted?
14. What overs and unders are normal on this quantity, and how is delivery handled?

**East African note:** many small and mid-sized jobs in Kampala, Nairobi, Kigali and Dar es
Salaam run on digital presses rather than litho. Digital devices have their own gamut and do not
behave like a litho press profile. Imported coated stock can be scarce or slow; plan an uncoated
alternative and adjust colour expectations. Humidity affects paper and drying, so allow extra
time. Confirm finishing capability locally before promising it; do not assume a finish seen in a
foreign sample is available.

## 2. Specification sheet (send with the files)

| Field | Entry |
|---|---|
| Job name and reference | |
| Client and account lead | |
| Trim size, orientation | |
| Extent (pages or panels) | |
| Quantity; acceptable overs/unders | |
| Process | litho / digital / large format / screen |
| Stock: name, weight, finish, whiteness; cover and text if different | |
| Colours: CMYK; named spot inks; varnish | |
| Colour profile and total ink limit (from printer, dated) | |
| Overprint and knock-out instructions | |
| Bleed; safety margin; spine rule | |
| Folds: type, panel widths; die-line reference; glue areas | |
| Binding: method; creep and gutter allowance | |
| Finishes: lamination (gloss, matt, soft-touch), spot varnish, foil, emboss or deboss, die-cut | |
| Proof: type, stock, number of rounds, approver | |
| Press check: date, time, attendee, sign-off authority | |
| Delivery: address, date, packing, split deliveries | |
| Contingency days in the schedule | |
| Files supplied: names, PDF standard, date | |

## 3. Preflight checklist (run in a preflight tool before export)

**Fonts**
- [ ] All fonts embedded (subset is acceptable); licences permit embedding for print.
- [ ] No missing glyphs or substituted faces.

**Images**
- [ ] Effective resolution about 300 ppi at placed size for litho (about twice the screen
      ruling); large format and digital devices follow the printer's figure.
- [ ] No placed image enlarged much beyond its size (about 105-110 per cent at most); rescale at
      source instead.
- [ ] No images placed far above the needed resolution (bloated files, possible banding).
- [ ] Printed matter that was scanned shows no moiré; photograph flat originals instead.

**Colour**
- [ ] Colour mode and profile as the printer specified; RGB images converted, or embedded
      profiles with a conversion on export the printer has agreed.
- [ ] No unused or accidental spot colours; no CMYK swatch mistakenly set as a spot.
- [ ] Total ink within the printer's limit, including dark photographs and rich blacks.
- [ ] Rich black only on large areas; small text in 100 per cent black only.
- [ ] Black text overprints; overprint on spot and metallic inks agreed with the printer.
- [ ] No tints below the printer's minimum; no tints of tints (resolve to real values).

**Geometry**
- [ ] Trim size correct on every page; bleed at least the printer's figure (commonly 3 mm) on
      every edge element; none at the spine where the binder says so.
- [ ] Live content inside the safety zone; folios and small items clear of trim.
- [ ] Panel widths and fold marks per the printer; die-line on its own non-printing layer.
- [ ] Glue areas free of ink and varnish.

**File**
- [ ] Pasteboard clean; hidden and unused layers removed.
- [ ] Crop, registration and cutter marks as requested.
- [ ] PDF standard and version as requested (confirm current printer preference; PDF/X-4 keeps
      live transparency and profiles, PDF/X-1a flattens and is CMYK or spot only).
- [ ] File name carries job, version and date.
