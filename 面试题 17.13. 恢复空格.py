from typing import List

class Solution1:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n=len(sentence)
        mem=set(dictionary)
        self.ret=n
        def fun(idx,stack):
            if idx==n:
                unknown=0
                for i in stack:
                    if i not in mem:
                        unknown+=len(i)
                self.ret=min(unknown,self.ret)
                return
            for i in range(idx+1,n+1):
                stack.append(sentence[idx:i])
                fun(i,stack)
                stack.pop()
            return
        fun(0,[])
        return self.ret

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        n=len(sentence)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=dp[i-1]+1
            for word in dictionary:
                if i>=len(word):
                    if sentence[i-len(word):i]==word:
                        dp[i]=min(dp[i],dp[i-len(word)])
        return dp[-1]
sentence="jesslookedjustliketimherbrother"
dictionary = ["looked","just","like","her","brother"]
a=Solution()
print(a.respace(dictionary,sentence))