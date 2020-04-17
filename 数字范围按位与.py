class Solution1:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        #方法一:暴力法,肯定超时
        ret=m
        for i in range(m,n+1):
            ret&=i
            if ret==0:
                break
        return ret

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        #惊艳的解法
        ret=0
        while m!=n:
            m>>=1
            n>>=1
            ret+=1

        return n<<ret

a=Solution()
print(a.rangeBitwiseAnd(6,7))
