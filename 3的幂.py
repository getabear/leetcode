class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        #暴力法
        result=1
        while result<n:
            result*=3
        return result==n

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<3:
            if n!=1:
                return False
            else:
                return True
        result=3
        while result<n:
            result*=result
        while result>n:
            result//=3
        return result==n

a=Solution()
nums=[27,0,9,45]
for i in nums:
    print(i,a.isPowerOfThree(i))

