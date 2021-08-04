#!/usr/bin/node

/* Write a function that prints the number of arguments already printed and the new argument value. (see example below)

Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value> */

exports.logMe = function (item) {
  if (!this.argsCount) {
    this.argsCount = 0;
  }

  console.log(`${this.argsCount++}: ${item}`);
};
