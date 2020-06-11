from typing import List

class Solution1:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        #第一版，暴力递归，超时了
        n=len(A)
        def fun(nums,deep):
            cnt=sum(nums)
            if cnt==n:
                return deep
            for index in range(n-K+1):
                if nums[index]==0:
                    tmp=nums[:]
                    for i in range(index,index+K):
                        if tmp[i]==0:
                            tmp[i]=1
                        else:
                            tmp[i]=0
                    return fun(tmp,deep+1)
            return -1
        return fun(A,0)
class Solution2:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # 优化甚微
        def fun(nums,deep):
            if len(nums)==sum(nums):
                return deep
            for i in range(len(nums)-K+1):
                if nums[i]==0:
                    for index in range(i,i+K):
                        if nums[index]:
                            nums[index]=0
                        else:
                            nums[index]=1
                    return fun(nums[i+1:],deep+1)
            return -1
        return fun(A,0)

class Solution3:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        # 优化甚微
        ret=0
        for index in range(len(A)-K+1):
            if A[index]==0:
                ret+=1
                for l in range(index,index+K):
                    if A[l]:
                        A[l]=0
                    else:
                        A[l]=1
        if A[len(A)-K:]==[1]*K:
            return ret
        else:
            return -1

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        #用数组记录那些需要翻转
        mem=[False]*(len(A)+1)
        flip=False
        cnt=0
        for index in range(len(A)):
            if mem[index]:   #如果为真，则需要将后面的翻转
                flip=not flip
            #如果翻转后为0，则需要再次翻转
            if (flip and A[index]) or (not flip and A[index]==0):
                if index + K > len(A): #如果超过数组的长度，则不能翻转成功
                    return -1
                flip=not flip   #翻转
                mem[index+K]=True  #标记K个数后需要翻转
                cnt+=1
        return cnt

a=Solution()
A=[1,0,1]
K=2
print(a.minKBitFlips(A,K))