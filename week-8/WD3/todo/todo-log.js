'use strict';

// var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';


function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest();
  probaRequest.open('GET', url);
  probaRequest.setRequestHeader('Content-Type', 'application/json');
  probaRequest.send();
  probaRequest.onreadystatechange = function() {
    console.log('allapot: ', probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  };
}

function createPostRequest(url) {
  var probaCreateRequest = new XMLHttpRequest();
  probaCreateRequest.open('POST', url);
  probaCreateRequest.setRequestHeader('Content-Type', 'application/json');
  probaCreateRequest.send(JSON.stringify({text: ':)'}));
}

var todoContainer = document.querySelector('.todo-container');

function todoCallback(response) {
  console.log(JSON.parse(response));
  var todoArray = JSON.parse(response);
  todoArray.forEach(function (todoItem) {
    console.log(todoItem.text);
    var newTodoItem = document.createElement('p');
    newTodoItem.innerText = todoItem.text;
    todoContainer.appendChild(newTodoItem);
  });
}

var url = 'https://mysterious-dusk-8248.herokuapp.com/todos';
createRequest(url, todoCallback);
createPostRequest(url);
