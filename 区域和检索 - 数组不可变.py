from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        if n!=0:
            self.dp=[nums[0]]*n
            for i in range(1,n):
                self.dp[i]=self.dp[i-1]+nums[i]

    def sumRange(self, i: int, j: int) -> int:
        if i==0:
            return self.dp[j]
        else:
            return  self.dp[j]-self.dp[i-1]