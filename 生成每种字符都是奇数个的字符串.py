class Solution:
    def generateTheString(self, n: int) -> str:
        if n&0x1==1:
            return 'w'*n
        else:
            return 'w'*(n-1)+'z'