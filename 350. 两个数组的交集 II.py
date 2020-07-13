from typing import List

class Solution1:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem=dict()
        for num in nums1:
            try:
                mem[num]+=1
            except:
                mem[num]=1
        res=[]
        for i in nums2:
            if i in mem:
                mem[i]-=1
                if mem[i]==0:
                    mem.pop(i)
                res.append(i)
        return res

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2.sort()
        def find(target,nums):
            l,r=0,len(nums)-1
            while l<=r:
                mid=l+(r-l)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return -1
        res=[]
        for num in nums1:
            idx=find(num,nums2)
            if idx!=-1:
                res.append(num)
                nums2.pop(idx)
        return res

a=Solution()
nums=[1,2,2,1]
nums2=[2]
print(a.intersect(nums,nums2))
