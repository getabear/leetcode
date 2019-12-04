import time
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0 for i in range(0,n+2)]
        # print(dp)
        def fun(i,n):
            if i!=0 and dp[i]!=0:
                return dp[i]
            if i>n:
                dp[i]=0
                return 0
            if i==n:
                dp[i]=1
                return 1
            dp[i]=fun(i+1,n)+fun(i+2,n)
            return dp[i]
        return fun(0,n)

a=Solution()
for i in range(1,10):
    print(a.climbStairs(i))
print(time.process_time())