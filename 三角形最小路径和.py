from typing import List


class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #暴力递归,果然超时了哈哈哈,接下来优化算法
        size=len(triangle)
        self.ret=float("inf")
        def fun(triangle: List[List[int]],level,sum,i):
            if level==size:
                if self.ret>sum:
                    self.ret=sum
                return
            fun(triangle,level+1,sum+triangle[level][i],i)
            fun(triangle,level+1,sum+triangle[level][i+1],i+1)
        if size==0:
            return 0
        sum=triangle[0][0]
        fun(triangle,1,sum,0)
        return self.ret

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #动态规划     提交后通过了,但是只超越了9%的人...
        #3个条件:
        # 1.定义dp数组含义   dp[level][i]为从底部到顶部最短的距离
        # 2.动态方程   dp[level][i]=min(dp[level+1][i],dp[level+1][i+1])+triangle[level][i]
        # 3.初始条件   这里level为底部 dp[level][i]=triangle[level][i]
        size=len(triangle)
        length=len(triangle[-1])
        if size==0:
            return 0
        #定义和初始化dp数组
        dp=[[i for i in triangle[-1]] for _ in range(size)]
        size-=2
        while size>=0:
            length=len(triangle[size])-1
            while length>=0:
                dp[size][length]=min(dp[size+1][length],dp[size+1][length+1])+triangle[size][length]
                length-=1
            size-=1
        return dp[0][0]

triangle=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
a=Solution()
print(a.minimumTotal(triangle))