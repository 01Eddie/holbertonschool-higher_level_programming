#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const link = `https://swapi-api.hbtn.io/api/films/${argv[2]}`;

/**
 * Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
 *
 * The first argument is the movie ID
 * You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
 * You must use the module request
 */

request(link, (err, res, body) => console.log(err || JSON.parse(body).title));
