// Start REST server
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

const app = express();

// just use JSON body data
app.use(bodyParser.json({
  inflate: true,
  limit: '100mb'
}));

// Start web page /
app.get('/', function (req, res) {

  try {
    data = req.body
    var html = '<html><body><h1> Consumer App is receiving two files </h1></body></html>';
    res.send(html);
  } catch (e) {
    console.log(e);
  }
});

// Receive Message
app.post('/get_data', function (req, res) {

  try {
    data = req.body
    console.log('data -> ', data);
    res.end('OK');
  } catch (e) {
    console.log(e);
  }
});

var server = app.listen(8081, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log("REST API listening at http://%s:%s", host, port);
});
