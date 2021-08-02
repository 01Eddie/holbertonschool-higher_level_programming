#!/usr/bin/node
const { argv } = require('process');

/**
 * If no arguments are passed to the script, print “No argument”
 * If only one argument is passed to the script, print “Argument found”
 * Otherwise, print “Arguments found” */
const ar = argv.length;
if (ar > 3) {
  console.log('Arguments found');
} else if (ar === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
