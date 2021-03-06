from typing import List
#有点不想做了,看看官方题解
#一次线性扫描,时间主要花费在排序上,所以时间复杂度为O(nlogn)
class Solution1:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ret=[]
        for interval in intervals:
            if not ret or interval[0]>ret[-1][1]:
                ret.append(interval)
            else:
                ret[-1][1]=max(interval[1],ret[-1][1])
        return ret

a=Solution()
interval=[[1,3],[2,6],[8,10],[15,18]]
print(a.merge(interval))

