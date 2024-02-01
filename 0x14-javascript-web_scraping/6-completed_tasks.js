#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const todosData = JSON.parse(body);
      const completedTasksByUser = {};

      todosData.forEach(todo => {
        if (todo.completed) {
          if (completedTasksByUser[todo.userId]) {
            completedTasksByUser[todo.userId]++;
          } else {
            completedTasksByUser[todo.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.log(`Error: Unable to fetch todos data. Status code: ${response.statusCode}`);
    }
  }
});
