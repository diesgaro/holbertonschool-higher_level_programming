#!/usr/bin/node
/*
Define Class Square extends Rectangle
*/

const rectangle = require('./4-rectangle');

class Square extends rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    const character = typeof (c) === 'undefined' ? 'X' : c;

    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
