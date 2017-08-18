#encoding:utf-8
import pymysql
import jieba
import os
import pickle
# import datetime
import time
from collections import namedtuple

from langconv import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from FindIndex import find_index
from ClearHTML import clean_html
from EmotionWord import *

mpl.rcParams['font.sans-serif'] = ['FangSong']
mpl.rcParams['axes.unicode_minus']=False

jieba.load_userdict('userDict.txt')

#首尾要选取的句子个数
FORWARD_NUM = 2
BACKWARD_NUM = 2

#首尾的权重
WEIGHT = 1.4103

# 转换繁体到简体
def cht_to_chs(line):
    line = Converter('zh-hans').convert(line)
    line.encode('utf-8')
    return line

# 转换简体到繁体
def chs_to_cht(line):
    line = Converter('zh-hant').convert(line)
    line.encode('utf-8')
    return line

#参数weight：默认为1，对于一篇ariticle的不同部分给予不同的权重
def get_partial_score(news,weight=1):
    news = cht_to_chs(news)
    news = clean_html(news)
    word_list = list(jieba.cut(news))

    pos_dict = {'times':0,'score':0}
    neg_dict = {'times':0,'score':0}

    for (index,word) in enumerate(word_list):
        word_score = 0
        #判断极性
        if (word in pos_emotion) or (word in pos_envalute):
            word_score+=weight
            '''
            两种情况：
            1. 非常 不 好吃
            2. 不是 很 好吃
            需要极性反转
            '''
            if (index-1>=0 and word_list[index-1] in neg_degree) or ( index-2>=0 and word_list[index-2] in neg_degree ):
                word_score = word_score*(-1)

        elif (word in neg_emotion) or (word in neg_envalute):
            word_score-=1
            '''
            1. 不是 不好
            2. 不是 很 不好
            极性反转
            '''
            if (index-1>=0 and word_list[index-1] in neg_degree) or ( index-2>=0 and word_list[index-2] in neg_degree ):
                word_score = word_score*(-1)
        #判断程度词
        if index-1>=0:
            #赫夫曼二叉树，加权路径最小
            if word_list[index-1] in more_degree or (index-2>=0 and word_list[index-2] in more_degree):
                    word_score = word_score*2
            elif word_list[index-1] in ish_degree or (index-2>=0 and word_list[index-2] in more_degree):
                    word_score = word_score*1.5
            elif word_list[index-1] in very_degree or (index-2>=0 and word_list[index-2] in more_degree):
                    word_score = word_score*2.5
            elif word_list[index-1] in least_degree or (index-2>=0 and word_list[index-2] in more_degree):
                    word_score = word_score*1.1
            elif word_list[index-1] in most_degree or (index-2>=0 and word_list[index-2] in more_degree):
                    word_score = word_score*3

        if word_score>0:
            #print(word,index)
            pos_dict['times']+=1
            pos_dict['score']+=word_score
        elif word_score<0:
            neg_dict['times'] += 1
            neg_dict['score'] += word_score
        
    return (pos_dict, neg_dict)
            
