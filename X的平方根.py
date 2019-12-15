class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        if left>right:
            return 0
        while left<right:
            mid=(left+right+1)>>1
            tp=x//mid
            if tp>mid:
                left=mid
            elif tp<mid:
                right=mid-1
            else:
                return mid
        return left

a=Solution()
print(a.mySqrt(8))
