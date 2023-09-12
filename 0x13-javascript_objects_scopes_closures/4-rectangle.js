#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    if (this.width !== undefined && this.height !== undefined) {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    }
  }

  rotate () {
    if (this.width !== undefined && this.height !== undefined) {
      // Exchange the width and height of the rectangle
      [this.width, this.height] = [this.height, this.width];
    }
  }

  double () {
    if (this.width !== undefined && this.height !== undefined) {
      // Double the width and height of the rectangle
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
