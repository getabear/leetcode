class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        dp=[[False]*n for i in range(n)]
        for i in range(n):
            dp[i][i]=True
        ret=0
        for i in range(n):
            for j in range(i):
                res=s[i]==s[j]
                if res and i-j<2:
                    dp[j][i]=res
                else:
                    dp[j][i]=res and dp[j+1][i-1]
                if dp[j][i]:
                    ret += 1
        return ret+n

a=Solution()
print(a.countSubstrings("abc"))


