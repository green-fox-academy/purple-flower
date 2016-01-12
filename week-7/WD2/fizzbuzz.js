'use strict';

for ( var a = 0; a <= 100; a++) {
  if (a % 15 === 0) {
    console.log('fizzbuzz');
  } else if (a % 3 === 0) {
    console.log('fizz');
  } else if (a % 5 === 0) {
    console.log('buzz');
  } else {
    console.log(a);
  }
}
