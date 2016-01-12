'use strict';

function Student() {
  this.grade = [];
  this.addGrade = function(grade) {
    this.grade.push(grade);
  };
  this.getAverage = function() {
    var gradeSum = this.grade.reduce(function(sum, grade) {
      return sum + grade;
    }, 0);
    return gradeSum / this.grade.length
  };
}

var jozsi = new Student();
jozsi.addGrade(4);
jozsi.addGrade(3);
jozsi.addGrade(5);
jozsi.addGrade(5);
console.log(jozsi.getAverage()); //4.25
