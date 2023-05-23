#!/usr/bin/node

const fs = require('fs');

// Check if the user provided the correct number of arguments
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

// Read the contents of the first file
fs.readFile(fileA, 'utf8', (err1, data1) => {
  if (err1) {
    console.error(err1);
    process.exit(1);
  }

  // Read the contents of the second file
  fs.readFile(fileB, 'utf8', (err2, data2) => {
    if (err2) {
      console.error(err2);
      process.exit(1);
    }

    // Concatenate the contents of the two files
    const result = data1 + data2;

    // Write the result to the destination file
    fs.writeFile(fileC, result, (err3) => {
      if (err3) {
        console.error(err3);
        process.exit(1);
      }

      // console.log(`Concatenated ${fileA} and ${fileB} to ${fileC}`);
    });
  });
});
