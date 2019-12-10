from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ret=[]
        def fun(nums,temp):
            if len(nums)==0:
                ret.append(temp[:])
            else:
                size=len(nums)
                rep=None   #用于剪枝
                for index in range(size):
                    if rep==nums[index]:#如果本次和上次一样,就跳过不选(即剪枝操作)
                        continue
                    temp.append(nums[index])
                    tp=nums[:]
                    tp.pop(index)
                    fun(tp,temp)
                    temp.pop()
                    rep=nums[index]
        nums.sort()
        fun(nums,[])
        return ret

a=Solution()
nums=[1,1,2,2]
print(a.permuteUnique(nums))
