from typing import List


class Solution1:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        self.ret = 0

        def fun(visit, val, level):
            for i in range(len(satisfaction)):
                if visit[i] == 0:
                    visit[i] = 1
                    fun(visit[:], val + level * satisfaction[i], level + 1)
                    self.ret = max(self.ret, val + level * satisfaction[i])
                    visit[i] = 0
            return

        visit = [0] * len(satisfaction)
        fun(visit, 0, 1)
        return self.ret


class Solution2:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        self.ret = 0
        mem = dict()

        def fun(visit, val, level):
            key = tuple(visit)
            if (key, val) in mem:
                self.ret = max(self.ret, val + mem[(key, val)])
                return
            for i in range(len(satisfaction)):
                if visit[i] == 0:
                    visit[i] = 1
                    self.ret = max(self.ret, val + level * satisfaction[i])
                    fun(visit[:], val + level * satisfaction[i], level + 1)
                    visit[i] = 0
            mem[(key, val)] = self.ret - val
            return

        visit = [0] * len(satisfaction)
        fun(visit, 0, 1)
        return self.ret


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()  #将大的满意度最后上
        # 与背包问题类似
        dp=[[0 for _ in range(len(satisfaction)+1)]for _ in range(len(satisfaction)+1)]
        dp[1][0]=0
        dp[1][1]=satisfaction[0]
        for i in range(1,len(satisfaction)+1):
            for j in range(1,i+1):
                if i==j:
                    dp[i][j]=dp[i-1][j-1]+j*satisfaction[i-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+j*satisfaction[i-1])
        ret=max(dp[len(satisfaction)])
        return ret

a = Solution()
l=[[-1,-8,0,5,-9],[4,3,2],[-1,-4,-5],[-2,5,-1,0,3,-3]]
# 14,20,0,35
for satisfaction in l:
    print(a.maxSatisfaction(satisfaction))
