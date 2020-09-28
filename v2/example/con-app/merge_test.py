import json
import requests

json1 = [
{
  "count": 6,
  "next": "null",
  "previous": "null",
  "results": [
    {
      "_id": 109,
      "Kebele": "huluko",
      "username": "username not found",
      "Specialization": "animal_health",
      "Zone": "west arsi",
      "Gender": "female",
      "Region": "oromia",
      "_uuid": "86a6f3b2-2f8f-46c1-a82b-2428be9aa6db",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "gedeb hasasa",
      "_submitted_by": "beza",
      "Education_Level": "2nd_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:86a6f3b2-2f8f-46c1-a82b-2428be9aa6db",
      "Email": "beza@digitalgreen.org",
      "Name": "Beza",
      "end": "2020-09-15T14:45:53.504+03:00",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "Ashami",
      "Date_of_employment": "2020-01-01",
      "Phone_Number": "+251911313159",
      "_submission_time": "2020-09-15T11:46:38",
      "Marital_Status": "married",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-15T14:41:43.445+03:00",
      "Date_of_Birth": "1990-01-01",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "Bogale",
      "Salutation": "ms",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM"
    },
    {
      "_id": 110,
      "Kebele": "huluko",
      "username": "beza",
      "Specialization": "rural_development_and_extension",
      "Zone": "west arsi",
      "Gender": "male",
      "Region": "oromia",
      "_uuid": "0f81e421-df3c-4743-b1da-a9ce79ab0d76",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "gedeb hasasa",
      "_submitted_by": "beza",
      "Education_Level": "2nd_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:0f81e421-df3c-4743-b1da-a9ce79ab0d76",
      "Name": "Firew",
      "end": "2020-09-15T14:50:26.158+03:00",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "Abebe",
      "Date_of_employment": "2019-01-06",
      "Phone_Number": "+251911384064",
      "_submission_time": "2020-09-15T11:50:40",
      "Marital_Status": "married",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-15T14:47:28.686+03:00",
      "Date_of_Birth": "1990-01-01",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "Kebede",
      "Salutation": "mr",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM"
    },
    {
      "_id": 111,
      "Kebele": "oda dawata",
      "username": "username not found",
      "Specialization": "animal_production",
      "Zone": "arsi",
      "Gender": "male",
      "Region": "oromia",
      "_uuid": "1c2769c4-6ec7-408e-b55e-875af06451df",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "tiyo",
      "_submitted_by": "null",
      "Education_Level": "2nd_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:1c2769c4-6ec7-408e-b55e-875af06451df",
      "Name": "sujit",
      "Employment_Date_in_Kebele": "2020-09-23",
      "end": "2020-09-24T21:31:34.460+05:30",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "MB C",
      "Date_of_employment": "2020-09-23",
      "Phone_Number": "8115479516",
      "_submission_time": "2020-09-23T12:07:41",
      "Marital_Status": "single",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-23T17:32:32.592+05:30",
      "Date_of_Birth": "1991-04-01",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "R K C",
      "Salutation": "mr",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM",
      "meta/deprecatedID": "uuid:24f11da8-0376-4c79-bce2-65c1db121113"
    },
    {
      "_id": 112,
      "Kebele": "boshee timbaako",
      "username": "digitalgreen",
      "Specialization": "animal_health",
      "Zone": "east  wollega",
      "Gender": "male",
      "Region": "oromia",
      "_uuid": "45bb5f2c-5c57-48d1-8f38-7e2da921d034",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "boneya boshe",
      "_submitted_by": "null",
      "Education_Level": "1st_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:45bb5f2c-5c57-48d1-8f38-7e2da921d034",
      "Name": "Vineet",
      "Employment_Date_in_Kebele": "2020-04-01",
      "end": "2020-09-25T14:42:31.249+05:30",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "VGF",
      "Date_of_employment": "2019-04-01",
      "Phone_Number": "9916669690",
      "_submission_time": "2020-09-23T12:08:32",
      "Marital_Status": "single",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-18T12:38:05.381+05:30",
      "Date_of_Birth": "1990-09-16",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "VF",
      "Salutation": "ms",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM",
      "meta/deprecatedID": "uuid:a400865b-600b-4928-9cee-1f2e8c16d7ee"
    },
    {
      "_id": 113,
      "Kebele": "koloba surara",
      "username": "digitalgreen",
      "Specialization": "animal_production",
      "Zone": "bale",
      "Gender": "male",
      "Region": "oromia",
      "_uuid": "ec37afd0-694b-486c-becb-260fffc1086f",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "gasera",
      "_submitted_by": "null",
      "Education_Level": "2nd_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:ec37afd0-694b-486c-becb-260fffc1086f",
      "Name": "Razak",
      "Pension_Number": "684646489",
      "Employment_Date_in_Kebele": "2020-09-07",
      "end": "2020-09-25T14:41:10.602+05:30",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "RGF",
      "Date_of_employment": "2020-09-14",
      "Phone_Number": "9845829465",
      "_submission_time": "2020-09-23T12:08:33",
      "Marital_Status": "single",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-18T12:43:45.517+05:30",
      "Date_of_Birth": "2020-09-23",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "RF",
      "Salutation": "mr",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM",
      "meta/deprecatedID": "uuid:0a0931c4-c209-47d4-9b9d-107294d84246"
    },
    {
      "_id": 114,
      "Kebele": "tulloo",
      "username": "digitalgreen",
      "Specialization": "animal_science",
      "Zone": "west arsi",
      "Gender": "male",
      "Region": "oromia",
      "_uuid": "e4105b1f-3135-41bf-97c6-5600fd75d1bb",
      "_bamboo_dataset_id": "",
      "_tags": [
        
      ],
      "Woreda": "kofele",
      "_submitted_by": "null",
      "Education_Level": "2nd_degree",
      "_xform_id_string": "aVzzVRBh6horqqawq4pNSS",
      "_validation_status": {
        
      },
      "meta/instanceID": "uuid:e4105b1f-3135-41bf-97c6-5600fd75d1bb",
      "Name": "sagar singh",
      "Employment_Date_in_Kebele": "2020-09-24",
      "end": "2020-09-24T16:37:00.928+05:30",
      "formhub/uuid": "23fdcf1f0d674b8c9f04198ae2d70643",
      "Grand_Father_s_Name": "grandfather's name",
      "Date_of_employment": "2020-09-24",
      "Phone_Number": "+917903147540",
      "_submission_time": "2020-09-24T11:07:13",
      "Marital_Status": "single",
      "_notes": [
        
      ],
      "_attachments": [
        
      ],
      "start": "2020-09-24T16:34:41.189+05:30",
      "Date_of_Birth": "1991-04-15",
      "_geolocation": [
        "null",
        "null"
      ],
      "Father_s_Name": "father's name",
      "Salutation": "mr",
      "_version_": "vtwbp34Xm8MQFVpAKpAQot",
      "_status": "submitted_via_web",
      "__version__": "v4r5U2BizKJQRTpwErpuqM"
    }
  ]
}
]

