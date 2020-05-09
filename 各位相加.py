class Solution:
    def addDigits(self, num: int) -> int:
        res=num
        while res//10:
            num=res
            res=0
            while num:
                res+=num%10
                num//=10
        return res
class Solution1:
    def addDigits(self, num: int) -> int:
        def fun(num):
            if num//10==0:
                return num
            res=0
            while num:
                res+=num%10
                num//=10
            return fun(res)
        return fun(num)

a=Solution1()
print(a.addDigits(0))