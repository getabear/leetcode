from typing import List

class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #暴力枚举，超时
        length=len(nums)
        if length==0:
            return 0
        res=0
        dp=[[0]*length for i in range(length)]
        for i in range(length):
            for j in range(i,length):
                if i==j:
                    dp[i][j]=nums[j]
                else:
                    dp[i][j]=dp[i][j-1]+nums[j]
                if dp[i][j]==k:
                    res+=1
        return res
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        length=len(nums)
        if length==0:
            return 0
        sum=0
        res=0
        mem=dict()
        for index,num in enumerate(nums):
            sum+=num
            if sum==k:
                res+=1
            if sum-k in mem:
                res+=mem[sum-k]
            if sum in mem:
                mem[sum]+=1
            else:
                mem[sum]=1
        return res

a=Solution()
print(a.subarraySum([-1,-1,1],0))
