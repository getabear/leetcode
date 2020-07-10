from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1<<31-1 为有符号的最大整数，1<<32-1 为无符号最大整数
        dp=[1<<31-1]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0 and dp[i-coin]!=-1:
                    dp[i]=min(dp[i-coin]+1,dp[i])
            if dp[i]==1<<31-1:
                dp[i]=-1
        return dp[amount]

a=Solution()
coins = [2147483647]
amount = 2
print(a.coinChange(coins,amount))