class Solution:
    def guessNumber(self, n: int) -> int:
        def guess(num):
            if num>6:
                return 1
            if num==6:
                return 0
            return -1
        def fun(n):
            left,right=1,n
            while left<=right:
                mid=left+(right-left)//2
                ret=guess(mid)
                if ret==0:
                    return mid
                elif ret==1:
                    right=mid-1
                elif ret==-1:
                    left=mid+1
            return -1
        return fun(n)
a=Solution()
print(a.guessNumber(10))