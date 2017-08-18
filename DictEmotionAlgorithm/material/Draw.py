#encoding:utf-8
import pickle
import matplotlib.pyplot as plt
import numpy as np
from operator import itemgetter

def drawScatter(scoreList):
    freqScore = dict()
    for score in scoreList:
        if freqScore.get(int(score['score']),'no')=='no':
            freqScore[abs(int(score['score']))] = 1
        else:
            freqScore[abs(int(score['score']))]+=1

    freqList = sorted(freqScore.items(),key=lambda score:score[0])
    length = len(freqList)
    firstScore = freqList[int(length*0.9)][0] #第一梯队分界线
    secondScore= freqList[int(length*0.8)][0] #第二梯队分界线

    firstXList = []
    firstYList = []
    secondXList = []
    secondYList = []
    thirdXList = []
    thirdYList = []

    for score in scoreList:
        if firstScore<=abs(score['score']):
            firstXList.append(score['days'])
            firstYList.append(score['score'])
        elif secondScore<=abs(score['score'])<firstScore:
            secondXList.append(score['days'])
            secondYList.append(score['score'])     
        else:
            thirdXList.append(score['days'])
            thirdYList.append(abs(score['score']))

    plt.scatter(firstXList,firstYList,label='Most Score',alpha=0.6,s=3,c='b')
    plt.scatter(secondXList,secondYList,label='Little Score',alpha=1,s=5,c='r',marker='+')
    plt.scatter(thirdXList,thirdYList,label='Scarce Score',alpha=0.8,s=5,c='g',marker='x')
    plt.xlabel('Days from 2015.01.01')
    plt.ylabel('Score')

    plt.legend(loc='upper left')
    plt.title('Scatter of Score Distribution')
    plt.show()

def drawHist(scoreList):
    scores = []#all scores
    for score in scoreList:
        scores.append(score['score'])
    plt.hist(scores,300,color='g',alpha=0.67)
    plt.xlabel('Score')
    plt.ylabel('Times')
    plt.title('Histogram of Score Distribution')
    #plt.legend('upper right')
    plt.show()

if __name__=='__main__':
    scoreList = []
    with open('2015AllScore.plk','rb')as f: #打开格式。注意结构格式
        scoreList = pickle.load(f)

    # print(scoreList[0])
    drawScatter(scoreList)
    drawHist(scoreList)
