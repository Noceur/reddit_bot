import smtplib
import time

#cache_link			= ["abc1", "abc2", "abc3", "abc4", "abc5"]
#cache_age			= ["1h", "2h", "3h", "4h", "5h"]

def send_msg(SUBJECT, TEXT, TEXT2=[]):
	fromaddr			= 'anotheruselessbot@gmail.com'
	toaddrs  			= 'dimoronen@gmail.com'
	username 			= 'anotheruselessbot@gmail.com'
	password 			= 'botbotbot'
	message 			= 'Subject: %s\n\n%s' % (SUBJECT, create_text(TEXT, TEXT2))
	server 				= smtplib.SMTP('smtp.gmail.com:587')

	#=====================================
	#			STARTING SERVICE
	#=====================================
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()
	print (message)

def create_text(TEXT, TEXT2):
	item_total = ""
	for item in TEXT:
		item_total += item + "\n"
		#item_total += TEXT2[item] + "\n"
	for item in TEXT2:
		item_total += str(item) + "\n"
	return item_total

#while True:
	#send_msg("TESTING", cache_link, cache_age)
	#time.sleep(100)
