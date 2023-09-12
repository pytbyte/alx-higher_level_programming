#!/usr/bin/node
const Sqr = require('./5-square');
class Square extends Sqr {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    // Check if c is undefined and set it to 'X' by default
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
