class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        mem=dict()
        def dfs(x,y,step):
            if (x,y,step) in mem:
                return mem[(x,y,step)]
            if x<0 or x>N-1 or y<0 or y>N-1:
                return 0
            if step == K:
                return 1
            p1 = dfs(x-1,y+2,step+1)
            p2 = dfs(x-1,y-2,step+1)
            p3 = dfs(x+1,y-2,step+1)
            p4 = dfs(x+1,y+2,step+1)
            p5 = dfs(x+2,y-1,step+1)
            p6 = dfs(x+2,y+1,step+1)
            p7 = dfs(x-2,y+1,step+1)
            p8 = dfs(x-2,y-1,step+1)
            mem[(x,y,step)] = (p1+p2+p3+p4+p5+p6+p7+p8)/8
            return mem[(x,y,step)]
        return dfs(r,c,0)

a=Solution()
print(a.knightProbability(3,2,0,0))