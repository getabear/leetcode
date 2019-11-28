from typing import List


# 有 n 个气球，编号为0 到 n-1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
#
# 现在要求你戳破所有的气球。每当你戳破一个气球 i 时，你可以获得 
# nums[left] * nums[i] * nums[right] 个硬币。 这里的 left 和 right 代表和 i 相邻的两个气球的序号。
# 注意当你戳破了气球 i 后，气球 left 和气球 right 就变成了相邻的气球。
#
# 求所能获得硬币的最大数量
# 复制数组不受影响   b=a[:]     //  如果直接b=a,则改变b,a也会改变
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        max=0
        record=0
        length=len(nums)
        if(length==1):
            return nums[0]
        for i in range(length):
            temp=nums[:]
            del temp[i]
            if(i==0):
                record=1*nums[i]*nums[i+1]+self.maxCoins(temp)
            elif(i==length-1):
                record=nums[i-1]*nums[i]*1+self.maxCoins(temp)
            else:
                record = nums[i - 1] * nums[i] * nums[i+1] + self.maxCoins(temp)
            if(record>max):
                max=record
        return max

nums=[3,1,5,8]
a=Solution()
print(a.maxCoins(nums))