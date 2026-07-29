const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace Header Logo src and Size
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_LIGHT\.png"[^>]*>/g,
    '<img src="assets/images/AT_LOGO_LIGHT-removebg.png" style="max-height: 75px; width: auto;" alt="AMAN Textile" />'
  );

  // Replace Footer Logo src and Size
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_DARK\.png"[^>]*>/g,
    '<img src="assets/images/AT_LOGO_DARK-removebg.png" style="max-height: 105px; width: auto; margin-bottom: 25px; transition: transform 0.3s ease;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed logos bg and size in ' + f);
  }
});
