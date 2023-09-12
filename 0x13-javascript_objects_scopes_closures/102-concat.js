#!/usr/bin/node
const fs = require('fs');

// Njia za faili za chanzo na marudio
const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const data1 = fs.readFileSync(sourceFilePath1, 'utf8');
const data2 = fs.readFileSync(sourceFilePath2, 'utf8');

const concatenatedData = data1 + data2;

fs.writeFileSync(destinationFilePath, concatenatedData);

console.log('Faili zimeunganishwa kwa mafanikio kwenye faili ya marudio.');
