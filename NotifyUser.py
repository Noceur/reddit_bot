import smtplib



def send_msg(SUBJECT, TEXT):
	fromaddr = 'anotheruselessbot@gmail.com'
	toaddrs  = 'dimoronen@gmail.com'
	username = 'anotheruselessbot@gmail.com'
	password = 'botbotbot'
	convert_message
	message = 'Subject: %s\n\n%s' % (SUBJECT, TEXT)
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, message)
	server.quit()