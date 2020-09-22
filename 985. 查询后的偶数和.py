from typing import List

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum_ = 0
        ret = []
        for a in A:
            if a&0x1 == 0:
                sum_ += a
        for num,idx in queries:
            if A[idx]&0x1 == 0:
                sum_ -= A[idx]
            if (A[idx]+num)&0x1 == 0:
                sum_ += A[idx]+num
            A[idx] += num
            ret.append(sum_)
        return ret

a=Solution()
A=[1,2,3,4]
queries=[[1,0],[-3,1],[-4,0],[2,3]]
print(a.sumEvenAfterQueries(A,queries))