import urllib.request
import re
import os

url = "http://www.naeementerprise.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8', errors='ignore')
        with open("homepage.html", "w", encoding="utf-8") as f:
            f.write(html)
        print("Successfully fetched homepage.html")
        
        # Find other links
        links = re.findall(r'href="([^"]+)"', html)
        internal_links = set()
        for link in links:
            if not link.startswith("http") and not link.startswith("#") and link.endswith(".html"):
                internal_links.add(link)
        print("Internal links found:", list(internal_links))
except Exception as e:
    print("Error:", e)
