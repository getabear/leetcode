from typing import List

class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left==[] or right==[]:
            if left==[] and right==[]:
                return 0
            elif left==[]:
                return n-min(right)
            else:
                return max(left)
        if len(left)==len(right):
            left.sort()
            right.sort()
            time=(left[-1]-right[0])/2
            return int(time+max(n-left[-1]+time,right[0]+time))
        else:
            if len(left)>len(right):
                left.sort()
                right.sort()
                time=(left[-len(right)]-right[0])/2
                return int(max(left[-1],time+max(n-left[-len(right)]+time,right[0]+time)))
            else:
                left.sort()
                right.sort()
                time=(left[-1]-right[len(right)-len(left)])/2
                return int(max(n-right[0],time+max(n-left[-1]+time,right[len(right)-len(left)]+time)))



a=Solution()
left=[5]
right=[4]
n=9
print(a.getLastMoment(n,left,right))