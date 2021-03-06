#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const fs = require('fs/promises');

/**
 * Write a script that gets the contents of a webpage and stores it in a file.
 *
 * The first argument is the URL to request
 * The second argument the file path to store the body response
 * The file must be UTF-8 encoded
 * You must use the module request
 */

const arLink = argv[2];
const arText = argv[3];

request(arLink, (err, res, body) => {
  !err ? fs.writeFile(arText, body, 'utf8', (_err) => {}) : console.log(err);
});
