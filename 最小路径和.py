from typing import List
# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
class Solution:
    ret = float("inf")  # 保证ret足够大
    def minPathSum(self, grid: List[List[int]]) -> int:
        m1 = len(grid)
        n1 = len(grid[0])
        def find(grid, m, n, distance):   #提交后超时,说明需要优化
            if m==m1-1 and n==n1-1:
                distance+=grid[m][n]
                self.ret=min(distance,self.ret)
                return
            elif m>=m1 or n>=n1:
                return
            else:
                find(grid,m+1,n,distance+grid[m][n])
                find(grid,m,n+1,distance+grid[m][n])
        find(grid,0,0,0)
        return self.ret

    def minPathSum2(self, grid: List[List[int]]) -> int:   #动态规划实现
        dp={}
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp.setdefault((i,j),grid[0][0])
                elif i==0:
                    dp.setdefault((i,j),dp[(i,j-1)]+grid[i][j])
                elif j==0:
                    dp.setdefault((i, j), dp[(i-1, j)] + grid[i][j])
                else :
                    dp.setdefault((i, j), min(dp[(i, j - 1)],dp[(i-1,j)])+grid[i][j])
        return dp[(m-1,n-1)]

grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
a=Solution()
print(a.minPathSum2(grid))

