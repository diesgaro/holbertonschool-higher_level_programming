#!/usr/bin/node
/*
    Make a request and store values in object
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
    const newObj = {};

    for (let i = 0; i < obj.length; i++) {
      if (!newObj[obj[i].userId]) {
        newObj[obj[i].userId] = 0;
      }

      if (obj[i].completed) {
        newObj[obj[i].userId] = newObj[obj[i].userId] + 1;
      }
    }
    console.log(newObj);
  }
});
