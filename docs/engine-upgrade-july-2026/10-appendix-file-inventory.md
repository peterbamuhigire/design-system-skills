# Appendix: Full Content Inventory

This inventory was captured before the audit reports were written. It excludes VCS/cache/dependency internals: `.git`, `node_modules`, `.venv`, `venv`, `__pycache__`, and `.pytest_cache`.

## Empty Directories

- `doctrine/examples`

## Temp/Backup Artefacts

None.

## Duplicate Content Hash Groups (Sample)

| SHA prefix | Size bytes | Count | Paths sample |
| --- | --- | --- | --- |
| 06ba38a94309 | 111552 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ThinRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ThinRoman.ttf |
| 9e4fb6eea9c5 | 110844 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraLightRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraLightRoman.ttf |
| 9a497d4c7930 | 107604 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-LightRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-LightRoman.ttf |
| d0cd268e800e | 99928 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraLightItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraLightItalic.ttf |
| 40a6ae415a3a | 99596 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ThinItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ThinItalic.ttf |
| 31b283d733e4 | 99000 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-RegularRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-RegularRoman.ttf |
| 4f9687efb025 | 98864 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-LightItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-LightItalic.ttf |
| e06ae68a4e0b | 95448 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-RegularItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-RegularItalic.ttf |
| d8ab8c244372 | 91984 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-MediumRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-MediumRoman.ttf |
| 76a9918e3d14 | 91084 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-MediumItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-MediumItalic.ttf |
| d8eb229a726a | 90000 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-SemiBoldRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-SemiBoldRoman.ttf |
| 48dabcd3c7ae | 88880 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-SemiBoldItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-SemiBoldItalic.ttf |
| dc2024014189 | 88612 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BoldRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BoldRoman.ttf |
| f8a1090b0846 | 88348 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraBoldItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraBoldItalic.ttf |
| b83f90fb14c0 | 88304 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BoldItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BoldItalic.ttf |
| 7dfe20b38e58 | 87996 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraBoldRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-ExtraBoldRoman.ttf |
| ae4b84b06ca9 | 85948 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BlackItalic.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BlackItalic.ttf |
| 181335a04104 | 85500 | 2 | fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BlackRoman.otf, fonts/08-body-ui-workhorses/publicalgnominia/PublicaIgnominia-BlackRoman.ttf |
| 53f27cbff163 | 58443 | 2 | fonts/05-friendly-humanist/bainsley/OFL-FAQ.txt, fonts/05-friendly-humanist/sans-mateo/OFL-FAQ.txt |
| 70788a590498 | 57832 | 2 | fonts/05-friendly-humanist/leggibilmente/Leggibilmente-LightItalic.otf, fonts/05-friendly-humanist/leggibilmente/Leggibilmente-LightItalic.ttf |

## Full Tree

