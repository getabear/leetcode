from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #看了大佬的解法,这道题用滑动窗口和hash表解决较好
        hash_map={}
        ret=[]
        if not s or not words:
            return []

        one_len=len(words[0])  #一个单词长度
        s_len=len(s)            #字符串长度
        all_len=one_len*len(words)  #所有单词长度

        def build_hash(words,map):   #建立hash_map函数
            for i in words:
                if i not in map:
                    map[i]=1
                else:
                    map[i]+=1
        def build_s_hash(s):   #判断是否符合条件
            i=0
            map={}
            while(i<all_len):
                if s[i:i+one_len] in hash_map:
                    if s[i:i+one_len] not in map:
                        map[s[i:i+one_len]]=1
                    else:
                        map[s[i:i + one_len]] += 1
                        if map[s[i:i + one_len]]>hash_map[s[i:i + one_len]]:
                            return False
                else:
                    return False
                i+=one_len
            return map==hash_map

        def fun(s):
            for i in range(s_len-all_len+1):
                if build_s_hash(s[i:all_len+i]):
                    ret.append(i)

        build_hash(words,hash_map)   #先建立单词表
        fun(s)
        return ret
'''
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        #方法一:暴力法,很明显提交又超时了...心态有点崩
        strs=[]
        ret=[]
        def fun(s,word):
            length=len(word)
            for i in range(len(s)-length+1):
                if s[i:length+i]==word:
                    if i not in ret:
                        ret.append(i)


        def generate(words,s):   #这里生成子串耗费了很多时间,  会生成差不多n!个子串(如果含有重复单词就不会)
            if len(words)==1:
                if s+words[0] not in strs:
                    strs.append(s + words[0])
                return
            else:
                for i in range(len(words)):
                    wds=words[:]
                    wds.pop(i)
                    generate(wds,s+words[i])

        if len(s)==0 or len(words)==0:
            return []
        else:
            generate(words, "")#生成子串
            for i in strs:
                fun(s,i)
        return ret
'''


a=Solution()
s ="barfoothefoobarman"
words = ["foo","bar"]
print(a.findSubstring(s,words))