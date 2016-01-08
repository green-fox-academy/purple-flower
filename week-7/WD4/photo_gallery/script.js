'use strict';

var images = [
  'images/1.jpg',
  'images/2.jpg',
  'images/3.jpg',
  'images/4.jpg',
  'images/5.jpg',
  'images/6.jpg',
  'images/7.jpg',
  'images/8.jpg',
  'images/9.jpg',
  'images/10.jpg'
];


var currentPosition = 0;

var nextButton = document.querySelector('.image-navigate-next');
var previousButton = document.querySelector('.image-navigate-back');
var bigImage = document.querySelector('.big-image');
var smallImageBox = document.querySelector('.thumb-box');

smallImagesCreator();
var first = document.getElementById('pic0');
first.classList.add('active');
var actives = smallImageBox.querySelectorAll('active');


nextButton.addEventListener('click', function() {
  moveToNextPicture();
})

previousButton.addEventListener('click', function() {
  moveToPreviousPicture();
})


function moveToNextPicture() {
  if (currentPosition === images.length-1) {
    currentPosition = 0;
    showBigPicture(images[currentPosition]);
  } else {
    showBigPicture(images[++currentPosition]);
  }
  actives = smallImageBox.querySelectorAll('.active');
  console.log(actives);
  for (var i = 0; i < actives.length; i++) {
    actives[i].classList.remove('active');
  }
  document.getElementById('pic' + currentPosition).classList.add('active');
}

function moveToPreviousPicture() {
  if (currentPosition === 0) {
    currentPosition = images.length -1;
    showBigPicture(images[currentPosition])
  } else {
    showBigPicture(images[--currentPosition]);
  }
  actives = smallImageBox.querySelectorAll('.active');
  console.log(actives);
  for (var i = 0; i < actives.length; i++) {
    actives[i].classList.remove('active');
  }
  document.getElementById('pic' + currentPosition).classList.add('active');
}

function showBigPicture (src) {
  bigImage.setAttribute('src', src)
}


function smallImagesCreator () {
  for (var i = 0; i < images.length; i++) {
    var smallImage = document.createElement('img');
    smallImage.setAttribute('id', 'pic' + i);
    smallImage.setAttribute('src', images[i]);
    smallImageBox.appendChild(smallImage);
  };
}


smallImageBox.addEventListener('click', function(event) {
  var smallImageSrc = event.target.getAttribute('src')
  showBigPicture(smallImageSrc);
  currentPosition = images.indexOf(smallImageSrc);
  actives = smallImageBox.querySelectorAll('.active');
  console.log(actives);
  for (var i = 0; i < actives.length; i++) {
    actives[i].classList.remove('active');
  }
  event.target.classList.add('active');
});
