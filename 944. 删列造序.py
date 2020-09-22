from typing import List

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        length=len(A)
        if length==0:
            return 0
        width=len(A[0])
        ret=0
        for i in range(width):
            for j in range(1,length):
                if A[j][i]<A[j-1][i]:
                    ret+=1
                    break
        return ret