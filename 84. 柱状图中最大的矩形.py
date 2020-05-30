from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights=[0]+heights+[0]
        stack=[]
        ret=0
        for index,i in enumerate(heights):
            while stack and heights[stack[-1]]>i:
                high=stack.pop()
                ret=max(ret,heights[high]*(index-stack[-1]-1))
            stack.append(index)
        return ret

a=Solution()
heights=[2,1,2]
print(a.largestRectangleArea(heights))
