from typing import List

class Solution1:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 用的字典，咱们用分组异或
        dc1=set()
        for i in nums:
            if i in dc1:
                dc1.remove(i)
            else:
                dc1.add(i)
        res=[]
        for i in dc1:
            res.append(i)
        return res

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ret=0
        for i in nums:
            ret^=i
        a,b=0,0
        mask = 1
        while ret & mask == 0:
            mask = mask << 1
        for num in nums:
            if num & mask == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]



