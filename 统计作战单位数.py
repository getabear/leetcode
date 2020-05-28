from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #递归的暴力解法,通过
        n=len(rating)
        self.ret=0
        def fun(last,index,step):
            if step==3:
                self.ret+=1
                return
            if index==n:
                return
            for i in range(index,n):
                if rating[i]>last:
                    fun(rating[i],i+1,step+1)
            return
        fun(-1,0,0)
        rating=rating[::-1]
        fun(-1,0,0)
        return self.ret




a=Solution()
rating=[2,5,3,4,1]
print(a.numTeams(rating))

