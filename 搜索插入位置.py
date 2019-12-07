from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        mid=(left+right)//2
        if target<nums[0]:
            return 0
        while(left<right):
            if nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            else: #nums[mid]==target
                return mid
            if mid==(left+right)//2:
                return mid+1
            mid=(left+right)//2


a=Solution()
nums=[1,3,5,6]
target=0
print(a.searchInsert(nums,target))