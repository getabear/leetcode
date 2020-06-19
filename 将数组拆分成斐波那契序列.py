from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n=len(S)
        self.ret=[]
        def fun(index,ret):
            if index>=len(S):
                if len(ret)>=3:
                    self.ret=ret[:]
                return
            for i in range(1,n+1):
                num=int(S[index:index+i])
                if num>(1<<31)-1:
                    return
                if len(ret)<2:
                    ret.append(num)
                    fun(index+i,ret)
                    ret.pop()
                else:
                    if ret[-1]+ret[-2]==num:
                        ret.append(num)
                        fun(index+i,ret)
                        ret.pop()
                    elif ret[-1]+ret[-2]>num:
                        continue
                    else:
                        return
                if num==0:
                    return
        fun(0,[])
        return self.ret

S="539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
a=Solution()
ret=a.splitIntoFibonacci(S)
print(ret)