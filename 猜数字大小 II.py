class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][i]=0
        for b in range(1,n+1):    #根据分析，我们需要斜着遍历数组，根据y=kx+b，斜率是不变的截距b在改变
            for i in range(1,n+1):  #确定x，这里的i代表x
                j=i+b               #确定y，这里的j代表y
                if j>n:             #防止越界
                    break
                for k in range(i,j+1):
                    if k==i:    #处理边界
                        dp[i][j] =k+dp[k+1][j]
                    elif k==j:   #处理边界
                        dp[i][j] =min(dp[i][j],k+dp[i][k-1])
                    else:
                        dp[i][j]=min(dp[i][j],k+max(dp[i][k-1],dp[k+1][j]))
        return dp[1][n]

a=Solution()
print(a.getMoneyAmount(10))