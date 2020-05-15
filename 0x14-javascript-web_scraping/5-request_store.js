#!/usr/bin/node
/*
    Make a request and print the result
*/
const request = require('request');
const fs = require('fs');
const args = process.argv;

const url = args[2];
const fileStream = fs.createWriteStream(args[3]);

request(url).pipe(fileStream);
