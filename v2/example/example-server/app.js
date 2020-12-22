/*
  Example of a very simple REST consumer app.

  This app accepts sensor values from POST requests to 
  http://<host>:8081/temp
  and displays them under
  http://<host>:8081/
  
  For demonstration purposes only.

  (C) Fraunhofer AISEC, 2017
*/
var temp = 0

// Start REST server
var express = require('express')
  , app = express()

let csvToJson = require('convert-csv-to-json');

const request = require('request');

const options_da = {
  url: 'https://testdadmin.digitalgreen.org/api/v2/assets/aVzzVRBh6horqqawq4pNSS/data.json/',
  headers: {
    'Authorization': 'Token a5a9824dcd5a1b07b3178be67bdfc73788f77d42'
  }
};

const options_merge = {
  url: 'http://api-app:8888/',
};

var DaData = []
// just use raw body data
var bodyParser = require('body-parser')
var options = {
  inflate: true,
  limit: '100mb',
  type: 'text/xml'
};
app.use( bodyParser.raw(options) );

var wheat_data = ""
var da_data = ""

var flag_da = true
var flag_wheat = true

// indentify the json data and assign
function identify_data(data){
  try{
    data = JSON.parse(data)
    // console.log(data, "identify")
    if (data["next"]===null){
    if(flag_da){
        da_data = [data]
        console.log("received da data")
        flag_da = false
    }
      //console.log('in if part')
    }
    else if(data.length > 0){
    if(flag_wheat){
        wheat_data = data
        console.log("received wheat data")
        flag_wheat = false
    }
      //console.log(wheat_data)
    }
  }
  catch(e){
    console.log(e, "error22222")
  }
};

// Start REST endpoint /temp
app.post('/temp', function (req, res) {
  temp = req.body.toString()
  console.log(temp, "data in here")
  identify_data(temp);
  if(wheat_data != ""){
    if(da_data != ""){
      merge_data(da_data, wheat_data);
    }
    else{
	 console.log("waiting for file 2")
    }
  }
  else{
	console.log("waiting for file 1")
  }
  res.end('OK')
})

// Start web page /
app.get('/', function (req, res, next) {
  try {
    var html = '<html><body><h1>Temp '+Number(temp).toFixed(2)+'</h1></body></html>'
    // da_data();
    res.send(html)
  } catch (e) {
    console.log(e)
  }
})


function merge_data(DaData, wheat_data){
  console.log("in merge data");
  var reqData = {"data1": DaData, "data2" : wheat_data};
  var headersOpt = {  
    "content-type": "application/json",
  };
  request(
          {
          method:'post',
          url:'http://api-app:8888/', 
          body: reqData, 
          headers: headersOpt,
          json: true,
      }, function (error, response, body) {  
          //Print the Response
          console.log(body,"+++++");
          da_data = "";
          wheat_data = "";
          flag_da = true
          flag_wheat = true
  });
};

var server = app.listen(8081, function () {
  var host = server.address().address
  var port = server.address().port
  console.log("REST API listening at http://%s:%s", host, port)
})