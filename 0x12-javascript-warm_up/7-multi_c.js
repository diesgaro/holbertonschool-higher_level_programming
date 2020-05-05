#!/usr/bin/node
const myNumber = process.argv[2];
let i = 0;

if (isNaN(myNumber)) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(myNumber)) {
    console.log('C is fun');
    i++;
  }
}
