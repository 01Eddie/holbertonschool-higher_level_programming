#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

/**
 * Write a script that writes a string to a file.
 *
 * The first argument is the file path
 * The second argument is the string to write
 * The content of the file must be written in utf-8
 * If an error occurred during while writing, print the error object
 */
const arFile = argv[2];
const arText = argv[3];
fs.writeFile(arFile, arText, 'utf8', (err) => {
    if (err) console.log(err);
});
