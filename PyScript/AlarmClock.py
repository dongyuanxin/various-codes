from optparse import OptionParser
import time
from winsound import Beep
try:
    import pygame
except Exception as e:
    print('Failed:',e)
    exit(1)

__author__=='AsuraDong'
usage = "Usage:%prog"
parser = OptionParser(usage=usage,verson="%prog 1.0 at python 3.x")
parser.add_option('-t','--time',dest = "time",default=30.0,type='float',help="启动时间:单位min")
parser.add_option('-m','--music',dest='music',help="闹铃音乐")
(options,args) = parser.parse_args()

TIME = options.time*60
try:
    MUSIC = options.music
except KeyError :
    time.sleep(TIME)
    winsound.Beep(100,2000)
else:
    pygame.mixer.init()
    pygame.mixer.music.load(MUSIC)
    time.sleep(TIME)
    pygame.mixer.music.play()