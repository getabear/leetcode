class Solution:
    def max_Array(self,nums):   #算法复杂度    N^2
        max=0
        sum=0
        length=len(nums)
        for i in range(length):
            for j in range(i,length):
                sum+=nums[j]
                if(sum>max):
                    max=sum
            sum=0
        return max

    def max_Array2(self, nums):   #动态规划,算法复杂度 N
        sum=0
        ans=nums[0]
        for i in nums:
            if(sum>=0):
                sum+=i
            else:
                sum=i
            ans=max(sum,ans)
        return ans

    def max_Array3(self, nums):   #递归的方法,分3种情况  左边 中间 右边   时间复杂度 NlogN
        left_max = 0
        right_max = 0
        mid_max = 0
        length=len(nums)
        # if(length==0):
        #     return 0
        if(length==1):
            return nums[0]
        else:
            mid=length//2    #取整
            left_max=self.max_Array3(nums[0:mid])
            right_max=self.max_Array3(nums[mid:length])
        left_start=mid
        right_start=mid+1
        mid_sum=0
        mid_max=0
        while (left_start>=0):
            mid_sum+=nums[left_start]
            left_start-=1
            if(mid_sum>mid_max):
                mid_max=mid_sum
        mid_sum=mid_max
        while(right_start<length):
            mid_sum+=nums[right_start]
            right_start+=1
            if(mid_sum>mid_max):
                mid_max=mid_sum
        return max(mid_max,left_max,right_max)








nums=[-2,1,-3,4,-1,2,1,-5,4]
a=Solution()
print(a.max_Array3(nums))
