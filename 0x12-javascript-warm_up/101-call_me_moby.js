#!/usr/bin/node

function callFunctionNTimes (n, func) {
  for (let i = 0; i < n; i++) {
    func();
  }
}

module.exports = { callFunctionNTimes };
