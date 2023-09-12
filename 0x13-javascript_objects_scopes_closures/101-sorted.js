#!/usr/bin/node
const { dict } = require('./101-data');

const occurrencesById = {};

for (const userId in dict) {
  const occurrences = dict[userId];
  occurrencesById[occurrences] = occurrencesById[occurrences] || [];
  occurrencesById[occurrences].push(userId);
}

console.log(occurrencesById);
