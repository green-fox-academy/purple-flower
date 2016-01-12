'use strict';

function sumOfNumberList(array) {
  var sum = 0;
  for (var i = 0; i < array.length; i++) {
    sum += array[i];
  }
  return sum;
}


console.log(sumOfNumberList([1, 2, 3]))
