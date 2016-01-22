'use strict';

var url = 'http://localhost:3000/todos';
var todoContainer = document.querySelector('.todo-container');
var todoInput = document.querySelector('.todo-input');
var addButton = document.querySelector('.add-item-button');
var completeItemButton = document.querySelector('.complete-item-button');
var removeCompletedItemsButton = document.querySelector('.remove-completed-items-button');


function createRequest(method, url, data, callback) {
  var todoRequest = new XMLHttpRequest();
  todoRequest.open(method, url);
  todoRequest.setRequestHeader('Content-Type', 'application/json');
  todoRequest.send(data);
  todoRequest.onreadystatechange = function() {
    console.log(todoRequest.response)
    if (todoRequest.readyState === 4) {
      return callback(todoRequest.response);
    }
  };
}

var listCallback = function(response) {
  var todoItems = JSON.parse(response);
  todoContainer.innerHTML = "";
  todoItems.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.setAttribute('id', todoItem.id);
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);

  })
}

var refresh = function() {
  createRequest('GET', url, {}, listCallback);
}
refresh();

var createTodoCallback = function (response) {
  refresh();
}

addButton.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: todoInput.value});
  createRequest('POST', url, newTodo, createTodoCallback);
  todoInput.value = "";

});
