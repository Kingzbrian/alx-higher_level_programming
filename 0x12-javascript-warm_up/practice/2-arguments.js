#!/usr/bin/node
const lent = process.argv.length;
if (lent === 2) {
  console.log('No argument');
} else if (lent === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
