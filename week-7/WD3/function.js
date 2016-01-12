'use strict';

function add(a, b) {
  return a + b;
}

console.log(add(1, 2));

// a köv. ugyanaz:

var add = function (a, b) { return a + b; };
console.log(add(1, 2));
