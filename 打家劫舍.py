from typing import List

class Solution1:
    def rob(self, nums: List[int]) -> int:
        #重复子问题过多,超时了
        self.res=0
        def fun(nums,sum):
            if len(nums)<=1:
                if len(nums)==1:
                    sum+=nums[0]
                if sum>self.res:
                    self.res=sum
                return
            fun(nums[2:],sum+nums[0]) #偷第一家
            fun(nums[3:],sum+nums[1]) #偷第二家

        fun(nums,0)
        return self.res

class Solution2:
    #加入记忆数组,成功通过所有的测试用例
    def rob(self, nums: List[int]) -> int:
        self.res = 0
        length=len(nums)
        mem={}

        def fun(index, sum):
            if index in mem:
                if mem[index]+sum>self.res:
                    self.res=sum+mem[index]
                return sum+mem[index]
            if index+1>=length:
                tmp=sum
                if index==length-1:
                    sum+=nums[index]
                if sum>self.res:
                    self.res=sum
                mem[index]=sum-tmp
                return sum
            res=fun(index+2,sum+nums[index])
            res1=fun(index+3,sum+nums[index+1])
            mem[index]=max(res,res1)-sum
            return max(res,res1)

        fun(0,0)
        return self.res


class Solution:
    #这次利用动态规划解决问题
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<2:
            return nums[-1]
        dp=[0 for i in nums]
        dp[-1]=nums[-1]
        dp[-2]=max(nums[-1],nums[-2])

        for i in range(len(nums)-3,-1,-1):
            dp[i]=max(dp[i+1],dp[i+2]+nums[i])

        return dp[0]


a=Solution()
nums=[2,7,9,3,1]
print(a.rob(nums))