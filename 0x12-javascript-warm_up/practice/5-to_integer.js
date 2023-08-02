#!/usr/bin/node
const firstArgs = parseInt(process.argv[2]);
if (isNaN(firstArgs)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstArgs);
}
