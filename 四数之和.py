from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        if n<4:
            return []
        nums.sort()
        ret=[]
        for i in range(n-3):
            if i-1>=0 and nums[i]==nums[i-1]:
                continue
                #看到大佬们的优化,另外此题可以使用哈希表
                # # 当数组最小值和都大于target 跳出
                # if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                #     break
                # # 当数组最大值和都小于target,说明i这个数还是太小,遍历下一个
                # if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                #     continue
            for j in range(i+1,n-2):
                if j-i>1 and nums[j]==nums[j-1]: #前两个数可以选择相同的,如果不加j-i>1则不能选相同的
                    continue
                x=j+1
                y=n-1
                while x<y:
                    sum=nums[i]+nums[j]+nums[x]+nums[y]
                    if sum==target:
                        ret.append([nums[i],nums[j],nums[x],nums[y]])
                        while x<y and nums[x]==nums[x+1]:
                            x+=1
                        while x<y and nums[y]==nums[y-1]:
                            y-=1
                        x+=1
                        y-=1
                    elif sum<target:
                        x+=1
                    else:
                        y-=1
        return ret


a=Solution()
nums=[0,0,0,0]
print(a.fourSum(nums,0))