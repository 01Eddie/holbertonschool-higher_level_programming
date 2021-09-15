#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

/**
 * Write a script that computes the number of tasks completed by user id.
 *
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed task
 * You must use the module request
 */

request(argv[2], (err, res, body) => {
  if (err) console.log(err);
  else {
    const taskByUsers = {};
    body = JSON.parse(body);
    for (let i = 0; i < body.length; i++) {
      const IDuser = body[i].userId;
      const complete = body[i].completed;

      if (complete && !taskByUsers[IDuser]) taskByUsers[IDuser] = 0;
      if (complete) taskByUsers[IDuser]++;
    }
    console.log(taskByUsers);
  }
});
