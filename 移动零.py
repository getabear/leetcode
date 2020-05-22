from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length=len(nums)
        slow,fast=0,0
        while fast<length:
            if nums[fast]!=0:
                nums[slow],nums[fast]=nums[fast],nums[slow]
            if nums[slow]==0:
                fast+=1
            else:
                slow+=1
                fast+=1
        return

a=Solution()
nums=[0,1,0,3,12]
a.moveZeroes(nums)
print(nums)
