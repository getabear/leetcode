from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #方法一:hash表法
        ret={}
        for i in nums:
            if i in ret:
                if ret[i]==2:
                    ret.pop(i)
                else:
                    ret[i]+=1
            else:
                ret[i]=1
        return ret.popitem()[0]
#有大佬利用卡洛图做出来啦,暂时没看
nums=[0,1,0,1,0,1,99]
a=Solution()
print(a.singleNumber(nums))