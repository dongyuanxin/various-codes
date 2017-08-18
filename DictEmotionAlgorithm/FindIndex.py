def find_index(article,forward_num=2,backward_num=2):
    '''
    article:字符串文章
    forward_num:前n句
    backward_num:后n句
    返回类型：[font_index,back_index]。不存在的话为None
    
    调用的时候：
    正向：sentence[:index+1]
    反向：sentence[index+1:]
    '''
    backward_num = backward_num +1 #语言特性，注意！！！
    punctuation = "。！？"
    x1 = article.count("。")
    x2 = article.count("!")
    x3 = article.count("？")
    if x1+x2+x3 <= forward_num+backward_num-1:
        return [None,None] #当句子太少的时候，认为没有意义
    else:
        forward_flag = 0
        forward = [] #记录每个符号在forward_num到达的最远位置
        for punc in punctuation:
            count = 0 #记录统计多少个符号
            punc_position = 0 #前n句的i符号的句界线
            tem = article.find(punc,punc_position,len(article))
            while tem>=0 and count<forward_num:
                forward_flag = 1 #标志变量，只要进入循环，说明找到了标点
                count = count+1
                punc_position = tem
                #print("符号是：",punc,".位置是：",punc_position,"count:",count)#调试样例
                tem = article.find(punc,punc_position+1,len(article))

            if punc_position!=0:#只有找到这个标点的时候
                forward.append(punc_position)

        backward_flag = 0
        backward = []
        tem_article = article[::-1] 
        for punc in punctuation:
            count = 0
            punc_position = 0 #舍弃最后一个符号
            tem = tem_article.find(punc,punc_position,len(tem_article))
            while tem>=0 and count<backward_num:
                backward_flag  = 1
                count = count +1
                punc_position = tem
                #print("符号是：",punc,".位置是：",punc_position,"count:",count)
                tem = tem_article.find(punc,punc_position+1,len(tem_article))
            if punc_position:
                backward.append((-1)*(1+punc_position))
        #print(backward)

        if forward_flag and backward_flag:
            return [min(forward),min(backward)]
        elif forward_flag:
            return [min(forward),None]
        elif backward_flag:
            return [None,min(backward)]
        else :
            return [None,None]
           
if __name__=="__main__":
    s = "你好，再见。我真的恶不主动if噢违法。方法，么法我一。风飞花？凤凰飞！牛瑞瑞、分。0附近热熊积分。"  
    ss = "fef，efef"
    #print(s[-1],s[-15],s[-19])
    print(find_index(s))
    print(s[0:18],'\n',s[-19:-1])
    print(find_index(ss))

