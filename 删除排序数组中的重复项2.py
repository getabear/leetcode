from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #提交直接就通过了 击败99%
        #但是这是pop()的结果,可能只是python这里的实现不怎么消耗时间
        def fun(nums:List[int]):
            size=len(nums)
            if size<3:
                return
            #定义三个指针
            first=0
            second=first+1
            third=second+1
            while third<len(nums):
                #如果有三个数相等
                if nums[first]==nums[second] and nums[second]==nums[third]:
                    nums.pop(third)
                    continue
                first+=1
                second = first + 1
                third = second + 1

        return fun(nums)
class Solution1:
    #咱们用第二种方法
    def removeDuplicates(self, nums: List[int]) -> int:
        def fun(nums):
            size=len(nums)
            if size<3:
                return size
            sp=1
            fp=2
            while(fp<size):
#大佬的解题链接
#https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/solution/c-shuang-zhi-zhen-dan-ci-sao-miao-tu-jie-by-dexin/
                if nums[sp-1]!=nums[fp]:
                    sp+=1
                    nums[sp]=nums[fp]
                fp+=1
            return sp+1
        return fun(nums)
a=Solution1()
nums=[0,0,1,1,1,1,2,3,3]
a.removeDuplicates(nums)
print(nums)