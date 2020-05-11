from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #利用桶来实现查找缺失的数字
        length=len(nums)
        bucket=[-1 for i in range(length+1)]
        for i in nums:
            bucket[i]=i
        for i in range(length+1):
            if bucket[i]!=i:
                return i
a=Solution()
print(a.missingNumber([1]))