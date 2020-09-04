from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n=len(citations)
        if n==0 or citations[-1]==0:
            return 0
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            # h值低了
            if citations[mid] < n-mid:
                left=mid+1
            else:
                right=mid-1

        return n-left
a=Solution()
citations=[100,1]
print(a.hIndex(citations))