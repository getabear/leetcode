class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 你可以通过调用 bool (version) 接口来判断版本号 version
        # 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对
        # 调用 API 的次数。
        def isBadVersion(n):   #这是我们的假接口
            mem={1:True,2:True,3:True,4:False,5:False}
            return mem[n]
        l,r=1,n
        while l<=r:
            mid=l+(r-l)//2
            if isBadVersion(mid)==False:
                l=mid+1
            else:
                r=mid-1
        return l

a=Solution()
print(a.firstBadVersion(5))