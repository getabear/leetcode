from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        #递归方法解题,复杂度高
        size=len(nums)
        self.step_min=size
        def fun(nums,index,step):
            if index==size-1:
                if step<self.step_min:
                    self.step_min=step
                return
            else:
                for i in range(1,nums[index]+1):
                    if i+index>size-1:
                        if step+1<self.step_min:
                            self.step_min=step+1
                        return
                    else:
                        fun(nums,i+index,step+1)
                return

        fun(nums, 0, 0)
        return self.step_min

class Solution1:
    def jump(self, nums: List[int]) -> int:
        #贪心法解题
        size=len(nums)
        self.min_step=size
        def fun(nums,index,step):
            cur=nums[index]
            #当前下标加上可以移动的步数到达末尾就直接记录
            if cur+index>=size-1:
                if self.min_step>step+1:
                    self.min_step=step+1
                return
            # 找到下标加值最大的,就是最优的(即走得最远的)
            nx=index
            temp=0
            for i,num in enumerate(nums[index+1:cur+1+index]):
                if i+num>temp:
                    temp=i+num
                    nx=i+index+1
            fun(nums,nx,step+1)
            return
        if size==1:
            return 0
        fun(nums,0,0)
        return self.min_step


a=Solution1()
# nums=[2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]
nums=[2,3,1,1,4]
print(a.jump(nums))
import time
print(time.process_time())
