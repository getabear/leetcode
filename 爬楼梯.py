import time
class Solution1:
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

class Solution:
    def climbStairs(self, n: int) -> int:
        dp_1=2    #前一步的方法数
        dp_2=1    #前两步的方法数
        if n==1:
            return 1
        if n==2:
            return 2
        start=3
        while start<=n:
            tmp=dp_1+dp_2
            dp_2=dp_1
            dp_1=tmp
            start+=1
        return tmp
a=Solution1()
for i in range(1,10):
    print(a.climbStairs(i))
print(time.process_time())