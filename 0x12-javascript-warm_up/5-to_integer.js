#!/usr/bin/node
const { argv} = require('process');

/**
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found” */

if (isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(argv[2]));
}
