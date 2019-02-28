# sending emails with python. need to enable 'less secure apps' in gmail.

import smtplib
from email.mime.text import MIMEText


def send_email(user, pwd, recipient, subject):
	'''
		user: sender's email address
		pwd: sender's email password
		recipient: recipient's email address
		subject: email subject
	'''
	try:
		msg = MIMEText('this is a test email!')
		msg['Subject'] = subject
		msg['From'] = user
		msg['To'] = recipient
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login(user, pwd)
		server.sendmail(user, recipient, msg.as_string())
		server.close()
		print 'The email sent successfully!'
	except Exception as e:
		# print '------------', e
		print 'Fail to send email'
		
a = sender's email
b = sender's email password
c = recipient's email
send_email(a, b, c, 'test') # replace a, b, c with the correct data.
    
    
