from typing import List


class Solution1:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 穷举的方式,超时了,通过205个测试用例
        self.ret = 0
        length = len(prices)

        def fun(index, k, flag, profit):
            if (index == length or k == 0):
                if profit > self.ret:
                    self.ret = profit
                return
            if flag:  # 如果持有股票
                fun(index + 1, k, flag, profit)  # 保持
                fun(index + 1, k - 1, 0, profit + prices[index])  # 卖出
            else:
                fun(index + 1, k, flag, profit)  # 保持
                fun(index + 1, k, 1, profit - prices[index])  # 买入
            return

        fun(0, k, 0, 0)
        return self.ret


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)

        if length==0:
            return 0

        if k>length:    #贪心算法,当交易次数多余价格的长度
            profit=0
            for i in range(1,length):
                diff=prices[i]-prices[i-1]
                profit+=diff if diff>0 else 0
            return profit

        # dp数组含义 dp[1][0][i]表示交易次数为1次,[0]未持有股票,prices[0]到princes[i]中的最大利益
        #          dp[1][1][i]表示交易次数为1次,[1]持有股票,prices[0]到princes[i]中的最大利益
        dp = [[[0 for z in range(length)] for j in [0, 1]] for i in range(k + 1)]

        for i in range(1, k + 1):
            for z in range(0,length):
                if z==0:
                    dp[i][1][0]=-prices[0]
                    dp[i][0][0]=0
                else:
                    dp[i][1][z] = max(dp[i][1][z - 1], dp[i-1][0][z - 1] - prices[z])
                    dp[i][0][z] = max(dp[i][0][z - 1], dp[i][1][z - 1] + prices[z])

        return dp[k][0][length-1]


a = Solution()
prices =[3,2,6,5,0,3]
print(a.maxProfit(2, prices))
