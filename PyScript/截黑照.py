import time
import os
__author__=='AsuraDong'
__date__=='2017/3/21 13:05'
try:
      import pyautogui
except:
      print('No this library')
      print('Please input "pip install pyautogui" in COMMAND')
      exit(1)
else:
      pyautogui.FAILSAFE=True

if os.name=='nt':
      filename = r'C:\我的python\黑照'
else:
      print('please debug by yourself')
      exit(0)
      
number = 0
if not os.path.exists(filename):
      os.makedirs(filename)
max_number = int(input('>>>截图多少张：\n'))
time.sleep(2)#切换屏幕的准备时间

while number<=max_number:
      photoname = 'No'+str(number)
      pyautogui.screenshot(os.path.join(filename,photoname+'.jpg'))
      time.sleep(0.1)#间歇时间
      number+=1
