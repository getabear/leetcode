from typing import List

class Solution1:
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

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res=[]
        def fun(nums,result):
            if len(nums)==0:
                res.append(result)
                return
            for i in nums:
                tmp=nums[:]
                tmp.remove(i)
                fun(tmp,result+[i])
        fun(nums,[])
        return res

a=Solution()
nums=[1,2,3]
print(a.permute(nums))