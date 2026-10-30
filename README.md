# Jamaica: law history in git

**Metadata only, no law text.** This repository holds a catalogue of Acts of Jamaica: for each Act, its number, title and the date the Governor-General gave assent. It does not hold the text of any Act, including the Constitution.

**What is in it now**

| Folder | Content | Versions | History |
| --- | --- | ---: | --- |
| `catalogue/` | One file per law: the Acts of the Houses of Parliament's reports for 2010/2011 and 2011/2012 (number, title, date of assent) and 28 laws recorded by WIPO Lex (title, subject, date, link) | one per date | 1888 to 2022 |
| `wipo-treaties/` | 50 treaty actions of Jamaica recorded by WIPO Lex (name, administering organisation, dates; no treaty text) | 42 | One per action date, 1963 to 2026 |
| `catalogue-by-year/` | One file per Act passed 2016-2022: number, title, link to the PDF | one per year | The Houses of Parliament's yearly lists give the year but not the date of assent, so each year is dated 31 December of that year as a placeholder |
| `un-treaties/` | Jamaica's signature, ratification, accession or acceptance of multilateral treaties deposited with the UN Secretary-General (UN Treaty Collection; no treaty text) | one per action date | From the earliest to the latest recorded action |

Each commit adds the Acts assented to on one date, dated that day and credited to a "catalogue-<date>" entry, so the history lists when each Act was passed.

## Why there is no law text

- The Houses of Parliament publish Acts as scans, and no terms were found that allow the law text to be copied. The 2015 amendment to the Copyright Act reinstated Crown copyright, so Lexifina did not assume that Acts are free to reproduce. No OCR was attempted.
- WIPO Lex (https://www.wipo.int/wipolex/en/members/profile/JM, CC BY 4.0, read 30 October 2026) supplies the WIPO catalogue entries and treaty actions, facts only. Facts (number, title, date) are not protected, so they are what this first build holds. Law text will follow when a reusable official source is found.

## What it does not show

- Most Acts before 2010, after 2022 or in 2012-2015 (the Houses of Parliament publish no list for those years; WIPO Lex adds 28 laws across 1888-2022), any regulation, and any court decision.
- The date of assent of the Acts of 2016-2022: only the year is given (the dates are handwritten on the PDF scans and OCR of them was not reliable), so those versions carry a 31 December placeholder date.
- The date an Act came into operation. Many Acts commence on a later day by notice; the catalogue gives only the date of assent.
- Acts 12/2011, 13/2011 and 14/2011, which are not in the two reports.
- The source prints one Act number as "10/2001"; it is read as 10/2011 (see `REPRODUCE.md`).

## How it is checked

- Every version is read back from git on its day and compared with the corpus (`tools/check_repo.py`; results in `REPRODUCE.md`).
- Each version names its source PDF and the sha256 of the bytes it was read from (`data/versions.json`).
