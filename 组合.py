from typing import List


#官方题解还有一个字典法,太惊艳了...
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #提交解题通过了,但是只击败了30%的用户
        nums=[i for i in range(1,n+1)]
        ret=[]
        def fun(n,k,index,l):
            if k==0:
                ret.append(l[:])
            for i in range(index,n):
                l.append(nums[i])
                fun(n,k-1,i+1,l)
                l.remove(nums[i])

        fun(n,k,0,[])
        return ret

class Solution1:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #提交解题通过了,击败了80%的用户
        nums=[i for i in range(1,n+1)]
        ret=[]
        def fun(n,k,index,l):
            if k==0:
                ret.append(l[:])
            for i in range(index,n):
                #这里我们对其剪枝,成功提高效率
                if n-i<k:
                    break
                l.append(nums[i])
                fun(n,k-1,i+1,l)
                l.remove(nums[i])

        fun(n,k,0,[])
        return ret

a=Solution1()
n=4
k=2
print(a.combine(n,k))