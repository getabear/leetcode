from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        def fun(nums,temp):
            if len(nums)==0:
                ret.append(temp[:])
            else:
                for i in nums:
                    temp.append(i)
                    tp=nums[:]
                    tp.remove(i)
                    fun(tp,temp)
                    temp.remove(i)
        fun(nums,[])
        return ret

a=Solution()
nums=[1,2,3]
print(a.permute(nums))