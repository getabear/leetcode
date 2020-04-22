from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtab=set()
        for i in nums:
            if i in hashtab:
                return True
            hashtab.add(i)
        return False