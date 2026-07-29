const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Reduce Header Logo Size to 50px
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_LIGHT-removebg\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_LIGHT-removebg.png" style="max-height: 50px; width: auto;" alt="AMAN Textile" />'
  );

  // Additionally catch the old logo just in case some pages weren't updated
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_LIGHT\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_LIGHT-removebg.png" style="max-height: 50px; width: auto;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Reduced navbar logo size in ' + f);
  }
});
