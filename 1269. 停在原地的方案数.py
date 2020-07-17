
#先写出暴力解法
class Solution1:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.res=0
        def fun(idx,step):
            if step==steps:
                if idx==0:
                    self.res+=1
                return
            if idx==0:
                fun(idx, step + 1)
                fun(idx+1,step+1)
            elif idx==arrLen-1:
                fun(idx, step + 1)
                fun(idx-1,step+1)
            else:
                fun(idx, step + 1)
                fun(idx - 1, step + 1)
                fun(idx + 1, step + 1)
        fun(0,0)
        return self.res
#加字典的暴力解法优化
class Solution2:
    def numWays(self, steps: int, arrLen: int) -> int:
        self.res=0
        mem=dict()
        def fun(idx,step):
            if (idx,step) in mem:
                self.res+=mem[(idx,step)]
                return
            if step==steps:
                if idx==0:
                    self.res+=1
                return
            tmp=self.res
            if idx==0:
                fun(idx, step + 1)
                fun(idx+1,step+1)
            elif idx==arrLen-1:
                fun(idx, step + 1)
                fun(idx-1,step+1)
            else:
                fun(idx, step + 1)
                fun(idx - 1, step + 1)
                fun(idx + 1, step + 1)
            mem[(idx,step)]=self.res-tmp
        fun(0,0)
        return self.res%(10**9+7)

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        #定义dp数组的含义:
        #dp[i][j]代表当前位置在i处，走j步回到0处的方法数
        tmp=min(steps,arrLen)   #如果当前位置大于了步数，怎么也回不到0
        dp=[[0 for _ in range(steps+1)] for _ in range(tmp)]
        dp[0][0]=1
        for i in range(1,steps+1):
            for j in range(tmp):
                if j==0:
                    dp[j][i]=dp[j+1][i-1]+dp[j][i-1]
                elif j==tmp-1:
                    dp[j][i]=dp[j-1][i-1]+dp[j][i-1]
                else:
                    dp[j][i]=dp[j-1][i-1]+dp[j+1][i-1]+dp[j][i-1]
        return dp[0][steps]%(10**9+7)
a=Solution()
print(a.numWays(2,4))
