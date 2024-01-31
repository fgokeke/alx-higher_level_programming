#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const filmsData = JSON.parse(body).results;
      const moviesWithWedgeAntilles = filmsData.filter(movie => movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));
      console.log(`${moviesWithWedgeAntilles.length}`);
    } else {
      console.log(`Error: Unable to fetch films data. Status code: ${response.statusCode}`);
    }
  }
});