```text
./
.gitignore (562 bytes)
AGENTS.md (1667 bytes)
CLAUDE.md (2565 bytes)
CONTRIBUTING.md (3375 bytes)
LICENSE (1094 bytes)
README.md (11583 bytes)
docs/
  RESUME.md (2961 bytes)
  docs/audits/
    docs/audits/post-phase-1/
      00-reaudit-summary.md (3515 bytes)
      02-coverage-and-taxonomy-reaudit.md (13338 bytes)
      03-existing-groups-reaudit.md (29306 bytes)
      05-per-output-type-reaudit.md (9032 bytes)
    docs/audits/post-v2-plan/
      00-reaudit-summary.md (5142 bytes)
      02-coverage-and-taxonomy-reaudit.md (5118 bytes)
      03-existing-groups-reaudit.md (6149 bytes)
      05-per-output-type-reaudit.md (5919 bytes)
  docs/book-study/
    00-synthesis.md (4671 bytes)
    01-ui-ux-craft.md (30914 bytes)
    02-interaction-patterns.md (19967 bytes)
    03-ux-writing.md (24481 bytes)
    04-storytelling-and-apple-craft.md (34845 bytes)
    05-fixing-bad-ux.md (12991 bytes)
    06-word-excel-tooling.md (11390 bytes)
  docs/initial-analysis/
    00-executive-summary.md (4509 bytes)
    01-methodology-and-rubric.md (2561 bytes)
    02-coverage-and-taxonomy.md (10734 bytes)
    03-existing-groups-audit.md (24676 bytes)
    04-gap-analysis-new-skills.md (13984 bytes)
    05-per-output-type-readiness.md (19345 bytes)
    06-2026-standards-benchmark.md (33067 bytes)
    07-hardening-existing-skills.md (31870 bytes)
    08-reading-list.md (18115 bytes)
    09-master-scorecard.md (3775 bytes)
    10-roadmap-to-world-class.md (3354 bytes)
    README.md (1335 bytes)
  docs/plans/
    docs/plans/hardening-june/
      PLAN-v2-book-informed.md (6088 bytes)
      README.md (5109 bytes)
      examples-backfill-tracker.md (1430 bytes)
      docs/plans/hardening-june/phase-0-foundations/
        00-overview.md (1587 bytes)
        01-taxonomy-migration.md (4902 bytes)
        02-cross-cutting-standards-refs.md (2789 bytes)
        03-examples-convention.md (1937 bytes)
        04-dedup-decks-and-color.md (3075 bytes)
      docs/plans/hardening-june/phase-1-p0-skills/
        00-overview.md (2364 bytes)
        01-skill-specs.md (8116 bytes)
        02-p0-ten-hardening.md (2896 bytes)
        03-sequencing-and-effort.md (2577 bytes)
      docs/plans/hardening-june/phase-2-p1-wave/
        00-overview.md (1763 bytes)
        01-skill-specs.md (5211 bytes)
        02-sequencing-and-effort.md (1900 bytes)
      docs/plans/hardening-june/phase-3-ceiling/
        00-overview.md (1713 bytes)
        01-p2-skill-specs.md (3602 bytes)
        02-reading-extraction-plan.md (3193 bytes)
        03-ongoing-program.md (2299 bytes)
doctrine/
  design-doctrine.md (9046 bytes)
  doctrine/examples/
  doctrine/references/
    ai-slop-banned-fonts.md (6182 bytes)
    ai-slop-taxonomy.md (6253 bytes)
    creative-selection-and-taste.md (7591 bytes)
    embedding-by-format.md (2316 bytes)
    font-groups-and-usage.md (5855 bytes)
    interaction-anti-patterns.md (13291 bytes)
    licensing-and-embedding.md (2524 bytes)
    living-slop-refresh-protocol.md (3502 bytes)
    pairing-principles.md (3243 bytes)
    system-font-fallbacks.md (3790 bytes)
    type-scale-and-spacing.md (2094 bytes)
    wcag-2.2-criteria.md (2947 bytes)
    web-performance-budgets-2026.md (1976 bytes)
fonts/
  README.md (10628 bytes)
  SUMMITSOFT-COMMERCIAL-LICENSE.pdf (5043084 bytes)
  fonts/01-formal-institutional/
    MANIFEST.md (2989 bytes)
    fonts/01-formal-institutional/arapey/
      ArapeyItalic-LwGZ.ttf (29568 bytes)
      ArapeyRegular-X2Md.ttf (26764 bytes)
      LICENSE.txt (90 bytes)
    fonts/01-formal-institutional/arodora-pro/
      ArodoraPro-Light.otf (74560 bytes)
      ArodoraPro-LightItalic.otf (78648 bytes)
      readme.txt (271 bytes)
    fonts/01-formal-institutional/aurelis/
      AurelisADFNo2Std-Bold.otf (41388 bytes)
      AurelisADFNo2Std-BoldItalic.otf (44488 bytes)
      AurelisADFNo2Std-Italic.otf (44092 bytes)
      AurelisADFNo2Std-Regular.otf (40704 bytes)
      AurelisADFScriptNo2Std-CdIta.otf (49992 bytes)
      AurelisADFScriptNo2Std-ExtIt.otf (44504 bytes)
      AurelisADFScriptNo2Std-Italic.otf (45036 bytes)
      NOTICE.txt (2040 bytes)
    fonts/01-formal-institutional/beau/
      BeauRegular-0nLo.ttf (230108 bytes)
      LICENSE.txt (89 bytes)
    fonts/01-formal-institutional/buenard/
      Buenard-Bold.ttf (58992 bytes)
      Buenard-Regular.ttf (60188 bytes)
      FONTLOG.txt (2147 bytes)
      OFL.txt (4410 bytes)
    fonts/01-formal-institutional/crimson-pro/
      CrimsonPro-ExtraLight.ttf (218976 bytes)
      CrimsonPro-ExtraLightItalic.ttf (224688 bytes)
      LICENSE.txt (565 bytes)
    fonts/01-formal-institutional/fjord/
      FjordOne-Jy9B.ttf (54156 bytes)
      LICENSE.txt (89 bytes)
    fonts/01-formal-institutional/lightweight-serif/
      LICENSE.txt (517 bytes)
      LIGHTWEIGHT SERIF.ttf (20256 bytes)
    fonts/01-formal-institutional/pelagiad/
      LICENSE.txt (4439 bytes)
      Pelagiad.ttf (30836 bytes)
    fonts/01-formal-institutional/podkova/
      OFL.txt (4475 bytes)
      Podkova-Bold.ttf (152512 bytes)
      Podkova-ExtraBold.ttf (147564 bytes)
      Podkova-Medium.ttf (142156 bytes)
      Podkova-Regular.ttf (130012 bytes)
      Podkova-Roman-VF.ttf (185908 bytes)
      Podkova-SemiBold.ttf (149304 bytes)
      Podkova-VF.ttf (190484 bytes)
    fonts/01-formal-institutional/spectral/
      LICENSE.txt (556 bytes)
      Spectral-Bold.ttf (293908 bytes)
      Spectral-BoldItalic.ttf (301912 bytes)
      Spectral-ExtraBold.ttf (276956 bytes)
      Spectral-ExtraBoldItalic.ttf (288176 bytes)
      Spectral-ExtraLight.ttf (252172 bytes)
      Spectral-ExtraLightItalic.ttf (275572 bytes)
      Spectral-Italic.ttf (286552 bytes)
      Spectral-Light.ttf (280728 bytes)
      Spectral-LightItalic.ttf (296716 bytes)
      Spectral-Medium.ttf (293248 bytes)
      Spectral-MediumItalic.ttf (300184 bytes)
      Spectral-Regular.ttf (276492 bytes)
      Spectral-SemiBold.ttf (289484 bytes)
      Spectral-SemiBoldItalic.ttf (299520 bytes)
    fonts/01-formal-institutional/trykker/
      OFL.txt (4489 bytes)
      Trykker-Regular.ttf (38140 bytes)
  fonts/02-editorial-literary/
    MANIFEST.md (3848 bytes)
    fonts/02-editorial-literary/andada/
      Andadaht_2015-Bold.otf (186948 bytes)
      Andadaht_2015-Bold.ttf (150980 bytes)
      Andadaht_2015-Bold.woff2 (61652 bytes)
      Andadaht_2015-BoldItalic.otf (183380 bytes)
      Andadaht_2015-BoldItalic.ttf (151632 bytes)
      Andadaht_2015-BoldItalic.woff2 (60848 bytes)
      Andadaht_2015-Italic.otf (185636 bytes)
      Andadaht_2015-Italic.ttf (152136 bytes)
      Andadaht_2015-Italic.woff2 (61116 bytes)
      Andadaht_2015-Regular.otf (185932 bytes)
      Andadaht_2015-Regular.ttf (150680 bytes)
      Andadaht_2015-Regular.woff2 (59508 bytes)
      LICENSE.md (4337 bytes)
      OFL.txt (4391 bytes)
      README.md (1757 bytes)
    fonts/02-editorial-literary/arrose/
      ARROSE.otf (99792 bytes)
      ARROSE.ttf (99792 bytes)
      License.txt (4483 bytes)
    fonts/02-editorial-literary/bernhard/
      B066000D.TTF (52608 bytes)
      LICENSE.txt (574 bytes)
    fonts/02-editorial-literary/bordeaux/
      B061013D.TTF (54392 bytes)
      B061033D.TTF (52172 bytes)
      B062000D.TTF (58424 bytes)
      LICENSE.txt (567 bytes)
    fonts/02-editorial-literary/broadsheet-ldo/
      BroadsheetLdo-vmGL.ttf (112040 bytes)
      BroadsheetLdoBold-w1W9.ttf (98212 bytes)
      BroadsheetLdoBoldItalic-7BKD.ttf (75608 bytes)
      BroadsheetLdoItalic-mLyv.ttf (89156 bytes)
      LICENSE.txt (79 bytes)
    fonts/02-editorial-literary/cardiff/
      Cardiff-5a2v.ttf (67984 bytes)
      CardiffBold-6av1.ttf (66940 bytes)
      CardiffBoldItalic-9op2.ttf (69292 bytes)
      CardiffItalic-yjAV.ttf (71248 bytes)
      LICENSE.txt (77 bytes)
    fonts/02-editorial-literary/coconat/
      Coconat-Bold.otf (40068 bytes)
      Coconat-Bold.woff2 (24368 bytes)
      Coconat-Demi.otf (41976 bytes)
      Coconat-Demi.woff2 (26424 bytes)
      Coconat-Regular.otf (38428 bytes)
      Coconat-Regular.woff2 (23720 bytes)
      LICENSE.txt (4392 bytes)
      copyright.glif (1352 bytes)
      copyright.glyph (1789 bytes)
    fonts/02-editorial-literary/cormorant-garamond/
      CormorantGaramond-Bold.ttf (871756 bytes)
      CormorantGaramond-BoldItalic.ttf (623224 bytes)
      CormorantGaramond-Italic.ttf (617128 bytes)
      CormorantGaramond-Light.ttf (885304 bytes)
      CormorantGaramond-LightItalic.ttf (614148 bytes)
      CormorantGaramond-Medium.ttf (878880 bytes)
      CormorantGaramond-MediumItalic.ttf (623428 bytes)
      CormorantGaramond-Regular.ttf (884540 bytes)
      CormorantGaramond-SemiBold.ttf (891380 bytes)
      CormorantGaramond-SemiBoldItalic.ttf (619608 bytes)
      LICENSE.txt (586 bytes)
    fonts/02-editorial-literary/fraunces/
      LICENSE.txt (556 bytes)
      fraunces-italicsoftwonkopszwght.ttf (414904 bytes)
      frauncessoftwonkopszwght.ttf (360440 bytes)
    fonts/02-editorial-literary/hattori-hanzo/
      Hattori Hanzo Italic.otf (36616 bytes)
      Hattori Hanzo.otf (36424 bytes)
      readme.txt (639 bytes)
    fonts/02-editorial-literary/negara-serif/
      LICENSE.txt (77 bytes)
      NegaraserifHairlineitalic-nRgjJ.otf (88580 bytes)
    fonts/02-editorial-literary/newsreader/
      LICENSE.txt (562 bytes)
      Newsreader-Italic[opsz,wght].ttf (496176 bytes)
      Newsreader[opsz,wght].ttf (451856 bytes)
    fonts/02-editorial-literary/nicolas-cochin/
      LICENSE.txt (572 bytes)
      N010013T.TTF (89468 bytes)
      N010016T.TTF (88908 bytes)
      N010033T.TTF (85720 bytes)
      N045016D.TTF (109092 bytes)
    fonts/02-editorial-literary/requiner/
      LICENSE.txt (508 bytes)
      Requiner-6RRLM.otf (36972 bytes)
    fonts/02-editorial-literary/rozina/
      Rozina V07-Bold.otf (44792 bytes)
      RozinaV06.otf (62448 bytes)
      readme.txt (160 bytes)
    fonts/02-editorial-literary/theano-didot/
      LICENSE.txt (91 bytes)
      TheanoDidotRegular-R3pA.ttf (379224 bytes)
      TheanoModernRegular-B7Wd.ttf (393684 bytes)
      TheanoOldStyleRegular-87Mg.ttf (463676 bytes)
    fonts/02-editorial-literary/vendome/
      LICENSE.txt (565 bytes)
      V004003T.TTF (56816 bytes)
      V004004T.TTF (56232 bytes)
      V004006T.TTF (53484 bytes)
      V004023T.TTF (55532 bytes)
      V004024T.TTF (55864 bytes)
      V004043T.TTF (54268 bytes)
      V004123D.TTF (43648 bytes)
    fonts/02-editorial-literary/windsor/
      LICENSE.txt (565 bytes)
      W002013D.TTF (64604 bytes)
      W002016D.TTF (66480 bytes)
      W002020D.TTF (67252 bytes)
      W002057D.TTF (64096 bytes)
      W010000D.TTF (64728 bytes)
      W013016D.TTF (113760 bytes)
  fonts/03-modern-product-grotesque/
    MANIFEST.md (3619 bytes)
    fonts/03-modern-product-grotesque/alan-sans/
      AlanSans-Black.otf (70660 bytes)
      AlanSans-Black.ttf (95084 bytes)
      AlanSans-Black.woff2 (38060 bytes)
      AlanSans-Bold.otf (73496 bytes)
      AlanSans-Bold.ttf (95296 bytes)
      AlanSans-Bold.woff2 (38796 bytes)
      AlanSans-ExtraBold.otf (73208 bytes)
      AlanSans-ExtraBold.ttf (95308 bytes)
      AlanSans-ExtraBold.woff2 (38732 bytes)
      AlanSans-Light.otf (70548 bytes)
      AlanSans-Light.ttf (95112 bytes)
      AlanSans-Light.woff2 (37572 bytes)
      AlanSans-Medium.otf (73328 bytes)
      AlanSans-Medium.ttf (95464 bytes)
      AlanSans-Medium.woff2 (38888 bytes)
      AlanSans-Regular.otf (72748 bytes)
      AlanSans-Regular.ttf (95800 bytes)
      AlanSans-Regular.woff2 (38888 bytes)
      AlanSans-SemiBold.otf (73516 bytes)
      AlanSans-SemiBold.ttf (95432 bytes)
      AlanSans-SemiBold.woff2 (38776 bytes)
      AlanSans[wght].woff2 (57484 bytes)
      OFL.txt (4388 bytes)
      README.md (2352 bytes)
    fonts/03-modern-product-grotesque/alfaqix/
      AlfaqixAlgorithm-SemiBold.otf (50096 bytes)
      AlfaqixDiode-SemiBold.otf (47404 bytes)
      AlfaqixEllipsoid-SemiBold.otf (50876 bytes)
      AlfaqixServo-SemiBold.otf (47624 bytes)
      LICENSE.txt (168 bytes)
      Typodermic Desktop EULA 2023.pdf (145707 bytes)
    fonts/03-modern-product-grotesque/basnet/
      1001fonts-basnet-eula.txt (2347 bytes)
      Basnet-ThinExpanded.otf (24616 bytes)
    fonts/03-modern-product-grotesque/coco/
      Coco-Bold.otf (43080 bytes)
      Coco-BoldCondensed.otf (43200 bytes)
      Coco-BoldCondensedItalic.otf (45736 bytes)
      Coco-BoldItalic.otf (45608 bytes)
      Coco-Condensed.otf (23660 bytes)
      Coco-CondensedItalic.otf (25328 bytes)
      Coco-Italic.otf (25684 bytes)
      Coco-Regular.otf (24384 bytes)
      readme.txt (741 bytes)
    fonts/03-modern-product-grotesque/esmeralda/
      COPYRIGHT.md (423 bytes)
      LICENSE.rtf (5110 bytes)
      README.rtf (20178 bytes)
      esmeraldagroterk-Regular.otf (26772 bytes)
      esmeraldagroterk-Regular.woff2 (17036 bytes)
    fonts/03-modern-product-grotesque/firjar/
      Firjar-Black.ttf (83668 bytes)
      Firjar-Black.woff2 (29596 bytes)
      Firjar-Bold.ttf (82564 bytes)
      Firjar-Bold.woff2 (29812 bytes)
      Firjar-ExtraBold.ttf (85344 bytes)
      Firjar-ExtraBold.woff2 (30104 bytes)
      Firjar-ExtraLight.ttf (78472 bytes)
      Firjar-ExtraLight.woff2 (29132 bytes)
      Firjar-Light.ttf (79788 bytes)
      Firjar-Light.woff2 (29536 bytes)
      Firjar-Regular.ttf (80880 bytes)
      Firjar-Regular.woff2 (29556 bytes)
      Firjar-SimiBold.ttf (82236 bytes)
      Firjar-SimiBold.woff2 (29500 bytes)
      Firjar-Thin.ttf (78088 bytes)
      Firjar-Thin.woff2 (28384 bytes)
      FirjarCondensed-Black.ttf (82440 bytes)
      FirjarCondensed-Black.woff2 (28960 bytes)
      FirjarCondensed-Bold.ttf (81480 bytes)
      FirjarCondensed-Bold.woff2 (29488 bytes)
      FirjarCondensed-ExtraBold.ttf (83752 bytes)
      FirjarCondensed-ExtraBold.woff2 (29820 bytes)
      FirjarCondensed-ExtraLight.ttf (78704 bytes)
      FirjarCondensed-ExtraLight.woff2 (28876 bytes)
      FirjarCondensed-Light.ttf (78664 bytes)
      FirjarCondensed-Light.woff2 (28988 bytes)
      FirjarCondensed-Regular.ttf (79528 bytes)
      FirjarCondensed-Regular.woff2 (28948 bytes)
      FirjarCondensed-SimiBold.ttf (80712 bytes)
      FirjarCondensed-SimiBold.woff2 (29212 bytes)
      FirjarCondensed-Thin.ttf (76360 bytes)
      FirjarCondensed-Thin.woff2 (27644 bytes)
      FirjarExpanded-Black.ttf (86380 bytes)
      FirjarExpanded-Black.woff2 (29772 bytes)
      FirjarExpanded-Bold.ttf (84284 bytes)
      FirjarExpanded-Bold.woff2 (30076 bytes)
      FirjarExpanded-ExtraBold.ttf (88336 bytes)
      FirjarExpanded-ExtraBold.woff2 (30704 bytes)
      FirjarExpanded-ExtraLight.ttf (79120 bytes)
      FirjarExpanded-ExtraLight.woff2 (29260 bytes)
      FirjarExpanded-Light.ttf (82608 bytes)
      FirjarExpanded-Light.woff2 (29588 bytes)
      FirjarExpanded-Regular.ttf (82252 bytes)
      FirjarExpanded-Regular.woff2 (29720 bytes)
      FirjarExpanded-SimiBold.ttf (84172 bytes)
      FirjarExpanded-SimiBold.woff2 (29980 bytes)
      FirjarExpanded-Thin.ttf (78632 bytes)
      FirjarExpanded-Thin.woff2 (28308 bytes)
      Firjar[wdth,wght].ttf (120740 bytes)
      Firjar[wdth,wght].woff2 (50756 bytes)
      OFL.txt (4390 bytes)
      README.md (4190 bytes)
    fonts/03-modern-product-grotesque/genaminto/
      Genaminto-Regular.otf (100940 bytes)
      Genaminto-Regular.ttf (97312 bytes)
      OFL.txt (4374 bytes)
      README.md (633 bytes)
    fonts/03-modern-product-grotesque/geoform/
      Geoform-BF6556c6e73002d.otf (174728 bytes)
      Geoform-Bold-BF6556c6e7190d1.otf (169548 bytes)
      Geoform-BoldItalic-BF6556c6e753041.otf (175312 bytes)
      Geoform-ExtraBold-BF6556c6e755e60.otf (173068 bytes)
      Geoform-ExtraBoldItalic-BF6556c6e7447bb.otf (174000 bytes)
      Geoform-ExtraLight-BF6556c6e7587d5.otf (173924 bytes)
      Geoform-ExtraLightItalic-BF6556c6e726a6e.otf (175780 bytes)
      Geoform-Heavy-BF6556c6e708a5d.otf (173344 bytes)
      Geoform-HeavyItalic-BF6556c6e72fe24.otf (175236 bytes)
      Geoform-Italic-BF6556c6e72e7a7.otf (176824 bytes)
      Geoform-Light-BF6556c6e751770.otf (170124 bytes)
      Geoform-LightItalic-BF6556c6e74adf6.otf (173892 bytes)
      Geoform-Medium-BF6556c6e620ac4.otf (174596 bytes)
      Geoform-MediumItalic-BF6556c6e73a415.otf (176052 bytes)
      Geoform-Thin-BF6556c6e72e8c9.otf (170804 bytes)
      Geoform-ThinItalic-BF6556c6e758695.otf (174164 bytes)
      LICENSE.txt (507 bytes)
    fonts/03-modern-product-grotesque/hangar/
      Hangar.otf (30532 bytes)
      LICENSE.txt (4726 bytes)
      README.md (568 bytes)
    fonts/03-modern-product-grotesque/juliett/
      Juliett-Bold.otf (72304 bytes)
      Juliett-Bold.ttf (72304 bytes)
      Juliett-BoldItalic.otf (77496 bytes)
      Juliett-BoldItalic.ttf (77496 bytes)
      Juliett-Italic.otf (78508 bytes)
      Juliett-Italic.ttf (78508 bytes)
      Juliett-Regular.otf (73852 bytes)
      Juliett-Regular.ttf (73852 bytes)
      License.txt (4485 bytes)
    fonts/03-modern-product-grotesque/magnisa_sans/
      LICENSE.txt (154 bytes)
      MagnisaSans-Italic.otf (35256 bytes)
      MagnisaSans-Italic.ttf (66480 bytes)
      MagnisaSans-Regular.otf (33724 bytes)
      MagnisaSans-Regular.ttf (82536 bytes)
    fonts/03-modern-product-grotesque/nevermind_bauhaus/
      LICENSE.txt (4351 bytes)
      NeverMindBauhaus-Bold.ttf (39632 bytes)
      NeverMindBauhaus-DemiBold.ttf (39448 bytes)
      NeverMindBauhaus-ExtraLight.ttf (38868 bytes)
      NeverMindBauhaus-Extrabold.ttf (39900 bytes)
      NeverMindBauhaus-Heavy.ttf (39680 bytes)
      NeverMindBauhaus-Light.ttf (38892 bytes)
      NeverMindBauhaus-Medium.ttf (39152 bytes)
      NeverMindBauhaus-Regular.ttf (39092 bytes)
      NeverMindBauhaus-Thin.ttf (38520 bytes)
      README.md (2553 bytes)
    fonts/03-modern-product-grotesque/orbix/
      LICENSE (4412 bytes)
      Orbix-Regular.otf (10320 bytes)
      Orbix-Regular.ttf (25108 bytes)
      Orbix-Regular.woff2 (9976 bytes)
      README-CN.md (2017 bytes)
      README.md (2249 bytes)
    fonts/03-modern-product-grotesque/oregon-ldo/
      LICENSE.txt (75 bytes)
      OregonLdo-d9q7.ttf (131748 bytes)
      OregonLdoBlack-PKlE.ttf (100352 bytes)
      OregonLdoBlackOblique-L3G4.ttf (87496 bytes)
      OregonLdoBlackSinistral-X3MK.ttf (87968 bytes)
      OregonLdoBold-gxe6.ttf (103612 bytes)
      OregonLdoBoldOblique-owpz.ttf (99656 bytes)
      OregonLdoBook-4BYD.ttf (138864 bytes)
      OregonLdoBookOblique-0W1X.ttf (121592 bytes)
      OregonLdoBookSinistral-eZ4B.ttf (121960 bytes)
      OregonLdoCondensed-Wyrv.ttf (101080 bytes)
      OregonLdoCondensedBlack-ax59.ttf (58004 bytes)
      OregonLdoCondensedBlackOblique-EaOl.ttf (64500 bytes)
      OregonLdoCondensedBold-OVg3.ttf (54108 bytes)
      OregonLdoCondensedBoldOblique-ZVaK.ttf (59828 bytes)
      OregonLdoCondensedOblique-3z2z.ttf (102224 bytes)
      OregonLdoDemibold-x3qR.ttf (123688 bytes)
      OregonLdoDemiboldOblique-p7LZ.ttf (106612 bytes)
      OregonLdoDemiboldSinistral-DOy0.ttf (106524 bytes)
      OregonLdoExtended-ALWm.ttf (103660 bytes)
      OregonLdoExtendedBlack-qZq0.ttf (60596 bytes)
      OregonLdoExtendedBlackOblique-VGJV.ttf (67168 bytes)
      OregonLdoExtendedBold-JRen.ttf (57724 bytes)
      OregonLdoExtendedBoldOblique-GOeZ.ttf (62028 bytes)
      OregonLdoExtendedOblique-jEv7.ttf (105756 bytes)
      OregonLdoExtrablack-z8ql.ttf (97856 bytes)
      OregonLdoExtrablackOblique-51wj.ttf (88972 bytes)
      OregonLdoExtrablackSinistral-6Y7v.ttf (89064 bytes)
      OregonLdoExtrabold-ywqZ.ttf (103800 bytes)
      OregonLdoExtraboldOblique-9YP0.ttf (89724 bytes)
      OregonLdoExtraboldSinistral-lg7q.ttf (89536 bytes)
      OregonLdoLight-nRd4.ttf (130276 bytes)
      OregonLdoLightOblique-1GMM.ttf (109420 bytes)
      OregonLdoLightSinistral-RpGe.ttf (120368 bytes)
      OregonLdoMedium-BWen.ttf (124228 bytes)
      OregonLdoMediumOblique-8MdA.ttf (106908 bytes)
      OregonLdoMediumSinistral-YzaL.ttf (105800 bytes)
      OregonLdoOblique-rgqK.ttf (114692 bytes)
      OregonLdoSinistral-MV9v.ttf (113268 bytes)
      OregonLdoSinistralBold-K7ae.ttf (102628 bytes)
      OregonLdoUltrablack-2OKX.ttf (95300 bytes)
      OregonLdoUltrablackOblique-vmqL.ttf (85048 bytes)
      OregonLdoUltrablackSinistral-w1q9.ttf (84340 bytes)
      OregonLdoVanishing-7BmD.ttf (308600 bytes)
      OregonLdoVanishingBold-mLmv.ttf (209808 bytes)
      OregonLdoVanishingBoldOblique-d987.ttf (231132 bytes)
      OregonLdoVanishingOblique-PKAE.ttf (254500 bytes)
    fonts/03-modern-product-grotesque/parsons-modern-sans/
      ParsonsModernSans-Regular.ttf (20040 bytes)
      readme.txt (1059 bytes)
    fonts/03-modern-product-grotesque/shinko-sans/
      LICENSE.txt (511 bytes)
      ShinkosansRegular-8OO50.otf (32808 bytes)
    fonts/03-modern-product-grotesque/vincendo/
      License.txt (4481 bytes)
      Vincendo-Italic.otf (103900 bytes)
      Vincendo-Italic.ttf (103900 bytes)
      Vincendo-Regular.otf (96616 bytes)
      Vincendo-Regular.ttf (96616 bytes)
    fonts/03-modern-product-grotesque/wavere/
      LICENSE.txt (139 bytes)
      READ THIS BEFORE USE.txt (133 bytes)
      Wavere-Regular.otf (15924 bytes)
      Wavere-Regular.ttf (15924 bytes)
  fonts/04-technical-data-code/
    MANIFEST.md (3566 bytes)
    fonts/04-technical-data-code/accuratist/
      Accuratist.otf (143308 bytes)
      Accuratist.ttf (108664 bytes)
      LICENSE.txt (187 bytes)
    fonts/04-technical-data-code/fifteen/
      Fifteen-Bold.ttf (352408 bytes)
      Fifteen-BoldItalic.ttf (24692 bytes)
      Fifteen-ExtraLight.ttf (358856 bytes)
      Fifteen-ExtraLightItalic.ttf (24592 bytes)
      Fifteen-Italic.ttf (24000 bytes)
      Fifteen-Light.ttf (353944 bytes)
      Fifteen-LightItalic.ttf (24436 bytes)
      Fifteen-Medium.ttf (354756 bytes)
      Fifteen-MediumItalic.ttf (24344 bytes)
      Fifteen-Regular.ttf (360336 bytes)
      Fifteen-SemiBold.ttf (353236 bytes)
      Fifteen-SemiBoldItalic.ttf (24644 bytes)
      Fifteen-Thin.ttf (355360 bytes)
      Fifteen-ThinItalic.ttf (24540 bytes)
      LICENSE (1097 bytes)
      README.md (2940 bytes)
    fonts/04-technical-data-code/gyrotrope/
      Gyrotrope-Black.otf (77108 bytes)
      Gyrotrope-Bold.otf (77552 bytes)
      Gyrotrope-ExtraBold.otf (77964 bytes)
      Gyrotrope-Medium.otf (75576 bytes)
      Gyrotrope-Regular.otf (70632 bytes)
      Gyrotrope-Semibold.otf (77576 bytes)
      GyrotropeVF.ttf (100680 bytes)
      OFL.txt (4410 bytes)
      README.md (1068 bytes)
    fonts/04-technical-data-code/isonorm/
      I011000D.TTF (54964 bytes)
      LICENSE.txt (565 bytes)
    fonts/04-technical-data-code/j-audio-cassette/
      J Audio Cassette.otf (23288 bytes)
      OFL.txt (4449 bytes)
    fonts/04-technical-data-code/jupiteroid/
      Jupiteroid-Bold.otf (78004 bytes)
      Jupiteroid-Bold.ttf (78004 bytes)
      Jupiteroid-Bold.woff2 (20572 bytes)
      Jupiteroid-BoldItalic.otf (86164 bytes)
      Jupiteroid-BoldItalic.ttf (86164 bytes)
      Jupiteroid-BoldItalic.woff2 (22576 bytes)
      Jupiteroid-Italic.otf (88012 bytes)
      Jupiteroid-Italic.ttf (88012 bytes)
      Jupiteroid-Italic.woff2 (22988 bytes)
      Jupiteroid-Light.otf (79304 bytes)
      Jupiteroid-Light.ttf (79304 bytes)
      Jupiteroid-Light.woff2 (20300 bytes)
      Jupiteroid-LightItalic.otf (87856 bytes)
      Jupiteroid-LightItalic.ttf (87856 bytes)
      Jupiteroid-LightItalic.woff2 (22308 bytes)
      Jupiteroid-Regular.otf (79872 bytes)
      Jupiteroid-Regular.ttf (79872 bytes)
      Jupiteroid-Regular.woff2 (20932 bytes)
      License.txt (7169 bytes)
    fonts/04-technical-data-code/meridiana/
      Infos.pdf (37700 bytes)
      LICENSE.txt (152 bytes)
      Meridiana-Black.otf (48404 bytes)
      Meridiana-BlackOblique.otf (57464 bytes)
      Meridiana-Oblique-black+red-COLRv1.ttf (62420 bytes)
      Meridiana-Oblique-black+red-sbix.ttf (225020 bytes)
      Meridiana-Oblique-black+white-COLRv1.ttf (62444 bytes)
      Meridiana-Oblique-black+white-sbix.ttf (233336 bytes)
      Meridiana-black+red-COLRv1.ttf (69520 bytes)
      Meridiana-black+red-sbix.ttf (212540 bytes)
      Meridiana-black+white-COLRv1.ttf (69544 bytes)
      Meridiana-black+white-sbix.ttf (215420 bytes)
    fonts/04-technical-data-code/narita/
      Narita-Monospace.otf (76336 bytes)
      readme.txt (79 bytes)
    fonts/04-technical-data-code/ocr/
      LICENSE.txt (557 bytes)
      O001000M.TTF (62136 bytes)
      O019000M.TTF (45272 bytes)
    fonts/04-technical-data-code/pointfree/
      UNLICENSE.txt (1233 bytes)
      pointfree.ttf (27052 bytes)
    fonts/04-technical-data-code/quartz/
      LICENSE.txt (563 bytes)
      Q005000D.TTF (47044 bytes)
    fonts/04-technical-data-code/relief-singleline/
      OFL.txt (4404 bytes)
      README.md (11071 bytes)
      ReliefSingleLine-Ornament.ttf (30884 bytes)
      ReliefSingleLineCAD-Regular.ttf (53496 bytes)
      ReliefSingleLineOTF-SVG-Regular.otf (299552 bytes)
      ReliefSingleLineOTF-SVGOrnament-Regular.otf (89992 bytes)
      ReliefSingleLineOrnamentOutline-Regular.otf (19136 bytes)
      ReliefSingleLineOrnamentOutline-Regular.woff2 (10992 bytes)
      ReliefSingleLineOutline-Regular.otf (62108 bytes)
      ReliefSingleLineOutline-Regular.woff2 (33696 bytes)
    fonts/04-technical-data-code/semi_coder/
      OFL.txt (4559 bytes)
      SemiCoder.otf (90248 bytes)
      SemiCoderT.ttf (44464 bytes)
    fonts/04-technical-data-code/serpentine/
      LICENSE.txt (571 bytes)
      S017016D.TTF (107388 bytes)
      S017036D.TTF (101940 bytes)
      S017126D.TTF (48568 bytes)
    fonts/04-technical-data-code/snv/
      LICENSE.txt (557 bytes)
      S061013D.TTF (46252 bytes)
      S061053D.TTF (46044 bytes)
      S061133D.TTF (47456 bytes)
    fonts/04-technical-data-code/sono/
      AUTHOR.txt (283 bytes)
      OFL.txt (4424 bytes)
      fonts/04-technical-data-code/sono/desktop/
        Sono-Bold.ttf (107896 bytes)
        Sono-ExtraBold.ttf (108216 bytes)
        Sono-ExtraLight.ttf (108752 bytes)
        Sono-Light.ttf (107336 bytes)
        Sono-Medium.ttf (109328 bytes)
        Sono-Regular.ttf (107236 bytes)
        Sono-SemiBold.ttf (108744 bytes)
      fonts/04-technical-data-code/sono/variable/
        SonoVariable.ttf (127692 bytes)
        SonoVariable.woff2 (53656 bytes)
      fonts/04-technical-data-code/sono/web/
        Sono-Bold.woff2 (40552 bytes)
        Sono-ExtraBold.woff2 (39644 bytes)
        Sono-ExtraLight.woff2 (38952 bytes)
        Sono-Light.woff2 (39884 bytes)
        Sono-Medium.woff2 (40540 bytes)
        Sono-Regular.woff2 (40092 bytes)
        Sono-SemiBold.woff2 (40452 bytes)
    fonts/04-technical-data-code/terminal-land/
      LICENSE.md (4430 bytes)
      README.md (77 bytes)
      TerminalLandMono-Bold.otf (37516 bytes)
      TerminalLandMono-Bold.woff2 (17344 bytes)
      TerminalLandMono-BoldItalic.otf (40260 bytes)
      TerminalLandMono-BoldItalic.woff2 (19448 bytes)
      TerminalLandMono-Italic.otf (39168 bytes)
      TerminalLandMono-Italic.woff2 (18984 bytes)
      TerminalLandMono-Regular.otf (36340 bytes)
      TerminalLandMono-Regular.woff2 (17032 bytes)
      TerminalLandMonoSans-Bold.otf (36060 bytes)
      TerminalLandMonoSans-Bold.woff2 (16756 bytes)
      TerminalLandMonoSans-BoldItalic.otf (37636 bytes)
      TerminalLandMonoSans-BoldItalic.woff2 (18028 bytes)
      TerminalLandMonoSans-Italic.otf (36832 bytes)
      TerminalLandMonoSans-Italic.woff2 (17664 bytes)
      TerminalLandMonoSans-Regular.otf (35412 bytes)
      TerminalLandMonoSans-Regular.woff2 (16480 bytes)
  fonts/05-friendly-humanist/
    MANIFEST.md (2836 bytes)
    fonts/05-friendly-humanist/arumira/
      Arumira-Medium.otf (38928 bytes)
      LICENSE.txt (145 bytes)
    fonts/05-friendly-humanist/atkinson-hyperlegible/
      AtkinsonHyperlegibleBold102.ttf (43756 bytes)
      AtkinsonHyperlegibleBoldItalic102.ttf (44664 bytes)
      AtkinsonHyperlegibleItalic102.ttf (43540 bytes)
      AtkinsonHyperlegibleRegular102.ttf (42596 bytes)
      LICENSE.txt (595 bytes)
    fonts/05-friendly-humanist/bainsley/
      Bainsley.ttf (479764 bytes)
      BainsleyBold.ttf (478536 bytes)
      BainsleyBoldItalic.ttf (395508 bytes)
      BainsleyItalic.ttf (424108 bytes)
      OFL-FAQ.txt (58443 bytes)
      OFL.txt (4519 bytes)
      Read_Me.txt (1759 bytes)
    fonts/05-friendly-humanist/bellota/
      Bellota-Black.otf (164096 bytes)
      Bellota-Black.ttf (234544 bytes)
      Bellota-BlackItalic.otf (166776 bytes)
      Bellota-BlackItalic.ttf (244488 bytes)
      Bellota-Bold.otf (165668 bytes)
      Bellota-Bold.ttf (249572 bytes)
      Bellota-BoldItalic.otf (167216 bytes)
      Bellota-BoldItalic.ttf (244736 bytes)
      Bellota-Extrablack.otf (163740 bytes)
      Bellota-ExtrablackItalic.otf (155920 bytes)
      Bellota-Extrabold.otf (168384 bytes)
      Bellota-Extrabold.ttf (241248 bytes)
      Bellota-ExtraboldItalic.otf (169704 bytes)
      Bellota-ExtraboldItalic.ttf (240284 bytes)
      Bellota-Extralight.otf (163248 bytes)
      Bellota-Extralight.ttf (209244 bytes)
      Bellota-ExtralightItalic.otf (162552 bytes)
      Bellota-ExtralightItalic.ttf (209340 bytes)
      Bellota-Italic.otf (163316 bytes)
      Bellota-Italic.ttf (221456 bytes)
      Bellota-Italic[wght].ttf (225964 bytes)
      Bellota-Light.otf (162292 bytes)
      Bellota-Light.ttf (212472 bytes)
      Bellota-LightItalic.otf (163180 bytes)
      Bellota-LightItalic.ttf (210320 bytes)
      Bellota-Medium.otf (160848 bytes)
      Bellota-Medium.ttf (230292 bytes)
      Bellota-MediumItalic.otf (162184 bytes)
      Bellota-MediumItalic.ttf (224852 bytes)
      Bellota-Regular.otf (160952 bytes)
      Bellota-Regular.ttf (223204 bytes)
      Bellota-Semibold.otf (164192 bytes)
      Bellota-Semibold.ttf (236660 bytes)
      Bellota-SemiboldItalic.otf (164304 bytes)
      Bellota-SemiboldItalic.ttf (239760 bytes)
      Bellota-Thin.otf (158296 bytes)
      Bellota-Thin.ttf (210260 bytes)
      Bellota-ThinItalic.otf (157240 bytes)
      Bellota-ThinItalic.ttf (204844 bytes)
      Bellota[wght].ttf (220976 bytes)
      OFL.txt (4386 bytes)
      readme.md (3007 bytes)
    fonts/05-friendly-humanist/galiver-sans/
      GALS.ttf (135740 bytes)
      GALSB.ttf (134500 bytes)
      GALSBI.ttf (229392 bytes)
      GALSI.ttf (230480 bytes)
      License.txt (67 bytes)
      SGALS.ttf (245580 bytes)
      SGALSB.ttf (243260 bytes)
      SGALSBI.ttf (254892 bytes)
      SGALSI.ttf (166648 bytes)
    fonts/05-friendly-humanist/gotu/
      AUTHORS.txt (342 bytes)
      Copyright.txt (118 bytes)
      Gotu-Regular.ttf (697836 bytes)
      OFL.txt (4349 bytes)
      README.md (1069 bytes)
    fonts/05-friendly-humanist/leggibilmente/
      Leggibilmente-BoldItalic.otf (57220 bytes)
      Leggibilmente-BoldItalic.ttf (57220 bytes)
      Leggibilmente-BoldRoman.otf (53308 bytes)
      Leggibilmente-BoldRoman.ttf (53308 bytes)
      Leggibilmente-ExtraBoldItalic.otf (57180 bytes)
      Leggibilmente-ExtraBoldItalic.ttf (57180 bytes)
      Leggibilmente-ExtraBoldRoman.otf (53308 bytes)
      Leggibilmente-ExtraBoldRoman.ttf (53308 bytes)
      Leggibilmente-ExtraLightItalic.otf (56696 bytes)
      Leggibilmente-ExtraLightItalic.ttf (56696 bytes)
      Leggibilmente-ExtraLightRoman.otf (53960 bytes)
      Leggibilmente-ExtraLightRoman.ttf (53960 bytes)
      Leggibilmente-LightItalic.otf (57832 bytes)
      Leggibilmente-LightItalic.ttf (57832 bytes)
      Leggibilmente-LightRoman.otf (53880 bytes)
      Leggibilmente-LightRoman.ttf (53880 bytes)
      Leggibilmente-MediumItalic.otf (57516 bytes)
      Leggibilmente-MediumItalic.ttf (57516 bytes)
      Leggibilmente-MediumRoman.otf (53704 bytes)
      Leggibilmente-MediumRoman.ttf (53704 bytes)
      Leggibilmente-NewsItalic.otf (57664 bytes)
      Leggibilmente-NewsItalic.ttf (57664 bytes)
      Leggibilmente-NewsRoman.otf (53784 bytes)
      Leggibilmente-NewsRoman.ttf (53784 bytes)
      Leggibilmente-RegularItalic.otf (57668 bytes)
      Leggibilmente-RegularItalic.ttf (57668 bytes)
      Leggibilmente-RegularRoman.otf (53724 bytes)
      Leggibilmente-RegularRoman.ttf (53724 bytes)
      Leggibilmente-SemiBoldItalic.otf (57384 bytes)
      Leggibilmente-SemiBoldItalic.ttf (57384 bytes)
      Leggibilmente-SemiBoldRoman.otf (53528 bytes)
      Leggibilmente-SemiBoldRoman.ttf (53528 bytes)
      Leggibilmente.ttf (150616 bytes)
      Leggibilmente.woff2 (75024 bytes)
      OFL.txt (4391 bytes)
      README.md (1150 bytes)
    fonts/05-friendly-humanist/lexend/
      LICENSE.txt (550 bytes)
      Lexend[wght].ttf (175756 bytes)
    fonts/05-friendly-humanist/momo-trust-display/
      MomoTrustDisplay-Regular.otf (64644 bytes)
      MomoTrustDisplay-Regular.ttf (93640 bytes)
      OFL.txt (4411 bytes)
      README.md (384 bytes)
    fonts/05-friendly-humanist/notes-sans/
      1001fonts-notes-sans-eula.txt (2391 bytes)
      NotesSans-Free.otf (45924 bytes)
    fonts/05-friendly-humanist/sans-mateo/
      OFL-FAQ.txt (58443 bytes)
      OFL.txt (4502 bytes)
      Read_Me.txt (1640 bytes)
      SansMateo.ttf (276980 bytes)
      SansMateoBold.ttf (278212 bytes)
      SansMateoBoldItalic.ttf (184500 bytes)
      SansMateoItalic.ttf (186712 bytes)
    fonts/05-friendly-humanist/super-starfish/
      Super Starfish.ttf (216416 bytes)
      readme.txt (332 bytes)
  fonts/06-expressive-display-artistic/
    MANIFEST.md (3666 bytes)
    fonts/06-expressive-display-artistic/belagak/
      Belagak.otf (63288 bytes)
      Belagak.ttf (62448 bytes)
      Readme.txt (450 bytes)
    fonts/06-expressive-display-artistic/broadway/
      B034000D.TTF (58660 bytes)
      B034800D.TTF (56936 bytes)
      B037000D.TTF (105196 bytes)
      B037000P.TTF (61892 bytes)
      B037128D.TTF (42148 bytes)
      B037298P.TTF (106928 bytes)
      B037800D.TTF (55148 bytes)
      B079000D.TTF (57756 bytes)
      B094000D.TTF (71440 bytes)
      LICENSE.txt (1337 bytes)
    fonts/06-expressive-display-artistic/capo-sfogliato/
      Capo_Sfogliato.otf (175900 bytes)
      Capo_Sfogliato.ttf (135240 bytes)
      Capo_Sfogliato.woff2 (88624 bytes)
      OFL.txt (4435 bytes)
      README.md (735 bytes)
    fonts/06-expressive-display-artistic/compacta/
      C01B033D.TTF (60688 bytes)
      LICENSE.txt (1337 bytes)
    fonts/06-expressive-display-artistic/frankfurter/
      F007014D.TTF (56540 bytes)
      F067014D.TTF (67356 bytes)
      F069000D.TTF (112292 bytes)
      LICENSE.txt (1340 bytes)
    fonts/06-expressive-display-artistic/genesys/
      Genesys.ttf (24532 bytes)
      OFL-FAQ.txt (59071 bytes)
      OFL.txt (4454 bytes)
    fonts/06-expressive-display-artistic/golden-goose/
      Freebie License with Commercial Grants-ud.pdf (97739 bytes)
      GoldenGooseUppercase-VariableVF.ttf (26248 bytes)
      LICENSE.txt (129 bytes)
    fonts/06-expressive-display-artistic/greengoth/
      Greengoth Expanded.ttf (53764 bytes)
      Greengoth Regular.ttf (51300 bytes)
      readme.txt (5363 bytes)
    fonts/06-expressive-display-artistic/hd-sinar/
      HDSinar-Reversed.otf (95472 bytes)
      HDSinar-Reversed.ttf (105576 bytes)
      HDSinar-Reversed.woff2 (43188 bytes)
      HDSinar-ReversedBold.otf (100324 bytes)
      HDSinar-ReversedBold.ttf (105792 bytes)
      HDSinar-ReversedBold.woff2 (44220 bytes)
      HDSinar-ReversedExtrabold.otf (99952 bytes)
      HDSinar-ReversedExtrabold.ttf (105820 bytes)
      HDSinar-ReversedExtrabold.woff2 (44196 bytes)
      HDSinar-ReversedExtralight.otf (101232 bytes)
      HDSinar-ReversedExtralight.ttf (105892 bytes)
      HDSinar-ReversedExtralight.woff2 (44464 bytes)
      HDSinar-ReversedHeavy.otf (95808 bytes)
      HDSinar-ReversedHeavy.ttf (105440 bytes)
      HDSinar-ReversedHeavy.woff2 (43048 bytes)
      HDSinar-ReversedLight.otf (101320 bytes)
      HDSinar-ReversedLight.ttf (105916 bytes)
      HDSinar-ReversedLight.woff2 (44328 bytes)
      HDSinar-ReversedMedium.otf (100920 bytes)
      HDSinar-ReversedMedium.ttf (105820 bytes)
      HDSinar-ReversedMedium.woff2 (44260 bytes)
      HDSinar-ReversedSemibold.otf (100692 bytes)
      HDSinar-ReversedSemibold.ttf (105872 bytes)
      HDSinar-ReversedSemibold.woff2 (44228 bytes)
      HDSinar-ReversedThin.otf (96048 bytes)
      HDSinar-ReversedThin.ttf (105552 bytes)
      HDSinar-ReversedThin.woff2 (43288 bytes)
      HDSinar-ReversedVF.ttf (238600 bytes)
      HDSinar-ReversedVF.woff2 (106840 bytes)
      LICENSE.txt (4385 bytes)
      README.md (569 bytes)
    fonts/06-expressive-display-artistic/horovod/
      Horovod-Regular.otf (38352 bytes)
      Horovod-Regular.ttf (155140 bytes)
      LICENSE RU.txt (5110 bytes)
      LICENSE.txt (2576 bytes)
    fonts/06-expressive-display-artistic/lapsus-pro/
      LapsusPro-Bold.otf (45532 bytes)
      SIL Open Font License.txt (4380 bytes)
    fonts/06-expressive-display-artistic/latin-wide/
      L006000D.TTF (103040 bytes)
      L006128D.TTF (41140 bytes)
      LICENSE.txt (1339 bytes)
    fonts/06-expressive-display-artistic/life-savers-family/
      life-savers.bold.ttf (179864 bytes)
      life-savers.extrabold.ttf (212396 bytes)
      life-savers.regular.ttf (198256 bytes)
      readme.txt (107 bytes)
    fonts/06-expressive-display-artistic/metropolitaines/
      LICENSE.txt (1344 bytes)
      M041000D.TTF (49936 bytes)
      M041000P.TTF (47540 bytes)
      M041296P.TTF (102952 bytes)
      M041800D.TTF (52116 bytes)
    fonts/06-expressive-display-artistic/rum-raisin/
      readme.txt (107 bytes)
      rum-raisin.regular.ttf (61812 bytes)
    fonts/06-expressive-display-artistic/southgetto/
      SOUTHGHETTO.ttf (32664 bytes)
      readme.txt (92 bytes)
    fonts/06-expressive-display-artistic/stop/
      LICENSE.txt (1333 bytes)
      S013000D.TTF (43280 bytes)
      S013800D.TTF (85332 bytes)
      S13000D2.TTF (48444 bytes)
    fonts/06-expressive-display-artistic/tenada/
      LICENSE.txt (125 bytes)
      Tenada.ttf (996112 bytes)
      readme_tenada_font.pdf (209083 bytes)
    fonts/06-expressive-display-artistic/thorowgood/
      LICENSE.txt (1339 bytes)
      T003003D.TTF (55260 bytes)
      T003023D.TTF (56492 bytes)
    fonts/06-expressive-display-artistic/thunderbird/
      LICENSE.txt (1340 bytes)
      T009013D.TTF (75280 bytes)
      T009053D.TTF (54720 bytes)
  fonts/07-script-cursive-handwritten/
    MANIFEST.md (3178 bytes)
    fonts/07-script-cursive-handwritten/choc/
      C047000D.TTF (73928 bytes)
      C047A00D.TTF (59120 bytes)
      LICENSE.txt (559 bytes)
    fonts/07-script-cursive-handwritten/coronet/
      C093000I.TTF (56132 bytes)
      LICENSE.txt (565 bytes)
    fonts/07-script-cursive-handwritten/dacomment/
      Dacomment.otf (34280 bytes)
      Dacomment.ttf (49816 bytes)
      More Info.txt (391 bytes)
      Read Me.pdf (536273 bytes)
    fonts/07-script-cursive-handwritten/dearjoe4/
      LICENSE.txt (568 bytes)
      dearJoe four.ttf (105868 bytes)
    fonts/07-script-cursive-handwritten/diskus/
      D012004D.TTF (55388 bytes)
      D012J04D.TTF (55076 bytes)
      LICENSE.txt (563 bytes)
    fonts/07-script-cursive-handwritten/flamenco/
      Flamenco-Light.ttf (34736 bytes)
      Flamenco-Regular.ttf (36700 bytes)
      OFL.txt (4408 bytes)
    fonts/07-script-cursive-handwritten/gargouillette/
      Gargouillette.ttf (34452 bytes)
      Terms.txt (484 bytes)
    fonts/07-script-cursive-handwritten/italianno/
      Italianno-Regular.ttf (137364 bytes)
      OFL.txt (4486 bytes)
    fonts/07-script-cursive-handwritten/kabarett/
      K018000D.TTF (67824 bytes)
      LICENSE.txt (567 bytes)
    fonts/07-script-cursive-handwritten/kunstlerschreib/
      K004004D.TTF (69600 bytes)
      K004006D.TTF (69400 bytes)
      K004J04D.TTF (65544 bytes)
      K004J06D.TTF (67936 bytes)
      LICENSE.txt (588 bytes)
    fonts/07-script-cursive-handwritten/meditation/
      Meditation.ttf (112488 bytes)
      Meditation_info.txt (490 bytes)
    fonts/07-script-cursive-handwritten/mistral/
      LICENSE.txt (565 bytes)
      M016000D.TTF (180164 bytes)
      M016J00D.TTF (176104 bytes)
      M016J00T.TTF (106040 bytes)
    fonts/07-script-cursive-handwritten/park-avenue/
      LICENSE.txt (573 bytes)
      P004000D.TTF (62292 bytes)
    fonts/07-script-cursive-handwritten/passions-conflict/
      LICENSE.txt (584 bytes)
      PassionsConflictROB.ttf (60716 bytes)
    fonts/07-script-cursive-handwritten/walking-straight/
      LICENSE.txt (583 bytes)
      walking Straight serif.otf (23164 bytes)
      walking Straight serif.ttf (49624 bytes)
      walking Straight signature.otf (79936 bytes)
      walking Straight signature.ttf (79936 bytes)
  fonts/08-body-ui-workhorses/
    MANIFEST.md (3767 bytes)
    fonts/08-body-ui-workhorses/absans/
      Absans-Regular.otf (106704 bytes)
      Absans-Regular.woff2 (56656 bytes)
      LICENSE.txt (4392 bytes)
      copyright.glif (2369 bytes)
      copyright.glyph (1028 bytes)
    fonts/08-body-ui-workhorses/alkia/
      Alkia.ttf (48908 bytes)
      LICENSE.txt (505 bytes)
    fonts/08-body-ui-workhorses/alvilde/
      Alvilde-YzYpq.otf (32488 bytes)
      LICENSE.txt (507 bytes)
    fonts/08-body-ui-workhorses/astonpoliz/
      Astonpoliz.otf (43380 bytes)
      Astonpoliz.ttf (41836 bytes)
      LICENSE.txt (472 bytes)
    fonts/08-body-ui-workhorses/dimica/
      Dimica-Light.otf (61668 bytes)
      OFL.txt (4572 bytes)
    fonts/08-body-ui-workhorses/el-messiri/
      ElMessiriBold-vm3ZO.otf (77600 bytes)
      ElmessiriMedium-K7BOp.otf (80756 bytes)
      ElmessiriRegular-MVYOr.otf (77788 bytes)
      ElmessiriSemibold-2O74K.otf (80896 bytes)
      LICENSE.txt (95 bytes)
    fonts/08-body-ui-workhorses/garamontio_sans/
      OFL.txt (4393 bytes)
      README.md (996 bytes)
      garamontio_sans.ttf (867744 bytes)
      garamontio_sans.woff2 (365308 bytes)
      garamontio_sans_it.ttf (744756 bytes)
      garamontio_sans_it.woff2 (334448 bytes)
    fonts/08-body-ui-workhorses/gemunu-libre/
      GemunuLibre[wght].ttf (256496 bytes)
      OFL.txt (4399 bytes)
      README.md (4908 bytes)
    fonts/08-body-ui-workhorses/gmarket_sans/
      GmarketSansBold.otf (889716 bytes)
      GmarketSansLight.otf (842968 bytes)
      GmarketSansMedium.otf (868048 bytes)
      License.txt (4602 bytes)
    fonts/08-body-ui-workhorses/infinity/
      1001fonts-infinity-eula.txt (1915 bytes)
      Infinity.ttf (20224 bytes)
    fonts/08-body-ui-workhorses/january/
      January-Regular.otf (63664 bytes)
      January-Regular.ttf (62184 bytes)
      LICENSE.txt (4447 bytes)
      README.md (1000 bytes)
    fonts/08-body-ui-workhorses/marie/
      LICENSE.txt (505 bytes)
      Marie-rv2rp.otf (21900 bytes)
    fonts/08-body-ui-workhorses/otfits-grotesk/
      1001fonts-otfits-grotesk-eula.txt (2435 bytes)
      Otfits Grotesk Reg Trial.otf (30188 bytes)
    fonts/08-body-ui-workhorses/otflag-sans/
      1001fonts-otflag-sans-eula.txt (2402 bytes)
      OtflagSans-Medium.otf (50208 bytes)
    fonts/08-body-ui-workhorses/portland-ldo/
      LICENSE.txt (77 bytes)
      PortlandLdo-L394.ttf (158172 bytes)
      PortlandLdoBold-X3aK.ttf (141580 bytes)
      PortlandLdoBoldItalic-gxM6.ttf (132544 bytes)
      PortlandLdoItalic-owPz.ttf (144632 bytes)
      PortlandLdoSinistral-4BvD.ttf (142512 bytes)
      PortlandLdoSinistralBold-0WrX.ttf (130532 bytes)
    fonts/08-body-ui-workhorses/public-sans/
      OFL.txt (4390 bytes)
      PublicSans-Italic-VF.ttf (107940 bytes)
      PublicSans-VF.ttf (103316 bytes)
    fonts/08-body-ui-workhorses/publicalgnominia/
      OFL.txt (4391 bytes)
      PublicaIgnominia-BlackItalic.otf (85948 bytes)
      PublicaIgnominia-BlackItalic.ttf (85948 bytes)
      PublicaIgnominia-BlackItalic.woff2 (33120 bytes)
      PublicaIgnominia-BlackRoman.otf (85500 bytes)
      PublicaIgnominia-BlackRoman.ttf (85500 bytes)
      PublicaIgnominia-BlackRoman.woff2 (31772 bytes)
      PublicaIgnominia-BoldItalic.otf (88304 bytes)
      PublicaIgnominia-BoldItalic.ttf (88304 bytes)
      PublicaIgnominia-BoldItalic.woff2 (34752 bytes)
      PublicaIgnominia-BoldRoman.otf (88612 bytes)
      PublicaIgnominia-BoldRoman.ttf (88612 bytes)
      PublicaIgnominia-BoldRoman.woff2 (33784 bytes)
      PublicaIgnominia-ExtraBoldItalic.otf (88348 bytes)
      PublicaIgnominia-ExtraBoldItalic.ttf (88348 bytes)
      PublicaIgnominia-ExtraBoldItalic.woff2 (34704 bytes)
      PublicaIgnominia-ExtraBoldRoman.otf (87996 bytes)
      PublicaIgnominia-ExtraBoldRoman.ttf (87996 bytes)
      PublicaIgnominia-ExtraBoldRoman.woff2 (33516 bytes)
      PublicaIgnominia-ExtraLightItalic.otf (99928 bytes)
      PublicaIgnominia-ExtraLightItalic.ttf (99928 bytes)
      PublicaIgnominia-ExtraLightItalic.woff2 (37212 bytes)
      PublicaIgnominia-ExtraLightRoman.otf (110844 bytes)
      PublicaIgnominia-ExtraLightRoman.ttf (110844 bytes)
      PublicaIgnominia-ExtraLightRoman.woff2 (38792 bytes)
      PublicaIgnominia-LightItalic.otf (98864 bytes)
      PublicaIgnominia-LightItalic.ttf (98864 bytes)
      PublicaIgnominia-LightItalic.woff2 (36820 bytes)
      PublicaIgnominia-LightRoman.otf (107604 bytes)
      PublicaIgnominia-LightRoman.ttf (107604 bytes)
      PublicaIgnominia-LightRoman.woff2 (38168 bytes)
      PublicaIgnominia-MediumItalic.otf (91084 bytes)
      PublicaIgnominia-MediumItalic.ttf (91084 bytes)
      PublicaIgnominia-MediumItalic.woff2 (35512 bytes)
      PublicaIgnominia-MediumRoman.otf (91984 bytes)
      PublicaIgnominia-MediumRoman.ttf (91984 bytes)
      PublicaIgnominia-MediumRoman.woff2 (34844 bytes)
      PublicaIgnominia-RegularItalic.otf (95448 bytes)
      PublicaIgnominia-RegularItalic.ttf (95448 bytes)
      PublicaIgnominia-RegularItalic.woff2 (36444 bytes)
      PublicaIgnominia-RegularRoman.otf (99000 bytes)
      PublicaIgnominia-RegularRoman.ttf (99000 bytes)
      PublicaIgnominia-RegularRoman.woff2 (36504 bytes)
      PublicaIgnominia-SemiBoldItalic.otf (88880 bytes)
      PublicaIgnominia-SemiBoldItalic.ttf (88880 bytes)
      PublicaIgnominia-SemiBoldItalic.woff2 (34744 bytes)
      PublicaIgnominia-SemiBoldRoman.otf (90000 bytes)
      PublicaIgnominia-SemiBoldRoman.ttf (90000 bytes)
      PublicaIgnominia-SemiBoldRoman.woff2 (34308 bytes)
      PublicaIgnominia-ThinItalic.otf (99596 bytes)
      PublicaIgnominia-ThinItalic.ttf (99596 bytes)
      PublicaIgnominia-ThinItalic.woff2 (36448 bytes)
      PublicaIgnominia-ThinRoman.otf (111552 bytes)
      PublicaIgnominia-ThinRoman.ttf (111552 bytes)
      PublicaIgnominia-ThinRoman.woff2 (38032 bytes)
      PublicaIgnominia.ttf (177076 bytes)
      PublicaIgnominia.woff2 (83296 bytes)
      README.md (1482 bytes)
    fonts/08-body-ui-workhorses/rijusans/
      License.txt (4481 bytes)
      Rijusans-Italic.otf (121032 bytes)
      Rijusans-Italic.ttf (121032 bytes)
      Rijusans-Regular.otf (101212 bytes)
      Rijusans-Regular.ttf (101212 bytes)
    fonts/08-body-ui-workhorses/ronaldson-gothic/
      OFL-FAQ.txt (30473 bytes)
      Open Font License.txt (4544 bytes)
      RonaldsonGothic.ttf (149616 bytes)
      RonaldsonGothicLicht.ttf (251216 bytes)
    fonts/08-body-ui-workhorses/sollarish/
      LICENSE.txt (509 bytes)
      Sollarish-Regular.ttf (43148 bytes)
    fonts/08-body-ui-workhorses/wonder_unit/
      OFL.txt (4359 bytes)
      WonderUnitSans-Black.ttf (55072 bytes)
      WonderUnitSans-Black.woff2 (22772 bytes)
      WonderUnitSans-BlackItalic.ttf (56684 bytes)
      WonderUnitSans-BlackItalic.woff2 (24100 bytes)
      WonderUnitSans-Bold.ttf (55376 bytes)
      WonderUnitSans-Bold.woff2 (23596 bytes)
      WonderUnitSans-BoldItalic.ttf (56648 bytes)
      WonderUnitSans-BoldItalic.woff2 (24576 bytes)
      WonderUnitSans-Extrabold.ttf (55388 bytes)
      WonderUnitSans-Extrabold.woff2 (23528 bytes)
      WonderUnitSans-ExtraboldItalic.ttf (56820 bytes)
      WonderUnitSans-ExtraboldItalic.woff2 (24616 bytes)
      WonderUnitSans-Light.ttf (53528 bytes)
      WonderUnitSans-Light.woff2 (22816 bytes)
      WonderUnitSans-LightItalic.ttf (54880 bytes)
      WonderUnitSans-LightItalic.woff2 (23908 bytes)
      WonderUnitSans-Medium.ttf (54908 bytes)
      WonderUnitSans-Medium.woff2 (23260 bytes)
      WonderUnitSans-MediumItalic.ttf (56424 bytes)
      WonderUnitSans-MediumItalic.woff2 (24552 bytes)
      WonderUnitSans-Regular.ttf (53700 bytes)
      WonderUnitSans-Regular.woff2 (22932 bytes)
      WonderUnitSans-RegularItalic.ttf (55004 bytes)
      WonderUnitSans-RegularItalic.woff2 (24072 bytes)
      WonderUnitSans-Semibold.ttf (54972 bytes)
      WonderUnitSans-Semibold.woff2 (23252 bytes)
      WonderUnitSans-SemiboldItalic.ttf (56232 bytes)
      WonderUnitSans-SemiboldItalic.woff2 (24312 bytes)
      WonderUnitSans-Thin.ttf (53120 bytes)
      WonderUnitSans-Thin.woff2 (22116 bytes)
      WonderUnitSans-ThinItalic.ttf (54396 bytes)
      WonderUnitSans-ThinItalic.woff2 (23160 bytes)
governance/
  design-quality-gate.md (2112 bytes)
integration/
  integration-plan.md (4047 bytes)
  migration-manifest.md (7316 bytes)
  trigger-block.md (1137 bytes)
skills/
  skills/00-cross-cutting-ops-qa-a11y/
    README.md (440 bytes)
    skills/00-cross-cutting-ops-qa-a11y/accessibility-wcag-2-2-compliance/
      SKILL.md (12374 bytes)
      skills/00-cross-cutting-ops-qa-a11y/accessibility-wcag-2-2-compliance/examples/
        wcag-2.2-audit-sheet.md (5569 bytes)
      skills/00-cross-cutting-ops-qa-a11y/accessibility-wcag-2-2-compliance/references/
        aria-patterns.md (6871 bytes)
        keyboard-and-focus.md (6164 bytes)
    skills/00-cross-cutting-ops-qa-a11y/design-audit/
      SKILL.md (20140 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-audit/examples/
        design-audit-filled.md (10331 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-audit/references/
        audit-rubric.md (5859 bytes)
        consistency-audit.md (1199 bytes)
        routing.md (185 bytes)
        triage-and-prioritization.md (5332 bytes)
        skills/00-cross-cutting-ops-qa-a11y/design-audit/references/lean-ux-validation/
          entrypoint.md (13967 bytes)
    skills/00-cross-cutting-ops-qa-a11y/design-critique-and-review-facilitation/
      SKILL.md (15451 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-critique-and-review-facilitation/examples/
        critique-session-worked.md (8549 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-critique-and-review-facilitation/references/
        critique-protocol.md (12276 bytes)
    skills/00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/
      SKILL.md (14640 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/examples/
        ethics-audit-filled.md (2602 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-ethics-and-anti-dark-patterns/references/
        dark-pattern-catalog.md (15400 bytes)
    skills/00-cross-cutting-ops-qa-a11y/design-qa-and-pre-launch-review/
      SKILL.md (13183 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-qa-and-pre-launch-review/examples/
        qa-review-filled.md (9167 bytes)
      skills/00-cross-cutting-ops-qa-a11y/design-qa-and-pre-launch-review/references/
        pre-launch-qa-checklist.md (7795 bytes)
    skills/00-cross-cutting-ops-qa-a11y/inclusive-and-assistive-design/
      SKILL.md (14505 bytes)
      skills/00-cross-cutting-ops-qa-a11y/inclusive-and-assistive-design/examples/
        inclusive-design-pass.md (2962 bytes)
      skills/00-cross-cutting-ops-qa-a11y/inclusive-and-assistive-design/references/
        inclusive-patterns.md (10370 bytes)
    skills/00-cross-cutting-ops-qa-a11y/internationalization-and-rtl-design/
      SKILL.md (12759 bytes)
      skills/00-cross-cutting-ops-qa-a11y/internationalization-and-rtl-design/examples/
        rtl-before-after.md (7064 bytes)
      skills/00-cross-cutting-ops-qa-a11y/internationalization-and-rtl-design/references/
        rtl-mirroring-rules.md (7830 bytes)
        string-expansion-budgets.md (7070 bytes)
    skills/00-cross-cutting-ops-qa-a11y/performance-as-ux-and-core-web-vitals/
      SKILL.md (9979 bytes)
      skills/00-cross-cutting-ops-qa-a11y/performance-as-ux-and-core-web-vitals/examples/
        performance-budget-sheet.md (6685 bytes)
      skills/00-cross-cutting-ops-qa-a11y/performance-as-ux-and-core-web-vitals/references/
        perceived-performance-patterns.md (9093 bytes)
    skills/00-cross-cutting-ops-qa-a11y/product-design-audit/
      SKILL.md (15985 bytes)
      skills/00-cross-cutting-ops-qa-a11y/product-design-audit/examples/
        product-audit-worked.md (13913 bytes)
      skills/00-cross-cutting-ops-qa-a11y/product-design-audit/references/
        audit-dimensions.md (7134 bytes)
        platform-lenses.md (11013 bytes)
        recommendation-format.md (8088 bytes)
    skills/00-cross-cutting-ops-qa-a11y/slop-doctrine-refresh-and-research-loop/
      SKILL.md (4476 bytes)
      skills/00-cross-cutting-ops-qa-a11y/slop-doctrine-refresh-and-research-loop/examples/
        font-default-refresh-note.md (766 bytes)
    skills/00-cross-cutting-ops-qa-a11y/ux-remediation-and-redesign/
      SKILL.md (14234 bytes)
      skills/00-cross-cutting-ops-qa-a11y/ux-remediation-and-redesign/examples/
        checkout-remediation-worked.md (9304 bytes)
      skills/00-cross-cutting-ops-qa-a11y/ux-remediation-and-redesign/references/
        remediation-lifecycle.md (7525 bytes)
        triage-matrix.md (7152 bytes)
    skills/00-cross-cutting-ops-qa-a11y/visual-product-slop-audit/
      SKILL.md (4850 bytes)
      skills/00-cross-cutting-ops-qa-a11y/visual-product-slop-audit/examples/
        slop-audit-filled.md (4871 bytes)
      skills/00-cross-cutting-ops-qa-a11y/visual-product-slop-audit/references/
        visual-tells-checklist.md (7773 bytes)
  skills/01-typography-and-fonts/
    skills/01-typography-and-fonts/ai-slop-typography-audit/
      SKILL.md (3081 bytes)
      skills/01-typography-and-fonts/ai-slop-typography-audit/examples/
        typography-audit-filled.md (9129 bytes)
    skills/01-typography-and-fonts/fluid-responsive-typography/
      SKILL.md (11704 bytes)
      skills/01-typography-and-fonts/fluid-responsive-typography/examples/
        fluid-type-scale.md (7928 bytes)
      skills/01-typography-and-fonts/fluid-responsive-typography/references/
        fluid-scale-math.md (7233 bytes)
    skills/01-typography-and-fonts/font-embedding-and-licensing/
      SKILL.md (2877 bytes)
      skills/01-typography-and-fonts/font-embedding-and-licensing/examples/
        embedding-worked-spec.md (11205 bytes)
    skills/01-typography-and-fonts/font-selection-and-pairing/
      SKILL.md (5404 bytes)
      skills/01-typography-and-fonts/font-selection-and-pairing/examples/
        applied-type-scale.md (6830 bytes)
      skills/01-typography-and-fonts/font-selection-and-pairing/references/
        pairing-catalog.md (7263 bytes)
        type-scale-recipes.md (7540 bytes)
    skills/01-typography-and-fonts/premium-font-scan/
      SKILL.md (3896 bytes)
      skills/01-typography-and-fonts/premium-font-scan/examples/
        premium-scan-worked.md (4824 bytes)
    skills/01-typography-and-fonts/variable-fonts-and-opentype-features/
      SKILL.md (7799 bytes)
      skills/01-typography-and-fonts/variable-fonts-and-opentype-features/examples/
        dashboard-type-system.md (6658 bytes)
      skills/01-typography-and-fonts/variable-fonts-and-opentype-features/references/
        opentype-features.md (6393 bytes)
        variable-axes.md (6190 bytes)
  skills/02-color-brand-and-visual-identity/
    skills/02-color-brand-and-visual-identity/accessible-color-and-contrast/
      SKILL.md (9159 bytes)
      skills/02-color-brand-and-visual-identity/accessible-color-and-contrast/examples/
        contrast-checked-palette.md (5529 bytes)
      skills/02-color-brand-and-visual-identity/accessible-color-and-contrast/references/
        apca-vs-wcag.md (4180 bytes)
        colorblind-safe-palettes.md (5049 bytes)
    skills/02-color-brand-and-visual-identity/brand-style-guide/
      SKILL.md (4650 bytes)
      skills/02-color-brand-and-visual-identity/brand-style-guide/examples/
        mini-style-guide-worked.md (5233 bytes)
      skills/02-color-brand-and-visual-identity/brand-style-guide/references/
        design-decisions.md (18151 bytes)
        legacy-guidance.md (18014 bytes)
        style-guide-template.md (18832 bytes)
    skills/02-color-brand-and-visual-identity/brand-visual-identity/
      SKILL.md (10486 bytes)
      skills/02-color-brand-and-visual-identity/brand-visual-identity/examples/
        identity-mini-guide.md (8590 bytes)
      skills/02-color-brand-and-visual-identity/brand-visual-identity/references/
        brand-consistency-gate.md (3175 bytes)
        identity-system-spec.md (5849 bytes)
        trust-architecture-checklist.md (3026 bytes)
    skills/02-color-brand-and-visual-identity/color-selection/
      SKILL.md (6936 bytes)
      skills/02-color-brand-and-visual-identity/color-selection/examples/
        palette-generation-worked.md (5073 bytes)
      skills/02-color-brand-and-visual-identity/color-selection/references/
        accessibility-contrast.md (10540 bytes)
        color-psychology.md (10469 bytes)
        color-schemes.md (10757 bytes)
        color-theory-fundamentals.md (7625 bytes)
        flux-process.md (17162 bytes)
        industry-color-psychology.md (13312 bytes)
        legacy-guidance.md (10056 bytes)
        practical-application.md (12106 bytes)
        tools-resources.md (10644 bytes)
      skills/02-color-brand-and-visual-identity/color-selection/scripts/
        palette_generator.py (7099 bytes)
    skills/02-color-brand-and-visual-identity/color-system-and-palette/
      SKILL.md (9777 bytes)
      skills/02-color-brand-and-visual-identity/color-system-and-palette/examples/
        oklch-palette-worked.md (5242 bytes)
      skills/02-color-brand-and-visual-identity/color-system-and-palette/references/
        oklch-ramp-construction.md (3946 bytes)
        semantic-color-roles.md (3378 bytes)
    skills/02-color-brand-and-visual-identity/dark-mode-and-theming/
      SKILL.md (11286 bytes)
      skills/02-color-brand-and-visual-identity/dark-mode-and-theming/examples/
        light-dark-token-pair.md (7983 bytes)
      skills/02-color-brand-and-visual-identity/dark-mode-and-theming/references/
        dark-mode-semantic-roles.md (6057 bytes)
    skills/02-color-brand-and-visual-identity/logo-and-wordmark-design/
      SKILL.md (14434 bytes)
      skills/02-color-brand-and-visual-identity/logo-and-wordmark-design/examples/
        aperture-mark-and-lockup-spec.md (8493 bytes)
      skills/02-color-brand-and-visual-identity/logo-and-wordmark-design/references/
        app-icon-and-favicon-system.md (5588 bytes)
        mark-construction.md (8616 bytes)
  skills/03-layout-grid-and-composition/
    skills/03-layout-grid-and-composition/composition-and-visual-hierarchy/
      SKILL.md (13707 bytes)
      skills/03-layout-grid-and-composition/composition-and-visual-hierarchy/examples/
        before-after-composition.md (7884 bytes)
      skills/03-layout-grid-and-composition/composition-and-visual-hierarchy/references/
        composition-and-flow.md (5767 bytes)
        hierarchy-techniques.md (5902 bytes)
    skills/03-layout-grid-and-composition/editorial-and-long-form-layout/
      SKILL.md (16703 bytes)
      skills/03-layout-grid-and-composition/editorial-and-long-form-layout/examples/
        long-form-article-layout-spec.md (8476 bytes)
      skills/03-layout-grid-and-composition/editorial-and-long-form-layout/references/
        editorial-layout-patterns.md (11270 bytes)
    skills/03-layout-grid-and-composition/layout-grid-and-spacing/
      SKILL.md (11474 bytes)
      skills/03-layout-grid-and-composition/layout-grid-and-spacing/examples/
        grid-template-worked.md (6353 bytes)
      skills/03-layout-grid-and-composition/layout-grid-and-spacing/references/
        grid-systems-catalog.md (6079 bytes)
        spacing-rhythm.md (5041 bytes)
    skills/03-layout-grid-and-composition/responsive-and-adaptive-layout/
      SKILL.md (15066 bytes)
      skills/03-layout-grid-and-composition/responsive-and-adaptive-layout/examples/
        responsive-grid-template.md (8557 bytes)
      skills/03-layout-grid-and-composition/responsive-and-adaptive-layout/references/
        breakpoint-strategy.md (6230 bytes)
        container-queries-and-intrinsic.md (8454 bytes)
  skills/04-web-and-ui-design/
    skills/04-web-and-ui-design/ai-agent-ux/
      SKILL.md (3678 bytes)
      skills/04-web-and-ui-design/ai-agent-ux/examples/
        agent-ux-spec-worked.md (14710 bytes)
      skills/04-web-and-ui-design/ai-agent-ux/references/
        generative-ai-ui-ux.md (3074 bytes)
        routing.md (980 bytes)
        skills/04-web-and-ui-design/ai-agent-ux/references/ai-agent-mobile-and-web-ux-patterns/
          entrypoint.md (11857 bytes)
          skills/04-web-and-ui-design/ai-agent-ux/references/ai-agent-mobile-and-web-ux-patterns/references/
            agent-inbox-spec.md (6390 bytes)
        skills/04-web-and-ui-design/ai-agent-ux/references/ai-agentic-ui/
          entrypoint.md (8244 bytes)
          skills/04-web-and-ui-design/ai-agent-ux/references/ai-agentic-ui/references/
            agentic-patterns.md (3457 bytes)
            checkpoint-primitives.md (4169 bytes)
            permission-framework.md (3320 bytes)
            progress-tiers.md (3145 bytes)
        skills/04-web-and-ui-design/ai-agent-ux/references/ai-ux-patterns/
          entrypoint.md (11712 bytes)
          skills/04-web-and-ui-design/ai-agent-ux/references/ai-ux-patterns/references/
            three-channels-and-discovery.md (5272 bytes)
    skills/04-web-and-ui-design/ai-output-design/
      SKILL.md (9019 bytes)
      skills/04-web-and-ui-design/ai-output-design/examples/
        ai-output-surface-worked.md (9025 bytes)
      skills/04-web-and-ui-design/ai-output-design/references/
        canvas-vs-chat.md (3035 bytes)
        five-output-principles.md (3016 bytes)
        inline-refinement.md (3167 bytes)
        routing.md (393 bytes)
        verifiability-patterns.md (3731 bytes)
        skills/04-web-and-ui-design/ai-output-design/references/ai-slop-prevention/
          entrypoint.md (13694 bytes)
    skills/04-web-and-ui-design/component-states-and-interaction-fidelity/
      SKILL.md (12057 bytes)
      skills/04-web-and-ui-design/component-states-and-interaction-fidelity/examples/
        input-state-matrix.md (10027 bytes)
      skills/04-web-and-ui-design/component-states-and-interaction-fidelity/references/
        component-anatomy.md (6326 bytes)
        state-matrix-method.md (8981 bytes)
    skills/04-web-and-ui-design/distinctive-by-design/
      SKILL.md (11730 bytes)
      skills/04-web-and-ui-design/distinctive-by-design/examples/
        before-after-distinctive.md (8441 bytes)
    skills/04-web-and-ui-design/form-ux-design/
      SKILL.md (9679 bytes)
      skills/04-web-and-ui-design/form-ux-design/examples/
        form-spec-worked.md (13375 bytes)
      skills/04-web-and-ui-design/form-ux-design/references/
        android-form-components.md (19989 bytes)
        form-accessibility.md (17181 bytes)
        form-validation.md (17980 bytes)
        ios-form-components.md (13401 bytes)
        skill-deep-dive.md (19477 bytes)
        web-form-components.md (22262 bytes)
    skills/04-web-and-ui-design/interaction-design-patterns/
      SKILL.md (16969 bytes)
      skills/04-web-and-ui-design/interaction-design-patterns/examples/
        pattern-applied-worked.md (9444 bytes)
      skills/04-web-and-ui-design/interaction-design-patterns/sections/
        01-behavior.md (13760 bytes)
        02-navigation.md (9429 bytes)
        03-layout.md (10025 bytes)
        04-actions.md (10520 bytes)
        05-data.md (9213 bytes)
        06-saas-web-app-patterns.md (3501 bytes)
    skills/04-web-and-ui-design/practical-ui-design/
      SKILL.md (11105 bytes)
      skills/04-web-and-ui-design/practical-ui-design/examples/
        ui-before-after-worked.md (7108 bytes)
      skills/04-web-and-ui-design/practical-ui-design/references/
        skill-deep-dive.md (21347 bytes)
        visual-consistency.md (1046 bytes)
    skills/04-web-and-ui-design/premium-ui-ux-design/
      SKILL.md (6953 bytes)
      skills/04-web-and-ui-design/premium-ui-ux-design/examples/
        premium-direction-worked.md (7415 bytes)
      skills/04-web-and-ui-design/premium-ui-ux-design/references/
        color-emotion-brand-systems.md (3431 bytes)
        data-visualization-dashboard-ux.md (4080 bytes)
        mobile-android-ios-premium-ux.md (3684 bytes)
        mobile-dashboard-ux-patterns.md (3608 bytes)
        premium-ui-ux-gate.md (2666 bytes)
        premium-ui-ux-specification-rules.md (4461 bytes)
        premium-visual-principles.md (4412 bytes)
        production-quality-handoff.md (2743 bytes)
        routing.md (235 bytes)
        saas-ux-scope-costing.md (5642 bytes)
        source-register.md (2365 bytes)
        skills/04-web-and-ui-design/premium-ui-ux-design/references/color-theory/
          entrypoint.md (10933 bytes)
          skills/04-web-and-ui-design/premium-ui-ux-design/references/color-theory/references/
            flux-process.md (17162 bytes)
        skills/04-web-and-ui-design/premium-ui-ux-design/references/design-by-nature/
          entrypoint.md (12128 bytes)
          skills/04-web-and-ui-design/premium-ui-ux-design/references/design-by-nature/references/
            forms-and-shapes.md (17651 bytes)
    skills/04-web-and-ui-design/webapp-gui-design/
      SKILL.md (19942 bytes)
      skills/04-web-and-ui-design/webapp-gui-design/examples/
        app-shell-spec-worked.md (15955 bytes)
      skills/04-web-and-ui-design/webapp-gui-design/references/
        interface-consistency.md (995 bytes)
        routing.md (180 bytes)
        skills/04-web-and-ui-design/webapp-gui-design/references/no-json-in-ui/
          entrypoint.md (12439 bytes)
      skills/04-web-and-ui-design/webapp-gui-design/sections/
        01-overview.md (1969 bytes)
        02-security-print-dates.md (1342 bytes)
        03-architecture-panels-menus.md (6831 bytes)
        04-permissions-dropdowns.md (5949 bytes)
        05-templates-components.md (8808 bytes)
        06-ajax-utilities.md (2958 bytes)
        07-responsive-photo-flatpickr.md (1545 bytes)
        08-best-practices-aesthetics.md (10925 bytes)
        09-interface-design.md (19835 bytes)
        10-saas-ux-principles.md (18991 bytes)
  skills/05-ux-process-research-and-psychology/
    skills/05-ux-process-research-and-psychology/demo-driven-design-process/
      SKILL.md (12393 bytes)
      skills/05-ux-process-research-and-psychology/demo-driven-design-process/examples/
        save-search-toast-iteration-log.md (10978 bytes)
      skills/05-ux-process-research-and-psychology/demo-driven-design-process/references/
        decision-capture.md (6804 bytes)
        demo-loop-and-fidelity.md (7408 bytes)
    skills/05-ux-process-research-and-psychology/enterprise-ux-process/
      SKILL.md (8409 bytes)
      skills/05-ux-process-research-and-psychology/enterprise-ux-process/examples/
        ux-engagement-worked.md (8019 bytes)
      skills/05-ux-process-research-and-psychology/enterprise-ux-process/references/
        arrive-framework.md (17271 bytes)
        discovery-evidence-bundle.md (630 bytes)
        maturity-checklist.md (4804 bytes)
        natoli-enterprise-playbook.md (1158 bytes)
        routing.md (270 bytes)
        skills/05-ux-process-research-and-psychology/enterprise-ux-process/references/experience-mapping/
          entrypoint.md (7959 bytes)
          skills/05-ux-process-research-and-psychology/enterprise-ux-process/references/experience-mapping/references/
            discovery-interview-patterns.md (7743 bytes)
            experience-mapping-anti-patterns.md (8141 bytes)
            hypothesis-and-validation-thresholds.md (8697 bytes)
            impact-map-construction.md (7891 bytes)
            journey-map-to-requirements.md (7313 bytes)
        skills/05-ux-process-research-and-psychology/enterprise-ux-process/references/service-design-blueprinting/
          entrypoint.md (8259 bytes)
          skills/05-ux-process-research-and-psychology/enterprise-ux-process/references/service-design-blueprinting/references/
            blueprint-anti-patterns.md (8367 bytes)
            blueprint-construction-and-swimlanes.md (8702 bytes)
            cx-ex-alignment.md (7484 bytes)
            frontstage-backstage-alignment.md (7918 bytes)
            service-failure-and-recovery.md (8683 bytes)
    skills/05-ux-process-research-and-psychology/heuristic-evaluation-and-design-critique/
      SKILL.md (13447 bytes)
      skills/05-ux-process-research-and-psychology/heuristic-evaluation-and-design-critique/examples/
        heuristic-evaluation-worked.md (10419 bytes)
      skills/05-ux-process-research-and-psychology/heuristic-evaluation-and-design-critique/references/
        heuristics-catalog.md (12735 bytes)
        severity-scoring.md (6038 bytes)
    skills/05-ux-process-research-and-psychology/journey-mapping-and-service-design/
      SKILL.md (11345 bytes)
      skills/05-ux-process-research-and-psychology/journey-mapping-and-service-design/examples/
        journey-map-and-opportunities.md (7875 bytes)
      skills/05-ux-process-research-and-psychology/journey-mapping-and-service-design/references/
        journey-map-templates.md (6961 bytes)
        service-blueprint.md (5150 bytes)
    skills/05-ux-process-research-and-psychology/ux-psychology/
      SKILL.md (5379 bytes)
      skills/05-ux-process-research-and-psychology/ux-psychology/examples/
        psychology-critique-worked.md (9583 bytes)
      skills/05-ux-process-research-and-psychology/ux-psychology/references/
        legacy-guidance.md (37030 bytes)
        three-levels-of-ux-scope.md (2134 bytes)
        three-paradigms-of-hci.md (3202 bytes)
    skills/05-ux-process-research-and-psychology/ux-research-and-usability-testing/
      SKILL.md (8758 bytes)
      skills/05-ux-process-research-and-psychology/ux-research-and-usability-testing/examples/
        research-plan-and-synthesis.md (7263 bytes)
      skills/05-ux-process-research-and-psychology/ux-research-and-usability-testing/references/
        research-method-selector.md (5386 bytes)
        usability-test-protocol.md (6954 bytes)
    skills/05-ux-process-research-and-psychology/wireframing-and-prototyping/
      SKILL.md (8752 bytes)
      skills/05-ux-process-research-and-psychology/wireframing-and-prototyping/examples/
        wireflow-example.md (6989 bytes)
      skills/05-ux-process-research-and-psychology/wireframing-and-prototyping/references/
        fidelity-ladder.md (7011 bytes)
  skills/06-sector-and-domain-ux/
    skills/06-sector-and-domain-ux/ecommerce-and-checkout-ux/
      SKILL.md (19050 bytes)
      skills/06-sector-and-domain-ux/ecommerce-and-checkout-ux/examples/
        checkout-flow-spec-worked.md (11083 bytes)
      skills/06-sector-and-domain-ux/ecommerce-and-checkout-ux/references/
        checkout-flow-patterns.md (13873 bytes)
    skills/06-sector-and-domain-ux/fintech-and-financial-product-ui/
      SKILL.md (8699 bytes)
      skills/06-sector-and-domain-ux/fintech-and-financial-product-ui/examples/
        send-money-screen-spec.md (8604 bytes)
      skills/06-sector-and-domain-ux/fintech-and-financial-product-ui/references/
        money-ux-patterns.md (11934 bytes)
    skills/06-sector-and-domain-ux/healthcare-ui-design/
      SKILL.md (19500 bytes)
      skills/06-sector-and-domain-ux/healthcare-ui-design/examples/
        clinical-screen-worked.md (10984 bytes)
      skills/06-sector-and-domain-ux/healthcare-ui-design/references/
        android-implementation.md (19958 bytes)
        clinical-workflows-ui.md (23129 bytes)
        color-typography.md (9306 bytes)
        communication-outreach-ui.md (23518 bytes)
        compliance-accessibility.md (18030 bytes)
        components.md (12541 bytes)
        dashboards-analytics-ui.md (21853 bytes)
        design-tokens.md (18810 bytes)
        desktop-patterns.md (11222 bytes)
        mobile-patterns.md (6055 bytes)
        patient-portal-ui.md (20039 bytes)
        patient-records-ui.md (23104 bytes)
        scheduling-telemedicine-ui.md (23721 bytes)
        tablet-patterns.md (7928 bytes)
        web-implementation.md (20545 bytes)
    skills/06-sector-and-domain-ux/legal-sector-ui-ux/
      SKILL.md (4969 bytes)
      skills/06-sector-and-domain-ux/legal-sector-ui-ux/examples/
        law-firm-screen-worked.md (9238 bytes)
      skills/06-sector-and-domain-ux/legal-sector-ui-ux/references/
        content-templates.md (9256 bytes)
        ethics-constraints.md (11806 bytes)
        legacy-guidance.md (19713 bytes)
        local-seo.md (12933 bytes)
    skills/06-sector-and-domain-ux/sector-strategies/
      ANTI-HOMOGENEITY-PRINCIPLE.md (7434 bytes)
      DARK-MODE-IMPLEMENTATION.md (9869 bytes)
      SKILL.md (4418 bytes)
      skills/06-sector-and-domain-ux/sector-strategies/examples/
        sector-strategy-worked.md (6709 bytes)
      skills/06-sector-and-domain-ux/sector-strategies/references/
        legacy-guidance.md (26237 bytes)
      skills/06-sector-and-domain-ux/sector-strategies/templates/
        README.md (4040 bytes)
        branding-colors-template.md (7176 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/app-landing-pages/
          README.md (1214 bytes)
          app-branding.md (6298 bytes)
          app-conversion.md (8396 bytes)
          app-type-patterns.md (5481 bytes)
          conversion-strategies.md (23787 bytes)
          design-tokens.md (12679 bytes)
          implementation-guide.md (18181 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/corporate/
          IMPLEMENTATION-GUIDE.md (20552 bytes)
          README.md (1158 bytes)
          client-conversion.md (5435 bytes)
          corporate-branding.md (4617 bytes)
          corporate-type-patterns.md (5666 bytes)
          design-tokens.md (10665 bytes)
          sector-brief-template.md (8101 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/ecommerce/
          README.md (1171 bytes)
          component-patterns.md (1866 bytes)
          design-tokens.md (1337 bytes)
          ecommerce-branding.md (4322 bytes)
          sector-brief-template.md (1367 bytes)
          shopping-conversion.md (5029 bytes)
          store-type-patterns.md (4315 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/education/
          IMPLEMENTATION-GUIDE.md (36215 bytes)
          README.md (2353 bytes)
          component-patterns-full.md (22566 bytes)
          component-patterns.md (2222 bytes)
          design-tokens.md (6900 bytes)
          enrollment-design.md (10169 bytes)
          school-branding.md (9012 bytes)
          school-type-patterns.md (12840 bytes)
          sector-brief-template.md (6271 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/healthcare/
          README.md (2952 bytes)
          component-patterns.md (1509 bytes)
          design-tokens.md (6303 bytes)
          healthcare-branding.md (8301 bytes)
          healthcare-type-patterns.md (6513 bytes)
          patient-trust-design.md (8677 bytes)
          premium-hospital-playbook.md (23503 bytes)
          sector-brief-template.md (1536 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/hobbyist-creator/
          README.md (1252 bytes)
          component-patterns.md (2703 bytes)
          creator-branding.md (6517 bytes)
          creator-type-patterns.md (5099 bytes)
          design-tokens.md (1441 bytes)
          engagement-design.md (7613 bytes)
          sector-brief-template.md (1527 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/legal/
          README.md (2612 bytes)
          client-trust-design.md (12419 bytes)
          design-tokens.md (5029 bytes)
          ethics-constraints.md (7711 bytes)
          legal-branding.md (9838 bytes)
          legal-type-patterns.md (12514 bytes)
          sector-brief-template.md (4830 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/nonprofit/
          COMPONENT-PATTERNS-INDEX.md (8685 bytes)
          README.md (8394 bytes)
          color-psychology.md (7108 bytes)
          design-tokens.md (8542 bytes)
          sector-brief-template.md (6112 bytes)
          storytelling-design.md (7069 bytes)
          sub-sector-patterns.md (6538 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/personal/
          IMPLEMENTATION-GUIDE.md (17821 bytes)
          README.md (1218 bytes)
          design-tokens.md (7517 bytes)
          portfolio-branding.md (4079 bytes)
          portfolio-conversion.md (4458 bytes)
          portfolio-type-patterns.md (4727 bytes)
          sector-brief-template.md (8934 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/professional-services/
          README.md (1266 bytes)
          client-acquisition.md (4425 bytes)
          component-patterns.md (1927 bytes)
          design-tokens.md (1369 bytes)
          sector-brief-template.md (1412 bytes)
          services-branding.md (2857 bytes)
          services-type-patterns.md (3958 bytes)
        skills/06-sector-and-domain-ux/sector-strategies/templates/tour-travel/
          IMPLEMENTATION-GUIDE.md (15879 bytes)
          README.md (2646 bytes)
          booking-conversion.md (12907 bytes)
          component-patterns.md (8669 bytes)
          design-tokens.md (10359 bytes)
          sector-brief-template.md (4428 bytes)
          travel-branding.md (9999 bytes)
          travel-type-patterns.md (14840 bytes)
  skills/07-mobile-ios-android-cross-platform/
    skills/07-mobile-ios-android-cross-platform/android-ui-ux-design/
      SKILL.md (6015 bytes)
      skills/07-mobile-ios-android-cross-platform/android-ui-ux-design/examples/
        android-screen-spec.md (7545 bytes)
      skills/07-mobile-ios-android-cross-platform/android-ui-ux-design/references/
        android-motion.md (5728 bytes)
        jetpack-compose-ui.md (8232 bytes)
        material-3-expressive.md (8414 bytes)
        skills/07-mobile-ios-android-cross-platform/android-ui-ux-design/references/jetpack-compose-ui/
          animation-and-polish.md (10212 bytes)
          composable-patterns.md (15673 bytes)
          data-tables.md (25635 bytes)
          design-philosophy.md (11121 bytes)
          layout-and-components.md (10369 bytes)
          navigation-and-performance.md (15897 bytes)
          responsive-adaptive.md (12392 bytes)
          skill-deep-dive.md (14971 bytes)
    skills/07-mobile-ios-android-cross-platform/app-store-presence-and-aso/
      SKILL.md (13074 bytes)
      skills/07-mobile-ios-android-cross-platform/app-store-presence-and-aso/examples/
        store-listing-asset-spec.md (9454 bytes)
      skills/07-mobile-ios-android-cross-platform/app-store-presence-and-aso/references/
        aso-asset-specs.md (9693 bytes)
    skills/07-mobile-ios-android-cross-platform/cross-platform-design-parity/
      SKILL.md (9988 bytes)
      skills/07-mobile-ios-android-cross-platform/cross-platform-design-parity/examples/
        parity-spec-one-screen.md (7108 bytes)
      skills/07-mobile-ios-android-cross-platform/cross-platform-design-parity/references/
        ios-vs-android-idioms.md (6420 bytes)
        react-native-implementation-readiness.md (4319 bytes)
        rn-flutter-mapping.md (5171 bytes)
    skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/
      SKILL.md (6623 bytes)
      skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/examples/
        ios-screen-spec.md (7049 bytes)
      skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/
        hig-liquid-glass.md (8399 bytes)
        ios-sensory-and-haptics.md (5960 bytes)
        ios-uikit-advanced.md (6173 bytes)
        swiftui-design.md (5487 bytes)
        swiftui-pro-patterns.md (5397 bytes)
        skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/ios-uikit-advanced/
          advanced-interactions.md (7934 bytes)
          skill-deep-dive.md (18079 bytes)
        skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/swiftui-design/
          skill-deep-dive.md (13264 bytes)
        skills/07-mobile-ios-android-cross-platform/ios-ui-ux-design/references/swiftui-pro-patterns/
          skill-deep-dive.md (12271 bytes)
    skills/07-mobile-ios-android-cross-platform/touch-gesture-and-haptics/
      SKILL.md (8909 bytes)
      skills/07-mobile-ios-android-cross-platform/touch-gesture-and-haptics/examples/
        gesture-haptics-map-transactions-list.md (8323 bytes)
      skills/07-mobile-ios-android-cross-platform/touch-gesture-and-haptics/references/
        gesture-and-haptics.md (13907 bytes)
  skills/08-motion-and-interaction/
    skills/08-motion-and-interaction/micro-interactions-and-feedback/
      SKILL.md (7196 bytes)
      skills/08-motion-and-interaction/micro-interactions-and-feedback/examples/
        toggle-switch-feedback-spec.md (7418 bytes)
      skills/08-motion-and-interaction/micro-interactions-and-feedback/references/
        micro-interaction-anatomy.md (9285 bytes)
    skills/08-motion-and-interaction/motion-design/
      SKILL.md (17054 bytes)
      skills/08-motion-and-interaction/motion-design/examples/
        micro-interaction-spec.md (5302 bytes)
      skills/08-motion-and-interaction/motion-design/references/
        reduced-motion.md (4394 bytes)
        spring-physics-and-easing.md (4284 bytes)
        view-transitions.md (3882 bytes)
  skills/09-design-systems-tokens-and-theming/
    README.md (361 bytes)
    skills/09-design-systems-tokens-and-theming/component-library-architecture/
      SKILL.md (10632 bytes)
      skills/09-design-systems-tokens-and-theming/component-library-architecture/examples/
        button-component-spec.md (11280 bytes)
      skills/09-design-systems-tokens-and-theming/component-library-architecture/references/
        atomic-structure.md (6469 bytes)
        component-doc-template.md (4480 bytes)
    skills/09-design-systems-tokens-and-theming/design-handoff-and-dev-spec/
      SKILL.md (13734 bytes)
      skills/09-design-systems-tokens-and-theming/design-handoff-and-dev-spec/examples/
        component-handoff-sheet.md (9205 bytes)
      skills/09-design-systems-tokens-and-theming/design-handoff-and-dev-spec/references/
        handoff-checklist.md (5472 bytes)
        redline-and-spec-format.md (5284 bytes)
    skills/09-design-systems-tokens-and-theming/design-tokens-and-naming/
      SKILL.md (11823 bytes)
      skills/09-design-systems-tokens-and-theming/design-tokens-and-naming/examples/
        semantic-mapping.md (3748 bytes)
        tokens.json (11501 bytes)
      skills/09-design-systems-tokens-and-theming/design-tokens-and-naming/references/
        token-export-formats.md (5751 bytes)
        token-tiers-and-naming.md (6804 bytes)
    skills/09-design-systems-tokens-and-theming/figma-and-tooling-workflow/
      SKILL.md (16069 bytes)
      skills/09-design-systems-tokens-and-theming/figma-and-tooling-workflow/examples/
        sample-design-system-figma-setup.md (8179 bytes)
      skills/09-design-systems-tokens-and-theming/figma-and-tooling-workflow/references/
        figma-conventions.md (11758 bytes)
  skills/10-content-design-and-ux-writing/
    README.md (292 bytes)
    skills/10-content-design-and-ux-writing/error-empty-and-system-messaging/
      SKILL.md (17695 bytes)
      skills/10-content-design-and-ux-writing/error-empty-and-system-messaging/examples/
        error-copy-library.md (12523 bytes)
      skills/10-content-design-and-ux-writing/error-empty-and-system-messaging/references/
        error-message-formula.md (12933 bytes)
        error-placement-taxonomy.md (4562 bytes)
    skills/10-content-design-and-ux-writing/ux-writing-and-microcopy/
      SKILL.md (13169 bytes)
      skills/10-content-design-and-ux-writing/ux-writing-and-microcopy/examples/
        before-after-microcopy.md (6312 bytes)
      skills/10-content-design-and-ux-writing/ux-writing-and-microcopy/references/
        button-and-cta-copy.md (5578 bytes)
        microcopy-patterns.md (7131 bytes)
        text-patterns-and-editing-curve.md (7316 bytes)
    skills/10-content-design-and-ux-writing/voice-tone-and-content-style-guide/
      SKILL.md (15975 bytes)
      skills/10-content-design-and-ux-writing/voice-tone-and-content-style-guide/examples/
        worked-voice-and-tone-guide.md (8674 bytes)
      skills/10-content-design-and-ux-writing/voice-tone-and-content-style-guide/references/
        voice-chart-and-tone-map.md (10963 bytes)
  skills/11-imagery-illustration-and-art-direction/
    README.md (306 bytes)
    skills/11-imagery-illustration-and-art-direction/ai-image-generation-art-direction/
      SKILL.md (11301 bytes)
      skills/11-imagery-illustration-and-art-direction/ai-image-generation-art-direction/examples/
        ai-image-brief-and-gate-run.md (6401 bytes)
      skills/11-imagery-illustration-and-art-direction/ai-image-generation-art-direction/references/
        ai-image-direction-and-gate.md (11465 bytes)
    skills/11-imagery-illustration-and-art-direction/iconography-system-design/
      SKILL.md (12083 bytes)
      skills/11-imagery-illustration-and-art-direction/iconography-system-design/examples/
        icon-set-spec.md (6591 bytes)
      skills/11-imagery-illustration-and-art-direction/iconography-system-design/references/
        icon-grid-and-stroke.md (7185 bytes)
    skills/11-imagery-illustration-and-art-direction/illustration-style-and-systems/
      SKILL.md (15253 bytes)
      skills/11-imagery-illustration-and-art-direction/illustration-style-and-systems/examples/
        illustration-style-spec.md (8335 bytes)
      skills/11-imagery-illustration-and-art-direction/illustration-style-and-systems/references/
        illustration-system.md (10029 bytes)
    skills/11-imagery-illustration-and-art-direction/photography-art-direction/
      SKILL.md (8373 bytes)
      skills/11-imagery-illustration-and-art-direction/photography-art-direction/examples/
        art-direction-board.md (6034 bytes)
      skills/11-imagery-illustration-and-art-direction/photography-art-direction/references/
        anti-stock-direction.md (6602 bytes)
        photo-treatment-system.md (5779 bytes)
  skills/12-data-viz-and-dashboards/
    skills/12-data-viz-and-dashboards/chart-selection-and-encoding/
      SKILL.md (10305 bytes)
      skills/12-data-viz-and-dashboards/chart-selection-and-encoding/examples/
        chart-selection-cases.md (7247 bytes)
      skills/12-data-viz-and-dashboards/chart-selection-and-encoding/references/
        chart-fit-decision.md (7860 bytes)
    skills/12-data-viz-and-dashboards/dashboard-and-data-product-design/
      SKILL.md (9629 bytes)
      skills/12-data-viz-and-dashboards/dashboard-and-data-product-design/examples/
        dashboard-spec.md (8374 bytes)
      skills/12-data-viz-and-dashboards/dashboard-and-data-product-design/references/
        dashboard-layout-patterns.md (8428 bytes)
        kpi-hierarchy.md (5845 bytes)
    skills/12-data-viz-and-dashboards/data-visualization/
      SKILL.md (30232 bytes)
      skills/12-data-viz-and-dashboards/data-visualization/examples/
        chart-worked-examples.md (6258 bytes)
      skills/12-data-viz-and-dashboards/data-visualization/references/
        analytics-dashboard-decision-story.md (2590 bytes)
        chart-encoding.md (8335 bytes)
        dashboard-patterns.md (5898 bytes)
        responsive-mobile-charts.md (1822 bytes)
        svg-css-js-implementation.md (22757 bytes)
  skills/13-presentations-and-documents/
    skills/13-presentations-and-documents/deck-system/
      SKILL.md (3674 bytes)
      skills/13-presentations-and-documents/deck-system/examples/
        variant-ai-strategy-presentation.md (24804 bytes)
        variant-annual-review.md (33423 bytes)
        variant-campaign-proposal.md (23124 bytes)
        variant-credentials.md (19380 bytes)
        variant-initial-pitch.md (23614 bytes)
        variant-monthly-report.md (18272 bytes)
        variant-quarterly-review.md (26587 bytes)
        variant-strategy-presentation.md (22543 bytes)
      skills/13-presentations-and-documents/deck-system/references/
        pitch-psychology.md (3895 bytes)
        presentation-frameworks.md (5441 bytes)
        storytelling.md (3077 bytes)
    skills/13-presentations-and-documents/design-storytelling-and-case-studies/
      SKILL.md (9123 bytes)
      skills/13-presentations-and-documents/design-storytelling-and-case-studies/examples/
        case-study-kesilex-onboarding.md (7274 bytes)
      skills/13-presentations-and-documents/design-storytelling-and-case-studies/references/
        case-study-structure.md (6503 bytes)
        narrative-frameworks.md (8818 bytes)
    skills/13-presentations-and-documents/docx-report-and-document-formatting/
      SKILL.md (9883 bytes)
      skills/13-presentations-and-documents/docx-report-and-document-formatting/examples/
        before-after-default-vs-designed.md (4749 bytes)
        report-style-table.md (5826 bytes)
      skills/13-presentations-and-documents/docx-report-and-document-formatting/references/
        accessible-docx-tags.md (3626 bytes)
        docx-style-system.md (7957 bytes)
        tables-and-figures.md (4173 bytes)
    skills/13-presentations-and-documents/email-and-newsletter-design/
      SKILL.md (20996 bytes)
      skills/13-presentations-and-documents/email-and-newsletter-design/examples/
        email-template-spec.md (3706 bytes)
      skills/13-presentations-and-documents/email-and-newsletter-design/references/
        email-bulletproof-patterns.md (16812 bytes)
    skills/13-presentations-and-documents/pdf-proposal-and-bankable-document-design/
      SKILL.md (6980 bytes)
      skills/13-presentations-and-documents/pdf-proposal-and-bankable-document-design/examples/
        exhibit-page-layout.md (4053 bytes)
        proposal-cover-spec.md (3725 bytes)
      skills/13-presentations-and-documents/pdf-proposal-and-bankable-document-design/references/
        cover-and-divider-systems.md (4646 bytes)
        print-ready-pdf-checklist.md (4678 bytes)
        proposal-section-architecture.md (5163 bytes)
    skills/13-presentations-and-documents/xlsx-and-financial-model-presentation/
      SKILL.md (14487 bytes)
      skills/13-presentations-and-documents/xlsx-and-financial-model-presentation/examples/
        kpi-model-summary-exhibit.md (8412 bytes)
      skills/13-presentations-and-documents/xlsx-and-financial-model-presentation/references/
        exhibit-and-print-layout.md (5575 bytes)
        xlsx-design-system.md (13580 bytes)
  skills/14-conversion-and-web-page-patterns/
    README.md (442 bytes)
    skills/14-conversion-and-web-page-patterns/empty-error-and-loading-states/
      SKILL.md (10233 bytes)
      skills/14-conversion-and-web-page-patterns/empty-error-and-loading-states/examples/
        states-for-a-table-component.md (8739 bytes)
      skills/14-conversion-and-web-page-patterns/empty-error-and-loading-states/references/
        state-matrix.md (9144 bytes)
    skills/14-conversion-and-web-page-patterns/landing-page-and-conversion-design/
      SKILL.md (15172 bytes)
      skills/14-conversion-and-web-page-patterns/landing-page-and-conversion-design/examples/
        landing-wireframe-spec.md (8616 bytes)
      skills/14-conversion-and-web-page-patterns/landing-page-and-conversion-design/references/
        conversion-credibility.md (6774 bytes)
        landing-anatomy.md (6391 bytes)
    skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/
      SKILL.md (13490 bytes)
      skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/examples/
        sitemap-and-nav-spec.md (11194 bytes)
      skills/14-conversion-and-web-page-patterns/navigation-and-information-architecture/references/
        ia-patterns.md (9902 bytes)
        nav-pattern-catalog.md (7825 bytes)
    skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/
      SKILL.md (17484 bytes)
      skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/examples/
        first-run-flow-for-a-team-todo-app.md (10135 bytes)
      skills/14-conversion-and-web-page-patterns/onboarding-and-first-run-design/references/
        onboarding-patterns.md (10148 bytes)
    skills/14-conversion-and-web-page-patterns/trust-credibility-and-social-proof/
      SKILL.md (17072 bytes)
      skills/14-conversion-and-web-page-patterns/trust-credibility-and-social-proof/examples/
        credibility-section-spec.md (8509 bytes)
      skills/14-conversion-and-web-page-patterns/trust-credibility-and-social-proof/references/
        trust-signal-catalog.md (9784 bytes)
  skills/_TEMPLATE/
    SKILL.md (1284 bytes)
    skills/_TEMPLATE/examples/
      example-1.md (735 bytes)
```
