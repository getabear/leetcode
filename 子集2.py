from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #提交后通过,按时效率低,今天不想做了
        ret=[]
        size=len(nums)
        def fun(n,tp,index):
            if n==0:
                if tp not in ret:
                    ret.append(tp[:])
                return
            for i in range(index,size):
                fun(n-1,tp,i+1)  #什么都不选
                if size-i<n:
                    break
                tp.append(nums[i])
                fun(n-1,tp,i+1)#选择nums[i]
                tp.pop()
        nums.sort()
        fun(size,[],0)
        return ret

a=Solution()
nums=[4,4,4,1,4]
print(a.subsetsWithDup(nums))
