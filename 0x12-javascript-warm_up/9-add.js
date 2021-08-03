#!/usr/bin/node

/**
 * add - function of addition
 * a: argv[2]
 * b: argv[3]
 * return: a + b */

function add (a, b) {
  return a + b;
}

const { argv } = require('process');
console.log(add(parseInt(argv[2]), parseInt(argv[3])));
