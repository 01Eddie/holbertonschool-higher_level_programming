#!/usr/bin/node

const { argv } = require('process');
let next = 0;

if (argv.length > 3) {
  argv.sort();
  next = argv[argv.length - 2];
  console.log(next);
} else {
  console.log(0);
}
