class Solution1:
    def rob(self,nums):
        nums1=nums[1:]    #解决环的问题;把他拆解为两个数组
        nums2=nums[0:-1]
        print(nums1)
        print(nums2)
        first=self.rob1(nums1)
        seconed=self.rob1(nums2)
        if first>seconed:
            return first
        else :
            return seconed
    def rob1(self,nums) -> int:
        if len(nums)==1:
            return nums[0]
        max=0
        for i in range(len(nums)):
            temp=nums[i]+self.rob1(nums[i+2:])
            if temp>max:
                max=temp
        return max

from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

        def fun(nums):
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
        if not nums:
            return 0
        if len(nums)<2:
            return nums[0]
        nums1 = nums[1:]  # 解决环的问题;把他拆解为两个数组
        nums2 = nums[0:-1]
        return max(fun(nums1),fun(nums2))



nums=[1,10,3,4,5,6,20,8]
a=Solution()    #应该先实例化,不然会报错
print(a.rob(nums))

# num=[1,2,3,4,5,6,7,8]
# print(len(num[8:]))