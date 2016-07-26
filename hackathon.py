import urllib2
import json
from datetime import datetime, timedelta
import requests
import os

API_KEY = "74680085cf15526dc4a9f1b488a6aa58"
CUST_ID = "577d5e520733d0184021f587"
DAYS = 2

def areBillsDueForCustomerIDSoon(custID):
	bills = getBillsAlmostDueForCustomer(custID,DAYS)
	if len(bills) > 0:
		print bills
		return True
	else:
		return False


def payAlmostDueBillsForCustomer(custID):
	url = "http://api.reimaginebanking.com/customers/"+custID+"/accounts?key="+API_KEY
	accounts = urllib2.urlopen(url)
	accountsJSON = json.load(accounts)
	for account in accountsJSON:
		# pay with the first savigs account we find
		if account['type'] == "Savings":
			# get bills due within two days and pay them off
			bills = getBillsAlmostDueForCustomer(custID, 2)
			for bill in bills:
				billAmount = int(bill['payment_amount'])
				account['balance'] -= billAmount
				# if we run out of money, return false
				if account['balance'] < 0:
					account['balance'] += billAmount

				else:
					requests.delete("http://api.reimaginebanking.com/bills/" + bill["_id"] + "?key=" + API_KEY)
			#managed to pay off all the bills near due
			res = requests.delete("http://api.reimaginebanking.com/accounts/" + account["_id"] + "?key=" + API_KEY)
			acctURL = """curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{\\\"type\\\": \\\"Savings\\\", \\\"nickname\\\": \\\"string\\\", \\\"rewards\\\": 0, \\\"balance\\\":""" + str(account['balance']) + """}" "http://api.reimaginebanking.com/customers/""" + CUST_ID + """/accounts?key=""" + API_KEY + '"'
			print acctURL
			os.system(acctURL)

			return True

def getBillsAlmostDueForCustomer(custID,numOfDays):
	url = "http://api.reimaginebanking.com/customers/"+custID+"/bills?key="+API_KEY
	bills = urllib2.urlopen(url)
	billsJSON = json.load(bills)
	billsDueIn = timedelta(days=numOfDays)
	billsAlmostDue = []

	for bill in billsJSON:
		if bill['status'] != 'paid':
			date = bill['payment_date']
			date_object = datetime.strptime(date, '%Y-%m-%d')
			if date_object - datetime.now() < billsDueIn:
				billsAlmostDue.append(bill)

	return billsAlmostDue

# areBillsDueForCustomerIDSoon(CUST_ID)
# payAlmostDueBillsForCustomer(CUST_ID)