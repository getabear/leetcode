class Solution1:
    def numWays(self, n: int) -> int:
        #加字典的递归
        self.ret=0
        mem={}
        def fun(step):
            if step in mem:
                self.ret+=mem[step]
                return
            if step>=n:
                if step==n:
                    self.ret+=1
                return
            tmp = self.ret
            fun(step+1)
            fun(step+2)
            mem[step]=self.ret-tmp
        fun(0)
        return self.ret%1000000007

class Solution:
    def numWays(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        dp_1=2
        dp_2=1
        for i in range(3,n+1):
            dp=dp_1+dp_2
            dp_2=dp_1
            dp_1=dp
        return dp%1000000007

a=Solution()
print(a.numWays(7))