import os
import re

html_files = ['index.html', 'homepage.html']

clean_attr = 'data-slider-settings=\'{"autoplay":{"delay":7000,"disableOnInteraction":false},"parallax":true,"mobparallax":true,"loop":true,"speed":2500}\''

for hfile in html_files:
    if os.path.exists(hfile):
        with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()

        html = re.sub(r'data-slider-settings=[\'"][^\'>]*[\'"]', clean_attr, html)

        with open(hfile, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Cleaned slider attribute in {hfile}")
