'use strict';

var createCandiesButton = document.querySelector('.create-candies');
var buyLollipopsButton = document.querySelector('.buy-lollipops');
var candiesStatus = document.querySelector('.candies');
var lollipopsStatus = document.querySelector('.lollipops');
var candyCreationCapacityStatus = document.querySelector('.speed');
var candiesAmount = 0;
var lollipopsAmount = 0;
var candyCreationCapacityPerS = 0;

setInterval(createCandyEverySec, 1000);

function createCandyEverySec() {
  candiesAmount += candyCreationCapacityPerS;
  updateCandiesStatus();
  enableLollipopButton();
}

createCandiesButton.addEventListener('click', createCandy);

function createCandy() {
  candiesAmount++;
  updateCandiesStatus();
  enableLollipopButton();
}

function updateCandiesStatus() {
  candiesStatus.innerText = candiesAmount;
}

buyLollipopsButton.addEventListener('click', buyLollipop);

function enableLollipopButton() {
  if (candiesAmount >= 10) {
    buyLollipopsButton.removeAttribute('disabled');
  } else {
    buyLollipopsButton.setAttribute('disabled', '');
  }
}

function buyLollipop() {
  if (candiesAmount >= 10) {
    useCandies();
    lollipopsAmount++;
    updateLollipopsStatus();
    setCandiesCreatedPerS();
  } else {
    alert('You do not have enough candies to buy a lollipop!')
  }
}

function updateLollipopsStatus() {
  lollipopsStatus.innerText = lollipopsAmount;
}

function useCandies() {
  candiesAmount -= 10;
  updateCandiesStatus();
  enableLollipopButton();
}

function setCandiesCreatedPerS() {
  var lollipopPerTen = Math.floor(lollipopsAmount/10);
  if (lollipopPerTen >= 1) {
    candyCreationCapacityPerS = lollipopPerTen;
    updateCandyCreationCapacityStatus();
  }
}

function updateCandyCreationCapacityStatus() {
  candyCreationCapacityStatus.innerText = candyCreationCapacityPerS;
}
