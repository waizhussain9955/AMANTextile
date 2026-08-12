import re

file_path = 'basic-apparel.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the duplicated names
duplicates = {
    'KITCHEN GLOVESKITCHEN GLOVES': 'KITCHEN GLOVES',
    'GOLOVES AND TOWELGOLOVES AND TOWEL': 'GOLOVES AND TOWEL',
    'TERRY KITCHEN TOWELLSTERRY KITCHEN TOWELLS': 'TERRY KITCHEN TOWELLS',
    'POT HOLDERS SETTPOT HOLDERS SETT': 'POT HOLDERS SETT',
    'POT HOLDERSPOT HOLDERS': 'POT HOLDERS',
    'DISH TOWELS SETDISH TOWELS SET': 'DISH TOWELS SET'
}

for dup, original in duplicates.items():
    content = content.replace(f'style="text-decoration: none !important;">{dup}</a>', f'style="text-decoration: none !important;">{original}</a>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed duplicated names in basic-apparel.html")
