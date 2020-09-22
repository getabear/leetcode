class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ret = 0
        last = 0
        while (numBottles+last) >= numExchange:
            ret += numBottles
            tmp = numBottles
            numBottles = (numBottles+last) // numExchange
            last = (tmp+last) % numExchange
        return ret+numBottles
a=Solution()
print(a.numWaterBottles(15,8))