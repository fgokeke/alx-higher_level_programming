#!/usr/bin/node

const num = Number(process.argv[2]);

if (!isNaN(num)) {
  console.log('My number:', Math.floor(num));
} else {
  console.log('Not a number');
}
