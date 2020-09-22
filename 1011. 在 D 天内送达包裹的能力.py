from typing import List

#暴力的算法，只通过了49个测试用例
class Solution1:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        dp=[weights[0]]*len(weights)  #前缀和
        max_=weights[0]
        for idx in range(1,len(weights)):
            if weights[idx] > max_:
                max_=weights[idx]
            dp[idx]=weights[idx]+dp[idx-1]
        temp = max_
        time = 0
        min_=max_
        while time != D:
           time = 0
           i, last = 0, 0
           max_ = min_
           min_ = 0
           while i < len(dp):
               if dp[i]-last > max_:
                   if min_ == 0:
                       min_=dp[i]-last
                   else:
                       min_=min(min_,dp[i]-last)
                   last=dp[i-1]
                   time+=1
               i+=1
           if dp[-1]-last <= max_:
               time+=1
           if max_==temp and time<D:
               return max_
        return max_

# 二分法，通过所有测试用例
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        dp = [weights[0]]*len(weights)  #前缀和
        sum_ = weights[0]
        max_ = weights[0]
        # 在数组中找到最大的值和整个数组的和，方便在接下来的地方进行二分,O(n)的时间复杂度
        for idx in range(1,len(weights)):
            if weights[idx] > max_:
                max_ = weights[idx]
            sum_ += weights[idx]
            dp[idx] = sum_
        left,right = max_,sum_
        while left <= right:
            mid = (left+right)//2
            last = 0
            time, i = 0, 0
            while i < len(dp):
                if dp[i]-last > mid:
                    last = dp[i-1]
                    time += 1
                i += 1
            if dp[-1]-last <= mid:
                time += 1
            # 选择的重量小了
            if time > D:
                left = mid+1
            else:
                right = mid-1
        return left

weights = [1,2,3,4,5,6,7,8,9,10]
D = 1
a = Solution()
print(a.shipWithinDays(weights,D))