def get_score(news):
    score = 0

    forward_index , backward_index = find_index(news,FORWARD_NUM,BACKWARD_NUM)
    if forward_index and backward_index:
        forward = news[:forward_index+1]
        forward_pos_dict,forward_neg_dict = get_partial_score(forward,WEIGHT)

        backward = news[backward_index+1:]
        backward_pos_dict,backward_neg_dict = get_partial_score(backward,WEIGHT)

        #首尾根据权重和频率计算
        if forward_pos_dict['times']+forward_neg_dict['times']:
            forward_pos_score = forward_pos_dict['score']*forward_pos_dict['times']/(forward_pos_dict['times']+forward_neg_dict['times'])
            forward_neg_score = forward_neg_dict['score']*forward_neg_dict['times']/(forward_pos_dict['times']+forward_neg_dict['times'])
        else:
            forward_pos_score = forward_neg_score = 0

        if backward_pos_dict['times']+backward_neg_dict['times']:
            backward_pos_score = backward_pos_dict['score']*backward_pos_dict['times']/(backward_pos_dict['times']+backward_neg_dict['times'])
            backward_neg_score = backward_neg_dict['score']*backward_neg_dict['times']/(backward_pos_dict['times']+backward_neg_dict['times'])
        else:
            backward_pos_score = backward_neg_score = 0

        score = score + forward_pos_score +  forward_neg_score + backward_pos_score +backward_neg_score

        if forward_index+abs(backward_index) < len(news):#如果 news ∉ (forward ∩ backward)
            middle_dict = get_partial_score(news[forward_index:len(news)-(backward_index+1)])
            score += (middle_dict[0]['score']+middle_dict[1]['score'])
    else:
        middle_dict = get_partial_score(news)
        score += (middle_dict[0]['score']+middle_dict[1]['score'])
    return score

# host = "172.31.238.166"
host = "172.31.238.141" # 最新的news所在的数据库
port = 3306
# user = "luowang"
# passwd = "root"
# db ="wise"
user = "wise_r"
passwd = "wise_r"
db = "wise"
charset = "UTF8"

def test():
    error = 0
    num = 0
    fileList = os.listdir('test')
    print('WEIGHT =',WEIGHT)
    for file in fileList:
        filename = 'test\\%s'%(file)
        with open(filename,'r',encoding='utf-8') as f:
            score = get_score(f.read())
            if file.startswith('neg') and score>0:
                error+=1
            elif file.startswith('pos') and score<0:
                error+=1
            elif file.startswith('neu') and score!=0:
                error+=1
        num+=1
    print("  rate =",1-error/num)
    return 1-error/num

def getWeight():
    global WEIGHT
    weightList = np.linspace(1,3,200,endpoint=True)
    rateList = [None]*200
    for weight,(index,rate) in zip(weightList,enumerate(rateList)):
        WEIGHT = weight
        rateList[index] = test()
    with open('weightRate.plk','wb')as f:
        List = list(zip(weightList,rateList))
        pickle.dump(List,f)
    print('写入 weightRate.plk 成功')

def get2016AllScore():
    try:
        # command = "select id,pub_date,news_content from dyx_emotion_analysis where pub_date between '2016-01-01' and '2016-12-31';"
        command = "select id,pub_date,news_content from wise_news where pub_date between '2016-01-01' and '2016-12-31';" # 针对最新的数据库
        conn = pymysql.Connect(host = host,port=port,user=user,passwd=passwd,db=db,charset=charset)
        cursor = conn.cursor()
    except Exception as error:
        print('连接失败',end=' ')
        print('原因是：\n',error)
    else:
        print('连接成功')
        print('执行中ing')

        baseStamp = time.mktime(time.strptime('2016-01-01','%Y-%m-%d')) #2016年的第一天的时间戳
        rsList = []
        cursor.execute(command)
        lineCount = cursor.rowcount
        for i in range(lineCount):
            rs = cursor.fetchone()
            rsDict = dict()
            rsDict['id'] = rs[0]
            rsDict['date'] = rs[1]
            nowStamp = time.mktime(time.strptime(rsDict['date'],'%Y-%m-%d')) # 现在的时间戳
            rsDict['days'] = (int)((nowStamp-baseStamp)/(24*60*60)) # 拿到天数差方便画图
            # 在处理成绩的时候会有各种bug
            try:
                news = cht_to_chs(clean_html(rs[2]))
                rsDict['score'] = get_score(news)
            except Exception as error:
                rsDict['score'] = 0
            else:
                pass 
            
            print('Index at:',i,rsDict)
            rsList.append(rsDict)
        with open('2016AllScore.plk','wb')as f:
            pickle.dump(rsList,f)

        print('执行完毕')
        cursor.close()
        conn.close()
if __name__=='__main__':
    get2016AllScore()