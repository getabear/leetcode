from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=0
        length=len(nums)
        while j<length:
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
            j+=1
        return i

a=Solution()
nums = [3,2,2,3]
val = 3
print(a.removeElement(nums,val))
print(nums)