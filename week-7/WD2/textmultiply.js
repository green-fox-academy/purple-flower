'use strict';

function textMultiply(string, number) {
  var output = '';
  for (var i = 0; i < number; i++) {
    output += string;
  }
  return output;

function textMultiply(text, number) {
  return number > 0 ? text + textMultiply(text, number -1) : '';
}

console.log(textMultiply('alma', 4));
