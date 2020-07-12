from typing import List

class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        h=len(dungeon)
        w=len(dungeon[0])
        #定义dp数组的含义为dp[i][j]为从【i】【j】到公主哪里所需的最低血量
        dp=[[0 for _ in range(w)] for _ in range(h)]
        if dungeon[h-1][w-1]>=0:
            dp[h-1][w-1]=1
        else:
            dp[h-1][w-1]=1+abs(dungeon[h-1][w-1])
        for x in range(w-2,-1,-1):
            if dungeon[h-1][x]>=0:
                dp[h-1][x]=max(1,dp[h-1][x+1]-dungeon[h-1][x])
            else:
                dp[h-1][x]=dp[h-1][x+1]+abs(dungeon[h-1][x])
        for y in range(h-2,-1,-1):
            if dungeon[y][w-1]>=0:
                dp[y][w-1]=max(1,dp[y+1][w-1]-dungeon[y][w-1])
            else:
                dp[y][w-1]=dp[y+1][w-1]+abs(dungeon[y][w-1])
        for j in range(w-2,-1,-1):
            for i in range(h-2,-1,-1):
                if dungeon[i][j]>=0:
                    dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])
                else:
                    dp[i][j]=min(dp[i+1][j],dp[i][j+1])+abs(dungeon[i][j])

        return dp[0][0]

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        h=len(dungeon)
        w=len(dungeon[0])
        #定义dp数组的含义为dp[i][j]为从【i】【j】到公主哪里所需的最低血量
        dp=[[0 for _ in range(w)] for _ in range(h)]
        if dungeon[h-1][w-1]>=0:
            dp[h-1][w-1]=1
        else:
            dp[h-1][w-1]=1+abs(dungeon[h-1][w-1])
        for x in range(w-2,-1,-1):
            dp[h-1][x]=max(1,dp[h-1][x+1]-dungeon[h-1][x])
        for y in range(h-2,-1,-1):
            dp[y][w-1]=max(1,dp[y+1][w-1]-dungeon[y][w-1])
        for j in range(w-2,-1,-1):
            for i in range(h-2,-1,-1):
                dp[i][j]=max(1,min(dp[i+1][j],dp[i][j+1])-dungeon[i][j])

        return dp[0][0]

dungeon=[[-2,-3, 3],
         [-5,-10,1],
         [10,30,-5]]
a=Solution()
print(a.calculateMinimumHP(dungeon))



