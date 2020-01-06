class Solution1:
    def minCut(self, s: str) -> int:
        #上一个程序的改版,处提交超时了
        #1.定义dp数组,dp[i][j] 为字符串s[i]到s[j]是否为回文串
        dp=[[False for i in s] for i in s]
        #2.状态转移方程  dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        #3.初始状态  dp[i][i]=True
        for i in range(len(s)):
            dp[i][i]=True
        for j in range(1,len(s)):
            for i in range(j):
                if i+1<=j-1:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                else:
                    dp[i][j]= s[i]==s[j]
        self.ret=[]

        def dfs(s, i, tp):
            if i == len(s):
                self.ret.append(tp[:])
                return
            for index in range(i, len(s)):
                if dp[i][index]:
                    dfs(s, index + 1, tp + [s[i:index + 1]])

        dfs(s, 0, [])
        res=len(dp)-1
        for i in self.ret:
            if len(i)-1<res:
                res=len(i)-1
        return res

class Solution:
    def minCut(self, s: str) -> int:
        #1.定义dp数组,dp[i][j] 为字符串s[i]到s[j]是否为回文串
        dp=[[False for i in s] for i in s]
        #2.状态转移方程  dp[i][j]=dp[i+1][j-1] and s[i]==s[j]
        #3.初始状态  dp[i][i]=True
        for i in range(len(s)):
            dp[i][i]=True
        for j in range(1,len(s)):
            for i in range(j):
                if i+1<=j-1:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                else:
                    dp[i][j]= s[i]==s[j]
        self.ret=len(dp)-1
        rec={}  #利用字典记录,空间减少时间复杂度,,提交通过击败41%
        def dfs(cut,i):
            if i in rec:
                if rec[i]+cut<self.ret:
                    self.ret=rec[i]+cut
                return
            if i==len(s):
                if self.ret>cut-1:
                    self.ret=cut-1
                return
            for index in range(i,len(s)):
                if dp[i][index]:
                    dfs(cut+1,index+1)
            if self.ret>=cut:
                rec[i]=self.ret-cut
        dfs(0,0)
        return self.ret
s="aab"
a=Solution()
print(a.minCut(s))