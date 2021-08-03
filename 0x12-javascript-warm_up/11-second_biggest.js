#!/usr/bin/node

const { argv } = require('process');

if (argv.length > 3) {
  argv.sort();
  console.log(argv[argv.length - 2]);
} else {
  console.log(0);
}
