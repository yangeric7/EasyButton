import serial
import hackathon
import datetime
from datetime import timedelta

CUST_ID = "577d5e520733d0184021f587"

conn = False

ser = serial.Serial("COM5",9600)

print "connecting..."
while not conn:
	serin = ser.read()
	conn = True

print "connected ..."
#ser.write('1')

# while ser.read() == '1':
# 	ser.read()

timeToReRun = timedelta(seconds=30)
lastRunTime = datetime.datetime.now()-timeToReRun
while True:
	#print ser.read()
	if ser.read() == '9':
		if lastRunTime+timeToReRun < datetime.datetime.now():
			print "paying bills"
			hackathon.payAlmostDueBillsForCustomer(CUST_ID)
			lastRunTime= datetime.datetime.now()
	