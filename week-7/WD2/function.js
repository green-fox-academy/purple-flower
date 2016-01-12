'use strict';

function greet(name) {
  console.log('Hi ' + name + '!');
}

greet('Lilla');


function add(a, b) {
  return a + b;
}

console.log(add(1, 2));


var osszead = add;
console.log(osszead(4, 5));

var szoroz = function multiply(a, b) {
  return a * b;
};

console.log(szoroz(4,5));
