from typing import List


#穷举所有可能,毫无悬念超时了,通过了198个测试用例,最后两个没通过
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        self.ret=0
        def fun(prices: List[int],n,profit,flag):
            if n==0 or len(prices)==0:
                if profit>self.ret:
                    self.ret=profit
                return
            if flag:#flag=1说明持有股票
                fun(prices[1:],n-1,profit+prices[0],0)#卖出
            else: #未持有股票
                fun(prices[1:],n,profit-prices[0],1)  #买入股票
            fun(prices[1:],n,profit,flag)#保持

        fun(prices,2,0,0)
        return self.ret

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size=len(prices)
        #dp[i][k][0]代表第i天未持有股票的利益   dp[i][k][1]代表第i天持有股票的利益 k是剩余交易次数
        dp=[[[0,0] for _ in range(3)] for _ in range(size) ]
        k=2
        if len(dp)==0:
            return 0
        for i in range(size):
            while k>=0:
                if i-1==-1:
                    dp[i][2][1] = -prices[i]
                    dp[i][2][0] = 0
                    dp[i][1][1]=-prices[i]
                    dp[i][1][0]=0
                    dp[i][0][1]=-prices[i]
                    dp[i][0][0]=0
                    break
                dp[i][k][1]=max(dp[i-1][k][1],dp[i-1][k][0]-prices[i])
                                    #保持               买入    [3,3,5,0,0,3,1,4]
                if k+1<3:
                    dp[i][k][0]=max(dp[i-1][k][0],dp[i-1][k+1][1]+prices[i])
                                    #保持              卖出
                else:
                    dp[i][k][0]=dp[i-1][k][0]

                k-=1
            k=2
        return dp[size-1][0][0]






a=Solution()
prices=[3,3,5,0,0,3,1,4]
print(a.maxProfit(prices))
