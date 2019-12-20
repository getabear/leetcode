from typing import List

class Solution:
    # 收获,遇到配对问题,可以想想是否有栈的解法
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def fun2(nums):#用来寻找最大的柱子
            nums=[0]+nums+[0]   #确保他的两边的值最小
            area=0  #记录最大面积
            stack=[]   #记录下标
            for index,i in enumerate(nums):
                while stack and nums[stack[-1]]>i:
                    #遇到比他们小的数,则以tp为下标的柱子遇到了以nums[tp]为高的面积
                    #底就为nums[tp]的左边和右边第一个小于他高度的下标相减
                    tp=stack.pop()
                    area=max(area,nums[tp]*(index-stack[-1]-1))
                stack.append(index)
            return area



        def fun1(matrix: List[List[str]]):
            high=len(matrix)
            if high==0:
                return 0
            record=[0 for i in range(len(matrix[0]))]
            ret=0
            for i in matrix:
                for index,j in enumerate(i):
                    if j=='1':
                        record[index]+=1
                    else:
                        record[index]=0
                ret=max(ret,fun2(record))
            return ret

        return fun1(matrix)

a=Solution()
matrix=[
]
print(a.maximalRectangle(matrix))


