"use strict"

var express = require("express");
var bodyParser = require("body-parser");
var items = require("./items.js");

var app = express();

// items.complete(15);
// items.complete(20);
// items.complete(21);
//
// items.removeCompleted();



app.use(express.static("public"));
app.use(bodyParser.json());


app.get("/todos", function (req, res) {
  items.all(function(result) {
    res.json(result);
  });
});



app.post("/todos", function (req, res) {
  var item = items.add(req.body.text, function(item){
  res.json(item);
 })
});



// app.put("/todos/:id", function (req, res) {
//   findItem(req, res, function (item) {
//     item.update(req.body);
//     res.json(item);
//   });
// });

app.delete("/todos/:id", function (req, res) {
  items.remove(req.params.id, function (item) {
    res.json(item);
  });
});

app.listen(3000, function () {
  console.log("Listening on port 3000...")
});
