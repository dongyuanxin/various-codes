import time
import re
import sys
import threading
import json
import pickle
from time import ctime
from socket import *
from random import choice,randint
from os import popen
__author__=='AsuraDong'
__date__=='2017/3/23 23:26'
_port_list = [21,23,25,53,38,80,135,137,139,1521,1433,3306,3389]

lock = threading.Lock()
dict_msg = {}

'''
#cmd moudle
host = sys.argv[1]
port = sys.argv[0]
Please modify the code by yourself
'''

class myThread(threading.Thread):
	def __init__(self,funs,args):
		threading.Thread.__init__(self)
		self.funs = funs
		self.__args = args
	def run(self):
		self.funs(*self.__args)
	def __repr__(self):
		return 'This a son class form threading.Thread'

class save():
	def __init__(self,dict_msg=None,filename=None):
		self.filename = None
		self.__dict_msg = dict_msg
	def __call__(self):
		print_dict(self.__dict_msg)
	def asBin(self):
		with open('C:\\ipSearch\\'+filename+'.bin','wb') as f:
			f.write(self.__dict_msg)
	def asJson(self):
		with open('C:\\ipSearch\\'+filename+'.txt','w') as f:
			self.__json_msg = json.dumps(self.__dict_msg)
			f.write(self.__json_msg)
	def asPic(self):
		with open('C:\\ipSearch\\'+filename+'.pic','wb') as f:
			f.write(self.__dict_msg)
	def check(self):
                pass
		'''for check a file'''

def scan_port(*args):
	host = args[0]
	port = args[1]
	global dict_msg
	try:
		tcpSock = socket(AF_INET,SOCK_STREAT)
		tcpSock.connect((host,port))
		if lock.acquire():
			print(port,'-->opened')
			dict_msg[port] = '-->opened'
			lock.release()
	except:
		if lock.acquire():
			print(port,'-->NOT opened')
			dict_msg[port] = '-->NOT opened'
			lock.release()

def input_ip():
	host = input('>>>input your own ip :\n')
	host_ = input('>>>ensure again:\n')
	while host!=host_:
		host = input('>>>input your own ip :\n')
		host_ = input('>>>ensure again:\n')
	return host

def search_ip():
	print('open the checking moudle,please waiting...')
	ip_info = popen('ipconfig')
	ip_msg = ip_info.read()
	ip_info.close()
	#print(ip_msg)
	host = re.search(r'IPv4.*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',ip_msg)
	try:
		host = host.group(1)
	except AttributeError as e:
		print(e)
		print('please check your ip by yourself')
		host = input_ip()
	else:
		print('Check succeed!!!Your own ip is :'+host)
	return host

def print_dict(dict_msg=None):
	print('*'*16,'have saved msg','*'*16)
	for item in dict_msg.items():
		print(item)

if __name__=='__main__':
	print('Now time is %s'% ctime())
	ip_ok = input('>>>If check your own ip?(Y/N):\n').strip()
	ip_ok = ip_ok.lower()
	while ip_ok !='y' and ip_ok!='n':
		ip_ok = input('>>>Please enter Y/N:\n').strip()
		ip_ok = ip_ok.lower()
		
	if ip_ok == 'n':
		host = input_ip()
	else:
		host = search_ip()
	
	moudle = input('>>>If you open the security port scan?(Y/N)\n').strip()
	moudle = moudle.lower()
	if moudle=='y':
		port_list = _port_list
	else:
		ports =input('>>>input the ports(125 or 125-1000):\n')
		port_list = re.findall(r'\d+',ports)
		port_list = range(int(port_list[0]),int(port_list[1])+1)
		t = []
		for i in port_list:
			t.append(i)
		port_list = t
	
	time_begin = time.clock()
	threads = []
	d = len(port_list)
	for i in range(0,d):
		temp = myThread(scan_port,(host,port_list[i]))
		threads.append(temp)
	for i in range(0,d):
		threads[i].start()
	for i in range(0,d):
		threads[i].join()
	print('The all time is ',time.clock()-time_begin)
	print('Now time is %s'% ctime())
	print('\n')
	print_dict(dict_msg)	
	
		
		
