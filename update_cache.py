import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'main.css?v=4' in content or 'main.css?v=5' in content:
        content = content.replace('main.css?v=4', 'main.css?v=6')
        content = content.replace('main.css?v=5', 'main.css?v=6')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated cache buster in {file}")
