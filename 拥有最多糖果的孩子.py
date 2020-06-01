from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_cnt=0
        for i in candies:
            if max_cnt<i:
                max_cnt=i
        ret=[]
        for i in candies:
            if i+extraCandies>=max_cnt:
                ret.append(True)
            else:
                ret.append(False)
        return ret
a=Solution()
candies=[12,1,12]
extraCandies=10
print(a.kidsWithCandies(candies,extraCandies))