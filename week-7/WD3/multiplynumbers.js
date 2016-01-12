'use strict';
//1st solution from 1 to 10

// function numberMultiply(input) {
//   var output = '';
//   for (var i = 1; i <= 10; i++) {
//     output += i + ' * ' + input + ' = ' + input * i + '\n';
//   }
//   return output;
// }
//
// for (var i = 1; i <= 10; i++ ) {
//   console.log(numberMultiply(i));
// }

//2nd solution

var szorzotabla1 = '';
for (var i = 1; i <= 10; i++) {
  szorzotabla1 += i + '*' + 4 + '=' + i*4 + '\n';
}
console.log(szorzotabla1);

//3rd solution

var szorzotabla2 = '';
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10].forEach(function(e) {
  szorzotabla2 += e + '*' + 4 + '=' + e*4 + '\n';
});
console.log(szorzotabla2);

//4th solution

var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
var szorzotabla3 = '';
var sorok = szamok.map(function(e) {
  return e + '*' + 4 + '=' + e*4 + '\n';
})
szorzotabla3 = sorok.join('');

console.log(szorzotabla3);

//function recursiveSzorzo(number, i) {
//  if (i > 10) {
//    return '';
//  }
//  return i + '*' + number + '=' + number * i + '\n' + recursiveSzorzo(number, i + 1);
//}

//console.log(recursiveSzorzo(4,1));
