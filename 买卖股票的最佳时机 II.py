from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        self.ret = 0
        def fun(prices,flag,profit):         #1.暴力搜索     flag=1持有  flag=0未持有
            if len(prices)==0:
                self.ret=max(self.ret,profit)
                return
            if(flag==0):
                fun(prices[1:],1,profit-prices[0]) #买入
                fun(prices[1:],0,profit)   #保持
            if(flag==1):
                fun(prices[1:],0,profit+prices[0])   #卖出
                fun(prices[1:],1,profit)     #保持
        def fun2(prices):   # 2.贪心算法,我们只做对当前最有利的选择
            ret=0
            for i in range(len(prices)-1):
                if(prices[i+1]-prices[i]>0):  #如果盈利就直接卖掉
                    ret+=prices[i+1]-prices[i]
            return ret
        self.ret=fun2(prices)
        return self.ret

a=Solution()
prices=[7,1,5,3,6,4]
print(a.maxProfit(prices))

