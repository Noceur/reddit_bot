import ipgetter
import time
import NotifyUser

currentIP = ipgetter.myip()

while True:
	if (currentIP == ipgetter.myip()):
		print ("Ip is the same")
	else:
		print ("Ip has changed to " + ipgetter.myip())
		currentIP = ipgetter.myip()
		NotifyUser.send_ip("IP changed", currentIP)
	print ("sleeping 1200s")
	time.sleep(1200)