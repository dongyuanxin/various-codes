import os
import time
import sys
from io import StringIO 

__author__=='AsuraDong'
__date__=='2017/3/21 13:00'

def main():
	if len(sys.argv)==2:
		filename = sys.argv[1]
	else:
		filename = input('>>>Input a filename:\n')

	if not os.path.isdir(filename):
		print('Please input a correct filename.')
		exit(0)
	if not os.access(filename,os.R_OK):
		print('No access.')
		exit(1)
	os.chdir(filename)
	for (dirpath,dirnames,filenames) in os.walk(filename):
		for onename in filenames:
			if os.path.splitext(onename)[1]=='.py':#输入您要转换的文件后缀名的类型/Type the name of the file you want to convert
				sio = StringIO()
				with open(os.path.join(dirpath,onename),'r',encoding = 'utf-8') as f:
					for line in f.readlines():
						sio.write(line)
				os.remove(os.path.join(dirpath,onename))
				with open(os.path.join(dirpath,os.path.splitext(onename)[0]+'.txt'),'w',encoding = 'utf-8')as f:
				#可以改变.txt,转换为别的文本格式/.txt can be changed to other text format
					f.write(sio.getvalue())

if __name__=='__main__':
	print(time.strftime('%Y %b %dth %H:%M:%S',time.localtime()))
	main()
	print(time.strftime('%Y %b %dth %H:%M:%S',time.localtime()))