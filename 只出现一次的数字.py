from typing import List

class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        #提交后时间有点久,超越了8%的用户...
        stack=[]
        #时间复杂度O(n^2)
        for i in nums:
            if i not in stack:
                stack.append(i)
            else:
                stack.remove(i)
        return stack[0]

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret=0
        for i in nums:
            ret^=i
        return ret

class Solution3:  #hash表法
    def singleNumber(self, nums: List[int]) -> int:
        ret={}
        for i in nums:
            try:
                ret.pop(i)
            except:
                ret[i]=1
        return ret.popitem()[0]

nums=[4,1,2,1,2]
a=Solution()
print(a.singleNumber(nums))