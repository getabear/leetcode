from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ret=[]
        def fun(tmp,num,sum,s):
            if(num==0):
                if sum==n:
                    ret.append(tmp)
                return
            for i in range(s,10):
                if i not in tmp:
                    if sum+i<=n:
                        fun(tmp+[i],num-1,sum+i,i+1)
                    else:
                        break
            return

        fun([],k,0,1)
        return ret

a=Solution()
print(a.combinationSum3(3,9))


