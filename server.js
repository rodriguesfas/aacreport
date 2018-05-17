"use strict";

const port = process.env.PORT || 4000;
const express = require("express");
const app = require("express")();
const bodyParser = require("body-parser");
const request = require("request");
const http = require("http").Server(app);
const io = require("socket.io").listen(http);

const routes = require("./routes/index.js");
//routes(app);

var words_chi, metrics;

app.use(express.static("public"));
app.use(bodyParser.urlencoded({ extended: true }));

app.set("view engine", "ejs");

app.get("/", function(req, res) {
  if (jsonData) {

    // Prepara os dados para ser enviado para o cliente.
    var jsonValidString = JSON.stringify(eval("(" + jsonData + ")"));
    var JSONObj = JSON.parse(jsonValidString);

    JSONObj.forEach(function(data) {
      metrics = data.metrics;
      words_chi = data.words_chi;
    });

    res.render("pages/profile", {
      metrics: metrics,
      words_chi: words_chi,
      error: null
    });

    //console.log(JSONObj);
  } else {
    res.render("index", { report: null, error: "Ohh não :(" });
  }
});

app.post("/", function(req, res) {
  let msg = req.body.msg;
  if (jsonData) {
    res.render("index", { report: null, error: "Yes :)" });
  } else {
    res.render("index", { report: null, error: "Ohh no :(" });
  }
});

io.sockets.on("connection", function(socket) {
  socket.on("click", function() {
    console.log("oi");
    //io.emit("report", jsonData);
    //io.emit("report", { report: jsonData });
  });
});

http.listen(port, function() {
  console.log(
    "listening on http://localhots:" + port + " | Para OFF o Server Ctrl+C"
  );
});

var connection = 0;

io.on("connection", function(socket) {
  console.log("Conectado!");
  connection++;

  io.emit("connection online", connection);
  socket.on("mensagem", function(msg) {
    io.emit("mensagem", msg);
  });

  socket.on("disconnect", function() {
    console.log("Desconectado!");
    connection--;
    io.emit("users", connection);
  });
});

/**
 * ------------------------------------------------------------------------------------
 * Run Pyhton
 */
var spawn = require("child_process").spawn,
  py = spawn("python", ["script/aacreport.py"]),
  data = "",
  jsonData = "";

py.stdout.on("data", function(data) {
  jsonData += data.toString();
  //jsonData += data;
});

py.stdout.on("end", function() {
  console.log("req: ", jsonData);
});

py.stdin.write(JSON.stringify(data));
py.stdin.end();
