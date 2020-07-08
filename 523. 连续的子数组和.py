from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp=[0 for i in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=dp[i-1]+nums[i]
            if k!=0:
                if dp[i]%k==0:
                    return True
            else:
                if dp[i]==0:
                    return True
        for i in range(2,len(nums)):
            for j in range(i-1):
                dp[i]-=nums[j]
                if k!=0:
                    if dp[i]%k==0:
                        return True
                else:
                    if dp[i]==0:
                        return True
        return False


nums=[0,1,0]
k = 0
a=Solution()
print(a.checkSubarraySum(nums,k))