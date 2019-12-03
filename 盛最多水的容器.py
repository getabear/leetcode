from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def fun(height):  # 首先,暴力法,leetcode 提交超时,得优化
            ret = 0
            min_=height[0]
            for index, i in enumerate(height):
                if i<min_:    #如果小于了前面的高度,就没必要继续算了
                    min_=i
                    continue
                for end, j in enumerate(height[1:]):
                    if i < j:
                        ret = max(ret, (end - index + 1) * i)
                    else:
                        ret = max(ret, (end - index + 1) * j)
            return ret

        def fun2(height):   #双指针法
            length=len(height)
            ret=0
            start=0
            end=length-1
            while(start<end):
                #计算面积
                if height[start]<=height[end]:
                    ret=max(ret,(end-start)*height[start])
                    start+=1    #移动指针
                else:
                    ret=max(ret,(end-start)*height[end])
                    end-=1
            return ret

        return fun2(height)


a = Solution()
height =[1,10,100,2,5,1,10,3,7]
print(a.maxArea(height))
