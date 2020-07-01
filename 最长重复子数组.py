from typing import List

class Solution1:
    def findLength(self, A: List[int], B: List[int]) -> int:
        #暴力法，超时了
        len_a=len(A)
        ret=0
        for i in range(len_a):
            for j in range(i+ret+1,len_a+1):
                length=j-i
                for k in range(len(B)):
                    if A[i:j]==B[k:k+length]:
                        ret=max(ret,length)
                        break
                    if k+length>len(B):
                        break
        return ret

class Solution2:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m=len(A)
        n=len(B)
        #dp数组含义： dp[i][j]=2 代表以A[i-1]和B[j-1]结尾的最大公共长度为2
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        self.res=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    self.res=max(self.res,dp[i][j])
        return self.res

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        m=len(A)
        n=len(B)
        #dp数组含义，dp[i][j]以A[i],B[j]为开始的最大公共数组的长度
        dp=[[0 for i in range(n+1)] for j in range(m+1)]
        self.res=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if A[i]==B[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                    self.res=max(self.res,dp[i][j])
        return self.res
A=[1,2,3,2,1]
B=[3,2,1,4,7]
a=Solution()
print(a.findLength(A,B))