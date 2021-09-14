#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

/**
 * Write a script that display the status code of a GET request.
 *
 * The first argument is the URL to request (GET)
 * The status code must be printed like this: code: <status code>
 * You must use the module request
 */

const arLink = argv[2];
request(arLink, (err, res) => console.log(err || 'code: ' + res.statusCode));
