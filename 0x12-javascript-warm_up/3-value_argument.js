#!/usr/bin/node
const arg = process.argv[2];
let message;
if (arg) {
  message = arg;
} else {
  message = 'No argument';
}
console.log(message);
