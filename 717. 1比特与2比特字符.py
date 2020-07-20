from typing import List

class Solution1:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #记忆递归
        nums=bits[:-1]
        mem=dict()
        def fun(idx):
            if idx in mem:
                return mem[idx]
            if idx>=len(nums):
                return idx==len(nums)
            res=False
            if nums[idx:idx+2] in [[1,0],[1,1]]:
                res=fun(idx+2)
            if not res:
                if nums[idx]==0:
                    res=fun(idx+1)
            mem[idx]=res
            return res
        return fun(0)

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        #使用dp
        n=len(bits)
        dp=[False for _ in range(n)]
        dp[n-1]=True
        if bits[n-2]==0:
            dp[n-2]=True
        for i in range(n-3,-1,-1):
            dp[i]=(dp[i+2] and bits[i:i+2] in [[1,1],[1,0]]) or \
                  (dp[i+1] and bits[i]==0)
        return dp[0]

a=Solution()
bits=[1, 1, 0]
print(a.isOneBitCharacter(bits))
