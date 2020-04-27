from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            #左边有序
            if nums[0]<=nums[mid]:
                if target>=nums[left] and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
a=Solution()
nums=[3,1]
target=1
print(a.search(nums,target))