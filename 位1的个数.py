class Solution1:
    def hammingWeight(self, n: int) -> int:
        ret=0
        while(n!=0):
            if(n&0x1):
                ret+=1
            n>>=1
        return ret

class Solution:
    def hammingWeight(self, n: int) -> int:
        ret=0
        while(n!=0):
            n&=n-1
            ret+=1
        return ret
