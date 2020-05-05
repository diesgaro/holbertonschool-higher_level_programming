#!/usr/bin/node
const myNumber = process.argv[2];
let message;
if (isNaN(myNumber)) {
  message = 'Not a number';
} else {
  message = 'My number: ' + parseInt(myNumber);
}
console.log(message);
