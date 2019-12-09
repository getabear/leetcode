from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        #暴力法
        def fun(height):
            size = len(height)
            index=1
            left=0
            right=0
            cur=0
            ret=0
            while(index<size-1):
                cur=index
                left=0
                right=0
                while(cur>=0):
                    left=max(left,height[cur])
                    cur-=1
                cur=index
                while(cur<size):
                    right=max(right,height[cur])
                    cur+=1
                ret+=min(right,left)-height[index]
                index+=1
            return ret

        def fun2(height):
            #动态规划,是暴力法的优化版本
            size = len(height)
            if size==0:
                return 0

            left =height[0]   #初始值改变下
            right = 0
            cur = 0
            ret = 0
            max_right=[height[size-1]]
            index = size - 2
            #维护一个数组,找到从index开始往右的最大值
            while(index>=0):
                max_right.append(max(max_right[-1],height[index]))
                index-=1
            index = 1
            while (index < size - 1):
                cur = index
                #left = 0可以不用清零,并且left=max(left,height[index])就可以了
                # right = 0 right使用前面维护的数组
                left = max(left, height[cur])
                right=max_right[size-index-1]
                ret += min(right, left) - height[index]
                index += 1
            return ret
        return fun2(height)

a=Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(a.trap(height))