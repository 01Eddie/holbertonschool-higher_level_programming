#!/usr/bin/node
const { argv} = require('process');

/**
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found” */

if (argv[2]) {
  console.log(argv[2]);
} else if (argv[1]) {
  console.log('No argument');
}
