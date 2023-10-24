#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <id>');
  process.exit(1);
}

const movieId = process.argv[2];
const APIurl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(APIurl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
