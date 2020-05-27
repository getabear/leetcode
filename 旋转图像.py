from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        m,n=len(matrix),len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        for h in range(m):
            for x in range(n):
                dp[x][m-h-1]=matrix[h][x]
        matrix[:]=dp[:]
        return

a=Solution()
matrix=[[1,2,3],[4,5,6],[7,8,9]]
a.rotate(matrix)