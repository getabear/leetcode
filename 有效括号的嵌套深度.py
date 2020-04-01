from typing import List

class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        ret=[]

        deep=0
        for i in seq:
            if i=='(':
                deep+=1
                ret.append(deep&0x1)
            if i==')':
                ret.append(deep&0x1)
                deep-=1

        return ret

a=Solution()
seq="(()())"
print(a.maxDepthAfterSplit(seq))
