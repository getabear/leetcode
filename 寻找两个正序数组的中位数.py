from typing import List
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #方式一：暴力排序,可以通过，但是时间复杂度为O（M+N），不满足题目要求
        def fun(nums1,nums2):
            len1=len(nums1)
            len2=len(nums2)
            nums=[]
            i1,i2=0,0
            while i1<len1 and i2<len2:
                if nums1[i1]<nums2[i2]:
                    nums.append(nums1[i1])
                    i1+=1
                else:
                    nums.append(nums2[i2])
                    i2+=1
            nums=nums+nums1[i1:]
            nums=nums+nums2[i2:]
            if len(nums)&0x1:
                return nums[len(nums)//2]
            return (nums[len(nums)//2]+nums[len(nums)//2-1])/2
        return fun(nums1,nums2)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #实现复杂度为O（log（M+N））的方法
        m=len(nums1)
        n=len(nums2)
        def find(k):
            index1,index2=0,0
            while True:
                if index1==m:
                    return  nums2[index2+k-1]
                if index2==n:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1],nums2[index2])
                newindex1=min(index1+k//2-1,m-1)
                newindex2=min(index2+k//2-1,n-1)
                if nums1[newindex1]<nums2[newindex2]:
                    k-=newindex1-index1+1
                    index1=newindex1+1
                else:
                    k-=newindex2-index2+1
                    index2=newindex2+1
        length=m+n
        if length&0x1:
            return find(length//2+1)
        return (find(length//2)+find(length//2+1))/2


a=Solution()
nums1=[1,2]
nums2=[4]
print(a.findMedianSortedArrays(nums1,nums2))