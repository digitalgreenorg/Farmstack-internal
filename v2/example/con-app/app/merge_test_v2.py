import json
import requests

url = "https://testdadmin.digitalgreen.org/api/v2/assets/aVzzVRBh6horqqawq4pNSS/data.json/"

payload = {}
headers = {
  'Authorization': 'Token a5a9824dcd5a1b07b3178be67bdfc73788f77d42'
}

response = requests.request("GET", url, headers=headers, data = payload)

# print(response.text.encode('utf8'))
json1 = [json.loads(response.text.encode('utf8'))]

json2 = [
  {
    "Year": "1-6, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Flowering to Milk Stage",
    "Region": "Amhara",
    "Zone": "East Gojam",
    "Woreda": "Enarje enawga",
    "Kebele": "",
    "Varieties": "Kekeba",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "1-6, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Flowering to Milk Stage",
    "Region": "Amhara",
    "Zone": "East Gojam",
    "Woreda": "Goncha siso",
    "Kebele": "",
    "Varieties": "Kekeba",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "1-6, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Flowering to Milk Stage",
    "Region": "Amhara",
    "Zone": "East Gojam",
    "Woreda": "Hulet eju",
    "Kebele": "",
    "Varieties": "Kekeba",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "6 -10, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Prevalence and Severity",
    "Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
    "Region": "Amhara",
    "Zone": "North Shewa",
    "Woreda": "Minjar Shenkora",
    "Kebele": "",
    "Varieties": "Ogolcho (1), Unknown (33)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "1-6, September 2020",
    "Disease": "Yellow rust",
    "Severity": "Low Incidence",
    "Growth Stage": "Tillering,Boot, Flowering",
    "Region": "Amhara",
    "Zone": "South Gondar",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Triticale (19), Kakaba (8), Ogolcho (2), Unknown (27)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "3 -9, September 2020",
    "Disease": "Yellow rust",
    "Severity": "Low Incidence and Severity",
    "Growth Stage": "Tillering, Boot, Flowering (mostly Tillering)",
    "Region": "Amhara",
    "Zone": "North Wello",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Dandaa(43), Hibist(1), Hidassie(2), Kekeba(6), Oat (1), Unknown (16), Triticale (6)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "3 -9, September 2020",
    "Disease": "Yellow rust",
    "Severity": "Low Incidence and Severity",
    "Growth Stage": "Tillering, Boot, Flowering (mostly Tillering)",
    "Region": "Amhara",
    "Zone": "South Wello",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Dandaa(43), Hibist(1), Hidassie(2), Kekeba(6), Oat (1), Unknown (16), Triticale (6)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "2 - 21, September 2020",
    "Disease": "Yellow Rust",
    "Severity": "Very High Prevalence and Severity in unsprayed fields",
    "Growth Stage": "N/A",
    "Region": "Oromia",
    "Zone": "Arsi",
    "Woreda": "Bekoji",
    "Kebele": "",
    "Varieties": "Kubsa, Hidassie, Wane, Lemu",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "2 - 21, September 2020",
    "Disease": "Yellow Rust",
    "Severity": "Very High Prevalence and Severity in unsprayed fields",
    "Growth Stage": "N/A",
    "Region": "Oromia",
    "Zone": "Arsi",
    "Woreda": "Meraro",
    "Kebele": "",
    "Varieties": "Kubsa, Hidassie, Wane, Lemu",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "22-23, September 2020",
    "Disease": "Yellow/Stripe Rust",
    "Severity": "Very High Incidence and Severity",
    "Growth Stage": "Tillering – Flowering (Mostly Tillering)",
    "Region": "Oromia",
    "Zone": "Bale",
    "Woreda": "Agarfa",
    "Kebele": "",
    "Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "22-23, September 2020",
    "Disease": "Yellow/Stripe Rust",
    "Severity": "Very High Incidence and Severity",
    "Growth Stage": "Tillering – Flowering (Mostly Tillering)",
    "Region": "Oromia",
    "Zone": "Bale",
    "Woreda": "Gasera",
    "Kebele": "",
    "Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "22-23, September 2020",
    "Disease": "Yellow/Stripe Rust",
    "Severity": "Very High Incidence and Severity",
    "Growth Stage": "Tillering – Flowering (Mostly Tillering)",
    "Region": "Oromia",
    "Zone": "Bale",
    "Woreda": "Goba",
    "Kebele": "",
    "Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "22-23, September 2020",
    "Disease": "Yellow/Stripe Rust",
    "Severity": "Very High Incidence and Severity",
    "Growth Stage": "Tillering – Flowering (Mostly Tillering)",
    "Region": "Oromia",
    "Zone": "Bale",
    "Woreda": "Sinana",
    "Kebele": "",
    "Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "6 -10, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Prevalence and Severity",
    "Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
    "Region": "Oromia",
    "Zone": "East Shewa",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Ogolcho (1), Unknown (33)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "6 -10, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Prevalence and Severity",
    "Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
    "Region": "Oromia",
    "Zone": "North Shewa",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Ogolcho (1), Unknown (33)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "6 -10, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Prevalence and Severity",
    "Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
    "Region": "Oromia",
    "Zone": "West Arsi",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Ogolcho (1), Unknown (33)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "19-20, September 2020",
    "Disease": "Yellow Rust",
    "Severity": "Low Incidence and Severity",
    "Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
    "Region": "Oromia",
    "Zone": "West Showa",
    "Woreda": "Chelia",
    "Kebele": "",
    "Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "19-20, September 2020",
    "Disease": "Yellow Rust",
    "Severity": "Low Incidence and Severity",
    "Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
    "Region": "Oromia",
    "Zone": "West Showa",
    "Woreda": "Liben Jawi",
    "Kebele": "",
    "Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "19-20, September 2020",
    "Disease": "Yellow Rust",
    "Severity": "Low Incidence and Severity",
    "Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
    "Region": "Oromia",
    "Zone": "West Showa",
    "Woreda": "Tokokutaye",
    "Kebele": "",
    "Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "18-19, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
    "Region": "SNNPR",
    "Zone": "Guragie",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "18-19, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
    "Region": "SNNPR",
    "Zone": "Hadiya",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
    "Forecast Date": "",
    "Message": ""
  },
  {
    "Year": "18-19, September 2020",
    "Disease": "Yellow rust",
    "Severity": "High Incidence and Severity",
    "Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
    "Region": "SNNPR",
    "Zone": "Siltie",
    "Woreda": "",
    "Kebele": "",
    "Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
    "Forecast Date": "",
    "Message": ""
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
			severity_disease_dict[woreda] = {"disease": value["Disease"], "severity": value["Severity"], "growth stage": value["Growth Stage"], "variety": value["Varieties"]}
		except Exception as e:
			print(e)

	# print(json.dumps(severity_disease_dict))
	# print(severity_disease_dict, "--")
	all_data = json1[0]["results"]
	da_data_list = []
	for data in all_data:
		# print(type(data))
		region = data["Region"].lower()
		zone = data["Zone"].lower()
		woreda = data["Woreda"].lower()
		kebele = data["Kebele"].lower()
		try:
			da_bot_data = {"Name": data["Name"], "Phone_Number": data["Phone_Number"], "Father_s_Name": data["Father_s_Name"], "Kebele": data["Kebele"], "Salutation": data["Salutation"], "Woreda": data["Woreda"]}
		except:
			print(data)
		try:
			da_bot_data["add_info"] = severity_disease_dict[woreda]
		except Exception as e:
			da_bot_data = []
		if da_bot_data != []:
			da_data_list.append(da_bot_data)
		# print(severity_disease_dict[region][zone][woreda][kebele])
		# always create
	# print(da_data_list)
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
	data = {'chat_id': '%s' % (chat_id), 'text': 'Hello %s type "/start" to receive wheat rust advisories.' % (name)}
	requests.post(url, data).json()


def call_telebots_dva():
	# {"name": "sagar singh", "chat_id": 817454976} {"chat_id": 1093201488, "name": "razak"}
	# conf_data = [{"name": "sujit", "chat_id": 695935397}, {"name": "vineet", "chat_id": 742873817}, {"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 1093201488, "name": "razak"}]
	conf_data = [{"chat_id": 443467414, "name": "beza"}]
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
	conf_data = [{"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 443467414, "name": "beza"}]
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
merge_jsons(json1, json2)
call_telebots_wrb()