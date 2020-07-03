from typing import List

class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        #策略有问题...
        mem=dict()
        for num in nums:
            try:
                mem[num]+=1
            except:
                mem[num]=1
        self.ret=0
        def fun(mem,res):
            if not mem:
                self.ret=max(self.ret,res)
                return
            m,rec=0,[]
            for key in mem.keys():
                if key*mem[key]>m:
                    m=key*mem[key]
                    rec=[key]
                elif key*mem[key]==m:
                    rec.append(key)
            for key in rec:
                dic=mem.copy()
                dic.pop(key)
                if key-1 in dic:
                    dic.pop(key-1)
                if key+1 in dic:
                    dic.pop(key+1)
                fun(dic,res+key*mem[key])
            return
        fun(mem,0)
        return self.ret

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        mem = dict()
        m=0
        for num in nums:
            try:
                mem[num] += 1
            except:
                mem[num] = 1
            m=max(m,num)
        dp=[0]*(m+1)
        if 1 in mem:
            dp[1]=mem[1]
        for i in range(2,m+1):
            if i in mem:
                dp[i]=max(dp[i-1],dp[i-2]+mem[i]*i)
            else:
                dp[i]=dp[i-1]
        return dp[-1]
a=Solution()
nums=[8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]
print(a.deleteAndEarn(nums))