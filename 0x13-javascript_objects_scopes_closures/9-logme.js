#!/usr/bin/node

let noArguments = 0;

exports.logMe = function (item) {
  console.log(`${noArguments}: ${item}`);
  noArguments++;
};
