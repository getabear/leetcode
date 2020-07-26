from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        h=len(matrix)
        if not h:
            return 0
        w=len(matrix[0])
        if not w:
            return 0
        visit=[[0 for _ in range(w)] for _1 in range(h)]
        mem = [[-1 for _ in range(w)] for _1 in range(h)]
        direct=[(0,1),(1,0),(0,-1),(-1,0)]
        def dfs(x,y):
            if mem[y][x] != -1:
                return mem[y][x]
            res=1
            for dx,dy in direct:
                if 0<=x+dx<w and 0<=y+dy<h and visit[y+dy][x+dx]==0 and \
                        matrix[y+dy][x+dx]>matrix[y][x]:
                    visit[y+dy][x+dx]=1
                    res=max(dfs(x+dx,y+dy)+1,res)
                    visit[y + dy][x + dx]=0
                mem[y][x]=res
            return res
        ret=1
        for high in range(h):
            for width in range(w):
                visit[high][width]=1
                ret=max(ret,dfs(width,high))
                visit[high][width] = 0
        return ret

a=Solution()
matrix=[
  [9,10,4],
  [6,6,8],
  [2,1,1]
]
print(a.longestIncreasingPath(matrix))