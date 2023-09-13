#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Tumia: ./script.js chanzo1.txt chanzo2.txt marudio.txt');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

try {
  const data1 = fs.readFileSync(sourceFilePath1, 'utf8');
  const data2 = fs.readFileSync(sourceFilePath2, 'utf8');
  fs.writeFileSync(destinationFilePath, data1 + data2);
  console.log('Faili zimeunganishwa kwa mafanikio kwenye faili ya marudio.');
} catch (error) {
  console.error('Kosa:', error.message);
}
