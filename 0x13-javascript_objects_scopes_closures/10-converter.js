#!/usr/bin/node

exports.converter = function (base) {
  if (base <= 1 || isNaN(base)) {
    return;
  }

  const digits = '0123456789abcdefghijklmnopqrstuvwxyz';
  return function convert (number) {
    if (number < base) {
      return digits[number];
    } else {
      return convert(Math.floor(number / base)) + digits[number % base];
    }
  };
};
