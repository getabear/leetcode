class Solution:
    def fun(self,nums,target):
        length=len(nums)
        ret=666
        temp2=666
        temp=nums[0]+nums[1]
        for i in range(2,length):
            sum=temp+nums[i]
            temp=sum-nums[i-2]
            if(sum>target):
                diff=sum-target
            else:
                diff=target-sum
            if(diff<temp2):
                temp2=diff
                ret=sum
        return ret

a=Solution()
nums=[-1,2,1,-4]
target=1
print(a.fun(nums,target))