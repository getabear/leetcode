from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tp=[1 for i in nums]
        start=0
        end=len(tp)-1
        for i in nums:
            if i==0:
                tp[start]=i
                start+=1
            elif i==2:
                tp[end]=i
                end-=1
        for index,i in enumerate(tp):
            nums[index]=i

a=Solution()
nums=[2,0,2,1,1,0]
a.sortColors(nums)
print(nums)