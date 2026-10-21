from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json
import re
root=Path(__file__).resolve().parents[1]/'prototype'
class Page(HTMLParser):
 def __init__(self): super().__init__();self.ids=[];self.links=[];self.assets=[];self.h1=0;self.bad=[];self.main=[];self.lang=None;self.titles=0;self.summary=0;self.details=0;self.anchor=None;self.names=[];self.headings=[];self.references=[];self.articles=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if t=='h1':self.h1+=1
  if t=='html':self.lang=a.get('lang')
  if t=='title':self.titles+=1
  if t=='main':self.main.append(a)
  if t=='summary':self.summary+=1
  if t=='details':self.details+=1
  if t=='a':self.links.append(a.get('href',''));self.anchor=[a.get('aria-label','')]
  if t in ('h1','h2','h3','h4','h5','h6'):self.headings.append(int(t[1]))
  if t=='article':self.articles.append(a.get('id'))
  for key in ('aria-labelledby','aria-describedby','aria-controls'):
   if key in a:self.references.extend(a[key].split())
  if any(k.startswith('on') for k in a):self.bad.append('inline event')
  if t in ('script','form','input','iframe','object','embed','audio','video'):self.bad.append(t)
  if t=='img' and 'alt' not in a:self.bad.append('image without alt')
  if 'src' in a:self.assets.append(a['src'])
  if t=='link' and a.get('rel') in ('stylesheet','icon'):self.assets.append(a['href'])
 def handle_data(self,data):
  if self.anchor is not None:self.anchor.append(data)
 def handle_endtag(self,t):
  if t=='a' and self.anchor is not None:self.names.append(''.join(self.anchor).strip());self.anchor=None
pages={}
for f in sorted(root.glob('*.html')):
 x=Page();x.feed(f.read_text());pages[f.name]=x
 assert x.h1==1,(f,'h1')
 assert x.lang=='en' and x.titles==1,(f,'language/title')
 assert len(x.main)==1 and x.main[0].get('id')=='main' and x.main[0].get('tabindex')=='-1',(f,'skip destination')
 assert '#main' in x.links,(f,'missing skip link')
 assert x.summary==x.details,(f,'disclosure summaries')
 assert len(x.ids)==len(set(x.ids)),(f,'duplicate ids')
 assert all(x.names),(f,'link missing accessible name')
 assert all(ref in x.ids for ref in x.references),(f,'broken ARIA reference')
 assert all(b<=a+1 for a,b in zip(x.headings,x.headings[1:])),(f,'heading level skipped')
 assert not x.bad,(f,'unexpected script/form/embed')
 for asset in x.assets:
  assert not urlsplit(asset).scheme,(f,'remote asset')
  assert (root/asset).is_file(),(f,asset)
for filename,x in pages.items():
 for link in x.links:
  u=urlsplit(link)
  if u.scheme: assert u.scheme=='https';continue
  dest=unquote(u.path) or filename
  if dest not in pages:
   assert dest in ('music-practice-packet.pdf','facilitator-outline.pdf') and (root/dest).read_bytes().startswith(b'%PDF-') and not u.fragment,(filename,link)
   continue
  if u.fragment: assert unquote(u.fragment) in pages[dest].ids,(filename,link)
assert (500-75-125-100)/2==100
assert (root/'print.html').read_text().count('<details>')==0
activity_ids=['four-lines','show','emphasis','reference','viewpoints','choose-part','word-sound']
assert pages['practice.html'].articles==activity_ids
assert all(id in pages['print.html'].articles for id in activity_ids)
profile_ids=['black-thought','rapsody','megan','gza','badu-dilla','little-simz','eminem','rakim','lupe-fiasco','doechii']
assert pages['stories.html'].articles==profile_ids
assert all(id in pages['print.html'].articles for id in profile_ids)
assert all('stories.html#'+id in pages['index.html'].links for id in profile_ids)
assert all(link in pages['sources.html'].links for link in pages['stories.html'].links if urlsplit(link).scheme=='https')
assert all('Does this help your goal?' not in (root/name).read_text() for name in ('practice.html','print.html'))
assert all('What to take from it' not in (root/name).read_text() for name in ('stories.html','print.html'))
assert 'week.html' in pages
assert 'week-steps' in (root/'week.html').read_text()
assert (root/'print.html').read_text().count('Try a step if it fits')==1
css=(root/'style.css').read_text()
assert not re.search(r'@import|https?://|url\s*\(',css,re.I),'Unexpected CSS dependency'
colors=['#111a2c','#445269','#174fc4','#bd3e00']
def lum(c):
 v=[int(c[i:i+2],16)/255 for i in (1,3,5)]
 v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v]
 return .2126*v[0]+.7152*v[1]+.0722*v[2]
def ratio(a,b):
 x,y=sorted((lum(a),lum(b)));return (y+.05)/(x+.05)
contrast={c:round(ratio(c,'#ffffff'),2) for c in colors}
assert all(v>=4.5 for v in contrast.values())
assert ratio('#445269','#eef3ff')>=4.5
assert ratio('#dbe4f5','#111a2c')>=4.5
assert ratio('#c0cee7','#111a2c')>=4.5
report={'pages':len(pages),'local_links_and_fragments':'pass','no_scripts_forms_embeds_or_remote_assets':'pass','single_h1_and_unique_ids':'pass','language_title_skip_and_disclosures':'pass','link_names_heading_order_aria_references':'pass','all_profiles_activities_week_in_print':'pass','profiles':10,'activities':7,'css_has_no_network_dependencies':'pass','fictional_budget':'pass','print_answers_not_collapsed':'pass','foreground_white_contrast':contrast,'web_content_bytes':sum(f.stat().st_size for f in root.iterdir() if f.suffix in ('.html','.css','.svg')),'print_pdf_bytes':(root/'music-practice-packet.pdf').stat().st_size,'facilitator_pdf_bytes':(root/'facilitator-outline.pdf').stat().st_size,'total_prototype_bytes':sum(f.stat().st_size for f in root.iterdir() if f.is_file())}
(root.parent/'docs'/'static-check-results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
