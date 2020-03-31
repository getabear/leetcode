from typing import List

class Solution1:  #毫无悬念超时了,还有一个测试用例没通过
    def maxProduct(self, nums: List[int]) -> int:
        length=len(nums)
        self.max1=nums[0]  #假设他为最大

        def fun(sum,index):
            if(index==length):
                if(sum>self.max1):
                    self.max1=sum
                return
            fun(sum*nums[index],index+1)
            if(self.max1<sum):
                self.max1=sum
            return

        for i in range(length):
            fun(nums[i],i+1)
        return self.max1

class Solution:   #优化算法;动态规划
    def maxProduct(self, nums: List[int]) -> int:
        #dpmax[i]为以下标i结尾的最大值
        #dpmin[i]为以下标i结尾的最小值
        #状态转移方程        dpmax[i]=max(dpmax[i-1]*nums[i],nums[i],dpmin[i-1]*nums[i])
        #                 dpmin[i]=min(dpmin[i-1]*nums[i],nums[i],dpmax[i-1]*nums[i])
        length=len(nums)
        if(length==0):
            return
        imax=nums[0]
        imin=nums[0]
        ret=nums[0]
        for i in range(1,length):
            tmp=imax  #保存信息tmp,因为后面会改变imax值
            imax=max(nums[i],imax*nums[i],imin*nums[i])
            imin=min(nums[i],imin*nums[i],tmp*nums[i])
            ret=max(ret,imax)
        return ret

a=Solution()
nums=[2,3,-2,4]
print(a.maxProduct(nums))