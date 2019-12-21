from typing import List

class Solution:
    #简单的循环就解决问题了
    def generate(self, numRows: int) -> List[List[int]]:
        i=1
        j=1
        ret=[[1] for _ in range(numRows)]
        while i<numRows:
            while j<i:
                ret[i].append(ret[i-1][j-1]+ret[i-1][j])
                j+=1
            ret[i].append(1)
            j=1
            i+=1
        return ret

a=Solution()
ret=a.generate(6)
print("nihao")