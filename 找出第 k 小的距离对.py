from typing import List
import heapq
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        #超时
        diff=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                tmp=abs(nums[i]-nums[j])
                #将小顶堆构造为大顶堆
                if len(diff)<k:
                    heapq.heappush(diff,-tmp)
                else:
                    if tmp<=-diff[0]:
                        heapq.heapreplace(diff,-tmp)
        return -diff[0]
class Solution1(object):
    #官方题解,二分法
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            #Is there k or more pairs with distance <= guess?
            count = left = 0
            for right, x in enumerate(nums):
                while x - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mi = (lo + hi) / 2
            if possible(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo

a=Solution()
nums=[62,100,4]
print(a.smallestDistancePair(nums,2))