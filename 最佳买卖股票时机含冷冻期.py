from typing import List

class Solution:
    def maxProfit(self, prices,money,flag):
        #flag代表是否持有股票,money代表钱的多少,flag=1持有,否则没有
        length=len(prices)
        temp=[-100,-100,-100,-100]
        if(length==0):
            return money
        if(flag):                   #如果持有,可以卖掉,或者继续保持
            temp[0]=self.maxProfit(prices[1:],money,flag)   #保持
            temp[1]=self.maxProfit(prices[2:],money+prices[0],0)  #卖出
        else:
            temp[2]=self.maxProfit(prices[1:],money-prices[0],1)  #买入
            temp[3]=self.maxProfit(prices[1:],money,flag)    #保持
        return self.max(temp)

    def max(self,temp):
        length=len(temp)
        max=0
        for i in range(length):
            if(temp[i]>max):
                max=temp[i]
        return max


a=Solution()
prices=[1,2,3,0,2,0,7]
# print(len(prices[7:]))
print(a.maxProfit(prices,0,0))