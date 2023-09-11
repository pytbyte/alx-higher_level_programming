#!/usr/bin/node

function factorial (n) {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result *= i;
  }
  return result;
}

const input = parseInt(process.argv[2]);

if (isNaN(input) || input < 0) {
  console.log(1);
} else {
  const answer = factorial(input);
  console.log(answer);
}
