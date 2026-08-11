from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        
    def handle_starttag(self, tag, attrs):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            self.tags.append(tag)
            
    def handle_endtag(self, tag):
        if tag not in ['img', 'br', 'hr', 'input', 'meta', 'link']:
            if not self.tags:
                print(f"Extra closing tag: {tag}")
            elif self.tags[-1] == tag:
                self.tags.pop()
            else:
                print(f"Mismatched tag: expected {self.tags[-1]}, got {tag}")

parser = MyHTMLParser()
with open('baby-product.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
print("Unclosed tags:", parser.tags)
