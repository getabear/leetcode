from typing import List

class Solution1:
    def minTime(self, time: List[int], m: int) -> int:
        #利用递归进行穷举
        self.T=float("inf")
        length=len(time)
        stack=[]
        def fun(index,m):
            if m<0:
                return
            if index==length and m>=0:
                self.T=min(self.T,max(stack))
                return
            tmp=0
            sum_time=0
            for i in range(index,length):
                tmp=max(time[i],tmp)
                sum_time+=time[i]
                stack.append(sum_time-tmp)
                fun(i+1,m-1)
                stack.pop(-1)
        if m>=length:
            return 0
        fun(0,m)
        return self.T

class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        def fun(mid,m):
            n=0
            max_t=0
            sum_t=0
            for t in time:
                max_t=max(t,max_t)
                sum_t+=t
                if sum_t-max_t>mid:
                    n+=1
                    max_t=t
                    sum_t=t
            return n<m

        def devide():
            l,r=0,sum(time)
            while l<=r:
                mid=l+(r-l)//2
                if fun(mid,m):
                    r=mid-1
                else:
                    l=mid+1
            return l
        return devide()


a=Solution()
time=[1,2,3,3]
m=2
print(a.minTime(time,m))