from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 测试该题暴力法居然可以通过...惊了
        def findMax(left,right):   #函数功能返回最大值的下标
            ret=left
            for i in range(left+1,right):
                if nums[i]>nums[ret]:
                    ret=i
            return ret

        index=findMax(0,0+k)
        res=[nums[index]]
        for i in range(1,len(nums)-k+1):
            if i<=index:
                if nums[index]>nums[i+k-1]:
                    res.append(nums[index])
                else:
                    index=i+k-1
                    res.append(nums[index])
            else:
                index=findMax(i,i+k)
                res.append(nums[index])
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
a=Solution()
print(a.maxSlidingWindow(nums,k))