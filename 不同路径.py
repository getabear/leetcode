class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #本算法典型的递归程序,但是数量大了就很耗时,很多重复的子问题
        def fun(m,n):
            if m==1 and n==1:
                return 1
            if m<1 or n<1:
                return 0
            else:
                return fun(m-1,n)+fun(m,n-1)

        return fun(m,n)

class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        dit={}
        #改进,咱们用字典记录下来,提交直接通过
        #用空间换时间
        def fun(m,n):
            if (m,n) in dit:
                return dit[(m,n)]
            if m==1 and n==1:
                return 1
            if m<1 or n<1:
                return 0
            else:
                dit[(m-1,n)]=fun(m-1,n)
                dit[(m,n-1)]=fun(m,n-1)
                return dit[(m-1,n)]+dit[(m,n-1)]

        return fun(m,n)

class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        #这次咱们用自底向上的动态规划,理论上比自顶向下的更加节省时间一点
        #分析: dp[i][j]为从i,j到终点的路径数
        #dp[0][j]=1   dp[i][0]=1
        #动态方程 dp[i][j]=dp[i-1][j]+dp[i][j-1]

        #初始化dp数组
        dp=[[1]*n]+[[1]+[0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]

a=Solution2()
print(a.uniquePaths(3,2))
