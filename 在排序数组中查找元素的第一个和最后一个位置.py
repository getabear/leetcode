from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 细节很麻烦,正如kmp算法发明者说的:
        #Although the basic idea of binary search is comparatively straightforward,
        #the details can be surprisingly tricky...
        left=0
        right=len(nums)
        if right==0:
            return [-1,-1]
        mid=(left+right)//2
        while(left<right):
            if nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            else:#nums[mid]==target
                temp=mid
                while(temp>=0 and nums[temp]==target):
                    temp-=1
                temp+=1
                while(mid<len(nums) and nums[mid]==target ):
                    mid+=1
                mid-=1
                return [temp,mid]
            if mid==(right+left)//2:
                break
            mid=(right+left)//2
        return [-1,-1]

a=Solution()
nums = [1]
target=1
print(a.searchRange(nums,target))