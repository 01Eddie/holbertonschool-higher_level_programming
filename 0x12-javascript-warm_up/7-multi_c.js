#!/usr/bin/node
const { argv } = require('process');

const arr = 'C is fun';

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < parseInt(argv[2]); index++) {
    console.log(arr);
  }
}
