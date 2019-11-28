from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index1=0
        index2=1
        while index2 < len(nums):
            if nums[index1]==nums[index2]:
                nums.pop(index2)
            else:
                index1,index2=index1+1,index2+1
        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
a=Solution()
print(a.removeDuplicates(nums))
print(nums)