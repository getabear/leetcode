class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor > 0 and dividend < 0 or divisor < 0 and dividend > 0:
            sign = 0   #负数
        else:
            sign = 1  #正数

        #转换为正数
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor

        count=0
        while(divisor<=dividend):#先移位使除数大于被除数
            divisor<<=1
            count+=1         #记录左移了几位,也就是乘以了2的几次方
        result=0      #返回值,记录商
        while count>0:
            divisor>>=1
            count-=1
            if dividend>=divisor:  #如果被除数大于除数,被除数减去除数,结果加上倍数.
                                    # 否则就不加,继续减小除数
                result+=1<<count
                dividend-=divisor
        if sign==0:
            result=-result
        return result if result>=-(1<<31) and result<=(1<<31)-1 else (1<<31)-1

    '''
        #暴力解法,超时是肯定的
        if divisor==1:
            return dividend if dividend<=(1<<31)-1 and dividend>=-(1<<31) else (1<<31)-1
        if divisor==-1:
            return -dividend if -dividend<=(1<<31)-1 and -dividend>=-(1<<31) else (1<<31)-1
        if divisor>0 and dividend<0 or divisor<0 and dividend>0:
            flag=0
        else:
            flag=1
        if dividend<0:
            dividend=-dividend
        if divisor<0:
            divisor=-divisor
        ret=0
        while(dividend>0 and dividend>=divisor):
            ret+=1
            if ret>(1<<31)-1 and flag==1 or ret>(1<<31) and flag==0:
                return (1<<31)-1
            dividend-=divisor
        return ret if flag else -ret
        '''





a=Solution()

dividend =-2147483648
divisor = 1
print(a.divide(dividend,divisor))