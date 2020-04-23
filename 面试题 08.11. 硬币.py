class Solution:
    def waysToChange(self, n: int) -> int:
        coins=[5,10,25]

        dp=[1 for i in range(n+1)]
        # dp[0]=1

        for coin in coins:
            for i in range(1,n+1):
                if i>=coin:
                    dp[i]=dp[i]+dp[i-coin]

        return dp[n]%1000000007


