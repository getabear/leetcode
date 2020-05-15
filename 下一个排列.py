import bisect
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1
        while index > 0:
            if nums[index] > nums[index - 1]:
                break
            index -= 1

        if index > 0:
            nums[index:] = sorted(nums[index:])
            swap_index = bisect.bisect(nums, nums[index - 1], lo=index)
            nums[swap_index], nums[index - 1] = nums[index - 1], nums[swap_index]
        else:
            nums.reverse()