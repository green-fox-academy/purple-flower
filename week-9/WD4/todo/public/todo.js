'use strict';

var url = 'http://localhost:3000/todos';
var todoContainer = document.querySelector('.todo-container');
var todoInput = document.querySelector('.todo-input');
var addButton = document.querySelector('.add-item-button');
var completeItemButton = document.querySelector('.complete-item-button');
var removeCompletedItemsButton = document.querySelector('.remove-completed-items-button');


var listCallback = function(response) {
  var todoItems = JSON.parse(response);
  todoItems.forEach(function(todoItem) {
    var newTodoItem = document.createElement('p');
    newTodoItem.setAttribute('id', todoItem.id);
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);

  })
}

var refresh = function() {
  todoContainer.innerHTML = "";
  createRequest('GET', url, {}, listCallback);
}


addButton.addEventListener('click', function() {
  var newTodo = JSON.stringify({text: todoInput.value});
  var createTodoCallback = function (response) {
    refresh();
  }
  // todoInput.innerText = "Write your next ToDo here!";
  createRequest('POST', url, newTodo, createTodoCallback);
});


// removeCompletedItemsButton.addEventListener('click', function() {
//
// })

// var completedTodo = JSON({completed: true});
//
// function setCompleted() {
//
// }
//
// createRequest('PUT', url, )
