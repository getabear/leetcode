class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def fun(n,m):
            if n==1:
                return 0
            x=fun(n-1,m)
            return  (m%n+x)%n

        return fun(n,m)

a=Solution()
print(a.lastRemaining(10,17))