import re

file_path = 'basic-apparel.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the duplicated strings and add the closing </a> tag
replacements = {
    'KITCHEN GLOVESKITCHEN GLOVES\r\n': 'KITCHEN GLOVES</a>\r\n',
    'KITCHEN GLOVESKITCHEN GLOVES\n': 'KITCHEN GLOVES</a>\n',
    'GOLOVES AND TOWEL GOLOVES AND TOWEL \r\n': 'GOLOVES AND TOWEL</a>\r\n',
    'GOLOVES AND TOWEL GOLOVES AND TOWEL \n': 'GOLOVES AND TOWEL</a>\n',
    'TERRY KITCHEN TOWELLSTERRY KITCHEN TOWELLS\r\n': 'TERRY KITCHEN TOWELLS</a>\r\n',
    'TERRY KITCHEN TOWELLSTERRY KITCHEN TOWELLS\n': 'TERRY KITCHEN TOWELLS</a>\n',
    'POT HOLDERS SETTPOT HOLDERS SETT\r\n': 'POT HOLDERS SETT</a>\r\n',
    'POT HOLDERS SETTPOT HOLDERS SETT\n': 'POT HOLDERS SETT</a>\n',
    'POT HOLDERSPOT HOLDERS\r\n': 'POT HOLDERS</a>\r\n',
    'POT HOLDERSPOT HOLDERS\n': 'POT HOLDERS</a>\n',
    'DISH TOWELS SETDISH TOWELS SET\r\n': 'DISH TOWELS SET</a>\r\n',
    'DISH TOWELS SETDISH TOWELS SET\n': 'DISH TOWELS SET</a>\n'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed basic-apparel.html broken links")
