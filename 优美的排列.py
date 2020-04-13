class Solution:
    def countArrangement(self, N: int) -> int:
        nums=[i for i in range(1,N+1)]
        self.ret=0

        def fun(i,nums):
            if len(nums)==0:
                self.ret+=1
                return
            for num in nums:
                if num%i==0 or i%num==0:
                    tmp=nums[:]
                    tmp.remove(num)
                    fun(i+1,tmp)
            return

        fun(1,nums)
        return self.ret

a=Solution()
print(a.countArrangement(2))