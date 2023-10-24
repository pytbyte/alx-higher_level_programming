#!/usr/bin/node
const fs = require('fs');

const main = () => {
  const args = process.argv.slice(2);

  if (args.length !== 2) {
    console.error('Usage: node 1-writeme.js <file-path> "content"');
    process.exit(1);
  }

  const [filePath, contentToWrite] = args;

  fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
};

main();
