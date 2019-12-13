from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        ret=[]
        for i in intervals:
            if not ret or i[0]>ret[-1][1]:
                ret.append(i)
            else:
                ret[-1]=[ret[-1][0],max(i[1],ret[-1][1])]
        return ret




a=Solution()
intervals=[[1,2],[3,5],[6,7],[8,10],[12,16]]
newinterval=[4,8]
print(a.insert(intervals,newinterval))