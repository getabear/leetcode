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
class Solution:
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

a=Solution1()
s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(a.wordBreak(s,wordDict))