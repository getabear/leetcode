from typing import List

class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem=dict()
        for num in nums:
            try:
                mem[num]+=1
            except:
                mem[num]=1
        array=[]
        for key in mem.keys():
            array.append((key,mem[key]))
        array.sort(key=lambda x:x[1],reverse=True)
        ret=[]
        for i in range(k):
            ret.append(array[i][0])
        return ret
from collections import Counter
import heapq   #是小顶堆
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mem=Counter(nums)
        heap=[]
        for i in mem.keys():
            if len(heap)<k:
                heapq.heappush(heap,(mem[i],i))
            elif( mem[i]>heap[0][0]):
                heapq.heapreplace(heap,(mem[i],i))
        ret=[]
        while heap:
            ret.append(heapq.heappop(heap)[1])
        return ret



a=Solution()
nums=[1,2,1,2,3]
print(a.topKFrequent(nums,2))
