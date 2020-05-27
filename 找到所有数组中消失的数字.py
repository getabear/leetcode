from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        n=len(nums)
        dp=[0]*(n+1)
        dp[0]=1
        for i in nums:
            dp[i]=1
        ret=[]
        for i in range(n+1):
            if dp[i]==0:
                ret.append(i)
        return ret
a=Solution()
nums=[4,3,2,7,8,2,3,1]
print(a.findDisappearedNumbers(nums))