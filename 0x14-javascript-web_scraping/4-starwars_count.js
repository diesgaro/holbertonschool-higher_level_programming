#!/usr/bin/node
/*
    Make a request and print the result
*/
const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET',
  headers: {
    'Accept-Charset': 'utf-8',
    'User-Agent': 'Holberton-1265'
  }
};

request(options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const obj = JSON.parse(body);
    let count = 0;
    for (let i = 0; i < obj.count; i++) {
      for (let j = 0; j < obj.results[i].characters.length; j++) {
        const strFind = obj.results[i].characters[j].search('/18/');
        if (strFind !== -1) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
