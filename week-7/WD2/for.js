'use strict';

for (var i = 0; i < 5; i++) {
  console.log(i);
}


var dogs = ['kecske', 'morzsi', 'subidubi'];

for (var i = 0; i < dogs.length; i++) {
  console.log(dogs[i]);
}


var student = {
  kor: 6,
  nev:'tibi',
  labmeret: 45
};

for (var key in student) {
  console.log(key);
  console.log(student[key]);
}
