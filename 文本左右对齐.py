from typing import List



#这道题把我恶心到了,太细节了
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        tmp=0  #用于记录单词长度
        ret=[]
        count=0
        index=0
        i=0
        while(i<len(words)):
            if tmp+len(words[i])<=maxWidth:
                tmp+=len(words[i])+1
                count+=1
            else:
                tp=maxWidth-tmp+count  #空格总个数
                index += count
                s = ""
                if count!=1:
                    tp1=tp%(count-1)  #看是否可以平分空格
                    tp2=tp//(count-1) #每个地方空几个空格
                    if tp1!=0:
                        s+=words[index-count]+" "*(tp1+tp2)
                        count-=1
                    while(count>1):
                        s+=words[index-count]+" "*tp2
                        count-=1
                    s+=words[index-1]
                    ret.append(s)
                    s=""
                    count=0
                    tmp=0
                if count==1:
                    s+=words[index-1]+" "*tp
                    ret.append(s)
                    count=0
                    tmp=0
                    s=""
                continue

            i+=1
        while index<len(words):
            if index!=len(words)-1:
                s+=words[index]+" "
            else:
                s += words[index]
            index+=1
        ret.append(s+" "*(maxWidth-len(s)))
        return ret




a=Solution()
words = ["What","must","be","acknowledgment","shall","be"]
r=a.fullJustify(words,16)
for i in r:
    print(i)