from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr)<=1:
            return True
        slow,fast=0,1
        d=arr[fast]-arr[slow]
        while fast<len(arr):
            if d!=arr[fast]-arr[slow]:
                return False
            else:
                fast+=1
                slow+=1
        return True
