# Jamaica: law history in git


Jamaica's law as a git history, on the design every country here shares: one file per unit, one commit per version on the day it took effect, and the record that made each change as the commit's author. For now it holds no law text, only facts: a catalogue of Acts of Jamaica and Jamaica's actions on treaties. `git blame` names the day's record behind every line; `git log` lists every entry for an Act or a treaty; picking a date gives the record as it stood that day.

Part of [lexifina/global-law](https://github.com/lexifina/global-law), one git history for every country's law: this is Jamaica's national law, which global-law reads at `jamaica/national/acts/`.

**What is in it now:** no law text. [`catalogue/`](catalogue/README.md) lists 45 Acts from the Houses of Parliament's reports for 2010/2011 and 2011/2012, each with its number, title and day of assent (31 March 2010 to 6 December 2011), and 28 laws recorded by WIPO Lex, the Constitution among them, with their titles and dates (1888 to 2022); [`catalogue-by-year/`](catalogue-by-year/README.md) lists 150 Acts passed in 2016-2022, with number, title and a link to the PDF. [`un-treaties/`](un-treaties/README.md) records 80 actions on 51 multilateral treaties deposited with the UN Secretary-General (34 signatures, 28 ratifications, 15 accessions, 2 acceptances and 1 succession), from 21 March 1963 to 23 October 2020, and [`wipo-treaties/`](wipo-treaties/README.md) Jamaica's part in 50 treaties as WIPO Lex records it. [`data/laws.csv`](data/laws.csv) lists every dated entry; [`REPRODUCE.md`](REPRODUCE.md) says how the files were made.

**Why there is no law text.** The Legal Information Portal of Jamaica ([lipj.gov.jm](https://lipj.gov.jm)) publishes the Revised Laws and the Acts of Parliament as page scans, and its terms of use call official legal documents public domain but limit the use of its legal repository to lawful, non-commercial purposes. The Houses of Parliament also publish Acts as scans. Until reuse is clear, only facts are taken; the laws will be added when it is.

Each Act is one file: `catalogue/act-29-2010.md` is Act No. 29/2010 and `catalogue-by-year/act-01-2016.md` Act No. 1/2016; `catalogue/law-08855.md` is WIPO Lex's entry for the Constitution of Jamaica. Each treaty is one file named from its number in the UN Treaty Collection: `un-treaties/untc-xxvii-7-d.md` is the Paris Agreement (XXVII-7-d).

The records are in English, with titles as the Houses of Parliament, WIPO Lex and the UN Treaty Collection print them.

## Questions as git commands

| Question | Command |
| --- | --- |
| Every action Jamaica took on the Paris Agreement | `git log -p --word-diff -- un-treaties/untc-xxvii-7-d.md` |
| Which action wrote each line? | `git blame un-treaties/untc-xxvii-7-d.md` |
| Every version of the Paris Agreement's record, with the day of each | `git log --format="%h %(trailers:key=In-force,valueonly,separator=) %an" -- un-treaties/untc-xxvii-7-d.md` |
| The record as it stood on 1 June 2016 | `python tools/on.py 2016-06-01 un-treaties untc-xxvii-7-d` |

**Outside git**, we also host this record publicly, for free:

- **[Ask Claude about Jamaica](https://global-law.lexifina.com/v1/try_claude?country=jamaica)**: opens Claude with a first question ready.
- **[Ask ChatGPT](https://global-law.lexifina.com/v1/try_chatgpt?country=jamaica)**: the same question in ChatGPT.
- **[Search Jamaica's record on our site](https://lexifina.com/law?country=jamaica&q=Paris+Agreement)**: a search for "Paris Agreement" in its catalogue of titles, no account needed.
- **[Developer REST API](https://global-law.lexifina.com/v1/search_law?query=Paris+Agreement&jurisdiction=jamaica)**: the same search as JSON, with no key. See the [documentation here](https://lexifina.com/api/global-law).

Both assistants read the record through the free Global law connector (MCP, `https://global-law.lexifina.com/mcp`); the first time, the chat gives you the link that adds it. Ask in English.

**Host it yourself easily.** All it takes is git and Python, and the tools run on your machine:

```sh
git clone --depth 1 https://github.com/lexifina/global-law && cd global-law
python3 tools/countries.py add jamaica/national/acts
python3 tools/law.py show 2026-01-01 jamaica/national/acts/un-treaties/untc-xxvii-7-d.md
```

Opened in Claude Code, Cursor, VS Code or Codex, the clone also starts a local MCP server with the same tools ([MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md)).

## Dates

Each commit is dated at noon, America/Jamaica, and carries its day in its `In-force:` trailer:

- for the Acts of 2010-2011, the day of the Governor-General's assent the reports give, not the day the Act came into operation;
- for the Acts of 2016-2022, 31 December of the year they were passed, as a placeholder: the lists give the year only;
- for WIPO Lex's laws and treaties, the date WIPO Lex records (for a law: promulgation, entry into force, commencement or adoption, in that order; some are only 1 January of a year), and for the UN treaties the day of Jamaica's action;
- git cannot store dates before 1970, so the 24 earlier commits are dated from 1970-01-01, one second apart, with the real day in `In-force:`. Ask for a date with `tools/on.py`, not `git log --before`.

Each day's entries are credited to a record named for that day (`Catalogue entries, assent of 2010-08-31`, `Ratification: Paris Agreement Paris, 12 December 2015`), with an e-mail address that cannot exist; the first version of each folder, the oldest available, to the publisher, `Houses of Parliament of Jamaica`.

## How it is checked

- `tools/check_repo.py` reads every version back from git on the day it took effect and on the day before and compares it with the corpus, whose hash is in `data/corpus.sha256`; it also checks that every commit's trailers parse, that `main` has no merge commits and that no commit is dated in the future.
- `tools/build.py` writes the history from that one corpus file, and the same corpus gives the same commit hashes. [`REPRODUCE.md`](REPRODUCE.md) records that the checks were not yet run for this build and that no second build has been compared.
- `data/versions.json` gives each version's source and the sha256 of what it was read from. Only facts are taken: numbers, titles, dates and links.

## What it does not show

- **Law text.** No Act, regulation or Constitution; the Portal lists 613 Revised Laws and 1,636 Acts of Parliament.
- **Most Acts.** Only the Acts the Houses of Parliament list for 2010-2011 and 2016-2022 (Acts 12, 13 and 14 of 2011 are not in the reports) and the 28 laws and regulations from WIPO Lex. No case law.
- **Days of assent for 2016-2022**, and the day any Act came into operation; many Acts commence later, by notice.
- **Most treaty actions.** Only the 78 UN status pages read and WIPO Lex's list; no treaty text, reservations or declarations.

## Sources

| Source | Kind | Past versions | Notes |
| --- | --- | --- | --- |
| [Houses of Parliament of Jamaica](https://www.japarliament.gov.jm/) | Reports on Acts passed (2010/2011, 2011/2012) and yearly lists of Acts passed (2016-2022) | yes, each Act on its day of assent (2010-2011) or year (2016-2022) | Facts only: number, title, day or year, and a link to the PDF; read on 30 October 2026 |
| [WIPO Lex](https://www.wipo.int/wipolex/en/members/profile/JM) | Catalogue of laws and treaties (CC BY 4.0) | yes, each entry on the date it records | 28 laws and 50 treaties: titles, dates and links; read on 30 October 2026 |
| [United Nations Treaty Collection](https://treaties.un.org/) | Status pages of multilateral treaties deposited with the UN Secretary-General | yes, each action on its day | Facts only: treaty names and the dates of Jamaica's actions; read on 29 October 2026 |

## Licence

See [`LICENSE`](LICENSE). Only facts are taken, which copyright does not protect: no text of any Act, and none of the reports' wording; WIPO Lex's content is CC BY 4.0 (source: World Intellectual Property Organization, which does not endorse this repository). Lexifina's arrangement, tables, commit messages and tools are CC BY 4.0.

No AI model wrote, translated or corrected legal text; the scripts were written by an AI model, and no model runs when the history is built (see [`REPRODUCE.md`](REPRODUCE.md)).

## More

From [lexifina/global-law](https://github.com/lexifina/global-law):

- [FEATURES.md](https://github.com/lexifina/global-law/blob/main/FEATURES.md): every feature, and what every corpus must support (`git blame`, `law.py`, the MCP tools)
- [FAQ.md](https://github.com/lexifina/global-law/blob/main/FAQ.md): questions and answers · [CONTRIBUTING.md](https://github.com/lexifina/global-law/blob/main/CONTRIBUTING.md): proposing changes · [MCP.md](https://github.com/lexifina/global-law/blob/main/MCP.md): the MCP server · [REPRODUCE.md](https://github.com/lexifina/global-law/blob/main/REPRODUCE.md): how it was built · [CHANGELOG.md](https://github.com/lexifina/global-law/blob/main/CHANGELOG.md)
- [FRESHNESS.md](https://github.com/lexifina/global-law/blob/main/FRESHNESS.md): how current each corpus is · [Monitoring](https://github.com/lexifina/global-law/tree/main/monitoring): whether updates are running · [WATCHING.md](https://github.com/lexifina/global-law/blob/main/WATCHING.md): how each official source is watched for changes
- [performance/](https://github.com/lexifina/global-law/tree/main/performance): how fast the tools are, measured
- [visualisations/](https://github.com/lexifina/global-law/tree/main/visualisations): charts and bridges across the world's law
- [Vulnerabilities](https://github.com/lexifina/global-law/tree/main/vulnerabilities): mistakes in legislation as published
