class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #判断一个数是否为平方数
        def judge(n):
            left,right=0,n
            while left<=right:
                mid=left+(right-left)//2
                tmp=mid*mid
                if tmp==n:
                    return True
                elif tmp>n:
                    right=mid-1
                else:
                    left=mid+1
            return False

        for i in range(c+1):
            if i*i>c:
                break
            if judge(c-i*i):
                return True
        return False


a=Solution()
print(a.judgeSquareSum(3))