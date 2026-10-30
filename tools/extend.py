"""Jamaica: add Acts passed 2016-2022 (title, number, link; year only) as act `catalogue-by-year`."""
import json, re, hashlib, collections
from urllib.parse import quote
raw = json.load(open('.tmp/acts_years_raw.json', encoding='utf8'))
BASE = 'https://www.japarliament.gov.jm/'
PAGE = {2016: 1621, 2017: 1722, 2018: 1889, 2019: 2129, 2020: 2239, 2021: 2362, 2022: 2518}
ents, skipped, seen = [], [], set()
for y, href, txt in raw:
    txt = txt.replace('Agreements At,', 'Agreements Act,').replace('Events) Acts, 2018', 'Events) Act, 2018')  # typos in the list text
    m = re.match(r'(.*?\bAct,?\s*\d{4})\W*(?:Act\s*)?(?:No\.?\s*(\d+))?', txt.replace(' ', ' '))
    if not m or not m.group(2):
        skipped.append((y, txt)); continue
    title, no = re.sub(r'\s+', ' ', m.group(1)).strip().rstrip(','), int(m.group(2))
    title = re.sub(r'\bAct,\s*(\d{4})$', r'Act, \1', title)
    if (y, no) in seen: continue
    seen.add((y, no))
    ents.append(dict(y=y, no=no, title=title, url=BASE + quote(href.lstrip('/'), safe="/%()")))
print(len(ents), 'acts; skipped', skipped)
c = json.load(open('corpus.json', encoding='utf8'))
by = collections.defaultdict(list)
for e in ents: by[e['y']].append(e)
laws, versions = {}, []
for i, y in enumerate(sorted(by)):
    d = f'{y}-12-31'; lk = f'catalogue-year-{y}'
    laws[lk] = {'label': f'Catalogue entries, Acts passed in {y}', 'title': f'Acts passed in {y} (assent dates not given)', 'kind': 'publisher', 'enacted': d, 'published': None,
                'url': BASE + f'index.php?option=com_content&view=article&id={PAGE[y]}', 'temporary_until': None, 'restores': None,
                'note': f"Facts only: the Acts the Houses of Parliament list as passed in {y}. The list gives the year, not the date of assent, so the version is dated 31 December {y} as a placeholder. No Act text."}
    ch = {}
    for e in sorted(by[y], key=lambda e: e['no']):
        ch[f"act-{e['no']:02d}-{y}"] = {'label': f"Act No. {e['no']}/{y}", 'kind': 'act',
            'text': f"# {e['title']}\nAct No.: {e['no']}/{y}\nYear passed: {y}\nDate of assent: not given by the source (the version date, 31 December {y}, is a placeholder)\nPDF: {e['url']}\nSource: Houses of Parliament of Jamaica, Acts Passed in {y}\n"}
    v = {'from': d, 'source_url': laws[lk]['url'], 'sha256': hashlib.sha256(open(f'.tmp/art{PAGE[y]}.html', 'rb').read()).hexdigest(), 'credits': {k: [lk] for k in ch}}
    v['units' if i == 0 else 'changes'] = ch
    versions.append(v)
c['laws'].update(laws)
c['acts'] = [a for a in c['acts'] if a['slug'] != 'catalogue-by-year'] + [{'slug': 'catalogue-by-year', 'short': 'CAT-Y', 'title': 'Catalogue of Acts of Jamaica passed 2016-2022, by year (facts only), no law text', 'url': BASE,
    'first_law': None, 'earlier_laws': [], 'versions': versions}]
c['sources'] = [s for s in c['sources'] if not s['name'].startswith('Acts Passed in 20')] + [{'name': f'Acts Passed in {y} (Houses of Parliament)', 'url': BASE + f'index.php?option=com_content&view=article&id={PAGE[y]}', 'retrieved': '2026-10-30',
    'licence': 'Facts only (Act number, title, year, link); copyright notice on the site, so no descriptive wording or Act text is copied. robots.txt disallows only /japarlia/ system folders.', 'notes': 'HTML list of links to PDF scans.'} for y in sorted(by)]
c['decisions'] = [d for d in c['decisions'] if not d.startswith('Acts passed 2016')]
c['decisions'].append(f"Acts passed 2016-2022: {len(ents)} Acts from the Houses of Parliament's yearly lists. The lists give the year, not the assent date (the dates are handwritten on the PDF scans, and OCR of them was unreliable, so none was read), so each year's version is dated 31 December of that year as a placeholder. Only number, title and link are recorded. Items without an Act number in the list text were skipped: {len(skipped)}.")
json.dump(c, open('corpus.json', 'w', encoding='utf8', newline='\n'), ensure_ascii=False, indent=1)
