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

// Start REST endpoint /temp
app.post('/temp', function (req, res) {
  temp = req.body
  wheat_data = temp.toString()
  console.log(wheat_data, "----")
  var headersOpt = {  
    "content-type": "text/plain",
  };
  request(
          {
          method:'post',
          url:'http://api-app:8888/format/', 
          body: wheat_data, 
          headers: headersOpt,
          json: true,
      }, function (error, response, body) {  
          //Print the Response
          console.log(error)
          //console.log(body,"+++++");
          wheat_data = JSON.parse(body)
          //console.log('received temp ' + wheat_data)
          da_data(wheat_data);
  });
  res.end('OK')
})

// Start web page /
app.get('/', function (req, res, next) {
  try {
    var html = '<html><body><h1>Temp '+Number(temp).toFixed(2)+'</h1></body></html>'
    da_data();
    res.send(html)
  } catch (e) {
    console.log(e)
  }
})

// get da data
function da_data(wheat_data){
  var da_data = {}
  console.log("in da_data")
  try {
    request(options_da, function (error, response, body) {
      da_data = [JSON.parse(body)]
      console.log(da_data, "-------", wheat_data)
      merge_data(da_data, wheat_data);
    });
  } catch (e) {
    console.log(e)
  }
}

function merge_data(DaData, wheat_data){
  console.log("in merge data")
  // read csv file and convert to json
  // let wheat_data = csvToJson.getJsonFromCsv("");
  let wheat_data_1 = [
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Gedeb Assassa",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "Hi Mr. / Ms xxx I am a representative from MoA/BoA to send you an early warning message on wheat rust incidence specific to your area. If you want to receive the message please press yes or else no",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Boot",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Jeju",
      "Kebele": "Huruta Dore, Hijara",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shoa",
      "Woreda": "Boset",
      "Kebele": "Sifa",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Jeju",
      "Kebele": "Huruta Dore, Tibilay",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Kolobahawass",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Eillalaa, Gidara",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Garadima 9",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "High (> 40%)",
      "Growth Stage": "Maturity",
      "Region": "oromia",
      "Zone": "",
      "Woreda": "Werer ARC Research Field",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Iodehetosa",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Hetosa",
      "Kebele": "Borulencha",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Tiyo",
      "Kebele": "Gonde State Farm",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Tiyo",
      "Kebele": "Odadoweta",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Tiyo",
      "Kebele": "Shala Chabiti",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Digalu Tijo",
      "Kebele": "Ashabaka Wolkite",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Digelu Tijo",
      "Kebele": "Ashabaka",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Lemu Bilbilo",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Lemu Bilbilo",
      "Kebele": "Dawabursa",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Lemu Bilbilo",
      "Kebele": "Meraro",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Honkolowabe",
      "Kebele": "Sirbo",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Gedeb Assassa",
      "Kebele": "Hanto",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Gedeb Assassa",
      "Kebele": "Huruba Welkita",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Dodola",
      "Kebele": "Edo",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rutst",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Dodola",
      "Kebele": "Dodola Mazoria",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rutst",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Dodola",
      "Kebele": "Herero",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "",
      "Zone": "",
      "Woreda": "D-3 Bedahamo, Amibara",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Garadima,9",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Bole",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "Oromia",
      "Zone": "East Shoa",
      "Woreda": "Boset",
      "Kebele": "Sifa",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Jeju",
      "Kebele": "Bilkadore,Kemberu",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Sarayoba",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Garadimaa9",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale garadimaa",
      "Kebele": "tere",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Tedecha bela",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Kolobohawass",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Seraweba",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Maturity",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale garadima",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Flowering",
      "Region": "Oromia",
      "Zone": "East Shoa",
      "Woreda": "Boset",
      "Kebele": "Sifa",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale",
      "Kebele": "Garadimaa9",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shoa",
      "Woreda": "Boset",
      "Kebele": "Sifa",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Low (< 20%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Garadimaa tere",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Lemu Bilbilo",
      "Kebele": "Meraro",
      "Forecast Date": "",
      "Message": "xxxxxx",
      "Action": "????",
      "Language / Translation": "",
      "Extra infoamation": "Availablity of Chemicals"
    },
    {
      "Year": 2020,
      "Disease": "Yellow Rust / Stripe Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "West Arsi",
      "Woreda": "Dodola",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Tillering",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Tedechabela-6hase",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Garadimaa",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Tedechabela-hasse",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Dough",
      "Region": "",
      "Zone": "",
      "Woreda": "WARC Field Breeding Plotno 14",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Seraweba",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Stem Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Garadimaa tere",
      "Kebele": "",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Milk",
      "Region": "Oromia",
      "Zone": "Arsi",
      "Woreda": "Sire",
      "Kebele": "Tedechabelaa-hasse",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    },
    {
      "Year": 2020,
      "Disease": "Leaf Rust",
      "Severity": "Moderate (20 - 40%)",
      "Growth Stage": "Dough",
      "Region": "Oromia",
      "Zone": "East Shewa",
      "Woreda": "Fentale Garadimaa",
      "Kebele": "f9",
      "Forecast Date": "",
      "Message": "",
      "Action": "",
      "Language / Translation": "",
      "Extra infoamation": ""
    }
  ]
  var reqData = {"data1": DaData, "data2" : wheat_data};
  // request.post(options_merge,
  //   { json: true, body: reqData },
  //     function(err, res, body) {
  //       console.log(err, res, body, "+++++++");
  // });

  // request.post(options_merge, {
  //   body: reqData
  // });
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
  });
};

var server = app.listen(8081, function () {
  var host = server.address().address
  var port = server.address().port
  console.log("REST API listening at http://%s:%s", host, port)
})
