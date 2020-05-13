#!/usr/bin/node
/*
    Make a request and print the result
*/
const request = require('request');
const args = process.argv;

const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + args[2],
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
    console.log(JSON.parse(body).title);
  }
});
