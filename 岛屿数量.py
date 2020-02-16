from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        class UnionFind:
            def __init__(self,n):
                self.count=n
                self.parent=[i for i in range(n)]
                self.size=[1 for i in range(n)]
            def find(self,p):
                while(p!=self.parent[p]):
                    self.parent[p]=self.parent[self.parent[p]]   #路径压缩
                    p=self.parent[p]
                return p
            def union(self,p,q):
                rootp=self.find(p)
                rootq=self.find(q)
                if rootp==rootq:
                    return
                if self.size[rootp]>self.size[rootq]:
                    self.parent[rootq]=rootp
                    self.size[rootp]+=self.size[rootq]
                elif self.size[rootp]<=self.size[rootq]:
                    self.parent[rootp]=rootq
                    self.size[rootq]+=self.size[rootp]
                self.count-=1
        row=len(grid)
        if row==0:
            return 0
        col=len(grid[0])
        def getindex(x,y):
            return x*col+y
        directions=[(1,0),(0,1)]
        node=col*row
        uf=UnionFind(node+1)
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='0':
                    uf.union(getindex(i,j),node)
                if grid[i][j]=='1':
                    for direction in directions:
                        newx=i+direction[0]
                        newy=j+direction[1]
                        if newx<row and newy<col and grid[newx][newy]=='1':
                            uf.union(getindex(newx,newy),getindex(i,j))
        return uf.count-1

