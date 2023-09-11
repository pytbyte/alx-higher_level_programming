#!/usr/bin/node
const [, , firstArgument] = process.argv;

if (firstArgument !== undefined) {
  console.log(firstArgument);
} else {
  console.log('No argument');
}
