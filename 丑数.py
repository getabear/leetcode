class Solution:
    def isUgly(self, num: int) -> bool:
        mem=dict()
        def fun(num):
            if num==1:
                return True
            if num in mem:
                return mem[num]
            for i in [2,3,5]:
                if num%i==0:
                    if fun(num//i):
                        return True
            mem[num]=False
            return False
        if num==0:
            return False
        return fun(num)

a=Solution()
print(a.isUgly(14))