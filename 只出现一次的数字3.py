from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        mem=set()
        for i in nums:
            if i not in mem:
                mem.add(i)
            else:
                mem.remove(i)
        res=[]
        for i in mem:
            res.append(i)
        return res