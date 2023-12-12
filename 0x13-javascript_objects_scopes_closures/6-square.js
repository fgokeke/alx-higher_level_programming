#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let i;
      const row = c.repeat(this.width);
      for (i = 0; i < this.height; i++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
