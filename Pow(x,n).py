class Solution1:
    def myPow(self, x: float, n: int) -> float:
        #递归解决方案

        #flag的值默认为1代表n为正数
        flag=1

        # 修改flag为0 并且更改n为正数
        if n<0:
            flag=0
            n=-n
        def fun(x,n):
            #如果n为0,返回1
            if n==0:
                return 1

            else:
                #原理:  x^n=(x^n)^2
                #n为奇数,n//2不能整除,所以分情况
                if n&0x1==1:
                    ret=x*fun(x,n-1)  #n-1会变为偶数

                #n为偶数
                else:
                    ret=fun(x,n//2)
                    ret=ret*ret
                return ret
        res=fun(x,n)
        return res if flag else 1/res

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            flag=-1
            n=-n
        else:
            flag=1
        def fun(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            tmp=fun(x,n//2)
            return tmp*tmp if not n&0x1 else tmp*tmp*x
        return fun(x,n) if flag==1 else 1/fun(x,n)

a=Solution()
print(a.myPow(2,-2147483648))