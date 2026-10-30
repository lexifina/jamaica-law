"""Jamaica: Acts passed 2016-2022 from the Houses of Parliament's yearly pages (.tmp/art<id>.html). Writes .tmp/acts_years.json."""
import re, html, json
from urllib.parse import quote
PAGES = {2016: 1621, 2017: 1722, 2018: 1889, 2019: 2129, 2020: 2239, 2021: 2362, 2022: 2518}
out = []
for y, aid in PAGES.items():
    s = open(f'.tmp/art{aid}.html', encoding='utf8', errors='ignore').read()
    i = s.find(f'Acts Passed in {y}'); j = s.find('Important Notices', i)
    seg = s[i:j]
    for m in re.finditer(r'<a [^>]*href="([^"]+\.pdf)"[^>]*>(.*?)</a>', seg, re.S):
        href, txt = m.group(1), re.sub(r'\s+', ' ', html.unescape(re.sub('<[^>]+>', '', m.group(2)))).replace('�', ' ').replace('\xa0', ' ').strip()
        if 'STO-' in href or not txt: continue
        out.append((y, href, txt))
    print(y, len([o for o in out if o[0] == y]))
json.dump(out, open('.tmp/acts_years_raw.json', 'w'), ensure_ascii=False, indent=0)
for o in out[:3] + out[-3:]: print(o)
