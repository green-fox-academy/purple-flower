'use strict';

function PowerRangers(color) {
  this.color = color;
}


function Fighter() {
  this.isPowerfull = true;
}

PowerRangers.prototype = new Fighter();

var yellowRanger = new PowerRangers('yellow');

console.log(yellowRanger.color);
console.log(yellowRanger.isPowerfull);
