import requests
import re
from bs4 import BeautifulSoup
import threading
import time
import threading

url_list=['http://weibo.cn/mukewang']#注意格式
max_thread = 20#跑的线程
END = 2#结束的页码
#请重新构造，每次！！！加'#'的都需要重新构造
my_cookies={}
my_cookies['ALF']='1492662735'#
my_cookies['SCF']='AkLF8lG7zPYonQch2IOXRdC6qwXnb_kuyRPAeNDniYWCXwFrl_0ukQ1rAVZVhJfIj47w2vQ1qK1vGQuaT7aZ2qM.'#
my_cookies['SUB']='_2A2511MlJDeRxGeBP6VsZ9ybNyz-IHXVXNtcBrDV6PUJbktBeLWmlkW0Nwbf8kTpbj5W17Uld9R2Fx2QeSw..'#
my_cookies['SUBP']='0033WrSXqPxfM725Ws9jqgMF55529P9D9W5mimf_wqpnqAaue3CBhljC5JpX5o2p5NHD95QceKz41hMReK50Ws4Dqcj1Pfv19P9LM._VdNUVPfYt'#
my_cookies['SUHB']='0ftZV6sKyewuV4'#
my_cookies['SSOLoginState']='1490073881'#
my_cookies['_T_WM']='c912472e0063ba086f7fee3ec20bcbe0'

my_headers={}
my_headers['Host']='weibo.cn'
my_headers['User-Agent']='Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.14 Safari/537.36'
my_headers['Connection']='keep-alive'
my_headers['Accept-Language']='zh-CN,zh;q=0.8'
my_headers['Referer']='http://weibo.cn/mukewang?page=2'
my_headers['Accept-Encoding']='gzip, deflate, sdch'
my_headers['Accept-Language']='zh-CN,zh;q=0.8'
my_headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'

mes_dict={}
def spider(url=None,page=None,headers=None,cookies=None):
      global mes_dict
      mes_set = set()
      page_url = url+'?page='+str(page)
      html = requests.get(page_url,headers=headers,cookies=cookies)
      bs = BeautifulSoup(html.content,"html.parser")
      weibo_list = bs.find_all(['span'],{'class':'ctt'})
      time_list = bs.find_all(['span'],{'class':'ct'})
      if page==1:
            zip_list = zip(time_list,weibo_list[3:])#+V有三个
      else:
            zip_list = zip(time_list,weibo_list,)
      for Time,Weibo in zip_list:
            mes_set.add('From'+Time.get_text()+'\n  '+Weibo.get_text())
            #print('From'+Time.get_text()+'\n  '+Weibo.get_text())
      mes_dict[page]=mes_set
      
if __name__=='__main__':
      thread_list = []
      for url in url_list:
            for page in range(1,END):
                  #spider(url,page,my_headers,my_cookies)
                  t = threading.Thread(target=spider,args=(url,page,my_headers,my_cookies,))
                  thread_list.append(t)
            for each in thread_list:each.start()
            for each in thread_list:each.join()
            time.sleep(1)#简称停歇
                  
                        
