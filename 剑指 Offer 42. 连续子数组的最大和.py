from typing import List

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        dp=[0]*n
        dp[0]=nums[0]
        ret=nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
            ret=max(ret,dp[i])
        return ret

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp_1=nums[0]
        ret=nums[0]
        for i in range(1,len(nums)):
            dp_1=max(dp_1+nums[i],nums[i])
            ret=max(dp_1,ret)
        return ret
a=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(a.maxSubArray(nums))
