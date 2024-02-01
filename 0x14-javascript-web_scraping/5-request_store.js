#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      fs.writeFile(filePath, body, 'utf-8', (writeError) => {
        if (writeError) {
          console.error(writeError);
        }
      });
    } else {
      console.log(`Error: Unable to fetch the webpage. Status code: ${response.statusCode}`);
    }
  }
});
