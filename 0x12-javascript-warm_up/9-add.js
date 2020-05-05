#!/usr/bin/node
const numberA = process.argv[2];
const numberB = process.argv[3];

console.log(add(numberA, numberB));

function add (a, b) {
  return parseInt(a) + parseInt(b);
}
