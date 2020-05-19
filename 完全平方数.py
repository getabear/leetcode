class Solution1:
    def numSquares(self, n: int) -> int:

        self.res=n
        def fun(n,step):
            if n<0:
                return
            if n==0:
                self.res=min(self.res,step)
                return
            for i in range(1,n):
                fun(n-i*i,step+1)
            return

        fun(n,0)
        return self.res
import math
class Solution:
    def numSquares(self, n: int) -> int:
        square_nums=[i**2 for i in range(0,int(math.sqrt(n))+1)]
        dp=[i for i in range(n+1)]
        for i in range(n+1):
            for j in square_nums:
                if i<j:
                    break
                dp[i]=min(dp[i],dp[i-j]+1)
        return dp[n]


a=Solution()
print(a.numSquares(12))