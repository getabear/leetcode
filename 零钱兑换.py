# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。

class Solution:
    def __init__(self,coins):
        self.coins=coins
    def find_coin(self,amount):
        ret=666
        if (amount == 0):
            return 0
        if(amount<self.coins[0]): #假设coins是按照从小到大的顺序排列的
            return 666
        else:
            for i in self.coins:
                value=1+self.find_coin(amount-i)    #假设选中i
                if(value<ret):
                    ret=value
        if(ret>=666):    #如果是很大就说明没找到解决方案
            ret=-1
        return ret

coins=[1,2,5]
a=Solution(coins)
print(a.find_coin(11))