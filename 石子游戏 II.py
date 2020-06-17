from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        mem={}
        dp=[0]*len(piles)
        dp[-1]=piles[-1]   #dp数组用于记录从i到末尾的总和
        for i in range(len(piles)-2,-1,-1):
            dp[i]=piles[i]+dp[i+1]

        def fun(index,M):
            if (index,M) in mem:
                return mem[(index,M)]
            if index>=len(piles):
                return 0
            if index+2*M>=len(piles):
                return dp[index]
            ret=0
            for x in range(1,2*M+1):
                ret=max(dp[index]-fun(index+x,max(x,M)),ret)
            mem[(index,M)]=ret
            return ret
        return fun(0,1)

a=Solution()
piles=[8,9,5,4,5,4,1,1,9,3,1,10,5,9,6,2,7,6,6,9]
print(a.stoneGameII(piles))
