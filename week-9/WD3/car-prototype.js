'use strict';

function Car2(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
}

Car2.prototype.ride = function(km) {
    this.km += km;
}


var trabant = new Car2('zold', 'Trabant', 400);

trabant.ride(0.02);
console.log(trabant.km);
