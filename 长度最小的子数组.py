from typing import List

class Solution1:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        # 暴力法,毫无疑问失败了...
        res=1
        length=len(nums)
        dp=[0 for _ in nums]
        for j in range(1,length+1):
            for i in range(length):
                if i+res-1<length:
                    dp[i]+=nums[i+res-1]
                else:
                    break
                if dp[i]>=s:
                    return res
            res+=1
        return 0

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        #双指针法:没想到双指针还可以这样用
        total=0
        res=len(nums)+1
        left=0
        for i in range(len(nums)):
            total+=nums[i]
            right=i
            while total>=s:
                res=min(res,right-left+1)
                total-=nums[left]
                left+=1
        return res if res!=len(nums)+1 else 0



s=4
nums=[2,3,1,2,4,3]
a=Solution()
print(a.minSubArrayLen(s,nums))
