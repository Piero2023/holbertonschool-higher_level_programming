#!/usr/bin/node
/* a script that computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (body === undefined) {
    console.error('error:', error);
  } else {
    /* json to a javascript object */
    const tojavasobj = JSON.parse(body);
    const complete = {};

    for (const task of tojavasobj) {
      if (task.completed === true) {
        if (complete[task.userId]) {
          complete[task.userId]++;
        } else {
          complete[task.userId] = 1;
        }
      }
    }
    console.log(complete);
  }
}
);
