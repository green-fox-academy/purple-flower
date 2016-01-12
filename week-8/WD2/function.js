'use strict';

// 1
// var button = document.querySelector('button');
//
// button.addEventListener('click', shout);
//
// function shout() {
//   console.log('AJAJAJAJ');
//   console.log('AJAJAJAJ');
//   console.log('AJAJAJAJ');
// }

// 2
var human = {
  word: ['kacsa', 'macska', 'mamlasz'],
  name: 'Tibbor',
  speak: speak
};

function speak() {
  for (var i = 0; i < this.word.length; i++) {
    console.log('I am ' + this.name);
    console.log('bla bla bla' + this.word[i]);
  }
}

human.speak();

// 3
var human = {
  word: ['kacsa', 'macska', 'mamlasz'],
  name: 'Tibbor',
  speak: speak
};

function speak() {
  var _this = this
  this.word.forEach(function(w) {
    console.log('I am ' + _this.name);
    console.log('bla bla bla' + w);
  });
}

human.speak();
