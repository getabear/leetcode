from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        max1=nums[0]
        for i in nums:
            if(sum>0):
                sum+=i
            else:
                sum=i
            max1=max(max1,sum)
        return max1

    def maxSubArray2(self, nums: List[int]) -> int:   #分治算法
        length=len(nums)
        mid=length//2
        if(length==1):
            return nums[0]    #保证返回数组
        left_sub=self.maxSubArray2(nums[0:mid])
        right_sub=self.maxSubArray2(nums[mid:length])
        sum=0
        ret=nums[mid]
        temp=mid
        while(temp>=0):
            sum+=nums[temp]
            ret=max(sum,ret)
            temp-=1
        temp=mid+1
        sum=ret
        while(temp<length):
            sum+=nums[temp]
            ret=max(sum,ret)
            temp+=1
        return max(ret,left_sub,right_sub)




nums= [1]
a=Solution()
print(a.maxSubArray2(nums))