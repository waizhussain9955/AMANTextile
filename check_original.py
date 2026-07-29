import urllib.request
import re

req = urllib.request.Request('http://www.naeementerprise.com/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode('utf-8')

links = re.findall(r'<link[^>]*href=[\'"]([^\'"]+)[\'"][^>]*>', html)
print("ORIGINAL CSS LINKS:")
for l in links:
    if '.css' in l:
        print(l)
