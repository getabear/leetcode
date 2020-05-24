from typing import List
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp=nums[:]
        tmp.sort()
        l=0
        while(l<len(nums)):
            if nums[l]!=tmp[l]:
                break
            l+=1
        if l==len(nums):
            return 0
        start=l
        r=len(nums)-1
        while r>=0:
            if nums[r]!=tmp[r]:
                break
            r-=1
        end=r
        return end-start+1


a=Solution()
nums=[1,3,2,2,2]
print(a.findUnsortedSubarray(nums))