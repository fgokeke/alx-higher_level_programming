#!/usr/bin/node

const num = Number(process.argv[2]);

let i, j, row;

if (!isNaN(num)) {
  for (i = 0; i < num; i++) {
    row = '';
    for (j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
