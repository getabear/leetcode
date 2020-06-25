from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums)<2:
            return
        nums.sort()
        slow=0
        ret=0
        while slow<len(nums):
            ret+=nums[slow]
            slow+=2
        return ret
a=Solution()
nums=[1,4,3,2]
print(a.arrayPairSum(nums))