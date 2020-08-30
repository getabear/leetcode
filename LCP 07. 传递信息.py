from typing import List

# 提交通过，但是含有子问题，可以进行优化
class Solution1:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        list=[[] for i in range(n)]
        for rel in relation:
            list[rel[0]].append(rel[1])
        self.res=0
        # addr：当前的位置  deep是调用的深度，也可以理解为路程
        def dfs(addr,deep):
            if deep==k:
                if addr==n-1:
                    self.res+=1
                return
            for nextAddr in list[addr]:
                dfs(nextAddr,deep+1)
        dfs(0,0)
        return self.res

class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        #dp[i][j]代表第i轮，可以传到节点j的路径数
        # 递推关系 dp[i][j]=dp[i-1][x] 其中x可以下一步到达节点j
        dp=[[0 for _ in range(n)] for i in range(k+1)]
        dp[0][0]=1
        for i in range(1,k+1):
            for rela in relation:
                dp[i][rela[1]]+=dp[i-1][rela[0]]

        return dp[k][n-1]


a=Solution()
n = 5
relation = [[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
k = 3
print(a.numWays(n,relation,k))