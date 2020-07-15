class Solution:
    def numSub(self, s: str) -> int:
        n=len(s)
        dp=[0]*n  #代表素组右边连续1的个数
        if s[-1]=='1':
            dp[-1]=1
        for idx in range(n-2,-1,-1):
            if s[idx]=='1':
                dp[idx]=dp[idx+1]+1
        res=0
        for i in dp:
            res+=i
        return res%(10**9 + 7)

a=Solution()
s="000"
print(a.numSub(s))
