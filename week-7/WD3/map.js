'use strict';

var benaszavak = [
  'kuty',
  'macsk',
  'alm',
  'kacs'
];

var faszaSzavak = [];

for (var i = 0; i < benaszavak.length; i++) {
  faszaSzavak.push(benaszavak[i] + 'a');
}

console.log(faszaSzavak);


//2nd solution
var faszaSzavak2 = [];

benaszavak.forEach(function(szo) {
  faszaSzavak2.push(szo + 'a');
});

console.log(faszaSzavak2);


//3rd solution
var faszaSzavak3 = benaszavak.map(function(szo) {
  return szo + 'a';
});

console.log(faszaSzavak3);
