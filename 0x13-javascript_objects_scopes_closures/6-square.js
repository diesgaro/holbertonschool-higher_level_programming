#!/usr/bin/node
/*
Define Class Square extends Square
*/

const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
