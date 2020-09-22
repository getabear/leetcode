from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ret=[0]*len(nums)
        left,right=0,len(nums)-1
        for num in nums:
            if num&0x1==1:   #奇数
                ret[left]=num
                left+=1
            else:
                ret[right]=num
                right-=1
        return ret


nums=[1,2,3,4]
a=Solution()
a.exchange(nums)
print(nums)