from typing import List

class Solution1:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #暴力递归：超时在意料之中

        # find()函数参数说明：day为当前的日期，last为买了几天的票，start为从哪里开始搜索；
        # 返回值为下次开始需要买票的下标
        def find(day,last,start):
            i=start
            end=day+last-1
            while i<len(days):
                if end>=days[i]:
                    i+=1
                else:
                    break
            return i

        self.res=float("inf")
        #start为days的下标，标志我们开始的位置
        def fun(start,cost):
            if start>=len(days):
                self.res=min(self.res,cost)
                return
            tmp=start
            start=find(days[tmp],1,start)
            fun(start,cost+costs[0])
            start = find(days[tmp], 7, start)
            fun(start,cost+costs[1])
            start = find(days[tmp], 30, start)
            fun(start, cost + costs[2])
        fun(0,0)
        return self.res

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[0 for i in range(days[-1]+1)]
        index=0
        for i in range(1,days[-1]+1):
            if i!=days[index]:
                dp[i]=dp[i-1]
            else:
                dp[i]=min(dp[max(i-1,0)]+costs[0],
                          dp[max(i-7,0)]+costs[1],
                          dp[max(i-30,0)]+costs[2])
                index+=1
        return dp[days[-1]]





a=Solution()
days=[1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,
      38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,
      84,85,88,89,91,93,94,97,99]
costs=[9,38,134]
print(a.mincostTickets(days,costs))
