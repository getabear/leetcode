from typing import List



class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size=len(nums)
        start=0
        end=size-1
        while(start<end-1):  #二分法细节太多,我怕死循环就这样写
            mid=(start+end)>>1
            if nums[mid]==target:
                return True
            if nums[start]<nums[mid]:#前面有序
                if target>=nums[start] and target<=nums[mid]:
                    #在这里查找
                    end=mid
                else:#去后面部分查找
                    start=mid
            elif nums[mid]<nums[end]:#后面有序
                if target>=nums[mid] and target<=nums[end]:
                    #在这里查找
                    start=mid
                else:#去前面部分查找
                    end=mid
            else:
                if nums[start]==target:
                    return True
                start+=1

        while start<=end:   #最后依次遍历最后2个数
            if nums[start]==target:
                return True
            start+=1
        return False

#下面是大佬写的算法
class Solution1:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        if size == 0:
            return False

        left = 0
        right = size - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[left]:
                if nums[left] <= target <= nums[mid]:
                    # 落在前有序数组里
                    right = mid
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                # 让分支和上面分支一样
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                # 要排除掉左边界之前，先看一看左边界可以不可以排除
                if nums[left] == target:
                    return True
                left = left + 1
        # 后处理，夹逼以后，还要判断一下，是不是 target
        return nums[left] == target
# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/er-fen-cha-zhao-by-liweiwei1419/


