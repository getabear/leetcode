from typing import List

class Solution:
    #解法1  暴力法,一次遍历,提交后居然通过了,我人突然傻掉了,时间复杂度O(n)
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        ret=nums[0]
        for i in nums:
            ret=min(ret,i)
        return ret

#方法二:    二分法
class Solution1:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

a=Solution1()
nums=[3,4,5,6,7,0,1,2]
print(a.findMin(nums))