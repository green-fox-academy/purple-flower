'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'},
];

console.log(groupBySex(kids));

function groupBySex(kids) {
  var output = {female: [], male: []};

  kids.forEach(function(currentKid) {
    if (currentKid.sex === 'female') {
      output.female.push(currentKid);
    } else if (currentKid.sex === 'male') {
      output.male.push(currentKid);
    }
  })
  return output
}
