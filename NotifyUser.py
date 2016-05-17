import smtplib



def send_msg(SUBJECT, TEXT):

	fromaddr			= 'anotheruselessbot@gmail.com'
	toaddrs  			= 'dimoronen@gmail.com'
	username 			= 'anotheruselessbot@gmail.com'
	password 			= 'botbotbot'
	message 			= 'Subject: %s\n\n%s' % (SUBJECT, create_text(TEXT))
	server 				= smtplib.SMTP('smtp.gmail.com:587')
	#=====================================
	#			STARTING SERVICE
	#=====================================
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()

def create_text(TEXT):
	
