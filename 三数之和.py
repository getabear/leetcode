# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素\
# a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #暴力法   leetcode提交后超时了
        ret = []
        length = len(nums)
        if length<3:
            return []
        nums.sort()
        if nums[0]>0:
            return []
        for i in range(length):
            for j in range(i+1,length):
                for k in range(j+1,length):
                    if nums[i]+nums[j]+nums[k]==0 and \
                    [nums[i],nums[j],nums[k]] not in ret:
                        ret.append([nums[i],nums[j],nums[k]])
        return ret

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        #双指针法   L左指针  R右指针
        ret = []
        length = len(nums)
        if length < 3:
            return []
        nums.sort()   #升序排列
        if nums[0] > 0:
            return []
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:    #为了跳过重复答案
                continue
            L=i+1
            R=length-1
            while(L<R):
                sum=nums[i]+nums[L]+nums[R]
                if sum==0:
                    ret.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]): #去重复,如果下一项和本项相同
                        L+=1
                    while(L<R and nums[R]==nums[R-1]):#去重复,如果下一项和本项相同,这个下一项指的他的前一项,应为R指针匙向前移动的
                        R-=1
                    L+=1
                    R-=1
                elif sum<0:
                    L+=1
                elif sum>0:
                    R-=1
        return ret
# sort()
# 方法语法：
#
# list.sort(cmp=None, key=None, reverse=False)
# 参数
# cmp - - 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key - - 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取
# 自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse - - 排序规则，reverse = True
# 降序， reverse = False
# 升序（默认）。

nums = [-1, 0, 1, 2, -1, -4]
a=Solution()
print(a.threeSum2(nums))

