if __name__=='__main__':
    wordSet = set() #避免词语重复，采用集合结构
    with open('myDict.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            if len(line.strip('\n').strip())>=2 and ('.' not in line): #拿到规则的长度大于等于2的词语
                wordSet.add(line.strip('\n').strip())
    with open('userDict.txt','w',encoding='utf-8')as f:
        for word in wordSet:
            f.write(word+'  1000000\n') #每个词语保证分词效果，给予大的权重