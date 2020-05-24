class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def fun(num):
            if num<2:
                return True
            tmp=num//2
            left=0
            right=tmp
            while left<=right:
                mid=left+(right-left)//2
                ret=mid*mid
                if ret==num:
                    return True
                elif ret<num:
                    left=mid+1
                else:
                    right=mid-1
            return False
        return fun(num)

a=Solution()
print(a.isPerfectSquare(4))