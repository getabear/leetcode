from typing import List
class Solution1:
    def countBits(self, num: int) -> List[int]:   #方法一,暴力法
        dp=[]
        dp.append(0)
        for i in range(1,num+1):
            if i&0x1==1:  #奇数
                dp.append(dp[i-1]+1)
            else:
                temp=i
                count=0
                while temp!=0:
                    count+=temp&0x1
                    temp=temp>>1
                dp.append(count)
        return dp

    def countBits2(self, num: int) -> List[int]:   #方法二: 动态规划
        dp = []
        dp.append(0)
        for i in range(1, num + 1):
            if i & 0x1 == 1:  # 奇数
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i>>1])     #如果是偶数,则和它的右移一位的一样多
        return dp

class Solution:
    def countBits(self, num: int) -> List[int]:
        if num<1:
            return [0]
        dp=[0]*(num+1)
        dp[1]=1
        for i in range(2,num+1):
            if i&0x1:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=dp[i>>1]
        return dp
a=Solution()
print(a.countBits(2))
print(a.countBits(5))
