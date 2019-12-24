from typing import List

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        #方法1:递归思路,超时了
        self.ret=0
        def fun(prices,flag,n,tp):
            if len(prices)==0 or n==0:
                if tp>self.ret:
                    self.ret=tp
                return
            if flag:#持有
                fun(prices[1:],0,n-1,tp+prices[0])
            else:  #未持有
                fun(prices[1:],1,n,tp-prices[0])
            #保持
            fun(prices[1:],flag,n,tp)
            return

        fun(prices,0,1,0)
        return self.ret

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size=len(prices)
        if size<=1:
            return 0
        dp=[[0,0] for i in range(size)]
        #dp[i][0]代表第i天未持有股票的利益
        #dp[i][1]代表第i天持有股票的利益
        for i in range(size):
            if i==0:#处理i-1越界问题
                dp[i][0]=0
                dp[i][1]=-prices[i]
                continue
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])

            # 由于只能买卖一次,所以持有时不能是max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][1]=max(dp[i-1][1],-prices[i])
        return dp[size-1][0]



a=Solution()
print(a.maxProfit([7,1,5,3,6,4]))