from typing import List

class Solution1:
    #提交后超时了,但是会少说明算法是对的
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        for word in wordDict:
            size=len(word)
            if s[:size]==word:
                ans=self.wordBreak(s[size:],wordDict)
                if ans:
                    return ans
                else:
                    continue
        return False
class Solution2:
    #优化算法,解决子问题,加了字典用以记录,成功提交通过超越98%的提交
    def __init__(self):
        self.mem={}
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
        for word in wordDict:
            size=len(word)
            if s[:size]==word:
                if len(s[size:]) in self.mem:
                    ans=self.mem[len(s[size:])]
                else:
                    ans=self.wordBreak(s[size:],wordDict)
                if ans:
                    return ans
                else:
                    self.mem[len(s)]=ans
                    continue
        return False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #使用动态规划
        #dp数组含义，dp[i]代表从i到s的末尾是否可以拆分
        dp=[False]*(len(s)+1)
        #初始状态：
        dp[len(s)]=True
        #状态转移  dp[i]=s[i:i+len(word)]==word and dp[i+len(word)]
        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                n=len(word)
                if i+n>len(s):
                    dp[i]=False
                else:
                    dp[i]=s[i:i+n]==word and dp[i+n]
                    if dp[i]:
                        break
        return dp[0]

a=Solution()
s="leetcode"
wordDict=["leet","code"]
print(a.wordBreak(s,wordDict))