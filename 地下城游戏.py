from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        high=len(dungeon)
        if(high==0):
            return
        width=len(dungeon[0])

        #定义dp数组,含义 dp[x][y]为到从dungeon[-1][-1]到dungeon[x][y]所需的最少血量
        dp=[[0 for i in range(width)] for j in range(high)]

        #初始化条件
        if(dungeon[-1][-1]>0):
            dp[-1][-1]=1
        else:
            dp[-1][-1]=1-dungeon[-1][-1]

        for i in range(high-2,-1,-1):
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])
        for j in range(width-2,-1,-1):
            dp[-1][j]=max(1,dp[-1][j+1]-dungeon[-1][j])
        for i in range(high-2,-1,-1):
            for j in range(width-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]



dungeon=[[-2,-3,3],[-5,-10,1],[10,30,-5]]
a=Solution()
print(a.calculateMinimumHP(dungeon))