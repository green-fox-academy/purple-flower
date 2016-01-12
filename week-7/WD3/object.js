'use strict';

var humwee = {
  type: 'Render katonai Hummer',
  color: 'Terep',
  km: 20000,
  ride: function(km) {
    this.km += km;
  }
};

humwee.ride(200);

console.log(humwee.km);
