from typing import List
import copy
class Solution1:
    def removeBoxes(self, boxes: List[int]) -> int:
        #说来可笑，只通过了9个测试用例就超时了哈哈哈哈哈
        # 时间复杂度 n的阶乘
        self.dp=[]
        for idx,box in enumerate(boxes):
            if idx==0:
                self.dp.append([box,1])
            elif self.dp[-1][0]==box:
                self.dp[-1][1]+=1
            else:
                self.dp.append([box,1])
        self.ret=0
        def fun(dp,res):
            if len(dp)==0:
                self.ret=max(self.ret,res)
                return
            for idx in range(len(dp)):
                tmp=copy.deepcopy(dp)
                tmp.pop(idx)
                if idx==0 or idx==len(dp)-1:
                    fun(tmp,res+dp[idx][1]**2)
                else:
                    if tmp[idx][0]==tmp[idx-1][0]:
                        tmp[idx][1]+=tmp[idx-1][1]
                        tmp.pop(idx-1)
                    fun(tmp,res+dp[idx][1]**2)
            return
        fun(self.dp,0)
        return self.ret

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        dp = [[[0]*n for i in range(n)] for j in range(n)]
        result = self._removeBoxes(boxes,dp,0,n-1,0)
        return result

    def _removeBoxes(self,boxes,dp,l,r,k):
        if l>r: return 0
        if dp[l][r][k] !=0: return dp[l][r][k]
        while r>l and boxes[r] == boxes[r-1]:
            r = r-1
            k = k+1
        dp[l][r][k] =  self._removeBoxes(boxes,dp,l,r-1,0)+(k+1)**2
        for i in range(l,r):
            if(boxes[i] == boxes[r]):
                dp[l][r][k] = max(dp[l][r][k],self._removeBoxes(boxes,dp,l,i,k+1)+self._removeBoxes(boxes,dp,i+1,r-1,0))
        return dp[l][r][k]


a=Solution()
boxes=[1,2,3,4,5,6,7,8,9,10]
print(a.removeBoxes(boxes))