from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        def fun(s,flag):
            if len(s) == n:
                res.append(int(s, 2))
            elif flag==0:
                fun(s + '0', 0)
                fun(s + '1', 1)
            else:
                fun(s + '1', 0)
                fun(s + '0', 1)
        if n==0:
            return [0]
        fun('', 0)
        return res


a=Solution()
print(a.grayCode(2))