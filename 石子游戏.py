from typing import List
class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        #暴力法，时间复杂度过高，超时
        def fun(flag,start,end):
            if start==end:
                if flag==0:
                    return piles[start]
                else:
                    return 0
            if flag==0:
                ret1=fun(1,start+1,end)
                ret2=fun(1,start,end-1)
                return max(ret1+piles[start],ret2+piles[end])
            elif flag==1:
                ret1=fun(0,start+1,end)
                ret2=fun(0,start,end-1)
                return min(ret1,ret2)
        tmp=fun(0,0,len(piles)-1)
        tmp2=sum(piles)-tmp
        return tmp>tmp2

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[[[0]*2 for j in range(n)] for i in range(n)]
        #dp[s][e][0]的含义时,从s到e的下标先手取得的最大值
        for i in range(n):
            dp[i][i][0]=piles[i]
        for b in range(1,n):
            for r in range(b,n):
                l=r-b
                left=dp[l+1][r][1]+piles[l]
                right=dp[l][r-1][1]+piles[r]
                if left>right:
                    dp[l][r][0]=left
                    dp[l][r][1]=dp[l+1][r][0]
                else:
                    dp[l][r][0]=right
                    dp[l][r][1]=dp[l][r-1][0]
        return dp[0][n-1][0]>dp[0][n-1][1]

import time
a=Solution()
piles=[5,100,5]
print(a.stoneGame(piles))
print(time.process_time())
