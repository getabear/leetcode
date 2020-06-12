from typing import List

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        high=len(A)
        if not high:
            return 0
        width=len(A[0])
        if not width:
            return 0
        direct=[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(x,y):
            A[y][x]=0
            for dx,dy in direct:
                if x+dx>=0 and x+dx<width and y+dy>=0 and y+dy<high:
                    if A[y+dy][x+dx]==1:
                        dfs(x+dx,y+dy)
            return
        for x in range(width):
            if A[0][x]==1:
                dfs(x,0)
            if A[high-1][x]==1:
                dfs(x,high-1)
        for y in range(high):
            if A[y][0]==1:
                dfs(0,y)
            if A[y][width-1]==1:
                dfs(width-1,y)
        res=0
        for x in range(width):
            for y in range(high):
                res+=A[y][x]
        return res

a=Solution()
A=[[0,0,0,1,1,1,0,1,0,0],[1,1,0,0,0,1,0,1,1,1],[0,0,0,1,1,1,0,1,0,0],[0,1,1,0,0,0,1,0,1,0],[0,1,1,1,1,1,0,0,1,0],[0,0,1,0,1,1,1,1,0,1],[0,1,1,0,0,0,1,1,1,1],[0,0,1,0,0,1,0,1,0,1],[1,0,1,0,1,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,1]]
print(a.numEnclaves(A))