#!/usr/bin/node
const args = process.argv;

if (args.length <= 3) {
  console.log(0);
} else {
  console.log(getSecondBig(args));
}

function getSecondBig (args) {
  let i = 2;
  const array = [];
  while (i < args.length) {
    array.push(parseInt(args[i]));
    i++;
  }
  return (array.sort(function (a, b) { return a - b; })[array.length - 2]);
}
