'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

function getAgeByName(kids, name) {
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].name === name) {
      return kids[i].age;
    }
  }
}


function getAgeByName2 (kids, name) {
  var output_age = 0;
  kids.forEach(function(kid) {
    kid.age = output_age
  });
  return output_age
}


console.log(getAgeByName(kids, 'Gerda')); // 9
console.log(getAgeByName(kids, 'Zsolti')); // 9
