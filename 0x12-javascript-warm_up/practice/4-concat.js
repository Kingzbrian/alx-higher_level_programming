#!/usr/bin/node
const firstArg = process.argv[2];
const secondArg = process.argv[3];
if (firstArg === undefined) {
  console.log('undefined is undefined');
} else if (firstArg === process.argv[2] && secondArg === undefined) {
  console.log(firstArg + ' ' + 'is' + ' ' + 'undefined');
} else {
  console.log(firstArg + ' ' + 'is' + ' ' + secondArg);
}
