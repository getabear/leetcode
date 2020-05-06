from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        l=[1]*length
        r=[1]*length
        for i in range(1,length):
            l[i]=l[i-1]*nums[i-1]
        for i in range(length-2,-1,-1):
            r[i]=r[i+1]*nums[i+1]
        output=[]
        for i in range(0,length):
            output.append(l[i]*r[i])
        return output

nums=[1,2,3,4]
a=Solution()
print(a.productExceptSelf(nums))