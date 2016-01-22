'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function getAges(kids) {
  var array = [];
  kids.forEach(function(kid) {
    array.push(kid.age);
  });
  return array;
}

console.log(getAges(kids)); // [8, 7, 6, 9, 8]
