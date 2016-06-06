import ipgetter
import time
import NotifyUser
import datetime

currentIP = ipgetter.myip()
currentIP = "1.1.1.1"
numberofloops = 0

while True:
	numberofloops += 1
	#print ("check #" str(numberofloops) + "\n" + "At: " + str(datetime.datetime.now()))
	print ("Loop #" + str(numberofloops) + "\n" + "At: " + str(datetime.datetime.now()))
	print ("\nChecking IP")
	if (currentIP == ipgetter.myip()):
		print ("Ip is the same")
	else:
		print ('Ip has changed to "' + ipgetter.myip())
		currentIP = ipgetter.myip()
		NotifyUser.send_ip("IP changed", currentIP)
	print ("sleeping 1200s")
	time.sleep(1200)