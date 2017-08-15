from pyautogui import *
from time import sleep
from random import randint,choice
import os
from time import localtime
__author__=='AsuraDong'
__date__=='2017/3/23 23:27'
def test():
      sleep(3)
      x,y=position()
      print(x,y)

myinfo=['jinwanwocaishihidaozuiwandenanren','haiyoushuimeishuia','hhh',
        'jinyewumian','yizhidaotianliang','haiyourenhuozhema',
        'qichuanglou']
num=0
x=511
y=202

print('3秒准备时间，请将输入法切换哦，并且调整页面');sleep(3)
while True:
      sleep(1)

      moveTo(361,477)
      click()

      moveTo(x,y)
      click(x=x,y=y,clicks=2,interval=0.5)
      click(x=745,y=648)
      sleep(0.5)
      click(x=993,y=646)
      
      typewrite(choice(myinfo),interval=0.1)
      hotkey('space','enter')
      sleep(randint(60*60*50,60*60*60))
      num+=1
      if num==len(myinfo):
            break

t = localtime()
if(t.tm_mday==16 and t.tm_hour==6):
      os.system("shutdown -s -t %d" % 10)

