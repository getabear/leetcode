from typing import List

class Solution1:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n = len(A)
        mem = set()
        dp = [[0 for _ in range(n)] for _i in range(n)]
        for i in range(n):
            dp[i][i] = A[i]
            if dp[i][i] not in mem:
                mem.add(dp[i][i])
        for i in range(n):
            for j in range(i+1,n):
                dp[i][j] = dp[i][j-1] | A[j]
                if dp[i][j] not in mem:
                    mem.add(dp[i][j])
        return len(mem)

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        n=len(A)
        mem=set()
        for i in range(n):
            mem.add(A[i])
            for j in range(i-1,-1,-1):
                if (A[j]|A[i])==A[j]:
                    break
                A[j]|=A[i]
                mem.add(A[j])
        return len(mem)

A=[1,2,4]
a=Solution()
print(a.subarrayBitwiseORs(A))