from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mem=dict()
        length=len(nums)
        tmp=length//3
        res=[]
        for i in nums:
            if i not in mem:
                mem[i]=1
            else:
                mem[i]+=1
        for m,n in mem.items():
            if n>tmp:
                res.append(m)
        return res

nums=[1,1,1,3,3,2,2,2]
a=Solution()
print(a.majorityElement(nums))