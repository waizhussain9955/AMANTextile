const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Fix footer logo size to be smaller and remove extreme negative margins
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_DARK-removebg\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_DARK-removebg.png" style="width: 120px; height: auto; display: block; margin-top: -15px; margin-bottom: -5px; transition: transform 0.3s ease;" alt="AMAN Textile" />'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Final footer logo fix in ' + f);
  }
});
