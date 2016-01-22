'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function filterNamesBySex(kids, sex) {
  var output_array = [];
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].sex === sex) {
      output_array.push(kids[i].name);
    }
  }
  return output_array;
}

console.log(filterNamesBySex(kids, 'female')); // ['Julika', 'Gerda']
