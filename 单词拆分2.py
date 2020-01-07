from typing import List
from collections import defaultdict

class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.ret=[]
        #毫无悬念超出时间限制...,因为太多重复子问题
        wordDict=set(wordDict)
        def dfs(s,start,res):
            if len(s)==start:
                self.ret.append(res[:-1])
                return
            for i in range(start,len(s)+1):
                if s[start:i] in wordDict:
                    dfs(s,i,res+s[start:i]+" ")

        dfs(s,0,"")

        return self.ret


class Solution:
    #解题结果正确,但是leetcode需要顺序也正确就很烦
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        #自底向上的动态规划
        #1.定义 dp[i]为从s[i]到s的末尾的排列组合
        #2.状态转移方程  if s[?:i] in wordDict:
        #               for x in dp[i]:
        #                   dp[?].append(s[?:i]+" "+x)
        #             if s[?:] in wordDict:
        #               dp[?:].append(s[?:])
        #3.初始状态  dp[i]=s的最后的最短的一个单词
        #返回值 dp[0]为答案

        # 建立列表的字典
        dp=defaultdict(list)

        wordDict=set(wordDict)  #形成字典,查询复杂度为O(1)

        #建立初始化状态
        for i in range(len(s)-1,-1,-1):
            if s[i:] in wordDict:
                dp[i].append(s[i:])
                break

        queue=[i]
        while(queue):
            index=queue.pop(0)
            if index==0:
                break
            for i in range(index-1,-1,-1):
                if s[i:index] in wordDict:
                    for x in dp[index]:
                        dp[i].append(s[i:index]+" "+x)
                        if i not in queue:
                            queue.append(i)
                if s[i:] in wordDict:
                    dp[i].append(s[i:])
                    if i not in queue:
                        queue.append(i)
            del dp[index]

        return dp[0]

a=Solution1()
s="aaaaaaa"
wordDict=["aaaa","aa","a"]


ret=a.wordBreak(s,wordDict)
print(ret)
tp=[]
# ["aaaa aa a","aaaa a a a","aaaa a aa","aa aaaa a","aa aa aa a","aa aa a a a","aa aa a aa","aa a aaaa","aa a aa a a","aa a aa aa","aa a aaaa","aa a a aa a","aa a a a a a","aa a a a aa","aa a aaaa","a aaaa a a","a aaaa aa","a aa aaaa","a aa aa a a","a aa aa aa","a aa aaaa","a aa a aa a","a aa a a a a","a aa a a aa","a aa aaaa","a a aaaa a","a a aa aa a","a a aa a a a","a a aa a aa","a a a aaaa","a a a aa a a","a a a aa aa","a a a aaaa","a a a a aa a","a a a a a a a","a a a a a aa","a a a aaaa"]
temp=["a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"]
for i in temp:
    if i in ret:
        tp.append(i)
print(len(tp))
print(len(temp))
print(tp==temp)
