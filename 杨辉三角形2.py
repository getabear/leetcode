from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        i=1
        j=1
        ret=[[1] for _ in range(rowIndex+1)]
        while i<rowIndex+1:
            while j<i:
                ret[i].append(ret[i-1][j-1]+ret[i-1][j])
                j+=1
            ret[i].append(1)
            j=1
            i+=1
        return ret[-1]
a=Solution()
print(a.getRow(3))