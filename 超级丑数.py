from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if not n:
            return []
        ret=[1]
        mem=[0]*len(primes)
        while len(ret)<n:
            res=float("inf")
            flag=0
            for index,prime in enumerate(primes):
                tmp=prime * ret[mem[index]]
                if tmp<res:
                    rec = index
                    if tmp>ret[-1]:
                        res=tmp
                    else:
                        flag=1
                        break
            mem[rec] += 1
            if flag:
                continue
            ret.append(res)
        return ret[-1]

a=Solution()
n=45
primes=[2,3,7,13,17,23,31,41,43,47]
print(a.nthSuperUglyNumber(n,primes))
