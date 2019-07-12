import urllib.request
import re
import datetime
url=r"https://www.atg.world/user-dashboard"
content=urllib.request.urlopen(url)
title_regex=r"<title>(.+?)</title>"
pattern=re.compile(title_regex)
content=content.read()
content=content.decode('utf-8','ignore')
title=re.findall(pattern,content)
print(title)
print('-'*80)
t1=datetime.datetime.now()
content=urllib.request.urlopen(url)
t2=datetime.datetime.now()
t=t2-t1
print('time taken for response is:',t)
print('-'*80)
print(content.code)         #to fetch the HTTP response code
print('-'*80)
contents=content.read()
contents=contents.decode('utf-8','ignore')
print(contents)
