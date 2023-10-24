#!/usr/bin/node
const queried_data= require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js url');
  process.exit(1);
}

const url = process.argv[2];

queried_data(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});