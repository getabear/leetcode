class Solution:
    #计算5的个数,看了大佬的解题,有点痛苦哈哈哈
    def trailingZeroes(self, n: int) -> int:
        ret=0
        while n>0:
            ret+=n//5
            n=n//5
        return ret
