#!/usr/bin/node
const request = require('request'); // Import the request module to make HTTP requests

const url = process.argv[2]; // The URL to request, passed as the first command line argument

// Make an HTTP GET request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`); // Print the status code of the response
  }
});
