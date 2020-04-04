class Solution:
    def reverseBits(self, n: int) -> int:
        ret=0
        for i in range(32):
            ret <<= 1
            if(n&0x1):
                ret|=0x1
            n>>=1
        return ret