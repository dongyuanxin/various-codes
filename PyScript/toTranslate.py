import urllib.request
import urllib.parse
import json
__author__='AsuraDong'
__date__=='2017/3/21 14::00'

head={}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'

    data={}
    data['type']='AUTO'
    data['i']=None
    data['doctype']='json'
    data['xmlVersion']='1.8'
    data['keyfrom']='fanyi.web'
    data['ue']='UTF-8'
    data['action']='FY_BY_CLICKBUTTON'
    data['typoResult']='true'
    
while True:
    words=input('请输入您的要翻译的句子：')
    data['i']=words
    data=urllib.parse.urlencode(data).encode('utf-8')
    request=urllib.request.Request(url,data,head)
    response=urllib.request.urlopen(request)
    html=response.read().decode('utf-8')
    html=json.loads(html)
    translated=html['translateResult'][0][0]['tgt']
    print(' '*10+'翻译的结果是：\n',end='')
    print(' '*24,end='')
    print(translated)
