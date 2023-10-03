#!/usr/bin/node
const myVal = parseInt(process.argv[2]);
if (isNaN(myVal)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myVal; i++) {
    let row = '';
    for (let j = 0; j < myVal; j++) {
      row += 'x';
    }
    console.log(row);
  }
}
