# 回溯递归，提交后超时了
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        self.ret=0
        def fun(s_idx,t_idx):
            if t_idx==len(t):
                self.ret+=1
                return
            if len(t)-t_idx>len(s)-s_idx:
                return
            for idx in range(s_idx,len(s)):
                if t[t_idx]==s[idx]:
                    fun(idx+1,t_idx+1)
        fun(0,0)
        return self.ret
#加入字典的回溯递归通过了提交，但是时间复杂度依旧不够低
class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        mem=dict()
        self.ret=0
        def fun(s_idx,t_idx):
            if (s_idx,t_idx) in mem:
                self.ret+=mem[(s_idx,t_idx)]
                return
            if t_idx==len(t):
                self.ret+=1
                return
            if len(t)-t_idx>len(s)-s_idx:
                return
            temp=self.ret
            for idx in range(s_idx,len(s)):
                if t[t_idx]==s[idx]:
                    fun(idx+1,t_idx+1)
            mem[(s_idx,t_idx)]=self.ret-temp
        fun(0,0)
        return self.ret
#使用动态规划
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


a=Solution()
S = "babgbag"
T = "bag"
print(a.numDistinct(S,T))