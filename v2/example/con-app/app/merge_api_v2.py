# import asyncio
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import tornado.ioloop
import tornado.web
import json
import requests

print("---merge_api--")

# PREV_JSON = ""
FILE_DATA = "No file data"
MERGE_STATUS = "Waiting to merge"
TELEGRAM_STATUS = "Not sending data, waiting for file"
JSON_1 = {}

class JSONEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, ObjectId):
			return str(o)
		return json.JSONEncoder.default(self, o)

def parse_json2(json2):
	data = []
	json2 = json2.replace("}]", "").replace('[', '').replace('{', '').replace(']','')
	for val in json2.split('},'):
		temp_dict = {}
		for v in val.split(', '):
			try:
				key, val1 = v.split('=')
				prev = key.strip()
				temp_dict[key.strip()] = val1.strip()
			except:
				# key, val, val1 = v.split('=')
				# val += val1
				# print(prev, v.strip())
				temp_dict[prev] += ', ' + v.strip()
		data.append(temp_dict)
	return data


def detect_change(json2):
	# global PREV_JSON
	# print(PREV_JSON, json2)
	try:
		with open("prev_json.json", "r") as ofs:
			data = json.loads(ofs.readlines()[0])
			if data == json2:
				print("same data received")
				return False
			else:
				print("in if case", json2)
				with open("prev_json.json", "w") as ofs:
					ofs.write(json.dumps(json2))
				return True
	except:
		with open("prev_json.json", "w") as ofs:
			ofs.write(json.dumps(json2))
		return True

