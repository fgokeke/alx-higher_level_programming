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
      let moviesWithWedgeAntilles = 0;
      for (const filmIdx in filmsData) {
        const filmChars = filmsData[filmIdx].characters;
        for (const charIndex in filmChars) {
          if (filmChars[charIndex].includes(`${characterId}`)) {
            moviesWithWedgeAntilles++;
          }
        }
      }
      console.log(`${moviesWithWedgeAntilles}`);
    } else {
      console.log(`Error: Unable to fetch films data. Status code: ${response.statusCode}`);
    }
  }
});
