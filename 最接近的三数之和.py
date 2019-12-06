from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        def fun1(target,temp):
            if target-temp>0:
                return target-temp
            else:
                return temp-target
        def fun(nums:List[int],target:int):
            length=len(nums)
            if length<3:
                return []
            nums.sort()
            ret=float("inf")
            temp=0
            for i in range(length):
                if i>1 and nums[i]==nums[i-1]:
                    continue
                L=i+1
                R=length-1
                while(L<R):
                    temp=nums[i]+nums[L]+nums[R]
                    if temp==target:
                        return temp
                    elif temp>target:
                        if fun1(temp,target)<ret:
                            ret=fun1(temp,target)
                            res=temp
                        R-=1
                    elif temp<target:
                        if fun1(temp,target)<ret:
                            ret=fun1(temp,target)
                            res=temp
                        L+=1

            return res
        return fun(nums,target)

a=Solution()
nums=[-20,-32,0,9,18,10,1,-20,-17,-19,-3,-5,-19,10,6,-11,1,-17,-15,6,17,-18,-3,16,19,-20,-3,-17,-15,-3,12,1,-9,4,1,12,-2,14,4,-4,19,-20,6,0,-19,18,14,1,-15,-5,14,12,-4,0,-10,6,6,-6,20,-8,-6,5,0,3,10,7,-2,17,20,12,19,-13,-1,10,-1,14,0,7,-3,10,14,14,11,0,-4,-15,-8,3,2,-5,9,10,16,-4,-3,-9,-8,-14,10,6,2,-12,-7,-16,-6,10]

target=-52
print(a.threeSumClosest(nums,target))