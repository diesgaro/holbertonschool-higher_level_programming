#!/usr/bin/node
/*
    Make a request and print the result
*/
const request = require('request');

request(process.argv[2], (err, res, body) => {
  let count = 0;
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    for (let i = 0; i < obj.count; i++) {
      for (let j = 0; j < obj.results[i].characters.length; j++) {
        if (obj.results[i].characters[j].endsWith('/18/')) {
          count++;
        }
      }
    }
  }
  console.log(count);
});
