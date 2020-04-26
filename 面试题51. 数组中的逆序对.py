from typing import List

class Solution1:
    def reversePairs(self, nums: List[int]) -> int:
        # 超时了
        self.ret=0

        def fun(start,nums):
            if len(nums)==0:
                return
            if start>nums[0]:
                self.ret+=1
            fun(start,nums[1:])

        for index,i in enumerate(nums):   #循环被我写成了递归,也还算厉害哈哈哈
            fun(i,nums[index+1:])
        return self.ret

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #想到过排序,但是没想到是归并啊啊啊果然还是太菜了
        self.ret=0
        def merge(nums1,nums2):
            len1=len(nums1)
            len2=len(nums2)
            nums=[]
            i1,i2=0,0
            while(i1<len1 and i2<len2):
                if nums1[i1]<=nums2[i2]:
                    nums.append(nums1[i1])
                    i1+=1
                    self.ret += i2
                else:
                    nums.append(nums2[i2])
                    i2+=1
            self.ret += len2 * (len1 - i1)
            nums+=nums1[i1:]
            nums+=nums2[i2:]
            return nums

        def divide(nums):
            length=len(nums)
            if length<=1:
                return nums[:]
            left=divide(nums[:length//2])
            right=divide(nums[length//2:])
            return merge(left,right)

        divide(nums)
        return self.ret

nums=[]
a=Solution()
print(a.reversePairs(nums))