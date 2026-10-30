import pymupdf,re,json
rows=[]
for f in ('src/a1011.pdf','src/a1112.pdf'):
    t=' '.join(p.get_text() for p in pymupdf.open(f)).replace('’',"'")
    t=re.sub(r'\s+',' ',t)
    parts=re.split(r'(?<!\d)(\d{1,2}/20\d\d) ',t)
    for i in range(1,len(parts),2):
        no,body=parts[i],parts[i+1]
        m=re.search(r'Assent on (\d{4}/\d{2}/\d{2})',body)
        seg=body.split(' To ',1)[0]
        mt=re.search(r'\b(The |An )?[A-Z][^.]*?\bAct,? ?\d{4}',seg[seg.find('Ministry'):] if False else seg)
        k=re.search(r'\bThe (?=[A-Z])',seg)
        title=seg[k.start():] if k else seg
        rows.append((f,no,title.strip(),m.group(1) if m else None))
for r in rows: print(r)
json.dump(rows,open('src/rows.json','w'))
