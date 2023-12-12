#!/usr/bin/node

exports.converter = function (base) {
  if (base <= 1 || isNaN(base)) {
    return;
  }

  return function convert (number) {
    if (number < base) {
      return '0123456789abcdefghijklmnopqrstuvwxyz'[number];
    } else {
      return convert(Math.floor(number / base)) + '0123456789abcdefghijklmnopqrstuvwxyz'[number % base];
    }
  };
};