json2 = [
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

def merge_jsons(json1, json2):

	merge_cols = ['Region', 'Zone', 'Woreda', 'Kebele']
	data_fromda = ['Name', 'Phone_Number', 'Father_s_Name', 'Kebele']

	severity_disease_dict = {}

	for value in json2:
		region = value["Region"].lower()
		zone = value["Zone"].lower()
		woreda = value["Woreda"].lower()
		kebele = value["Kebele"].lower()
		# check if region already present
		try:
			severity_disease_dict[region]
			# check if zone already present
			try:
				severity_disease_dict[region][zone]
				# check if woreda is present
				try:
					severity_disease_dict[region][zone][woreda]
					# check if kebele is present
					try:
						severity_disease_dict[region][zone][woreda][kebele].append({"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"]})
					except:
						severity_disease_dict[region][zone][woreda][kebele] = [{"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"]}]
				except:
					severity_disease_dict[region][zone][woreda] = {}
					severity_disease_dict[region][zone][woreda][kebele] = [{"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"]}]
			except:
				severity_disease_dict[region][zone] = {}
				severity_disease_dict[region][zone][woreda] = {}
				severity_disease_dict[region][zone][woreda][kebele] = [{"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"]}]
		except:
			severity_disease_dict[region] = {}
			severity_disease_dict[region][zone] = {}
			severity_disease_dict[region][zone][woreda] = {}
			severity_disease_dict[region][zone][woreda][kebele] = [{"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"]}]

	# print(json.dumps(severity_disease_dict))
	all_data = json1[0]["results"]
	da_data_list = []
	for data in all_data:
		# print(type(data))
		region = data["Region"].lower()
		zone = data["Zone"].lower()
		woreda = data["Woreda"].lower()
		kebele = data["Kebele"].lower()
		da_bot_data = {"Name": data["Name"], "Phone_Number": data["Phone_Number"], "Father_s_Name": data["Father_s_Name"], "Kebele": data["Kebele"]}
		try:
			severity_disease_dict[region]
			try:
				severity_disease_dict[region][zone]
				try:
					severity_disease_dict[region][zone][woreda]
					try:
						da_bot_data["add_info"] = severity_disease_dict[region][zone][woreda][kebele]
					except:
						dat = severity_disease_dict[region][zone][woreda]
						da_bot_data["add_info"] = list(dat.values())[0]
				except:
					dat = severity_disease_dict[region][zone]
					da_bot_data["add_info"] = list(list(dat.values())[0].values())[0]
			except:
				dat = severity_disease_dict[region]
				da_bot_data["add_info"] = list(list(list(dat.values())[0].values())[0].values())[0]
		except:
			pass
		da_data_list.append(da_bot_data)
		# print(severity_disease_dict[region][zone][woreda][kebele])
		# always create
		with open("merged_data.json", "w+") as ofs:
			ofs.write(json.dumps(da_data_list))

