# How this repository was made (Jamaica)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Report on Acts passed in Parliament, legislative year 2010/2011 | <https://www.japarliament.gov.jm/attachments/502_Report%20of%20Acts%20Passed%20during%20the%20Legislative%20Year%202010-2011.pdf> | 2026-10-30 | Facts only; the page states "Copyright (c) 2008 Jamaica Houses of Parliament", so no descriptive wording is copied. |
| Report on Acts passed in Parliament, legislative year 2011/2012 | <https://www.japarliament.gov.jm/attachments/663_Report%20of%20Acts%20that%20have%20been%20passed%20for%20the%20Legislative%20Year%202011-2012.pdf> | 2026-10-30 | Facts only; the page states "Copyright (c) 2008 Jamaica Houses of Parliament", so no descriptive wording is copied. |
| Acts Passed in 2016 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=1621> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2017 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=1722> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2018 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=1889> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2019 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=2129> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2020 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=2239> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2021 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=2362> | 2026-10-30 | Facts only (Act number, title, year, link). |
| Acts Passed in 2022 (Houses of Parliament) | <https://www.japarliament.gov.jm/index.php?option=com_content&view=article&id=2518> | 2026-10-30 | Facts only (Act number, title, year, link). |
| UN Treaty Collection (MTDSG status pages) | <https://treaties.un.org/> | 2026-10-29 | Facts only (treaty action, date, depositary); no text copied |
| WIPO Lex member profile | <https://www.wipo.int/wipolex/en/members/profile/JM> | 2026-10-30 | WIPO content: CC BY 4.0 (https://www.wipo.int/web/terms-of-use); only facts copied |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `catalogue` | Catalogue of Acts of Jamaica: Houses of Parliament reports of 2010-2012 and WIPO Lex records (facts only), no law text | 50 | 1888-05-02 to 2022-02-11 |
| `catalogue-by-year` | Catalogue of Acts of Jamaica passed 2016-2022, by year (facts only), no law text | 7 | 2016-12-31 to 2022-12-31 |
| `un-treaties` | Treaty actions of Jamaica on multilateral treaties deposited with the UN Secretary-General (UN Treaty Collection; no treaty text) | 64 | 1963-03-21 to 2020-10-23 |
| `wipo-treaties` | Treaty actions of Jamaica recorded by WIPO Lex (facts only; no treaty text) | 42 | 1963-03-26 to 2026-07-16 |

The build made 185 commits:

| Commits | Kind |
| ---: | --- |
| 4 | first version of an act |
| 181 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 24 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 187 laws in the record.
- 344 tags.

## Dates

Each commit is dated at noon (America/Jamaica) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Not applicable: this repository lists the date each Act received the Governor-General's assent, not the date it came into operation. https://www.japarliament.gov.jm/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `50e5a3da39427832f942f5f7de8fc65e001a54b4d76e86a5a1304824763579e4` (1019290 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- OCR was not attempted.
- Each unit is one Act from the Houses of Parliament's 'Report on Acts passed' for 2010/2011 and 2011/2012, with Act number, title and the Governor-General's assent date. Each version adds the Acts assented to on one date and is dated that day.
- The 2010/2011 report prints the number of the Jamaica International Financial Services Authority Act as '10/2001'; it is read as 10/2011 (the title says 2011 and the assent date is 1 April 2011).
- The title of Act 29/2010 is printed with the ministry name run into it ('Office of the Prime Minister Town and Country Planning ...'); the ministry was removed by hand.
- Acts 12/2011, 13/2011 and 14/2011 are not in the two reports and are not listed.
- Acts passed 2016-2022: 150 Acts from the Houses of Parliament's yearly lists. The lists give the year, not the assent date (the dates are handwritten on the PDF scans, and OCR of them was unreliable, so none was read), so each year's version is dated 31 December of that year as a placeholder. Only number, title and link are recorded. Items without an Act number in the list text were skipped: 0.
- UN Treaty Collection: 53 multilateral treaties deposited with the UN Secretary-General, with the state's signature, ratification, accession, succession, acceptance or approval dates. Facts only; one version per action date, with the first version credited to the action. Treaties outside the 78 status pages read are not listed.
- WIPO Lex: 28 laws from the member profile dated by the date WIPO Lex records (promulgation, entry into force, commencement, adoption, in that order); 11 laws with no recorded date are left out. Treaty actions: 50. Titles, dates and links only; no text. WIPO Lex gives some laws only 'January 1' of a year, a placeholder rather than a known date.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none
