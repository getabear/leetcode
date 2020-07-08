from typing import List

class Solution1:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        # 递归超时了
        ret=[0]
        mem=dict()
        def fun(val,k):
            if (val,k) in mem:
                return
            if k==0:
                if val!=ret[-1]:
                    ret.append(val)
                return
            fun(val+shorter,k-1)
            fun(val+longer,k-1)
            mem[(val,k)]=1
            return
        fun(0,k)
        return ret[1:]

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        ret=[]
        if k!=0:
            if shorter!=longer:
                for i in range(k,-1,-1):
                    ret.append(i*shorter+(k-i)*longer)
            else:
                ret.append(k*shorter)
        return ret
a=Solution()
shorter=1
longer=2
k=3
print(a.divingBoard(shorter,longer,k))