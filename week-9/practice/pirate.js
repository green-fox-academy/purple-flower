'use strict';

var pirates = [
  {name: 'Jack', id: 1},
  {name: 'Bob', id: 2},
  {name: 'Omar', id: 3},
  {name: 'Olaf', id: 4},
  {name: 'Boris', id: 5}
];

var stashes = [
  {pirateId: 3, gold: 4},
  {pirateId: 4, gold: 1},
  {pirateId: 2, gold: 5},
  {pirateId: 5, gold: 3},
  {pirateId: 1, gold: 8}
];

function getGoldByPirateName(name) {
  var pirateId;
  for (var i = 0; i < pirates.length; i++) {
    if (pirates[i].name === name) {
      pirateId = pirates[i].id;
    }
  }
  for (var i = 0; i < stashes.length; i++) {
    if (stashes[i].pirateId === pirateId) {
      return stashes[i].gold;
    }
  }
}


console.log(getGoldByPirateName('Olaf')); // -> 1
