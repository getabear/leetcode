from typing import List
# 官方题解还有分治的解法,但是时间复杂度为nlog(n),
# 最坏为O(n^2)我就暂时不做了


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #栈的解法,大佬们真的太厉害了,我哭了,这是怎么想到的啊
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #新的数小于了栈顶的数,就计算面积
            while stack and heights[stack[-1]] > heights[i]:
                #维护一个递增的栈
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

class Solution1:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #先来个穷举的解法
        def fun(heights: List[int]):
            size=len(heights)
            ret=0
            for index,i in enumerate(heights):
                left=index
                right=index
                while left>=0:
                    if heights[left]<i:
                        break
                    left-=1
                while right<size:
                    if heights[right]<i:
                        break
                    right+=1
                ret=max(ret,i*(right-left-1))
            return ret
        # 复杂度分析,首先依次遍历heights的每个元素复杂度O(n),然后需要寻找左右小于他的
        # 高度的下标复杂度也为O(n),所以复杂度综合为O(n^2)
        # 提交后毫无悬念的超时了......
        return fun(heights)
a=Solution()
heights=[1,1000,1,1,1]
print(a.largestRectangleArea(heights))