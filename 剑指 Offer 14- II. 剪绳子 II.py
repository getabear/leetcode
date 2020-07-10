class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        dp=[0 for _ in range(n+1)]
        dp[1],dp[2]=1,1
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],max(dp[i-j],(i-j))*j)
        return dp[n]%1000000007

class Solution1:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        dp=[0 for _ in range(n+1)]
        dp[1],dp[2]=1,1
        for i in range(3,n+1):
            for j in range(1,i):
                #这里需要注意，我感觉题目出问题了，
                # 感觉有时候不用最大值余1000000007才会取得最大的结果
                #没关系，理解了dp就行
                dp[i]=max(dp[i],max(dp[i-j],(i-j))*j)%1000000007
        return dp[n]
a=Solution()
b=Solution1()
print(a.cuttingRope(100))
print(b.cuttingRope(100))