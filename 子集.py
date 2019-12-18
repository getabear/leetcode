from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #提交leetcode,通过了,但是只击败了10%的用户
        #内存消耗只击败了5%的用户
        ret=[]
        size=len(nums)
        def fun(index,k,tp):
            if k==0:
                ret.append(tp[:])
            for i in range(index,size):
                #剪枝
                if size-i<k:
                    break
                tp.append(nums[i])
                fun(i+1,k-1,tp)
                tp.remove(nums[i])

            return
        for i in range(size+1):
            fun(0,i,[])
        return ret

class Solution1:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #咱们换一下思路
        #击败99%,可以了哈哈哈
        ret = []
        size = len(nums)
        def fun(index, k, tp):
            if k == 0:
                ret.append(tp[:])
            for i in range(index, size):
                fun(i+1,k-1,tp)
                # 剪枝
                if size - i < k:
                    break
                tp.append(nums[i])
                fun(i + 1, k - 1, tp)
                tp.remove(nums[i])
            return
        fun(0,size,[])
        return ret

a=Solution1()
nums=[1,2,3]
print(a.subsets(nums))

