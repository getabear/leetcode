class solution:
    def fun(self,nums):
        count=1
        ret=1
        length=len(nums)
        # temp=nums[0]
        for i in range(length):
            j=i+1
            temp=nums[i]
            for j in range(j,length):
                if(nums[j]>temp):
                    temp=nums[j]
                    count+=1
                    if(count>ret):
                        ret=count
            count=1

        return ret

nums=[10,1,2,2,2,7,101,18]
a=solution()
print(a.fun(nums))



