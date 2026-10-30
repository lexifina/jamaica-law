import json,re,hashlib,collections
rows=json.load(open('src/rows.json'))
U={'src/a1011.pdf':'https://www.japarliament.gov.jm/attachments/502_Report%20of%20Acts%20Passed%20during%20the%20Legislative%20Year%202010-2011.pdf',
   'src/a1112.pdf':'https://www.japarliament.gov.jm/attachments/663_Report%20of%20Acts%20that%20have%20been%20passed%20for%20the%20Legislative%20Year%202011-2012.pdf'}
NAME={'src/a1011.pdf':'Report on Acts passed in Parliament, legislative year 2010/2011','src/a1112.pdf':'Report on Acts passed in Parliament, legislative year 2011/2012'}
ents=[]
for f,no,title,d in rows:
    if no=='10/2001': no='10/2011'
    m=re.match(r'(.*?\bAct,? ?\d{4})',title); title=m.group(1).strip().rstrip('.')
    if title.startswith('Office of the Prime Minister'): title='The Town and Country Planning (Negril and Green Island Area Local Planning Authority) (Validation and Indemnity) Act, 2010'
    n,y=no.split('/')
    ents.append(dict(f=f,key='act-%02d-%s'%(int(n),y),no=no,title=title,date=d.replace('/','-')))
bydate=collections.defaultdict(list)
for e in ents: bydate[e['date']].append(e)
laws={};versions=[]
for i,d in enumerate(sorted(bydate)):
    lk='catalogue-'+d
    laws[lk]={'label':'Catalogue entries, assent of %s'%d,'title':'Acts assented to on %s'%d,'kind':'publisher','enacted':d,'published':None,'url':U[bydate[d][0]['f']],'temporary_until':None,'restores':None,
      'note':"Facts only: the Acts that received the Governor-General's assent on this date, as listed by the Houses of Parliament. No Act text."}
    ch={}
    for e in bydate[d]:
        u={'label':'Act No. '+e['no'],'kind':'act','text':"# %s\nAct No.: %s\nGovernor-General's assent: %s\nSource: Houses of Parliament of Jamaica, %s\n"%(e['title'],e['no'],e['date'],NAME[e['f']])}
        ch[e['key']]=u
    v={'from':d,'source_url':U[bydate[d][0]['f']],'sha256':hashlib.sha256(open(bydate[d][0]['f'],'rb').read()).hexdigest(),'credits':{k:[lk] for k in ch}}
    if i==0: v['units']=dict(ch)
    else: v['changes']=ch
    versions.append(v)
first=sorted(bydate)[0]
corpus={'country':{'code':'JM','name':'Jamaica','slug':'jamaica','lang':'en','tz':'America/Jamaica','future_branch':'future',
  'publisher':{'name':'Houses of Parliament of Jamaica','email':'parliament@japarliament.invalid'},
  'default_in_force_rule':{'text':"Not applicable: this repository lists the date each Act received the Governor-General's assent, not the date it came into operation.",'source':'https://www.japarliament.gov.jm/'},
  'licence_note':"Facts only (Act number, title, assent date) from the Houses of Parliament of Jamaica; no Act text and none of the reports' descriptive wording is copied."},
 'sources':[{'name':NAME[f],'url':U[f],'retrieved':'2026-10-30','licence':'Facts only; the page states "Copyright (c) 2008 Jamaica Houses of Parliament", so no descriptive wording is copied.','notes':'PDF with a text layer.'} for f in U],
 'laws':laws,
 'acts':[{'slug':'catalogue','short':'CAT','title':'Catalogue of Acts of Jamaica (facts only, 2010-2011), no law text','url':'https://www.japarliament.gov.jm/','first_law':'catalogue-'+first,'earlier_laws':[],'versions':versions}],
 'applies':[],
 'decisions':["Jamaica's revised laws (laws.moj.gov.jm) were unreachable (HTTP 503 maintenance notice on every path) and the Houses of Parliament's Act PDFs are scans, and no reuse terms permitting copying of the law text were found (the 2015 amendment to the Copyright Act reinstated Crown copyright), so no law text is published; OCR was not attempted.",
  "Each unit is one Act from the Houses of Parliament's 'Report on Acts passed' for 2010/2011 and 2011/2012, with Act number, title and the Governor-General's assent date. Each version adds the Acts assented to on one date and is dated that day.",
  "The 2010/2011 report prints the number of the Jamaica International Financial Services Authority Act as '10/2001'; it is read as 10/2011 (the title says 2011 and the assent date is 1 April 2011).",
  "The title of Act 29/2010 is printed with the ministry name run into it ('Office of the Prime Minister Town and Country Planning ...'); the ministry was removed by hand.",
  'Acts 12/2011, 13/2011 and 14/2011 are not in the two reports and are not listed.'],
 'ai_use':['none']}
json.dump(corpus,open('corpus.json','w',encoding='utf8'),ensure_ascii=False,indent=1)
print(len(ents),len(versions))
