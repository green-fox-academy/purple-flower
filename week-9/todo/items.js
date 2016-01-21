"use-strict"

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test',
  password: 'test',
  database: 'todo'
});


connection.connect();

var TodoItem = function () {
  this.id = nextId();
  this.text = "";
  this.completed = false;
}

TodoItem.prototype.update = function(attributes) {
  this.text = attributes.text || "";
  this.completed = !!attributes.completed;
};

var currId = 0;
function nextId() {
  return ++currId;
}

var items = {};

function getItem(todo_id) {
  connection.query('SELECT * FROM todo WHERE todo_id=?', todo_id,
    function(err, result) {
      if (err) throw err;
      return (result);
    });
}

function addItem(attributes) {
  connection.query('INSERT INTO todo SET ?', attributes, function(err, result) {
    if (err) throw err;
    console.log(result.insertId);
  });
}

//remove comleted todo items
function removeCompletedItem() {
  connection.query('DELETE FROM todo WHERE status="completed"',
    function(err, result) {
      if (err) throw err;
      console.log(result);
    });
}

//remove selected todo items
function removeItem(todo_id) {
  connection.query('DELETE FROM todo WHERE todo_id=?', todo_id,
    function(err, result) {
      if (err) throw err;
      console.log(result);
    });
}

function setItemCompleted(todo_id) {
  connection.query('UPDATE todo SET status="completed" WHERE todo_id=?', todo_id,
    function(err, result) {
      if (err) throw err;
      console.log(result);
    });
}

function allItems(callback) {
  connection.query('SELECT * FROM todo',
  function(err, result) {
    if (err) throw err;
    return callback(result);
  });
}

module.exports = {
  get: getItem,
  add: addItem,
  remove: removeItem,
  removeCompleted: removeCompletedItem,
  complete: setItemCompleted,
  all: allItems,
};
