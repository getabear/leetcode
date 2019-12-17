from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i1=0
        i2=0
        num=[]
        while i1<m and i2<n:
            if  nums1[i1]<nums2[i2]:
                num.append(nums1[i1])
                i1+=1
            else:
                num.append(nums2[i2])
                i2 += 1
        while i1<m:
            num.append(nums1[i1])
            i1+=1
        while i2<n:
            num.append(nums2[i2])
            i2+=1
        nums1[:]=num[:]
        return

a=Solution()
nums1=[1,2,3,4]
nums2=[2,5,6]
a.merge(nums1,len(nums1),nums2,len(nums2))
print(nums1)