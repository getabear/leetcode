from typing import List

class Solution1:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ret=[0]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]>nums[j]:
                    ret[i]+=1
        return ret

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        import bisect
        queue = []
        res = []
        for num in nums[::-1]:
            loc = bisect.bisect_left(queue, num)
            res.append(loc)
            queue.insert(loc, num)
        return res[::-1]



