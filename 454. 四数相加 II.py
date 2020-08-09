from typing import List
# 时间复杂度O(n^2)，超时了，前面系数为3
class Solution1:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        tmp1=[]
        for i in A:
            for j in B:
                tmp1.append(i+j)
        tmp2=[]
        for i in C:
            for j in D:
                tmp2.append(i+j)
        res=0
        for i in tmp1:
            for j in tmp2:
                if i+j==0:
                    res+=1
        return res

# 时间复杂度为O(n^2) 但是前面的系数变为了2
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        sum1=dict()
        for i in A:
            for j in B:
                if i+j not in sum1:
                    sum1[i+j]=1
                else:
                    sum1[i+j]+=1
        res=0
        for i in C:
            for j in D:
                tmp=i+j
                if -tmp in sum1:
                    res+=sum1[-tmp]
        return res