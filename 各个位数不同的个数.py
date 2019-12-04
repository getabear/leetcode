class Solution:
    def countNumbersWithUniqueDigits(self, n):
        dp=[]
        dp.append(10)    #n=1时
        if(n==1):
            return dp[n-1]
        else:
            ret,mul=10,9
            for i in range(1,min(n,10)):
                mul*=10-i   #计算n位的不同数字的数量
                ret+=mul
            return ret

a=Solution()
print(a.countNumbersWithUniqueDigits(2))