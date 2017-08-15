import os
try:
    import requests
except Exception as e:
    print("Error is :\n"+e)
    exit(0)
HEADERS = {}
HEADERS['Accept'] = 'application/json, text/plain, */*'
HEADERS['Host'] = 'www.uooconline.com'
HEADERS['Origin'] = 'http://www.uooconline.com'
HEADERS['Referer'] = 'http://www.uooconline.com/learn/index'
HEADERS['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'

FORM_DATA = {}
FORM_DATA['cid'] = '1157191662'
FORM_DATA['hidemsg_'] = 'true'
FORM_DATA['network'] = '3'
FORM_DATA['subsection_id'] = '0'

REQUEST_URL = "http://www.uooconline.com/learn/mark"

def getCookie(Str):
    t = Str.split(';')
    cookieDict = {}
    for each in t:
        each = each.strip(" ").split("=")
        cookieDict[each[0]] = each[1]
    return cookieDict

def main():
    while True:
        url = input('>>>enter your URL:')
        print(url)
        FORM_DATA['section_id']=url.split(r'/')[-2]
        FORM_DATA['chapter_id']=url.split(r'/')[-3]
        FORM_DATA['video_length']=input(">>>enter Form Data's video_length:")
        FORM_DATA['video_pos'] = FORM_DATA['video_length']
        cookie = getCookie(input('>>>enter your Cookie:'))
        requests.get(url,headers=HEADERS,cookies=cookie)
        requests.post(url,headers=HEADERS,cookies=cookie,data=FORM_DATA)

        print('请通过测试题，进行下一步')
if __name__=='__main__':
    main()