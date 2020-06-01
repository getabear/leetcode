from typing import List

class Solution1:
    def arrayNesting(self, nums: List[int]) -> int:
        #暴力法，超时
        ret=0
        for num in nums:
            cnt=1
            start,i=num,num
            while nums[i]!=start:
                cnt+=1
                i=nums[i]
            ret=max(ret,cnt)
        return ret

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=len(nums)
        record=[0]*n   #用以记录那些访问过，访问过的不再访问以优化速度
        ret=0
        for index,num in enumerate(nums):
            if record[index]==0:
                record[index]=1   #标为已读
                cnt=1
                start,i=num,num
                while nums[i]!=start:
                    cnt+=1
                    record[i]=1
                    i=nums[i]
                ret=max(ret,cnt)
        return ret


a=Solution()
A=[5,4,0,3,1,6,2]
print(a.arrayNesting(A))