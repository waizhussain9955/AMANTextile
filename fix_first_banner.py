file_path = 'baby-product.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the first banner image which got messed up
content = content.replace(
    'title=BATHROBE%20SET&images=assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg&banner=assets/images/AT_LOGO_LIGHT-removebg.png',
    'title=BATHROBE%20SET&images=assets/images/baby-1.jpg%2Cassets/images/baby-2.jpg%2Cassets/images/baby-3.jpg%2Cassets/images/baby-4.jpg&banner=assets/images/baby-2.jpg'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed first banner")
