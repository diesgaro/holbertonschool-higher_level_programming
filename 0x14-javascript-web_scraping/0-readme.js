#!/usr/bin/node
/*
    Read and print content file
*/
const fs = require('fs');
const args = process.argv;

fs.readFile(args[2], 'utf-8', (err, data) => {
  if (data) {
    console.log(data);
  } else {
    console.error(err);
  }
});
