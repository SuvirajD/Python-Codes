import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders

def send(filename):
	from_add = 'suviraj.personal@gmail.com'      #E-mail ID used to send the e-mail
	to_add = 'suvirajdua@icloud.com'			 #E-mail ID receiving the e-mail
	subject = 'Your daily stock report is here!!'

	msg = MIMEMultipart()
	msg['From'] = from_add
	msg['To'] = to_add
	msg['Subject'] = subject


	body = "Hey there, here are your stock updates"
	msg.attach(MIMEText(body, 'plain'))
	my_file = open(filename, 'rb')
	part = MIMEBase('application','octet-stream')
	part.set_payload((my_file).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachments; filename = ' + filename)
	msg.attach(part)

	message = msg.as_string()


	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(from_add,'knrhypyhrqhpynsk')


	server.sendmail(from_add,to_add, message)

	server.quit()

