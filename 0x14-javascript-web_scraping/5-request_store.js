#!/usr/bin/node
const fs = require('fs');
const request = require('request');

function downloadFile(url, filePath) {
  const fileStream = fs.createWriteStream(filePath);

  request(url)
    .on('error', (error) => {
      console.error(error);
    })
    .pipe(fileStream);
}

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file-path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

downloadFile(url, filePath);