# send message via telegram api
def send_message_dva(name, chat_id):
	print(name, chat_id)
	url = f'https://api.telegram.org/bot1334865601:AAGM8u07ZzDqa__jV42DXiRFcUR3aMSm4g0/sendMessage'
	data = {'chat_id': '%s' % (chat_id), 'text': 'Hello %s type "/start" to start verification' % (name)}
	requests.post(url, data).json()

def send_message_wrb(name, chat_id):
	print(name, chat_id)
	url = f'https://api.telegram.org/bot1333903854:AAGhtAkHVlPNaM3y0Hu-D3l5rvHiaUqqLYE/sendMessage'
	data = {'chat_id': '%s' % (chat_id), 'text': 'Hello %s type "/start" to start verification' % (name)}
	requests.post(url, data).json()


def call_telebots_dva():
	# {"name": "sagar singh", "chat_id": 817454976} {"chat_id": 1093201488, "name": "razak"}
	# conf_data = [{"name": "sujit", "chat_id": 695935397}, {"name": "vineet", "chat_id": 742873817}, {"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 1093201488, "name": "razak"}]
	conf_data = [{"chat_id": 1093201488, "name": "razak"}]
	da_data_list = []
	with open("merged_data.json", "r") as ofs:
		da_data_list = json.loads(ofs.readlines()[0])
	for value in da_data_list:
		for key, val in value.items():
			# print(key, val)
			if key == "Name":
				for conf_d in conf_data:
					if val.lower() in conf_d["name"].lower():
						send_message_dva(val, conf_d["chat_id"])

def call_telebots_wrb():
	# {"name": "sagar singh", "chat_id": 817454976}
	# conf_data = [{"name": "sujit", "chat_id": 695935397}, {"name": "vineet", "chat_id": 742873817}, {"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 1093201488, "name": "razak"}]
	conf_data = [{"name": "sujit", "chat_id": 695935397}]
	da_data_list = []
	with open("merged_data.json", "r") as ofs:
		da_data_list = json.loads(ofs.readlines()[0])
	for value in da_data_list:
		for key, val in value.items():
			# print(key, val)
			if key == "Name":
				for conf_d in conf_data:
					if val.lower() in conf_d["name"].lower():
						send_message_wrb(val, conf_d["chat_id"])

# call_telebots_dva()
# call_telebots_wrb()