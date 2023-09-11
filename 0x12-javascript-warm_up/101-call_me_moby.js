#!/usr/bin/node

const callMeMoby = (x, theFunction) => {
    Array.from({ length: x }).forEach(() => theFunction());
  };
  
  module.exports = { callMeMoby };
  