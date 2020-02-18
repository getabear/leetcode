from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ret=0
        for i in nums:
            tp=0
            while i!=0:
                i//=10
                tp+=1
            if tp&0x1==0:
                ret+=1
        return ret

a=Solution()
nums=[555,901,482,1771]
print(a.findNumbers(nums))