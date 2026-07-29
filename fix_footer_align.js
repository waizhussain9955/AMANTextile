const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace footer logo style across all html files
  content = content.replace(
    /<img src="assets\/images\/AT_LOGO_DARK-removebg\.png" style="[^"]*" alt="AMAN Textile" \/>/g,
    '<img src="assets/images/AT_LOGO_DARK-removebg.png" style="max-width: 140px; height: auto; display: block; margin-bottom: 10px; transition: transform 0.3s ease;" alt="AMAN Textile" />'
  );

  // If the user modified it slightly differently, try to catch it
  content = content.replace(
    /<a href="index\.html" style="display: inline-block; margin-bottom: 20px;">/g,
    '<a href="index.html" style="display: block; margin-bottom: 5px;">'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Fixed footer logo alignment in ' + f);
  }
});
