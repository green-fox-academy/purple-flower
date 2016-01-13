'use strict';

var fs = require('fs');

try{
  var content = fs.readFileSync('alma.txt');
} catch(e) {
  content = 'para volt');
}

console.log(String(content));
