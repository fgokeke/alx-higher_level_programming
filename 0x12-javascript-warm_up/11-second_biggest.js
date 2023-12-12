#!/usr/bin/node

function findSecondLargest (args) {
  const integers = args.map(Number);

  if (integers.length < 2) {
    return 0;
  }

  let largest = Number.MIN_SAFE_INTEGER;
  let secondLargest = Number.MIN_SAFE_INTEGER;

  for (const num of integers) {
    if (num > largest) {
      secondLargest = largest;
      largest = num;
    } else if (num > secondLargest && num < largest) {
      secondLargest = num;
    }
  }
  return secondLargest;
}

const args = process.argv.slice(2);

console.log(findSecondLargest(args));
