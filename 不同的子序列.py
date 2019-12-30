class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        #提交后通过了51个测试用例,就超时了,但是证明算法是正确的
        self.res=0
        def fun(s,t):
            if len(t)==0:
                self.res+=1
                return
            if len(s)==0:
                return
            for i in range(len(s)):
                if s[i]==t[0]:
                    fun(s[i+1:],t[1:])
            return
        fun(s,t)
        return self.res

class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        #解决重复的子问题,加了mem后通过了提交
        self.res=0
        map={}
        def fun(s,s_start,t,t_start):
            if len(t)==t_start:
                self.res+=1
                return
            if len(s)==s_start:
                return
            if (s_start,t_start) in map:
                self.res+=map[(s_start,t_start)]
                return
            tp=self.res
            if s[s_start]==t[t_start]:
                fun(s,s_start+1,t,t_start+1)
            fun(s,s_start+1,t,t_start)
            map[(s_start,t_start)]=self.res-tp
            return
        fun(s,0,t,0)
        return self.res

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #最后动态规划
        #1.dp[m][n]的含义是从s[m:]中有几个t[n:]
        #2.状态转移方程   s[m]==t[n] 则 dp[m][n]=dp[m+1][n+1]+dp[m+1][n]
        #                        否则 dp[m][n]=dp[m+1][n]
        # 3.初始情况   当m=s_len时 dp[m][n]=0
        #            当n=t_len时  dp[m][n]=1
        dp=[[0  for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][len(t)]=1

        t_len=len(t)-1
        s_len=len(s)-1
        size=s_len
        sizet=t_len
        while sizet>=0:
            while size>=0:
                if s[size]==t[sizet]:
                    dp[size][sizet]=dp[size+1][sizet+1]+dp[size+1][sizet]
                else:
                    dp[size][sizet]=dp[size+1][sizet]
                size-=1
            size=s_len
            sizet-=1
        return dp[0][0]

a=Solution()
S="aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
T="bddabdcae"
import time
print(time.process_time())
print(a.numDistinct(S,T))
print(time.process_time())