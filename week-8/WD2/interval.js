'use strict';

var count = 0;

var interval = setInterval(function() {
  count++; //printelést számolja fél mp-ként
  console.log('Je-je-je-je', count);
}, 500);

setTimeout(function() {
  console.log('BOOOM');
  clearInterval(interval);
}, 5000);

setTimeout(function() {
  for (var i = 0; i < 200000; i++) {
    console.log(i);
  }
}, 2000)
