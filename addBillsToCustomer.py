import urllib2
import json
import requests

API_KEY = "74680085cf15526dc4a9f1b488a6aa58"
ACC_ID = "577d60d80733d0184021f589"

with open('bills.json') as json_data:
	data = json.load(json_data)
	json_data.close()

url = "http://api.reimaginebanking.com/accounts/"+ACC_ID+"/bills?key="+API_KEY 
for bill in data:
	resp = requests.post(url, bill)
	print resp.text
