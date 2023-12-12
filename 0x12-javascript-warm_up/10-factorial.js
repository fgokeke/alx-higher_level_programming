#!/usr/bin/node

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }

  number = Number(number);

  if (number === 0 || number === 1) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

const num = (process.argv[2]);

console.log(factorial(num));
