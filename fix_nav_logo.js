const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace Header Logo Size back to a reasonable height
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_LIGHT\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_LIGHT.png" style="max-height: 65px; width: auto;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed navbar logo size in ' + f);
  }
});
