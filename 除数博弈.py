class Solution1:
    def divisorGame(self, N: int) -> bool:
        if N<=1:
            return False
        dp=[[False for i in range(2)] for j in range(N+1)]
        #数字为1 轮到爱丽丝
        dp[1][0]=False
        #数字为1 轮到鲍勃
        dp[1][1]=True
        for i in range(2,N+1):
            for j in range(1,i):
                if i%j==0:
                    dp[i][0]=dp[i][0] or dp[i-j][1]   #有一次胜利的机会就胜利
            dp[i][1]=not dp[i][0]
        return dp[N][0]

class Solution:
    def divisorGame(self, N: int) -> bool:
        #奇数数，偶数赢
        return N&0x1==0
a=Solution()
print(a.divisorGame(5))