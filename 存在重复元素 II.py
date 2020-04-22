from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic=dict()

        for index,num in enumerate(nums):
            if num in dic:
                if index-dic[num]<=k:
                    return True
            dic[num]=index
        return False