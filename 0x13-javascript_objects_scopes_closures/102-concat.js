#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Tumia: ./script.js chanzo1.txt chanzo2.txt marudio.txt');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

fs.readFile(sourceFilePath1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Kosa kusoma faili ya chanzo cha kwanza: ${err.message}`);
    process.exit(1);
  }

  fs.readFile(sourceFilePath2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Kosa kusoma faili ya chanzo cha pili: ${err.message}`);
      process.exit(1);
    }

    const concatenatedData = data1 + data2;
    fs.writeFile(destinationFilePath, concatenatedData, (err) => {
      if (err) {
        console.error(`Kosa kuandika kwenye faili ya marudio: ${err.message}`);
        process.exit(1);
      }
      console.log('Faili zimeunganishwa kwa mafanikio kwenye faili ya marudio.');
    });
  });
});
