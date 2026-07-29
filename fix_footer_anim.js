const fs = require('fs');

const files = fs.readdirSync('.').filter(f => f.endsWith('.html'));

files.forEach(f => {
  let content = fs.readFileSync(f, 'utf8');
  let before = content;

  // Replace 2500 + to 1500 +
  content = content.replace(
    /2500 \+ \(index \* 200\)/g,
    '1500 + (index * 200)'
  );
  
  // Replace the comment if necessary
  content = content.replace(
    /2\.5 seconds base delay \(2500ms\)/g,
    '1.5 seconds base delay (1500ms)'
  );

  if (content !== before) {
    fs.writeFileSync(f, content, 'utf8');
    console.log('Reduced animation delay in ' + f);
  }
});
