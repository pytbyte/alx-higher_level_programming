#!/usr/bin/node

const userInput = process.argv[2];

if (isNaN(userInput)) {
  console.log('Not a number');
} else {
  const parsedNumber = parseInt(userInput);
  console.log('My number:', parsedNumber);
}
