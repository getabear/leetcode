class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        mem=dict()
        def fun(idx1,idx2,idx3):
            if (idx1,idx2) in mem:
                return mem[(idx1,idx2)]
            if idx3==len(s3):
                return idx1==len(s1) and idx2==len(s2)
            res=False
            if idx1<len(s1) and s1[idx1]==s3[idx3]:
                res=fun(idx1+1,idx2,idx3+1)
            if not res:
                if idx2<len(s2) and s2[idx2]==s3[idx3]:
                    mem[(idx1,idx2)]=fun(idx1,idx2+1,idx3+1)
                    return mem[(idx1,idx2)]
                mem[(idx1,idx2)]=False
                return False
            mem[(idx1,idx2)]=res
            return mem[(idx1,idx2)]
        return fun(0,0,0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n=len(s1),len(s2)
        if m+n!=len(s3):
            return False
        dp=[[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0]=True
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0] and s1[i-1]==s3[i-1]
        for j in range(1,n+1):
            dp[0][j]=dp[0][j-1] and s2[j-1]==s3[j-1]
        for i in range(1,m+1):
            for j in range(1,n+1):
                dp[i][j]=(dp[i-1][j] and s1[i-1]==s3[i+j-1])\
                    or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
        return dp[-1][-1]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
a=Solution()
print(a.isInterleave(s1,s2,s3))