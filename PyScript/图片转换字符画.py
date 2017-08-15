from PIL import Image
from optparse import OptionParser
import os
#__author__=='AsuraDong'

usage = "Usage:%prog"
parser = OptionParser(usage=usage,version="%prog 1.0 (Python3.x)")

parser.add_option("-f","--file",dest="InputFile")
parser.add_option("-o","--output",dest="OutFile")
parser.add_option("-w","--width",dest="width",type="int",default=80)
parser.add_option("-H","--height",dest="height",type="int",default=80)

(options,args) = parser.parse_args()

IMG = options.InputFile
WIDTH = options.width
HEIGHT = options.height
OUTPUT = options.OutFile

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
#将256个灰度值映射到70个字符串上面
def getChar(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
    unit = (256+1)/length #每个单位字符对应的灰度值长度
    return ascii_char[int(gray/unit)]

if __name__=='__main__':
    if IMG.split('.')[-1]=='jpg' or IMG.split('.')[-1]=='jpeg':
        im = Image.open(IMG)
        im = im.resize((WIDTH,HEIGHT))

        txt = ""
        for i in range(HEIGHT):
            for j in range(WIDTH):#用image模块，可以用getpixel获得像素值，给你个例子吧。得到的像素值应该是(R,G,B)
                txt = txt + getChar(* im.getpixel((j,i)))
            txt+='\n'
        if not os.path.exists(r'C:\myPython'):
            os.mkdir(r'C:\myPython')
        if OUTPUT:
            txtName = 'C:\\myPython\\'+OUTPUT
            with open(txtName,'w') as f:
                f.write(txt)
        else :
            txtName = 'C:\\myPython\\'+IMG.split('.')[0]+'.txt'
            with open(txtName,'w')as f:
                f.write(txt)
    else:
        print('请转化为jpg/jpeg图片格式')
        exit(1)