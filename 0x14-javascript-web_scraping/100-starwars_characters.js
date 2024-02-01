#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      const characters = movieData.characters;

      characters.forEach(characterUrl => {
        request(characterUrl, (characterError, characterResponse, characterBody) => {
          if (characterError) {
            console.error(characterError);
          } else {
            if (characterResponse.statusCode === 200) {
              const characterData = JSON.parse(characterBody);
              console.log(characterData.name);
            } else {
              console.log(`Error: Unable to fetch character data. Status code: ${characterResponse.statusCode}`);
            }
          }
        });
      });
    } else {
      console.log(`Error: Unable to fetch movie data. Status code: ${response.statusCode}`);
    }
  }
});
