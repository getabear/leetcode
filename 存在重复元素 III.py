from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        bucket=dict()
        if t<0:
            return False
        for index,i in enumerate(nums):
            tmp=i//(t+1)
            if tmp in bucket:
                return True
            if tmp-1 in bucket and abs(bucket[tmp-1]-i)<=t:
                return True
            if tmp+1 in bucket and abs(bucket[tmp+1]-i)<=t:
                return True
            bucket[tmp] = i
            if index>=k:
                bucket.pop(nums[index-k]//(t+1))
        return False
