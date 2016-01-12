'use strict';

var numbers = [5, 6, 3, 9];

var sum = numbers.reduce(function(acc, num) {
  return acc + num;
}, 0); // a nulla itt az acc(umulator) kezdeti értékét határozza meg

console.log(sum);
