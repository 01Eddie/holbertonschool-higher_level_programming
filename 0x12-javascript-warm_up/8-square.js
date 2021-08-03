#!/usr/bin/node

const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const drawX = 'X';
  for (let x = 0; x < parseInt(argv[2]); x++) {
    console.log(`${drawX}`.repeat(parseInt(argv[2])));
  }
}
