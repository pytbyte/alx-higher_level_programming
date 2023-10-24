#!/usr/bin/node
const request = require('request');

function fetchFilmCharacters (movieId) {
  const filmUrl = `https://swapi-api.hbtn.io/api/films/${movieId}`;

  request(filmUrl, (error, response, filmBody) => {
    if (!error && response.statusCode === 200) {
      const characters = JSON.parse(filmBody).characters;
      printCharacters(characters, 0);
    }
  });
}

function printCharacters (characters, index) {
  if (index < characters.length) {
    const characterUrl = characters[index];
    request(characterUrl, (error, response, characterBody) => {
      if (!error && response.statusCode === 200) {
        const characterData = JSON.parse(characterBody);
        console.log(characterData.name);
        printCharacters(characters, index + 1);
      }
    });
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: ./script.js <Movie-ID>');
  process.exit(1);
}

const movieId = process.argv[2];
fetchFilmCharacters(movieId);
