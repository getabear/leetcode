from typing import List

class Solution1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        #通过，但是还可以优化
        def merge(nums1,nums2):
            idx1,idx2=0,0
            nums=[]
            while idx1<len(nums1) and idx2<len(nums2):
                if nums1[idx1]<nums2[idx2]:
                    nums.append(nums1[idx1])
                    idx1+=1
                else:
                    nums.append(nums2[idx2])
                    idx2+=1
            nums+=nums1[idx1:]
            nums+=nums2[idx2:]
            return nums

        def fun(matrix):
            if len(matrix)==1:
                return matrix[0]
            mid=len(matrix)//2
            left=fun(matrix[:mid])
            right=fun(matrix[mid:])
            return merge(left,right)

        ret=fun(matrix)
        return ret[k-1]

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def merge(nums1,nums2):
            idx1,idx2=0,0
            nums=[]
            while idx1<len(nums1) and idx2<len(nums2):
                if nums1[idx1]<nums2[idx2]:
                    nums.append(nums1[idx1])
                    idx1+=1
                else:
                    nums.append(nums2[idx2])
                    idx2+=1
                if len(nums) == k:  #如果长度为k直接返回
                    return nums
            nums+=nums1[idx1:]
            nums+=nums2[idx2:]
            return nums

        def fun(matrix):
            if len(matrix)==1:
                return matrix[0]
            mid=len(matrix)//2
            left=fun(matrix[:mid])
            right=fun(matrix[mid:])
            return merge(left,right)

        ret=fun(matrix)
        return ret[k-1]

a=Solution()
matrix=[
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
print(a.kthSmallest(matrix,8))
