from typing import List

class Solution:
    #看了大佬们的题解,下次写程序可以考虐先满足一个条件,然后满足所有条件,不一定需一次满足所有..
    def candy(self, ratings: List[int]) -> int:
        left=[1 for i in ratings]
        right=left[:]
        n=len(ratings)
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                right[i]=right[i+1]+1
        res=0
        for i in range(n):
            res+=max(left[i],right[i])
        return res