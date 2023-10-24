#!/usr/bin/node
const request = require('request');

function countCompletedTasks (apiUrl) {
  request(apiUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    } else if (response.statusCode !== 200) {
      console.error(`Error: ${response.statusCode}`);
    } else {
      const todos = JSON.parse(body);
      const completedTasks = {};

      todos.forEach((task) => {
        if (task.completed) {
          completedTasks[task.userId] = (completedTasks[task.userId] || 0) + 1;
        }
      });

      console.log(completedTasks);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

const apiUrl = process.argv[2];
countCompletedTasks(apiUrl);
