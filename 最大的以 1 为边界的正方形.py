from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        h=len(grid)
        if h==0:
            return 0
        w=len(grid[0])
        if w==0:
            return 0
        #用以记录 grid[i][j]这个点的左边连续1的个数
        l=[[0 for _ in range(w+1)] for _ in range(h+1)]
        # 用以记录 grid[i][j]这个点的上边连续1的个数
        up=[[0 for _ in range(w+1)] for _ in range(h+1)]
        ret=0
        for i in range(1,h+1):
            for j in range(1,w+1):
                if grid[i-1][j-1]==1:
                    l[i][j]=l[i][j-1]+1
                    up[i][j]=up[i-1][j]+1
                for r in range(min(l[i][j],up[i][j]),0,-1):
                    if l[i-r+1][j]>=r and up[i][j-r+1]>=r:
                        ret=max(ret,r**2)
                        break
        return ret

a=Solution()
grid = [[1,1,1],[1,0,1],[1,1,1]]
print(a.largest1BorderedSquare(grid))