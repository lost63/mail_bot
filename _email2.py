import smtplib
from email.mime.text import MIMEText
from email.header import decode_header
from email.mime.multipart import MIMEMultipart
import mailparser
import email
import imaplib

# connect to Google's servers
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
EMAIL=username=from_addr = 'test_email@gmail.com'
PASSWORD=password = 'your_pass'
SERVER = 'imap.gmail.com'

#Список на какие адреса разрешается отправка почты
legal_list=['test1@gmail.com', 'test2@gmail.com']

#функция для проверки разрешенного списка адресатов почты
def legal_check(list_adrrs):
	k=0
	#ststus=''
	global legal_list
	if list_adrrs==list(list_adrrs):
		for i in list_adrrs:
			if i in legal_list:
				k+=1
	else:
		if list_adrrs in legal_list:
			k+=1
	if k >0:
		status='allow'
	else:
		status='deny'
	return status

#Функция проверки почтовго ящика
def check_email_box():
	# возвращает значения [[id, from, subject, content],[...]]
	global EMAIL; global PASSWORD;	global SERVER
	mail = imaplib.IMAP4_SSL(SERVER)
	mail.login(EMAIL, PASSWORD)
	mail.select('inbox')
	# it will return with its status and a list of ids
	status, data = mail.search(None, 'ALL')
	# by white spaces on this format: [b'1 2 3', b'4 5 6']
	mail_ids = []
	for block in data:
		# b'1 2 3'.split() => [b'1', b'2', b'3']
		mail_ids += block.split()
	# now for every id we'll fetch the email
	# to extract its content
	email_list = []
	for i in mail_ids:
		email_=[]
		email_.append(i)
		# the fetch function fetch the email given its id
		# and format that you want the message to be
		status, data = mail.fetch(i, '(RFC822)')
		# the content data at the '(RFC822)' format comes on
		# a list with a tuple with header, content, and the closing
		# byte b')'
		for response_part in data:
			# so if its a tuple...
			if isinstance(response_part, tuple):
				mail_p = mailparser.parse_from_bytes(response_part[1])
				if len(mail_p.from_[0])>1:
					email_.append(mail_p.from_[0][1])
				else:
					email_.append(mail_p.from_[0][0])
				email_.append(mail_p.subject)
				email_.append(mail_p.body)
				email_.append('html')
		email_list.append(email_)
	return email_list

#Удаление одного письма
def delete_one_email(id_, subject):
	# возвращает значения [[id=b'1', from, subject, content],[...]]
	global EMAIL
	global PASSWORD
	global SERVER
	mail = imaplib.IMAP4_SSL(SERVER)
	mail.login(EMAIL, PASSWORD)
	mail.select('inbox')
	status, data = mail.search(None, 'ALL')
	mail_ids = []
	mail_list = []
	for block in data:
		mail_ids += block.split()
	for i in mail_ids:
		mail_ = []
		mail_.append(i)
		status, data = mail.fetch(i, '(RFC822)')
		for response_part in data:
			if isinstance(response_part, tuple):
				message = email.message_from_bytes(response_part[1])
				mail_from = message['from']
				mail_subject = message['subject']
				mail_.append(mail_from)
				try:
					bytes, encoding = decode_header(mail_subject)[0]
					mail_subject = bytes.decode(encoding)
					mail_.append(mail_subject)
				except:
					pass
					mail_.append(mail_subject)
		mail_list.append(mail_)
	k=0
	for i in mail_list:
		if id_== i[0] and subject == i[2]:
			k+=1
		else:
			pass
	if k > 0:
		pass
		mail.store(id_, '+FLAGS', '(\Deleted)')
		mail.expunge()

#Удаление нескольких писем
def delete_several_email(id_subject):
	# возвращает значения [[id=b'1', from, subject, content],[...]]
	global EMAIL; global PASSWORD; global SERVER
	mail = imaplib.IMAP4_SSL(SERVER)
	mail.login(EMAIL, PASSWORD)
	mail.select('inbox')
	status, data = mail.search(None, 'ALL')
	mail_ids = []
	mail_list = []
	for block in data:
		mail_ids += block.split()
	for i in mail_ids:
		mail_ = []
		mail_.append(i)
		status, data = mail.fetch(i, '(RFC822)')
		for response_part in data:
			if isinstance(response_part, tuple):
				message = email.message_from_bytes(response_part[1])
				mail_from = message['from']
				mail_subject = message['subject']
				mail_.append(mail_from)
				try:
					bytes, encoding = decode_header(mail_subject)[0]
					mail_subject = bytes.decode(encoding)
					mail_.append(mail_subject)
				except:
					pass
					mail_.append(mail_subject)
		mail_list.append(mail_)
	for i in mail_list:
		for y in id_subject:
			if y[0] == i[0] and y[1] == i[2]:
				mail.store(y[0], '+FLAGS', '(\Deleted)') 
				mail.expunge()
			else:
				pass

#Отправка почты
def send_email(subject_, message_, to_addrs, format='html'):
	global smtp_ssl_host; global smtp_ssl_port;	global username
	global password; global from_addr
	if legal_check(to_addrs)=="deny":
		subject_ ="email is not legal "+str(to_addrs)
		to_addrs=username
	message = MIMEMultipart("alternative")
	if format=='html':
		message = MIMEMultipart("alternative", None, [MIMEText(message_,'html')])
	if format=='text':
		message = MIMEMultipart("alternative", None, [MIMEText(message_)])
	message['subject'] = subject_
	message['from'] = from_addr
	if to_addrs==list(to_addrs):
		message['to'] = ', '.join(to_addrs)
	else:
		message['to'] = (to_addrs)
	server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
	server.login(username, password)
	server.sendmail(from_addr, to_addrs, message.as_string())
	server.quit()

