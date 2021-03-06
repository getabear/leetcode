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
        #处理最后一行
        while index<len(words):
            if index!=len(words)-1:
                s+=words[index]+" "
            else:
                s += words[index]
            index+=1
        ret.append(s+" "*(maxWidth-len(s)))
        return ret

#附上leetcode上大佬的代码
class Solution1:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        l = 0
        s = []
        # 先将单词保存
        for i in range(len(words)):
            if l + len(words[i]) <= maxWidth:
                l = l + len(words[i]) + 1
                s.append(words[i])
            else:
                res.append(s)
                l = len(words[i]) + 1
                s = [words[i]]
        res.append(s)

        # 根据单词放空格
        ans = []
        for word in res[:-1]:
            if len(word) == 1:
                ans.append(word[0] + ' ' * (maxWidth - len(word[0])))
            elif len(word) == 2:
                ans.append(word[0] + ' ' * (maxWidth - len(word[0]) - len(word[1])) + word[1])
            else:  # 单词数大于2时
                sum1 = sum([len(i) for i in word])

                m = (maxWidth - sum1) // (len(word) - 1)
                n = (maxWidth - sum1) - m * (len(word) - 1)

                a = word[0]
                i = 1
                while i < len(word):
                    if n > 0:
                        a = a + ' ' * (m + 1) + word[i]
                    else:
                        a = a + ' ' * m + word[i]
                    i += 1
                    n -= 1
                ans.append(a)
        # 处理最后一行
        b = res[-1][0]
        i = 1
        while i < len(res[-1]):
            b = b + ' ' + res[-1][i]
            i += 1
        b += (maxWidth - len(b)) * ' '
        ans.append(b)

        return ans


a=Solution()
words = ["What","must","be","acknowledgment","shall","be"]
r=a.fullJustify(words,16)
for i in r:
    print(i)