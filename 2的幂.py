class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp=0
        while (1<<tmp)<n:
            tmp+=1
        if (1<<tmp)==n:
            return True
        return False

class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        tmp=1
        while tmp<n:
            tmp=tmp<<1
        if tmp==n:
            return True
        return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n&(n-1)==0