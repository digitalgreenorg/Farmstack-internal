// Start REST server
const express = require('express');
const bodyParser = require('body-parser');
const request = require('request');

const app = express();

const options_da = {
  url: 'https://testdadmin.digitalgreen.org/api/v2/assets/aVzzVRBh6horqqawq4pNSS/data.json',
  headers: {
    'Authorization': 'Token a5a9824dcd5a1b07b3178be67bdfc73788f77d42'
  },
  json: true
};

const options_merge = {
  url: 'http://api-app:8888/'
};

// just use JSON body data
app.use(bodyParser.json({
  inflate: true,
  limit: '100mb'
}));

var wheat_data = "";
var da_data = "";

var flag_da = true;
var flag_wheat = true;

// indentify the json data and assign
function identify_data(data) {
  try {
    // console.log(data, "identify")
    if (data["next"] === null) {
      if (flag_da) {
        da_data = [data];
        console.log("received da data");
        flag_da = false;
      }
      //console.log('in if part')
    }
    else if (data.length > 0) {
      if (flag_wheat) {
        wheat_data = data;
        console.log("received wheat data");
        flag_wheat = false;
      }
      //console.log(wheat_data)
    }
  }
  catch (e) {
    console.log(e, "error22222");
  }
};

// Start REST endpoint /temp
app.post('/temp', function (req, res) {
  temp = req.body;
  console.log(temp, "data in here");
  identify_data(temp);
  // console.log("wheat data", wheat_data, "---", "da data", da_data, "---")
  // trigger only if both data are valid
  if (wheat_data != "") {
    if (da_data != "") {
      merge_data();
    }
    else {
      console.log("waiting for file 2");
    }
  }
  else {
    console.log("waiting for file 1");
  }
  res.end('OK');
})

// Start web page /
app.get('/', function (req, res) {
  try {
    var html = '<html><body><h1>Consumer App</h1></body></html>';
    res.send(html);
  } catch (e) {
    console.log(e);
  }
});

function merge_data(wheat_data) {
  console.log("in merge data");
  var reqData = { "data1": da_data, "data2": wheat_data };
  var headersOpt = {
    "content-type": "application/json",
  };
  request({
    method: 'post',
    url: 'http://api-app:8888/',
    body: reqData,
    headers: headersOpt,
    json: true,
  }, function (error, response, body) {
    console.log(body, "+++++");
    da_data = "";
    wheat_data = "";
    flag_da = true;
    flag_wheat = true;
  });
};

var server = app.listen(8081, function () {
  var host = server.address().address;
  var port = server.address().port;
  console.log("REST API listening at http://%s:%s", host, port);
});
