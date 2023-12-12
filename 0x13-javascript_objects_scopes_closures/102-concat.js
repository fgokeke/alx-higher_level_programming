#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 5) {
  console.error('Usage: ./concat_files.js <file1> <file2> <destination>');
  process.exit(1);
}

const file1Path = process.argv[2];
const file2Path = process.argv[3];
const destinationPath = process.argv[4];

const file1Content = fs.readFileSync(file1Path, 'utf-8');

const file2Content = fs.readFileSync(file2Path, 'utf-8');

const concatenatedContent = file1Content + file2Content;

fs.writeFileSync(destinationPath, concatenatedContent, 'utf-8');
