from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #这次有障碍物,咱们还是先用自顶向下的动态规划,通过了的
        #太多细节,有点难以处理,不推荐...
        dit={}
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        def fun(i,j):
            if (i,j) in dit:
                return dit[(i,j)]
            if i==m-1 and j==n-1:
                if  obstacleGrid[i][j]!=1:
                    return 1
                else:
                    return 0
            if i>m-1 or j>n-1:
                return 0
            if i+1<m and obstacleGrid[i+1][j]!=1 and j+1<n and obstacleGrid[i][j+1]!=1:
                dit[(i+1,j)]=fun(i+1,j)
                dit[(i,j+1)]=fun(i,j+1)
                return dit[(i+1,j)]+dit[(i,j+1)]
            elif i+1<m and obstacleGrid[i+1][j]!=1:
                dit[(i + 1, j)] = fun(i + 1, j)
                return dit[(i + 1, j)]
            elif j+1<n and obstacleGrid[i][j+1]!=1:
                dit[(i, j + 1)] = fun(i, j + 1)
                return dit[(i, j + 1)]
            return 0
        return fun(0,0)


class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #这次咱们用自底向上的动态规划,提交leetcode比上一种解法快了4ms
        m=len(obstacleGrid)
        if m==0:
            return 0
        n=len(obstacleGrid[0])

        #起点和终点都有障碍物则返回0
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0

        #定义dp[i][j]为从obstacleGrid[i][j] 到obstacleGrid[m-1][n-1]的路径数
        #返回dp[0][0]
        dp=[[0]*n for _ in range(m)]
        dp[m-1][n-1]=1  #初始化最后一个为1
        i=m-1
        j=n-1
        while i>=0:
            while j>=0:
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    j-=1
                    continue
                if j==n-1 and i==m-1:  #最后一行 最后一列
                    j-=1
                    continue
                elif j==n-1:   #最后一列
                    dp[i][j]=dp[i+1][j]
                elif i==m-1:  #最后一行
                    dp[i][j]=dp[i][j+1]
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
                j-=1
            j=n-1
            i-=1
        return dp[0][0]



a=Solution1()
obstacleGrid=[[0,0]]
print(a.uniquePathsWithObstacles(obstacleGrid))