// Start REST server
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

const app = express();
var data = ''

// just use JSON body data
app.use(bodyParser.json({
  inflate: true,
  limit: '100mb'
}));

// Start web page /
app.get('/', function (req, res) {

  try {
    var html = '<html><body>CSV Data : '+  data +'</body></html>'
    res.send(html)
  } catch (e) {
    next(e)
  }

});

// Receive Message
app.post('/get_data', function (req, res) {

  try {
    var req_body = req.body;
    console.log('req_body ', JSON.stringify(req_body));

    data = data + (JSON.stringify(req_body));
    

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
