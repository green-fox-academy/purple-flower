'use strict';

var kids = [
  {name: 'Tibbor', candies: 2},
  {name: 'Steve', candies: 3},
  {name: 'Agoston', candies: 0},
  {name: 'Julika', candies: 7},
  {name: 'Krisztian', candies: 4}
];

function getTheRichestKidsName(kids) {
  var richestKid = kids[0];
  for (var i = 0; i < kids.length; i++) {
    if (kids[i].candies > richestKid.candies) {
      richestKid = kids[i];
    }
  }
  return richestKid.name;
}

console.log(getTheRichestKidsName(kids));


// 2nd solution
function getTheRichestKidsName2(kids) {
  var richestKid = kids[0];
  kids.forEach(function(currentKid) {
    if (currentKid.candies > richestKid.candies) {
      richestKid = currentKid;
    }
  });
  return richestKid.name;
}

console.log(getTheRichestKidsName2(kids));
