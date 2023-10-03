#!/usr/bin/node
const a = parseInt(process.argv[2]);

function factorial (b) {
  if (isNaN(b) || b == 0) {
    return (1);
  } else {
    return (b * factorial(b - 1));
  }
}
console.log(factorial(a));
