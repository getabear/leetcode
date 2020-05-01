from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        length=len(nums)
        if length==0:
            return []
        if length==1:
            return [str(nums[0])]
        ret=[]
        start,slow,fast=0,0,1
        while start<length:
            tmp=str(nums[start])
            slow=start
            fast=slow+1
            while(fast<length):
                if nums[fast]==nums[slow]+1:
                    fast+=1
                    slow+=1
                else:
                    break
            if nums[start]!=nums[slow]:
                tmp+='->'+str(nums[slow])
            ret.append(tmp)
            start=fast
        return ret
