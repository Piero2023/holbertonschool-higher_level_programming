#!/usr/bin/node

const fs = require('fs');
const request = require('request'); // Import the request module to make HTTP requests

const url = process.argv[2]; // The URL to request, passed as the first command line argument
const File = process.argv[3]; // The name of the file to write, passed as the second command line argument

request.get(url).pipe(fs.createWriteStream(File, 'utf-8'));
