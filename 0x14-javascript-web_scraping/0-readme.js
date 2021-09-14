#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
/**
 * Write a script that reads and prints the content of a file.

 * The first argument is the file path
* The content of the file must be read in utf-8
 * If an error occurred during the reading, print the error object
 */
const ar = argv[2];
fs.readFile(ar, 'utf8', (err, data) => {
  console.log(err || data); // log(err ? err : data) == es lo mismo solo que genera error en semistandard Unnecessary use of conditional expression for default assignment.
});
