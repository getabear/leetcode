from typing import List

class Solution1:
    #归并排序
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left,right):
            ret=[]
            leftsize=len(left)
            rightsize=len(right)
            index1=0
            index2=0
            while(index1<leftsize and index2<rightsize):
                if(left[index1]<right[index2]):
                    ret.append(left[index1])
                    index1+=1
                else:
                    ret.append(right[index2])
                    index2+=1
            ret+=left[index1:]
            ret+=right[index2:]
            return ret
        def devide(nums):
            size=len(nums)
            if size==1:
                return nums
            left=devide(nums[:size//2])
            right=devide(nums[size//2:])
            return merge(left,right)

        return devide(nums)

class Solution:
    #试试堆排序
    def sortArray(self, nums: List[int]) -> List[int]:




a=Solution()
nums=[5,1,1,2,0,0]
print(a.sortArray(nums))