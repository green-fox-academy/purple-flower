'use strict';

function Student() {
  this.grade =
}


ar dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);
dezso.addGrade('magyar', 4)

dezso.getCount(); //('rajz': 2, 'matek': 3)
console.log(dezso.getAverage()); //3.4
