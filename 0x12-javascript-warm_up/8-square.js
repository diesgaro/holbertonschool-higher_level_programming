#!/usr/bin/node
const myNumber = process.argv[2];
let i = 0;
let combineX = '';
let j = 0;

if (isNaN(myNumber)) {
  console.log('Missing size');
} else {
  while (j < parseInt(myNumber)) {
    combineX += 'X';
    j++;
  }

  while (i < parseInt(myNumber)) {
    console.log(combineX);
    i++;
  }
}
