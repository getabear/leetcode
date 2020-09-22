from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def judge(num):
            temp=num
            t=temp%10
            while temp:
                if (t!=0 and num%t==0):
                    temp//=10
                    t = temp % 10
                    continue
                else:
                    return False
            return True
        ret=[]
        for i in range(left,right+1):
            if judge(i):
                ret.append(i)
        return ret

a=Solution()
print(a.selfDividingNumbers(1,22))