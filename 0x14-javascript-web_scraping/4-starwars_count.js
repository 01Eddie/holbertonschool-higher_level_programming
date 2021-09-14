#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const link = argv[2];

/**
 * Write a script that prints the number of movies where the character “Wedge Antilles” is present.
 *
 * The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
 * Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
 * You must use the module request
 */

request(link, (err, res, body) => {
  if (err) console.log(err);
  let count = 0;
  const resultFilms = JSON.parse(body).results;
  for (let i = 0; i < resultFilms.length; i++) {
    const chars = resultFilms[i].characters;
    for (let j = 0; j < chars.length; j++) {
      const character = chars[j];
      const IDcharacter = character.split('/')[5];
      if (IDcharacter === '18') count++;
    }
  }
  console.log(count);
});
