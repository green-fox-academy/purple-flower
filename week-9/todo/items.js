"use-strict"

var mysql = require('mysql');
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'test',
  password: 'test',
  database: 'todo'
});


connection.connect();

function allItems(callback) {
  connection.query('SELECT * FROM todo',
  function(err, result) {
    if (err) throw err;
    return callback(result);
  });
}

function addItem(item, cb) {
  connection.query('INSERT INTO todo SET text=?', item, function(err, result) {
    if (err) throw err;
    cb(result)
  });
}


function setItemCompleted(todo_id) {
  connection.query('UPDATE todo SET status="completed" WHERE todo_id=?', todo_id,
    function(err, result) {
      if (err) throw err;
      console.log(result);
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
function removeItem(todo_id, cb) {
  connection.query('DELETE FROM todo WHERE todo_id=?', todo_id,
    function(err, result) {
      if (err) throw err;
      cb(result)
    });
}


module.exports = {
  add: addItem,
  remove: removeItem,
  removeCompleted: removeCompletedItem,
  complete: setItemCompleted,
  all: allItems,
};
