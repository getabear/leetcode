class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        ret=10
        count=9
        tmp=9
        for i in range(2,min(n+1,11)):  #超过10位一定重复
            count=count*tmp
            ret+=count
            tmp-=1
        return ret


