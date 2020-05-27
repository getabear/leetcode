from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n%k!=0:
            return False
        mem=dict()
        nums.sort()
        for i in nums:
            try:
                mem[i]+=1
            except:
                mem[i]=1
        for num,count in mem.items():
            while count>0:
                for next in range(num,k+num):
                    if next in mem:
                        mem[next]-=1
                        if mem[next]<0:
                            return False
                    else:
                        return False
                count-=1
        return True



nums=[1,2,3,4]
a=Solution()
print(a.isPossibleDivide(nums,3))