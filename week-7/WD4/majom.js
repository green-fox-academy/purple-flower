'use strict';

console.log('mukodik')

var cim = document.querySelector('.majom');
console.log(cim);

// cim.style.backgroundColor = 'pink';
cim.classList.add('piros');

// var majomKep = document.querySelector('img');
//
// majomKep.setAttribute('src', 'https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg');

var bodyvaltozoban = document.querySelector('body');

function kepcsinalo(src) {
  var ujkep = document.createElement('img');

  ujkep.setAttribute('src', src);

  bodyvaltozoban.appendChild(ujkep);
}


// for (var i = 0; i < 10; i++) {
//   kepcsinalo('http://www.kepeslap.com/images/11653/virag_25.jpg');
// }

var kepek = ['http://rewrite.origos.hu/s/img/i/1301/20130124-torpe-lajharmaki-szegedi-vadasparkban-20124.jpg',
'http://www.centrofeldenkraiscsm.it/problematiche/images/sport.jpg',
'http://img.hdwallpaperpc.com/cover/117/Nature_Lake_splendor_autumn_colors_leaves_beautiful_beauty_Clouds_colorful_fall_grass_Green_house_houses_lake_La_116539_detail_thumb.jpg',
'http://feelgrafix.com/data_images/out/28/969813-apple.jpg',
'http://lemon.hu/wp-content/uploads/2015/06/mars_2445397b.jpg'];

kepek.forEach(function(kepsrc) {
  kepcsinalo(kepsrc);
});

var gomb = document.querySelector('.csinal');

gomb.addEventListener('click', function() {
  alert('kattintottam');
  kepcsinalo('http://thesunflowerfoundation.net/images/sunflower-only.png');
});

window.addEventListener('scroll', function() {
  console.log('scroll', window.scrollY);
});

var cicagomb = document.querySelector('.cicat');
var kutyagomb = document.querySelector('.kutyat');
var valtoskep = document.querySelector('.cicakutyakep');

kutyagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://www.barathegyisegitokutya.hu/wp-content/uploads/2014/09/kutya_egeszsegvedelme.jpg');
});

cicagomb.addEventListener('click', function() {
  valtoskep.setAttribute('src', 'http://szepkepek.bloglap.hu/kepek/cica_2.jpg');
});
