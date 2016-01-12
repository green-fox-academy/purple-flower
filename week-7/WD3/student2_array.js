'use strict';

function Student() {
  // this.grades = [{subject: 'matek', grade: '4'}];
  this.grades = [];

  this.addGrade = function(s, g) {
    this.grades.push({subject: s, num: g});
  };

  this.getCount = function() {
    var output = {};
    this.grades.forEach(function(grade) {
      if (!(grade.subject in output)) {
        output[grade.subject] = 0;
      }
      output[grade.subject] ++;
    });
    return console.log(output);
  };

  this.getAverage = function() {
    var sum = 0;
    this.grades.forEach(function(grade) {
      sum += grade.num;
    });
    return sum / this.grades.length;
  };
}


var dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 4)

dezso.getCount(); //('rajz': 2, 'matek': 3)
console.log(dezso.getAverage()); //3.5

//szorglmi
// dezso.getAverageBySubject(); ('matek': 4.3, 'rajz': 2)
