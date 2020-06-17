from typing import List

class Solution1:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        #暴力法，又超时了
        ret=0
        for i in range(len(A)):
            distance=1
            for j in range(i+1,min(len(A),i+10001)):
                val=A[i]+A[j]-distance
                ret=max(val,ret)
                distance+=1
        return ret

class Solution2:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        #通过，时间复杂度O(n) 空间复杂度O(n)
        n=len(A)
        dec=[0]*n
        add=[0]*n
        dp=[0]*n   #dp数组含义，dp[i]代表从i到末尾的最大值的下标
        for index,val in enumerate(A):
            dec[index]=val-index
            add[index]=val+index
        for i in range(n-1,-1,-1):
            if i==n-1:
                dp[i]=i
            else:
                if dec[i]>=dec[dp[i+1]]:
                    dp[i]=i
                else:
                    dp[i]=dp[i+1]
        ret=0
        for i in range(n-1):
            ret=max(ret,add[i]+dec[dp[i+1]])
        return ret
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        #官方题解的枚举，太厉害了
        ret,add=0,A[0]
        for i in range(1,len(A)):
            ret=max(ret,add+A[i]-i)
            add=max(A[i]+i,add)   #add始终会超前dec，所以可以优化到O(1)的空间复杂度
        return ret

a=Solution()
A=[8,1,5,2,6]
print(a.maxScoreSightseeingPair(A))