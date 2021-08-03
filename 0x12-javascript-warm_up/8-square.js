#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let x = 0; x < parseInt(argv[2]); x++) {
        console.log('X'.repeat(x));
  }
}
