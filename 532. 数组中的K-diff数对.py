from typing import List
# 暴力法
class Solution1:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k<0:
            return 0
        mem=dict()
        for num in nums:
            if num not in mem:
                mem[num]=1
            else:
                mem[num]+=1
        res=dict()
        if k==0:
            for num in nums:
                if mem[num]>=2:
                    if (num,num) not in res:
                        res[(num,num)]=1
            return len(res)
        for num in nums:
            if num+k in mem:
                if (num,num+k) not in res:
                    res[(num,num+k)]=1
        return len(res)
import collections
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        c = collections.Counter(nums)
        for i in c:
            if k > 0 and i + k in c or k == 0 and c[i] > 1:
                res += 1
        return res


a=Solution()
nums=[1, 3, 1, 5, 4]
k = 0
print(a.findPairs(nums,k))