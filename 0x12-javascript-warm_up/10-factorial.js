#!/usr/bin/node

const { argv } = require('process');

/**
 * factorial - function of factorial
 * a: argv[2]
 * return: a */

function factorial (a) {
  if (isNaN(a)) {
    return 1;
  }
  if (a === 0) {
    return 1;
  }
  return a * factorial(a - 1);
}
console.log(factorial(parseInt(argv[2])));
