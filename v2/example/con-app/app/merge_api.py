import asyncio
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
import tornado.ioloop
import tornado.web
import json
import requests

print("---merge_api--")

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
	all_data = json1["results"]
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
	call_telebots_wrb()

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
	conf_data = [{"name": "sagar singh", "chat_id": 817454976}, {"name": "sujit", "chat_id": 695935397}]
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
	conf_data = [{"name": "sagar singh", "chat_id": 817454976}, {"name": "sujit", "chat_id": 695935397}]
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
	call_telebots_dva()

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("No get methods")
	
	def post(self):
		req_data = json.loads(self.request.body)
		# Output data to check correct operation
		# TODO: DISABLE for productive use!!! (data leak)
		print(req_data)
		merge_jsons(req_data["data1"], req_data["data2"])
		self.write("Processed")

def make_app():
	return tornado.web.Application([
		(r"/", MainHandler),
	])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()