def merge_jsons(json1, json2):
	global JSON_1
	json2 = [
		{
			"Date": "1-6, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Flowering to Milk Stage",
			"Region": "Amhara",
			"Zone": "East Gojam",
			"Woreda": "Enarje enawga",
			"Kebele": "",
			"Varieties": "Kekeba",
			"Control": "Please inform farmers in your area to be vigilant for early appearance of <Disease> Rust and take appropriate action"
		},
		{
			"Date": "1-6, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Flowering to Milk Stage",
			"Region": "Amhara",
			"Zone": "East Gojam",
			"Woreda": "Goncha siso",
			"Kebele": "",
			"Varieties": "Kekeba",
			"Control": ""
		},
		{
			"Date": "1-6, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Flowering to Milk Stage",
			"Region": "Amhara",
			"Zone": "East Gojam",
			"Woreda": "Hulet eju",
			"Kebele": "",
			"Varieties": "Kekeba",
			"Control": ""
		},
		{
			"Date": "6 -10, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Prevalence and Severity",
			"Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
			"Region": "Amhara",
			"Zone": "North Shewa",
			"Woreda": "Minjar Shenkora",
			"Kebele": "",
			"Varieties": "Ogolcho (1), Unknown (33)",
			"Control": ""
		},
		{
			"Date": "1-6, September 2020",
			"Disease": "Yellow rust",
			"Severity": "Low Incidence",
			"Growth Stage": "Tillering,Boot, Flowering",
			"Region": "Amhara",
			"Zone": "South Gondar",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Triticale (19), Kakaba (8), Ogolcho (2), Unknown (27)",
			"Control": ""
		},
		{
			"Date": "3 -9, September 2020",
			"Disease": "Yellow rust",
			"Severity": "Low Incidence and Severity",
			"Growth Stage": "Tillering, Boot, Flowering (mostly Tillering)",
			"Region": "Amhara",
			"Zone": "North Wello",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Dandaa(43), Hibist(1), Hidassie(2), Kekeba(6), Oat (1), Unknown (16), Triticale (6)",
			"Control": ""
		},
		{
			"Date": "3 -9, September 2020",
			"Disease": "Yellow rust",
			"Severity": "Low Incidence and Severity",
			"Growth Stage": "Tillering, Boot, Flowering (mostly Tillering)",
			"Region": "Amhara",
			"Zone": "South Wello",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Dandaa(43), Hibist(1), Hidassie(2), Kekeba(6), Oat (1), Unknown (16), Triticale (6)",
			"Control": ""
		},
		{
			"Date": "2 - 21, September 2020",
			"Disease": "Yellow Rust",
			"Severity": "Very High Prevalence and Severity in unsprayed fields",
			"Growth Stage": "N/A",
			"Region": "Oromia",
			"Zone": "Arsi",
			"Woreda": "Bekoji",
			"Kebele": "",
			"Varieties": "Kubsa, Hidassie, Wane, Lemu",
			"Control": ""
		},
		{
			"Date": "2 - 21, September 2020",
			"Disease": "Yellow Rust",
			"Severity": "Very High Prevalence and Severity in unsprayed fields",
			"Growth Stage": "N/A",
			"Region": "Oromia",
			"Zone": "Arsi",
			"Woreda": "Meraro",
			"Kebele": "",
			"Varieties": "Kubsa, Hidassie, Wane, Lemu",
			"Control": ""
		},
		{
			"Date": "22-23, September 2020",
			"Disease": "Yellow/Stripe Rust",
			"Severity": "Very High Incidence and Severity",
			"Growth Stage": "Tillering – Flowering (Mostly Tillering)",
			"Region": "Oromia",
			"Zone": "Bale",
			"Woreda": "Agarfa",
			"Kebele": "",
			"Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
			"Control": ""
		},
		{
			"Date": "22-23, September 2020",
			"Disease": "Yellow/Stripe Rust",
			"Severity": "Very High Incidence and Severity",
			"Growth Stage": "Tillering – Flowering (Mostly Tillering)",
			"Region": "Oromia",
			"Zone": "Bale",
			"Woreda": "Gasera",
			"Kebele": "",
			"Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
			"Control": ""
		},
		{
			"Date": "22-23, September 2020",
			"Disease": "Yellow/Stripe Rust",
			"Severity": "Very High Incidence and Severity",
			"Growth Stage": "Tillering – Flowering (Mostly Tillering)",
			"Region": "Oromia",
			"Zone": "Bale",
			"Woreda": "Goba",
			"Kebele": "",
			"Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
			"Control": ""
		},
		{
			"Date": "22-23, September 2020",
			"Disease": "Yellow/Stripe Rust",
			"Severity": "Very High Incidence and Severity",
			"Growth Stage": "Tillering – Flowering (Mostly Tillering)",
			"Region": "Oromia",
			"Zone": "Bale",
			"Woreda": "Sinana",
			"Kebele": "",
			"Varieties": "Dambal (30S), Ogolcho (30S), Unknown (60S)",
			"Control": ""
		},
		{
			"Date": "6 -10, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Prevalence and Severity",
			"Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
			"Region": "Oromia",
			"Zone": "East Shewa",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Ogolcho (1), Unknown (33)",
			"Control": ""
		},
		{
			"Date": "6 -10, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Prevalence and Severity",
			"Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
			"Region": "Oromia",
			"Zone": "North Shewa",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Ogolcho (1), Unknown (33)",
			"Control": ""
		},
		{
			"Date": "6 -10, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Prevalence and Severity",
			"Growth Stage": "Tillering - Boot (Mostly at Boot Stage)",
			"Region": "Oromia",
			"Zone": "West Arsi",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Ogolcho (1), Unknown (33)",
			"Control": ""
		},
		{
			"Date": "19-20, September 2020",
			"Disease": "Yellow Rust",
			"Severity": "Low Incidence and Severity",
			"Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
			"Region": "Oromia",
			"Zone": "West Showa",
			"Woreda": "Chelia",
			"Kebele": "",
			"Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
			"Control": ""
		},
		{
			"Date": "19-20, September 2020",
			"Disease": "Yellow Rust",
			"Severity": "Low Incidence and Severity",
			"Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
			"Region": "Oromia",
			"Zone": "West Showa",
			"Woreda": "Liben Jawi",
			"Kebele": "",
			"Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
			"Control": ""
		},
		{
			"Date": "19-20, September 2020",
			"Disease": "Yellow Rust",
			"Severity": "Low Incidence and Severity",
			"Growth Stage": "Tillring - Flowering (Mostly at Flowering Stage)",
			"Region": "Oromia",
			"Zone": "West Showa",
			"Woreda": "Tokokutaye",
			"Kebele": "",
			"Varieties": "Ogolcho, Dandaa, Kakaba, Unknown",
			"Control": ""
		},
		{
			"Date": "18-19, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
			"Region": "SNNPR",
			"Zone": "Guragie",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
			"Control": ""
		},
		{
			"Date": "18-19, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
			"Region": "SNNPR",
			"Zone": "Hadiya",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
			"Control": ""
		},
		{
			"Date": "18-19, September 2020",
			"Disease": "Yellow rust",
			"Severity": "High Incidence and Severity",
			"Growth Stage": "Tillering, Boot, Flowering (Mostly Boot)",
			"Region": "SNNPR",
			"Zone": "Siltie",
			"Woreda": "",
			"Kebele": "",
			"Varieties": "Dandaa(5), Hidassie (1), Kekeba (12),Shorima(1), Kingbird (1), Ogolcho(19), Unknown (1)",
			"Control": ""
		}
	]
	global MERGE_STATUS
	global FILE_DATA
	FILE_DATA = "Files received"
	# print(json1, json2)

	# if not detect_change(json2):
	# 	return False
	# try:
	# 	if json2[0]["Status"] == "No change":
	# 		return False
	# except:
	# 	print("merging data now")
	if JSON_1 == {}:
		JSON_1 = json1
	elif JSON_1 == json1:
		return False
	elif JSON_1 != json1:
		JSON_1 = json1

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
	# all_data = json1[0]["results"] change as suggested by Milux
	all_data = json1["results"]
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
	call_telebots_wrb()
	print("Sending messages ...")

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
	conf_data = [{"name": "sujit", "chat_id": 695935397}, {"name": "vineet", "chat_id": 742873817}, {"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 1093201488, "name": "razak"}]
	#conf_data = [{"name": "sagar singh", "chat_id": 817454976}, {"name": "sujit", "chat_id": 695935397}]
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
	return True

def call_telebots_wrb():
	global TELEGRAM_STATUS
	TELEGRAM_STATUS = "Messages sent via telegram"
	conf_data = [{"name": "sujit", "chat_id": 695935397}, {"name": "sagar singh", "chat_id": 817454976}, {"chat_id": 443467414, "name": "beza"}, {"name": "vineet", "chat_id": 742873817}, {"chat_id": 1093201488, "name": "razak"}]
	# conf_data = [{"name": "sagar singh", "chat_id": 817454976}]
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

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("No get methods")
	
	def post(self):
		req_data = json.loads(self.request.body)
		print("request received")
		if merge_jsons(req_data["data1"], req_data["data2"]):
			self.write("Processed")
		else:
			global FILE_DATA
			global MERGE_STATUS
			global TELEGRAM_STATUS
			FILE_DATA = "No file data"
			MERGE_STATUS = "Waiting to merge"
			TELEGRAM_STATUS = "Not sending data, waiting for file"
			self.write("No Change detected")


class JsonFormatter(tornado.web.RequestHandler):
	def get(self):
		self.write("No get methods")
	
	def post(self):
		req_data = json.dumps(parse_json2(str(self.request.body)))
		self.write(JSONEncoder().encode(req_data))
		self.finish()


class StatusUpdater(tornado.web.RequestHandler):
	def get(self):
		self.write("No get methods")
	
	def post(self):
		global FILE_DATA
		global MERGE_STATUS
		global TELEGRAM_STATUS
		self.write(JSONEncoder().encode(json.dumps({"File": FILE_DATA, "Merge": MERGE_STATUS, "Telegram": TELEGRAM_STATUS})))
		# FILE_DATA = "No file data"
		# MERGE_STATUS = "Waiting to merge"
		# TELEGRAM_STATUS = "Not sending data, waiting for file"
		self.finish()

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
		(r"/format/", StatusUpdater),
		(r"/get_updates/", StatusUpdater)
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
