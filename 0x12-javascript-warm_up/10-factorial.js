#!/usr/bin/node
const number = process.argv[2];

console.log(factorial(parseInt(number)));

function factorial (a) {
  if (isNaN(a) || !a) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
